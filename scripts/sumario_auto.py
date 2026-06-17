#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sumario_auto.py
===============
Gera o "Sumário do capítulo" automaticamente a partir da estrutura do
.tex (\\section / \\subsection, na ordem do documento) e injeta os dados
num objeto JS dentro do index.html, entre os marcadores:

    /*SUMARIO-AUTO-START*/ ... /*SUMARIO-AUTO-END*/

O painel de cada capítulo renderiza esse sumário ao abrir (PT e EN). Os
títulos são os da tese (PT). Assim o sumário aparece ATUALIZADO no site
a cada mudança da tese, sem tocar no conteúdo curado.

Uso:
    python scripts/sumario_auto.py [--source-root _tex]
"""
import argparse
import json
import os
import re
from pathlib import Path

from relatorio_divergencia_tese import (CHAPTER_FILES, clean_title,
                                        _match_brace_arg, _commands)

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent
# página alvo (curada). Configurável via env SITE_INDEX; padrão index.html.
INDEX = REPO_ROOT / os.environ.get("SITE_INDEX", "index.html")

# slug do capítulo -> id do nó-capítulo no grafo/index.html
NODE_ID = {"cap1": "cap1m", "cap2": "cap2", "cap3": "cap3", "cap4": "cap4"}

MARK = re.compile(r"/\*SUMARIO-AUTO-START\*/.*?/\*SUMARIO-AUTO-END\*/",
                  re.DOTALL)


def esc(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def parse_outline(tex: str) -> list[dict]:
    """Lista ordenada de seções, cada uma com suas subseções."""
    pat = re.compile(r"\\(section|subsection)\*?\s*\{")
    secs: list[dict] = []
    seen_section = False
    i = 0
    while True:
        m = pat.search(tex, i)
        if not m:
            break
        kind = m.group(1)
        arg, nxt = _match_brace_arg(tex, m.end() - 1)
        title = clean_title(arg)
        if not title:
            i = nxt
            continue
        if kind == "section":
            seen_section = True
            secs.append({"t": title, "subs": []})
        elif not seen_section:
            # subseções antes da 1ª \section são intros de capítulo:
            # o site as trata como seções de topo, então promovemos.
            secs.append({"t": title, "subs": []})
        else:
            secs[-1]["subs"].append(title)
        i = nxt
    return secs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-root", type=Path, default=REPO_ROOT / "_tex")
    args = ap.parse_args()

    data: dict[str, list] = {}
    for slug, fname in CHAPTER_FILES.items():
        src = args.source_root / fname
        if not src.exists():
            print(f"[sumario] aviso: {fname} não encontrado, pulando.")
            continue
        tex = src.read_text(encoding="utf-8")
        outline = parse_outline(tex)
        figs = [clean_title(c) for c in _commands(tex, "caption")]
        figs = [f for f in figs if f]
        if outline or figs:
            data[NODE_ID[slug]] = {"secs": outline, "figs": figs}

    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    repl = "/*SUMARIO-AUTO-START*/var SUMARIO_AUTO=" + payload + ";/*SUMARIO-AUTO-END*/"

    html = INDEX.read_text(encoding="utf-8")
    if not MARK.search(html):
        print("[sumario] ERRO: marcadores SUMARIO-AUTO não encontrados em index.html")
        return 1
    new = MARK.sub(lambda _: repl, html, count=1)
    INDEX.write_text(new, encoding="utf-8")

    tot = sum(len(v["secs"]) for v in data.values())
    print(f"[sumario] {len(data)} capítulos, {tot} seções injetadas em index.html")
    for k, v in data.items():
        print(f"  - {k}: {len(v['secs'])} seções, "
              f"{sum(len(s['subs']) for s in v['secs'])} subseções, "
              f"{len(v['figs'])} figuras")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
