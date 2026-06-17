#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cache_busting_figuras.py
========================
Anexa (ou atualiza) um parâmetro de versão ``?v=<hash>`` em cada URL de figura
referenciada no index.html (atributos ``src=`` e ``href=`` que apontam para
``figuras/...``). O hash vem do CONTEÚDO do arquivo, então a versão só muda
quando a figura muda — forçando o navegador a rebaixar exatamente as imagens
atualizadas, sem invalidar o cache das demais.

Resolve o problema clássico do GitHub Pages: quando uma figura é regenerada
mas mantém o mesmo nome de arquivo, o navegador continua exibindo a versão
em cache. Rode este script sempre que as figuras forem atualizadas.

Uso:
    python3 scripts/cache_busting_figuras.py
"""
from __future__ import annotations

import hashlib
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
INDEX = os.path.join(ROOT, os.environ.get("SITE_INDEX", "index.html"))

# captura: attr=("|') figuras/caminho.ext (?v=...)? ("|')
REF_RE = re.compile(
    r"""(?P<attr>\b(?:src|href)=)(?P<q>["'])"""
    r"""(?P<path>figuras/[^"'?]+?\.(?:png|jpg|jpeg|gif|svg|webp|pdf))"""
    r"""(?:\?v=[0-9a-f]+)?"""
    r"""(?P=q)""",
    re.IGNORECASE,
)


def short_hash(abs_path: str) -> str | None:
    if not os.path.isfile(abs_path):
        return None
    h = hashlib.sha256()
    with open(abs_path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()[:10]


def main() -> int:
    html = open(INDEX, encoding="utf-8").read()
    stats = {"updated": 0, "missing": 0, "unchanged": 0}
    missing: set[str] = set()

    def repl(m: re.Match) -> str:
        path = m.group("path")
        digest = short_hash(os.path.join(ROOT, path))
        if digest is None:
            stats["missing"] += 1
            missing.add(path)
            return m.group(0)  # arquivo ausente: não mexe
        q = m.group("q")
        stats["updated"] += 1
        return f"{m.group('attr')}{q}{path}?v={digest}{q}"

    new_html = REF_RE.sub(repl, html)
    if new_html != html:
        open(INDEX, "w", encoding="utf-8").write(new_html)
    print(f"cache-busting: {stats['updated']} referência(s) versionada(s); "
          f"{stats['missing']} sem arquivo local (mantidas).")
    if missing:
        print("  arquivos não encontrados (referência mantida sem versão):")
        for p in sorted(missing):
            print("   -", p)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
