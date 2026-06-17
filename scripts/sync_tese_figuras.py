#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sync_tese_figuras.py
====================
Sincroniza figuras de CONTEÚDO da tese para o site, conforme o mapa
``infranodus/figuras_tese_map.tsv``.

Cada linha do mapa liga um destino no site a uma origem na tese (um glob,
para tolerar nomes com timestamp que mudam a cada re-exportação). Para cada
entrada, copia-se a origem MAIS RECENTE que casa com o glob para o destino no
site — mas só quando o conteúdo difere, evitando churn desnecessário.

Diferente de ``sync_site_figuras.py`` (que cuida das figuras de análise
geradas aqui), este trata as figuras autorais da tese (diagramas, imagens,
gráficos) que são exibidas no site.

Uso:
    python3 scripts/sync_tese_figuras.py --source-root _tex
    python3 scripts/sync_tese_figuras.py --source-root /caminho/da/tese --dry-run
"""
from __future__ import annotations

import argparse
import glob
import os
import shutil
import sys
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent
REPO_ROOT = THIS_DIR.parent
DEFAULT_MANIFEST = REPO_ROOT / "infranodus" / "figuras_tese_map.tsv"


def _same_bytes(a: Path, b: Path) -> bool:
    if not a.exists() or not b.exists() or a.stat().st_size != b.stat().st_size:
        return False
    with a.open("rb") as fa, b.open("rb") as fb:
        while True:
            ca, cb = fa.read(65536), fb.read(65536)
            if ca != cb:
                return False
            if not ca:
                return True


def _newest(paths: list[str]) -> str | None:
    paths = [p for p in paths if os.path.isfile(p)]
    if not paths:
        return None
    return max(paths, key=lambda p: os.path.getmtime(p))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source-root", type=Path, default=REPO_ROOT / "_tex",
                    help="Diretório onde a tese (.tex) está montada (padrão: ./_tex).")
    ap.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not args.manifest.exists():
        print(f"manifesto não encontrado: {args.manifest}")
        return 2

    copied = unchanged = missing = 0
    no_source: list[str] = []
    for raw in args.manifest.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "\t" not in line:
            continue
        dest_rel, src_glob = (x.strip() for x in line.split("\t", 1))
        src = _newest(glob.glob(str(args.source_root / src_glob)))
        if src is None:
            missing += 1
            no_source.append(src_glob)
            continue
        dest = REPO_ROOT / dest_rel
        if _same_bytes(Path(src), dest):
            unchanged += 1
            continue
        print(f"{'(dry) ' if args.dry_run else ''}atualiza {dest_rel}  <-  "
              f"{os.path.relpath(src, args.source_root)}")
        if not args.dry_run:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(src, dest)
        copied += 1

    print(f"\n{copied} figura(s) {'seriam ' if args.dry_run else ''}atualizada(s); "
          f"{unchanged} já em dia; {missing} sem origem na tese.")
    if no_source:
        print("  sem origem (glob não casou — figura ainda não está na tese?):")
        for g in no_source:
            print("   -", g)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
