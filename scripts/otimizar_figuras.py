#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
otimizar_figuras.py
===================
Gera uma versão WebP otimizada de cada figura raster (PNG/JPG) em ``figuras/``
e reescreve as referências do ``index.html`` de ``.png``/``.jpg`` para
``.webp``. O objetivo é reduzir o peso que o visitante baixa ao abrir os
painéis de figura, sem perder os arquivos originais (as PNGs continuam no
repositório como saída nativa da análise).

Onde entra no pipeline
----------------------
Este passo roda no ``analyze.yml`` DEPOIS de toda sincronização e injeção de
figuras (``sync_site_figuras.py``, ``sync_tese_figuras.py``,
``tese_network*.py``, ``tese_documento.py``) e ANTES do cache-busting
(``cache_busting_figuras.py``). Assim, mesmo que a injeção volte a escrever
referências ``.png`` a cada regeneração, este script as reconverte para
``.webp`` de forma idempotente, e o cache-busting versiona os ``.webp``
resultantes.

Determinismo
------------
A codificação WebP do Pillow é determinística para a mesma entrada e os mesmos
parâmetros. Combinado com ``PYTHONHASHSEED=0`` (já usado pelo workflow), a
regeneração só produz commit quando uma figura de fato muda.

Uso:
    python scripts/otimizar_figuras.py [--force] [--dry-run]
    SITE_INDEX=index.html python scripts/otimizar_figuras.py

Opções:
    --force     reconverte mesmo que o .webp já esteja atualizado.
    --dry-run   mostra o que faria, sem escrever WebP nem tocar no index.html.
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
FIGURAS = ROOT / "figuras"
INDEX = ROOT / os.environ.get("SITE_INDEX", "index.html")

# Parâmetros de otimização.
QUALITY = 82          # qualidade WebP com perda; ~82 é indistinguível a olho.
METHOD = 6            # esforço de compressão do encoder (0..6); 6 = melhor.
MAX_SIDE = 3500       # px: só reduz imagens acima disso (nunca amplia).

RASTER_EXTS = {".png", ".jpg", ".jpeg"}

# Captura caminhos figuras/....(png|jpg|jpeg) entre aspas (atributos src=/href=
# ou strings em JS, como no array ANALISES), com ?v=... opcional. Mesma lógica
# do cache_busting_figuras.py.
REF_RE = re.compile(
    r"""(?P<q>["'])"""
    r"""(?P<path>figuras/[^"'?]+?\.(?:png|jpg|jpeg))"""
    r"""(?:\?v=[0-9a-f]+)?"""
    r"""(?P=q)""",
    re.IGNORECASE,
)


def _needs_rebuild(src: Path, dst: Path, force: bool) -> bool:
    if force or not dst.exists():
        return True
    return src.stat().st_mtime > dst.stat().st_mtime


def converter_um(src: Path, dry: bool, force: bool) -> tuple[bool, int, int]:
    """Converte uma imagem para WebP ao lado. Retorna (convertida, orig, novo)."""
    dst = src.with_suffix(".webp")
    orig = src.stat().st_size
    if not _needs_rebuild(src, dst, force):
        return False, orig, dst.stat().st_size if dst.exists() else 0
    if dry:
        return True, orig, 0

    with Image.open(src) as im:
        # Preserva transparência quando existe; caso contrário usa RGB.
        if im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info):
            im = im.convert("RGBA")
        else:
            im = im.convert("RGB")

        largest = max(im.size)
        if largest > MAX_SIDE:
            escala = MAX_SIDE / largest
            novo_tam = (round(im.size[0] * escala), round(im.size[1] * escala))
            im = im.resize(novo_tam, Image.LANCZOS)

        im.save(dst, "WEBP", quality=QUALITY, method=METHOD)

    return True, orig, dst.stat().st_size


def reescrever_index(dry: bool) -> tuple[int, int]:
    """Reescreve refs .png/.jpg -> .webp no index.html quando o .webp existe.

    O ?v= é descartado aqui; o cache_busting_figuras.py, que roda em seguida,
    reanexa o hash correto do arquivo .webp.
    """
    if not INDEX.exists():
        print(f"AVISO: {INDEX} não encontrado; pulando reescrita.")
        return 0, 0
    html = INDEX.read_text(encoding="utf-8")
    trocadas = mantidas = 0

    def repl(m: re.Match) -> str:
        nonlocal trocadas, mantidas
        path = m.group("path")
        webp_rel = re.sub(r"\.(png|jpg|jpeg)$", ".webp", path, flags=re.IGNORECASE)
        if (ROOT / webp_rel).is_file():
            trocadas += 1
            q = m.group("q")
            return f"{q}{webp_rel}{q}"
        mantidas += 1
        return m.group(0)

    novo = REF_RE.sub(repl, html)
    if novo != html and not dry:
        INDEX.write_text(novo, encoding="utf-8")
    return trocadas, mantidas


def main() -> int:
    args = sys.argv[1:]
    dry = "--dry-run" in args
    force = "--force" in args

    if not FIGURAS.is_dir():
        print(f"ERRO: pasta {FIGURAS} não existe.")
        return 1

    rasters = sorted(
        p for p in FIGURAS.rglob("*")
        if p.is_file() and p.suffix.lower() in RASTER_EXTS
    )

    convertidas = 0
    soma_orig = soma_novo = 0
    for src in rasters:
        conv, orig, novo = converter_um(src, dry, force)
        soma_orig += orig
        soma_novo += novo
        if conv:
            convertidas += 1
            reducao = (100 * (1 - novo / orig)) if (novo and orig) else 0
            marca = "(dry) " if dry else ""
            print(f"{marca}{src.relative_to(ROOT)}  "
                  f"{orig/1e6:.2f}MB -> {novo/1e6:.2f}MB  ({reducao:.0f}% menor)")

    trocadas, mantidas = reescrever_index(dry)

    print("")
    print(f"WebP: {convertidas}/{len(rasters)} imagem(ns) (re)convertida(s).")
    if soma_novo:
        print(f"Total rasters: {soma_orig/1e6:.1f}MB (PNG/JPG)  ->  "
              f"{soma_novo/1e6:.1f}MB (WebP)  "
              f"({100*(1 - soma_novo/soma_orig):.0f}% menor)")
    print(f"index.html: {trocadas} referência(s) apontando para .webp; "
          f"{mantidas} mantida(s) sem .webp correspondente.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
