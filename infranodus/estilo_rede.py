# -*- coding: utf-8 -*-
"""Identidade visual compartilhada das figuras de rede e trajetória da tese.

Alinha as redes InfraNodus e os diagramas de trajetória à paleta-mestra
adotada nas figuras do capítulo 2 (Okabe-Ito categórico, viridis sequencial,
marcador "bolinha" com borda branca, notação numérica pt-BR). Mantido
autônomo para os scripts continuarem reproduzíveis sem dependência externa.
"""
from __future__ import annotations

import numpy as np

# Núcleo categórico Okabe-Ito (à prova de daltonismo) na ordem de melhor
# separação para comunidades de rede.
OKABE_ITO_ORD = [
    "#0072B2",  # azul
    "#E69F00",  # laranja
    "#009E73",  # verde
    "#CC79A7",  # magenta
    "#56B4E9",  # azul claro
    "#D55E00",  # vermelho
    "#F0E442",  # amarelo
    "#999999",  # cinza
]
# Extensão para quando há mais comunidades/conceitos que o núcleo comporta
# (Gantt e alluvial chegam a 20), sem cair no arco-íris saturado.
_EXTENSAO = OKABE_ITO_ORD + [
    "#3a5fa0", "#b5651d", "#1b7a5a", "#8e4585", "#7fb2d6", "#a04000",
    "#c9b037", "#5a5a5a", "#264f78", "#d98c5f", "#2e8b57", "#b76e9b",
]

# Cores fixas de marcação na trajetória semântica (início/fim), do Okabe-Ito.
COR_INICIO = "#009E73"   # verde: início da leitura
COR_FIM = "#D55E00"      # vermelho: fim da leitura

# Tons neutros do desenho (fundo, arestas, borda da bolinha, texto).
COR_FUNDO = "#ffffff"
COR_ARESTA = "#9aa3ad"
COR_BORDA_NO = "#ffffff"  # borda branca da bolinha (identidade visual)
COR_TEXTO = "#0e1116"


def cores_categoricas(n: int) -> list[str]:
    """Devolve ``n`` cores categóricas a partir do Okabe-Ito (cicla se faltar)."""
    if n <= 0:
        return []
    return [_EXTENSAO[i % len(_EXTENSAO)] for i in range(n)]


def paleta_rgba(n: int):
    """Versão RGBA (0--1) das cores categóricas, p/ APIs que pedem array."""
    from matplotlib.colors import to_rgba
    return np.array([to_rgba(c) for c in cores_categoricas(max(n, 1))])


def num_ptbr(valor) -> str:
    """Inteiro pt-BR: ponto como separador de milhar."""
    return f"{int(round(valor)):,}".replace(",", ".")


def pct_ptbr(valor, casas: int = 1) -> str:
    """Número pt-BR com vírgula decimal, sem o símbolo '%'."""
    return f"{valor:,.{casas}f}".replace(",", "\x00").replace(".", ",").replace("\x00", ".")
