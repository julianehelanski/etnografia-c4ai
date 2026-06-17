#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
relatorio_divergencia_tese.py
=============================
Detecta DIVERGÊNCIA (drift) entre a estrutura da tese (.tex) e o último
estado conhecido, para que a curadoria do site (seções, subseções,
sumário, nomes de figuras — em PT e EN) seja atualizada sabendo
exatamente o que mudou.

NÃO reescreve nada do site. Apenas:
  1. extrai a estrutura de cada capítulo (\\section, \\subsection,
     figuras/\\includegraphics);
  2. compara com o snapshot anterior (SNAPSHOT);
  3. grava um relatório legível (REPORT) com o que foi adicionado,
     removido ou renomeado desde a última sincronização;
  4. atualiza o snapshot.

Uso:
    python scripts/relatorio_divergencia_tese.py [--source-root _tex]
"""
import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent
SNAPSHOT = HERE / "tex_structure_snapshot.json"
REPORT = REPO_ROOT / "docs" / "divergencia-tese.md"

CHAPTER_FILES = {
    "cap1": "ex_cap1.tex",
    "cap2": "ex_cap2.tex",
    "cap3": "ex_cap3.tex",
    "cap4": "ex_cap4.tex",
}

# ---------------------------------------------------------------------------
# Extração de LaTeX
# ---------------------------------------------------------------------------
def _match_brace_arg(text: str, start: int) -> tuple[str, int]:
    """Lê um argumento entre chaves a partir de '{' em text[start], com
    contagem de aninhamento. Retorna (conteudo, indice_apos_fecha)."""
    assert text[start] == "{"
    depth = 0
    for i in range(start, len(text)):
        c = text[i]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return text[start + 1:i], i + 1
    return text[start + 1:], len(text)


def _commands(text: str, name: str) -> list[str]:
    """Todas as ocorrências de \\name{...} (e \\name*{...}); devolve os
    argumentos crus, na ordem do texto."""
    out = []
    # aceita \name, \name*, e argumento opcional \name[...]{...}
    pat = re.compile(r"\\" + name + r"\*?\s*(?:\[[^\]]*\]\s*)?\{")
    i = 0
    while True:
        m = pat.search(text, i)
        if not m:
            break
        brace = m.end() - 1
        arg, nxt = _match_brace_arg(text, brace)
        out.append(arg)
        i = nxt
    return out


_WRAP = ("textit", "textbf", "emph", "enquote", "textsc", "texttt",
         "textsuperscript", "mbox", "textrm", "text")


def clean_title(s: str) -> str:
    """Converte um título LaTeX em texto legível."""
    prev = None
    while prev != s:
        prev = s
        for cmd in _WRAP:
            s = re.sub(r"\\" + cmd + r"\*?\s*\{([^{}]*)\}", r"\1", s)
    s = re.sub(r"\\[a-zA-Z]+\*?", "", s)      # comandos restantes
    s = s.replace("{", "").replace("}", "")
    s = s.replace("~", " ").replace("\\&", "&").replace("\\,", " ")
    return re.sub(r"\s+", " ", s).strip()


def parse_chapter(tex: str) -> dict:
    sections = [clean_title(x) for x in _commands(tex, "section")]
    subsections = [clean_title(x) for x in _commands(tex, "subsection")]
    figs_raw = _commands(tex, "includegraphics")
    figures = sorted({Path(re.sub(r"\[[^\]]*\]", "", f).strip()).name
                      for f in figs_raw})
    return {"sections": sections, "subsections": subsections,
            "figures": figures}


# ---------------------------------------------------------------------------
# Diff e relatório
# ---------------------------------------------------------------------------
def diff_lists(old: list[str], new: list[str]) -> tuple[list[str], list[str]]:
    so, sn = set(old), set(new)
    added = [x for x in new if x not in so]
    removed = [x for x in old if x not in sn]
    return added, removed


def render_section(slug: str, old: dict, new: dict) -> tuple[str, bool]:
    lines = [f"### {slug}"]
    any_change = False
    labels = {"sections": "Seções", "subsections": "Subseções",
              "figures": "Figuras"}
    for key, lbl in labels.items():
        added, removed = diff_lists(old.get(key, []), new.get(key, []))
        if not added and not removed:
            continue
        any_change = True
        lines.append(f"\n**{lbl}**")
        # heurística simples de renomeação: 1 removido + 1 adicionado
        if len(added) == 1 and len(removed) == 1:
            lines.append(f"- ✏️ renomeada (provável): "
                         f"`{removed[0]}` → `{added[0]}`")
        else:
            for a in added:
                lines.append(f"- ➕ adicionada: `{a}`")
            for r in removed:
                lines.append(f"- ➖ removida: `{r}`")
    if not any_change:
        lines.append("\n_Sem mudanças estruturais._")
    return "\n".join(lines), any_change


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-root", type=Path, default=REPO_ROOT / "_tex")
    args = ap.parse_args()

    current: dict[str, dict] = {}
    missing = []
    for slug, fname in CHAPTER_FILES.items():
        src = args.source_root / fname
        if not src.exists():
            missing.append(fname)
            continue
        current[slug] = parse_chapter(src.read_text(encoding="utf-8"))

    previous = {}
    if SNAPSHOT.exists():
        previous = json.loads(SNAPSHOT.read_text(encoding="utf-8")).get("chapters", {})

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    out = [f"# Divergência tese ↔ site",
           "",
           f"> Gerado em {now} por `scripts/relatorio_divergencia_tese.py`.",
           "> Compara a estrutura do `.tex` com a última sincronização.",
           "> **Não altera o site** — serve para você atualizar a curadoria",
           "> (seções, subseções, sumário, figuras) em PT e EN.",
           ""]

    if not previous:
        out.append("## Snapshot inicial criado")
        out.append("")
        out.append("Não havia snapshot anterior — este é o ponto de partida. "
                   "A partir da próxima atualização da tese, as mudanças "
                   "estruturais serão listadas aqui.")
        out.append("")
        for slug, st in current.items():
            out.append(f"- **{slug}**: {len(st['sections'])} seções, "
                       f"{len(st['subsections'])} subseções, "
                       f"{len(st['figures'])} figuras.")
        any_change = False
    else:
        any_change = False
        body = []
        for slug in CHAPTER_FILES:
            if slug not in current:
                continue
            txt, changed = render_section(slug, previous.get(slug, {}),
                                          current[slug])
            any_change = any_change or changed
            body.append(txt)
        if any_change:
            out.append("## Mudanças desde a última sincronização")
            out.append("")
            out.append("Atualize os nós/sumário/figuras correspondentes no "
                       "`index.html` (PT **e** EN).")
            out.append("")
        else:
            out.append("## Sem divergências")
            out.append("")
            out.append("A estrutura da tese não mudou desde a última "
                       "sincronização. Nada a fazer.")
            out.append("")
        out.append("\n\n".join(body))

    if missing:
        out.append("\n---\n")
        out.append("> ⚠️ Arquivos não encontrados em `_tex/`: "
                   + ", ".join(f"`{m}`" for m in missing))

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(out) + "\n", encoding="utf-8")
    SNAPSHOT.write_text(json.dumps({"generated": now, "chapters": current},
                                   ensure_ascii=False, indent=2),
                        encoding="utf-8")

    print(f"[drift] relatório: {REPORT}")
    print(f"[drift] snapshot:  {SNAPSHOT}")
    print(f"[drift] mudanças estruturais: {'sim' if any_change else 'não'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
