#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tese_network.py
===============
Gera a rede textual da TESE INTEIRA (Apresentação + capítulos 1–4 +
Considerações Finais) reaproveitando o pipeline de `infranodus_cap1.py`
(co-ocorrência · NPMI · Louvain · PageRank). Exporta um JSON compacto
para o site renderizar como grafo principal.

Cada capítulo é tokenizado separadamente e os fluxos são unidos com um
"sentinela" de quebra para impedir arestas espúrias na fronteira entre
capítulos. Registra ainda em quais capítulos cada termo aparece.

Uso:
    python3 infranodus/tese_network.py --source-root /tmp/tese
Saída:
    infranodus/tese_network.json
"""
import argparse
import json
from pathlib import Path

from infranodus_cap1 import (extract_tokens, build_graph, compute_npmi,
                             annotate_npmi, prune_graph, compute_metrics,
                             detect_topics, label_topic)

THIS_DIR = Path(__file__).resolve().parent

# (arquivo .tex, rótulo de capítulo no site, id curto)
CHAPTERS = [
    ("ex_cap0.tex", "Apresentação", "apresentacao"),
    ("ex_cap1.tex", "Capítulo 1 · método", "cap1"),
    ("ex_cap2.tex", "Capítulo 2 · figurações", "cap2"),
    ("ex_cap3.tex", "Capítulo 3 · C4AI", "cap3"),
    ("ex_cap4.tex", "Capítulo 4 · SPIRA", "cap4"),
    ("ex_cap5.tex", "Considerações finais", "final"),
]

# paleta para as comunidades (Louvain) — tons calmos, estilo cartográfico
PALETTE = ["#6c8ebf", "#9b59c6", "#56b04a", "#ef8a3c", "#27adc4",
           "#d6489b", "#e0a82e", "#8a76c4", "#3fa6bd", "#c0556a",
           "#5f9e6e", "#b07cc6"]

BREAK = "brk"  # sentinela: não colide com nenhum token real


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-root", type=Path, default=Path("/tmp/tese"))
    ap.add_argument("--top-n", type=int, default=260,
                    help="nós mantidos na rede completa (por frequência)")
    ap.add_argument("--min-edge", type=int, default=3,
                    help="peso mínimo de aresta na poda")
    ap.add_argument("--core", type=int, default=80,
                    help="nº de termos na vista núcleo (por PageRank)")
    ap.add_argument("--out", type=Path, default=THIS_DIR / "tese_network.json")
    args = ap.parse_args()

    all_tokens: list[str] = []
    term_chapters: dict[str, set[str]] = {}
    per_chapter_counts: list[tuple[str, int]] = []

    for fname, label, cid in CHAPTERS:
        src = args.source_root / fname
        if not src.exists():
            print(f"[tese] aviso: {fname} não encontrado, pulando.")
            continue
        toks = extract_tokens(src.read_text(encoding="utf-8"))
        per_chapter_counts.append((cid, len(toks)))
        for t in set(toks):
            term_chapters.setdefault(t, set()).add(cid)
        all_tokens.extend(toks)
        all_tokens.extend([BREAK] * 4)  # impede janela cruzar capítulos

    print(f"[1] Tokens totais: {len(all_tokens):,} "
          f"({', '.join(f'{c}:{n}' for c, n in per_chapter_counts)})")

    G_full = build_graph(all_tokens, window=4)
    npmi = compute_npmi(all_tokens, window=4)
    annotate_npmi(G_full, npmi)
    if BREAK in G_full:
        G_full.remove_node(BREAK)
    print(f"    Rede completa: {G_full.number_of_nodes()} nós, "
          f"{G_full.number_of_edges()} arestas")

    G = prune_graph(G_full, top_n=args.top_n, min_edge_weight=args.min_edge)
    annotate_npmi(G, npmi)
    print(f"[2] Após poda: {G.number_of_nodes()} nós, {G.number_of_edges()} arestas")

    deg, btw, pr = compute_metrics(G)
    comms = detect_topics(G)
    print(f"[3] Comunidades: {len(comms)} | tamanhos: {[len(c) for c in comms]}")

    # id de comunidade por nó
    comm_of: dict[str, int] = {}
    for i, c in enumerate(comms):
        for n in c:
            comm_of[n] = i

    # núcleo: top-N por PageRank
    core = sorted(G.nodes(), key=lambda n: pr.get(n, 0), reverse=True)[:args.core]
    core_set = set(core)

    # ordem de capítulo para um termo (menor índice em que aparece) — para cor de origem
    order = {cid: k for k, (_, _, cid) in enumerate(CHAPTERS)}

    nodes = []
    for n in G.nodes():
        chs = sorted(term_chapters.get(n, set()), key=lambda c: order.get(c, 99))
        nodes.append({
            "id": n,
            "community": comm_of.get(n, 0),
            "freq": int(G.nodes[n].get("freq", 0)),
            "degree": round(float(deg.get(n, 0)), 1),
            "pagerank": round(float(pr.get(n, 0)), 5),
            "betweenness": round(float(btw.get(n, 0)), 4),
            "chapters": chs,
            "core": n in core_set,
        })

    edges = []
    for u, v, d in G.edges(data=True):
        edges.append({
            "s": u, "t": v,
            "w": round(float(d.get("weight", 0)), 1),
            "npmi": round(float(d.get("npmi", 0)), 3),
        })

    communities = []
    for i, c in enumerate(comms):
        communities.append({
            "id": i,
            "size": len(c),
            "label": label_topic(c, deg, k=5),
            "color": PALETTE[i % len(PALETTE)],
        })

    payload = {
        "generated_from": "tese (Apresentação + cap1–4 + Considerações Finais)",
        "params": {"window": 4, "top_n": args.top_n,
                   "min_edge": args.min_edge, "core": args.core},
        "chapters": [{"id": cid, "label": label} for _, label, cid in CHAPTERS],
        "communities": communities,
        "nodes": nodes,
        "edges": edges,
    }
    args.out.write_text(json.dumps(payload, ensure_ascii=False,
                                   separators=(",", ":")), encoding="utf-8")
    kb = args.out.stat().st_size / 1024
    print(f"[4] JSON: {args.out}  ({kb:.0f} KB)  "
          f"{len(nodes)} nós, {len(edges)} arestas, {len(communities)} comunidades, "
          f"núcleo={len(core)}")
    # prévia das comunidades
    for c in communities:
        print(f"    T{c['id']} ({c['size']}): {', '.join(c['label'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
