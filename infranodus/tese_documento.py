#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tese_documento.py
=================
Extrai do `.tex` da tese os "paratextos" para apresentar na defesa:
resumo (PT), palavras-chave, sumário (capítulos · seções · subseções,
com um breve resumo por capítulo e uma nota por seção), lista de
ilustrações e lista de tabelas. Exporta JSON e, opcionalmente, reinjeta
num HTML (<script id="docdata">).

Uso:
    python3 infranodus/tese_documento.py --source-root /tmp/tese --inject index.html
"""
import argparse
import json
import re
import sys
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(THIS_DIR.parent / "scripts"))
from relatorio_divergencia_tese import clean_title, _match_brace_arg  # noqa: E402

# capítulo: (arquivo, número, título de exibição, resumo curado)
CHAPTERS = [
    ("ex_cap0.tex", "", "Apresentação",
     "A entrada em campo: a pergunta que move a tese — o que cientistas e "
     "engenheiros fazem ao desenvolver inteligência artificial — e o primeiro "
     "encontro com um sistema de IA (o SPIRA), que abre o percurso etnográfico."),
    ("ex_cap1.tex", "1", "Método",
     "O capítulo metodológico: constrói o método a partir da experiência de "
     "campo. Apresenta o patchwork como figuração do método, as existências "
     "parciais (incluindo o fazer-com IA generativa) e a compostagem, e nomeia "
     "a prática como tecnoetnografia."),
    ("ex_cap2.tex", "2", "Metáforas, figurações e alianças",
     "Revisão da literatura em duas tramas: a análise lexicométrica das "
     "figurações em seis obras de Latour e o mapeamento bibliométrico do campo "
     "brasileiro de IA nas ciências humanas, com as leituras de campo entre elas."),
    ("ex_cap3.tex", "3", "A rede que Fábio e Cláudio construíram",
     "Seguindo Fábio e Cláudio, diretores do C4AI: a genealogia da IBM, a "
     "racionalidade do ecossistema de inovação e o ciclo da parceria "
     "universidade–corporação, da fundação (2020) à dissolução (2025)."),
    ("ex_cap4.tex", "4", "A rede que Marcelo construiu",
     "Seguindo Marcelo Finger e o projeto SPIRA: a cadeia de translações que "
     "converte a voz de pacientes com Covid-19 em espectrogramas processados "
     "por redes neurais — da fala ao dado ao diagnóstico — e sua política "
     "ontológica."),
    ("ex_cap5.tex", "", "Considerações finais",
     "O arremate da tese: como seguir múltiplos atores articula as negociações "
     "institucionais e as práticas tecnocientíficas situadas na produção de "
     "conhecimento em e sobre inteligência artificial."),
]

ENV_RE = re.compile(
    r'\\begin\{(figure|table|longtable)\*?\}'
    r'|\\end\{(figure|table|longtable)\*?\}'
    r'|\\caption(?:\[([^\]]*)\])?\{')

SEC_RE = re.compile(r'\\(section|subsection)\*?\s*\{')


def _trunc(s: str, n: int = 170) -> str:
    s = s.strip()
    return s if len(s) <= n else s[:n - 1].rstrip() + "…"


def _pre(s: str) -> str:
    """Remove ruído de LaTeX preservando caixa, acentos e hífens (para exibição)."""
    s = re.sub(r"(?<!\\)%.*", "", s)                                   # comentários
    s = re.sub(r"\\(begin|end)\{[^}]*\}", " ", s)                      # ambientes
    s = re.sub(r"\\label\{[^}]*\}", " ", s)
    s = re.sub(r"\\(ref|cref|Cref|autoref|eqref|pageref|nameref)\{[^}]*\}", " ", s)
    s = re.sub(r"\\(parencite|textcite|cite[a-zA-Z]*)\*?(?:\[[^\]]*\])*\{[^}]*\}", " ", s)
    s = re.sub(r"\\includegraphics(?:\[[^\]]*\])?\{[^}]*\}", " ", s)
    s = re.sub(r"\\footnote\{[^{}]*\}", " ", s)
    s = re.sub(r"\\(selectlanguage|setstretch|setlength)\{[^}]*\}", " ", s)
    s = re.sub(r"\\(begingroup|endgroup|noindent|large|Large|centering|small|par)\b", " ", s)
    return s


def first_sentence(tex_segment: str) -> str:
    """Primeira frase de prosa de um trecho .tex (para nota de seção)."""
    txt = re.sub(r"\s+", " ", clean_title(_pre(tex_segment))).strip()
    m = re.search(r"(.+?[.!?])(\s|$)", txt)
    sent = (m.group(1) if m else txt)
    return _trunc(sent, 180)


def parse_outline(tex: str) -> list[dict]:
    """Seções (com subseções e nota de 1ª frase), na ordem do documento."""
    secs: list[dict] = []
    seen = False
    matches = list(SEC_RE.finditer(tex))
    for idx, m in enumerate(matches):
        kind = m.group(1)
        arg, nxt = _match_brace_arg(tex, m.end() - 1)
        title = clean_title(arg)
        if not title:
            continue
        # trecho até o próximo section/subsection → nota (1ª frase)
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(tex)
        body = tex[nxt:end]
        # corta no primeiro ambiente para evitar legendas como "nota"
        cut = re.search(r"\\begin\{(figure|table|longtable|itemize|enumerate)", body)
        if cut:
            body = body[:cut.start()]
        nota = first_sentence(body)
        if kind == "section" or not seen:
            seen = seen or kind == "section"
            secs.append({"t": title, "nota": nota, "subs": []})
        else:
            if secs:
                secs[-1]["subs"].append(title)
    return secs


def parse_captions(tex: str):
    """(figuras, tabelas): legendas na ordem do documento, por ambiente."""
    figs, tabs = [], []
    stack = []
    for m in ENV_RE.finditer(tex):
        g = m.group(0)
        if g.startswith(r"\begin"):
            stack.append(m.group(1))
        elif g.startswith(r"\end"):
            if stack:
                stack.pop()
        else:  # \caption
            short = m.group(3)
            if short:
                cap = clean_title(short)
            else:
                arg, _ = _match_brace_arg(tex, m.end() - 1)
                cap = _trunc(clean_title(arg))
            if not cap:
                continue
            env = stack[-1] if stack else "figure"
            (tabs if env in ("table", "longtable") else figs).append(cap)
    return figs, tabs


def parse_resumo(src: Path):
    raw = src.read_text(encoding="utf-8")
    clean = re.sub(r"\s+", " ", clean_title(_pre(raw))).strip()
    parts = re.split(r"Palavras[\s-]*chave\s*:?\s*", clean, maxsplit=1)
    resumo = parts[0].strip()
    palavras = []
    if len(parts) > 1:
        kw = parts[1].split(".")[0]   # só a frase das palavras-chave
        palavras = [k.strip() for k in re.split(r"[,;]", kw) if k.strip()]
    return resumo, palavras


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-root", type=Path, default=Path("/tmp/tese"))
    ap.add_argument("--out", type=Path, default=THIS_DIR / "tese_documento.json")
    ap.add_argument("--inject", type=Path, default=None)
    args = ap.parse_args()

    resumo, palavras = parse_resumo(args.source_root / "resumo.tex")

    sumario, figuras, tabelas = [], [], []
    fign = tabn = 0
    for fname, num, title, resumo_cap in CHAPTERS:
        src = args.source_root / fname
        if not src.exists():
            print(f"[doc] aviso: {fname} ausente, pulando.")
            continue
        tex = src.read_text(encoding="utf-8")
        sumario.append({
            "id": fname.replace("ex_", "").replace(".tex", ""),
            "num": num, "title": title, "resumo": resumo_cap,
            "sections": parse_outline(tex),
        })
        f, t = parse_captions(tex)
        for c in f:
            fign += 1
            figuras.append({"n": fign, "cap": num or title, "t": c})
        for c in t:
            tabn += 1
            tabelas.append({"n": tabn, "cap": num or title, "t": c})

    payload = {
        "resumo": resumo,
        "palavras_chave": palavras,
        "sumario": sumario,
        "figuras": figuras,
        "tabelas": tabelas,
    }
    data_str = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    args.out.write_text(data_str, encoding="utf-8")
    print(f"[doc] JSON: {args.out} ({args.out.stat().st_size/1024:.0f} KB) | "
          f"resumo={len(resumo)}c · {len(palavras)} palavras-chave · "
          f"{len(sumario)} capítulos · {len(figuras)} figuras · {len(tabelas)} tabelas")

    if args.inject is not None:
        assert "</script" not in data_str.lower()
        html = args.inject.read_text(encoding="utf-8")
        pat = re.compile(r'(<script type="application/json" id="docdata">).*?(</script>)', re.DOTALL)
        new, n = pat.subn(lambda m: m.group(1) + data_str + m.group(2), html, count=1)
        if n != 1:
            print(f"[doc] ERRO: <script id=docdata> não encontrado em {args.inject}")
            return 1
        args.inject.write_text(new, encoding="utf-8")
        print(f"[doc] reinjetado em {args.inject}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
