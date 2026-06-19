# {tecno-etnografia} — Rede textual da tese

Site interativo que acompanha a tese de doutorado **"{tecno-etnografia} de um
centro de inteligência artificial: seguindo cientistas e engenheiros —
universidade afora"** (Juliane Helanski · PPGCS/IFCH · Unicamp · 2026).

A página principal é uma **rede textual da tese**: um grafo de co-ocorrência de
conceitos gerado a partir do `.tex`, organizado em territórios temáticos. Pela
aba **`{a tese}`** abre-se um modal com resumo, sumário comentado, as galerias
de figuras de cada capítulo e as listas de ilustrações e tabelas.

## Identidade visual: a sintaxe LaTeX é proposital

Os títulos e subtítulos do site são escritos na **sintaxe de comandos LaTeX**
(`\title{…}`, `\chapter{…}`, `\section{…}`, `\subsection{…}`), com a estética
do editor onde a tese é escrita — comandos e chaves em **azul neon**, texto do
autor em **preto**, tudo **monoespaçado**, como no Overleaf. Isso não é
decoração: é uma escolha que **marca três coisas ao mesmo tempo**:

1. **O Overleaf / o LaTeX** como o ambiente material em que a tese é, de fato,
   escrita e composta — a infraestrutura técnica fica à vista, não escondida.
2. **O próprio conceito de _tecno-etnografia_** que a tese propõe e desenvolve:
   descrever práticas tecnocientíficas sem apagar a técnica que as sustenta.
   A interface pratica o que a tese argumenta.
3. **A lógica de "chamada" do LaTeX**, transposta para o site. Em LaTeX, um
   comando como `\chapter{…}` *chama* e estrutura um trecho do documento. Aqui,
   transpondo essa lógica, os comandos **chamam a própria tese**: `\title{…}`
   chama o trabalho, `\chapter{…}` os capítulos, `\section{…}` as seções,
   `\subsection{…}` as subseções, `\palavraschave{…}` as palavras-chave — e
   `\url{…}` os mapas de cada capítulo.

Convenção de cores (estilo editor LaTeX):

| Elemento | Estilo |
| --- | --- |
| Sintaxe LaTeX (comando + chaves) | azul neon, monoespaçado, sem negrito |
| Texto do autor (argumento) | preto, monoespaçado, sem negrito |
| Título do trabalho | preto, monoespaçado, **negrito** |

A tela de abertura reforça a metáfora ao apresentar a capa como o preâmbulo de
um documento: `\documentclass[doutorado]{tese}`, `\title{…}`, `\author{…}`,
`\begin{document}`.

## Figuras sincronizadas da tese

As figuras exibidas no site são sincronizadas a partir dos arquivos da tese e
versionadas por hash de conteúdo (cache-busting), para que atualizações na tese
se reflitam aqui sem cache obsoleto. Detalhes em
[`docs/sync-figuras-tese.md`](docs/sync-figuras-tese.md) e no script
[`scripts/cache_busting_figuras.py`](scripts/cache_busting_figuras.py).

## Estrutura

- `index.html` — o site (rede textual + modal da tese).
- `figuras/` — figuras da tese exibidas nas galerias por capítulo.
- `audio/` — gravação de voz do capítulo 4 (SPIRA).
- `infranodus/` — análise de rede textual e materiais de apoio.
- `docs/` — documentação de manutenção (sincronização de figuras, setup etc.).
- `scripts/` — utilitários (cache-busting das figuras).
