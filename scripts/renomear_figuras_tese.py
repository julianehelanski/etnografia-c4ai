#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
renomear_figuras_tese.py
========================
Renomeia os arquivos de figura da TESE (repositório tecno-etnografia-centro-ia)
conforme o título curto declarado em ``\\caption[...]`` e atualiza os caminhos
``\\includegraphics{...}`` correspondentes, para que a tese continue compilando.

Padrão do novo nome:  ``cap<N>-<slug-do-titulo-curto><ext>``
  - prefixo do capítulo deduzido do caminho (``figuras/cap.3/...`` → ``cap3``)
    ou, na falta, do nome do arquivo .tex (``ex_cap3.tex`` → ``cap3``);
  - slug: título curto com LaTeX removido (``\\texttt{C4AI}`` → ``c4ai``,
    ``\\ref{...}``/``\\footnote{...}`` descartados), acentos removidos, tudo em
    minúsculas, conteúdo entre parênteses (datas etc.) removido, e qualquer
    caractere não alfanumérico convertido em hífen.

Regras de segurança:
  - só renomeia arquivo que EXISTE em disco;
  - se o mesmo arquivo for incluído em mais de uma figura com títulos
    diferentes, mantém o primeiro nome e avisa (não duplica o git mv);
  - múltiplos ``\\includegraphics`` numa mesma figura recebem sufixo -1, -2, …;
  - colisões de nome no mesmo diretório recebem sufixo numérico.

Uso:
    # simulação (não altera nada) — imprime o mapa antigo -> novo:
    python3 scripts/renomear_figuras_tese.py /caminho/para/a/tese

    # aplica de fato (git mv + reescreve os .tex):
    python3 scripts/renomear_figuras_tese.py /caminho/para/a/tese --apply

Depois de --apply, revise com `git status`/`git diff` no repositório da tese e
faça o commit/push por lá.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
import unicodedata
from collections import defaultdict


ENV_RE = re.compile(r"\\begin\{figure\*?\}(.*?)\\end\{figure\*?\}", re.DOTALL)
INC_RE = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}")
# título curto: primeiro [...] depois de \caption, tolerando um nível de [ ]
CAP_SHORT_RE = re.compile(r"\\caption\[((?:[^\[\]]|\[[^\]]*\])*)\]")


def deaccent(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c))


def strip_latex(s: str) -> str:
    # comandos cujo conteúdo deve sumir por inteiro
    s = re.sub(r"\\(?:ref|cref|Cref|autoref|pageref|eqref|label|protect|footnote)"
               r"\b\s*\{[^{}]*\}", " ", s)
    # \cmd{conteudo} -> conteudo  (ex.: \texttt{C4AI} -> C4AI)
    for _ in range(3):
        s = re.sub(r"\\[a-zA-Z]+\*?\s*\{([^{}]*)\}", r" \1 ", s)
    # comandos soltos remanescentes
    s = re.sub(r"\\[a-zA-Z]+\*?", " ", s)
    return s.replace("~", " ")


def slugify(title: str) -> str:
    t = strip_latex(title)
    t = re.sub(r"\([^()]*\)", " ", t)          # remove (datas) e afins
    t = deaccent(t).lower()
    t = re.sub(r"[^a-z0-9]+", "-", t)
    return re.sub(r"-{2,}", "-", t).strip("-")


def chapter_prefix(inc_path: str, tex_name: str) -> str:
    m = re.search(r"cap\.?(\d+)", inc_path)
    if m:
        return "cap" + m.group(1)
    m = re.search(r"cap(\d+)", tex_name)
    return "cap" + m.group(1) if m else "cap"


FILE_EXTS = ["", ".pdf", ".png", ".jpg", ".jpeg", ".PNG", ".JPG", ".JPEG",
             ".pdf_tex", ".eps"]


def resolve_file(root: str, ref: str) -> str | None:
    """Devolve a extensão real do arquivo em disco para uma referência
    (que pode vir sem extensão, como é comum no LaTeX). None se não existir."""
    for e in FILE_EXTS:
        if os.path.exists(os.path.join(root, ref + e)):
            return e
    return None


def collect(root: str):
    """Varre os .tex e devolve (renomeações, avisos, refs sem arquivo, tex_files).

    Cada renomeação é (ref_antiga, ref_nova, arquivo_antigo, arquivo_novo):
      - ref_*    : o que aparece dentro de \\includegraphics{...} (pode não ter
                   extensão; preservamos o estilo);
      - arquivo_*: o caminho real em disco (com a extensão verdadeira).
    """
    rows: list[tuple[str, str, str, str]] = []
    seen_src: dict[str, tuple[str, str]] = {}   # ref original -> (ref nova, arq novo)
    used_targets: dict[tuple[str, str], int] = defaultdict(int)
    warnings: list[str] = []
    unresolved: list[str] = []

    tex_files = []
    for dirpath, _dirs, files in os.walk(root):
        if os.sep + ".git" in dirpath:
            continue
        for fn in files:
            if fn.endswith(".tex"):
                tex_files.append(os.path.join(dirpath, fn))
    tex_files.sort()

    for full in tex_files:
        tex_name = os.path.basename(full)
        txt = open(full, encoding="utf-8", errors="replace").read()
        for env in ENV_RE.findall(txt):
            capm = CAP_SHORT_RE.search(env)
            if not capm:
                continue
            incs = INC_RE.findall(env)
            if not incs:
                continue
            slug = slugify(capm.group(1))
            if not slug:
                warnings.append(f"título curto vazio após limpeza em {tex_name}: "
                                f"{capm.group(1)!r}")
                continue
            for i, inc in enumerate(incs):
                inc = inc.strip()
                if inc in seen_src:
                    warnings.append(
                        f"arquivo incluído em mais de uma figura, mantendo "
                        f"o 1º nome: {inc} -> {seen_src[inc][0]}")
                    continue
                real_ext = resolve_file(root, inc)
                if real_ext is None:
                    unresolved.append(inc)   # arquivo ausente: NÃO mexer
                    continue
                d = os.path.dirname(inc)
                ref_ext = os.path.splitext(os.path.basename(inc))[1]  # estilo da ref
                prefix = chapter_prefix(inc, tex_name)
                newstem = f"{prefix}-{slug}"
                if len(incs) > 1:
                    newstem += f"-{i + 1}"
                key = (d, newstem)
                used_targets[key] += 1
                if used_targets[key] > 1:
                    newstem = f"{newstem}-{used_targets[key]}"
                # extensão verdadeira do arquivo: a da própria ref, se houver;
                # senão, a descoberta em disco (refs LaTeX costumam vir sem ext).
                file_ext = ref_ext if ref_ext else real_ext
                new_ref = os.path.join(d, newstem + ref_ext) if d else newstem + ref_ext
                old_file = inc + ("" if ref_ext else real_ext)
                new_file = os.path.join(d, newstem + file_ext) if d else newstem + file_ext
                seen_src[inc] = (new_ref, new_file)
                if new_ref != inc:
                    rows.append((inc, new_ref, old_file, new_file))
    return rows, warnings, unresolved, tex_files


def apply_renames(root: str, rows, tex_files: list[str]) -> None:
    # 1) git mv dos arquivos reais (todos existem: collect já filtrou)
    moved = 0
    for _old_ref, _new_ref, old_file, new_file in rows:
        new_abs = os.path.join(root, new_file)
        os.makedirs(os.path.dirname(new_abs), exist_ok=True)
        r = subprocess.run(["git", "-C", root, "mv", old_file, new_file],
                           capture_output=True, text=True)
        if r.returncode != 0:
            os.replace(os.path.join(root, old_file), new_abs)
            subprocess.run(["git", "-C", root, "add", new_file], check=False)
            subprocess.run(["git", "-C", root, "rm", "--cached", old_file],
                           check=False, capture_output=True)
        moved += 1
    # 2) reescreve as referências nos .tex (substitui {ref_antiga} -> {ref_nova})
    repl = {old_ref: new_ref for old_ref, new_ref, _o, _n in rows}
    edited = 0
    for full in tex_files:
        txt = open(full, encoding="utf-8", errors="replace").read()
        orig = txt
        for old_ref, new_ref in repl.items():
            txt = txt.replace("{" + old_ref + "}", "{" + new_ref + "}")
        if txt != orig:
            open(full, "w", encoding="utf-8").write(txt)
            edited += 1
    print(f"\n[apply] {moved} arquivo(s) renomeado(s); {edited} .tex reescrito(s).")


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    apply = "--apply" in sys.argv
    if not args:
        print(__doc__)
        return 2
    root = args[0]
    if not os.path.isdir(root):
        print(f"diretório não encontrado: {root}")
        return 2

    rows, warnings, unresolved, tex_files = collect(root)
    print(f"{len(rows)} renomeação(ões) proposta(s) "
          f"({'APLICANDO' if apply else 'simulação — use --apply para aplicar'})\n")
    for old_ref, new_ref, _o, _n in rows:
        print(f"{old_ref}\n   -> {new_ref}")
    if warnings:
        print("\n--- avisos ---")
        for w in warnings:
            print("  *", w)
    if unresolved:
        print(f"\n--- {len(unresolved)} referência(s) sem arquivo em disco "
              f"(NÃO alteradas; provavelmente figuras geradas no build ou "
              f"ausentes do repositório) ---")
        for u in unresolved:
            print("  -", u)
    if apply:
        apply_renames(root, rows, tex_files)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
