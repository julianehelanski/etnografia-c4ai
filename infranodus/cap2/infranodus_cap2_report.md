# Análise de rede textual — Capítulo 2

> Análise de rede textual (*text network analysis*, Paranyushkin 2019)
> aplicada ao arquivo `ex_cap2.tex`. O texto foi limpo de comandos LaTeX,
> citações e notas de rodapé foram reincorporadas; janela deslizante de
> 4 *tokens* com pesos decrescentes pela distância (3-2-1). Comunidades
> detectadas por Louvain ponderado. Esta versão acrescenta duas métricas
> *informativas* que não dependem da frequência bruta: **PageRank** dos
> nós e **NPMI** das arestas. As métricas baseadas em frequência são
> mantidas em paralelo, para comparação.

## 1. Resumo quantitativo
- Tokens significativos: **28,289**
- Grafo bruto: **7059** nós · **66558** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **3606** arestas
- Tópicos detectados (Louvain): **7**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `artificial` | 1859 |
| 2 | `inteligencia` | 1845 |
| 3 | `latour` | 1149 |
| 4 | `militar` | 1090 |
| 5 | `ciencia` | 1016 |
| 6 | `rotulo` | 853 |
| 7 | `rede` | 820 |
| 8 | `analise` | 769 |
| 9 | `vocabulario` | 764 |
| 10 | `humano` | 688 |
| 11 | `campo` | 653 |
| 12 | `figuracao` | 610 |
| 13 | `rotulos` | 558 |
| 14 | `aime` | 554 |
| 15 | `teoria` | 527 |
| 16 | `catalogo` | 521 |
| 17 | `tecnologia` | 507 |
| 18 | `ocorrencias` | 501 |
| 19 | `science` | 491 |
| 20 | `tecnociencia` | 476 |
| 21 | `ator` | 469 |
| 22 | `action` | 465 |
| 23 | `descreve` | 453 |
| 24 | `objeto` | 451 |
| 25 | `leitura` | 438 |
| 26 | `obras` | 433 |
| 27 | `dado` | 419 |
| 28 | `figuracoes` | 412 |
| 29 | `capes` | 410 |
| 30 | `densidade` | 401 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `artificial` | 0.0319 |
| 2 | `inteligencia` | 0.0317 |
| 3 | `latour` | 0.0211 |
| 4 | `militar` | 0.0187 |
| 5 | `ciencia` | 0.0184 |
| 6 | `rede` | 0.0156 |
| 7 | `rotulo` | 0.0151 |
| 8 | `analise` | 0.0147 |
| 9 | `vocabulario` | 0.0139 |
| 10 | `humano` | 0.0130 |
| 11 | `campo` | 0.0127 |
| 12 | `figuracao` | 0.0114 |
| 13 | `aime` | 0.0106 |
| 14 | `rotulos` | 0.0104 |
| 15 | `catalogo` | 0.0099 |
| 16 | `tecnologia` | 0.0099 |
| 17 | `teoria` | 0.0097 |
| 18 | `tecnociencia` | 0.0095 |
| 19 | `ocorrencias` | 0.0092 |
| 20 | `descreve` | 0.0090 |
| 21 | `science` | 0.0089 |
| 22 | `leitura` | 0.0089 |
| 23 | `dado` | 0.0088 |
| 24 | `ator` | 0.0088 |
| 25 | `objeto` | 0.0088 |
| 26 | `obras` | 0.0085 |
| 27 | `action` | 0.0084 |
| 28 | `figuracoes` | 0.0082 |
| 29 | `capes` | 0.0082 |
| 30 | `partir` | 0.0081 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `press` | 154 | 97 | +57 |
| 2 | `university` | 168 | 120 | +48 |
| 3 | `joler` | 162 | 139 | +23 |
| 4 | `traducao` | 134 | 112 | +22 |
| 5 | `crawford` | 177 | 157 | +20 |
| 6 | `quadro` | 84 | 72 | +12 |
| 7 | `brasileira` | 82 | 71 | +11 |
| 8 | `cadeia` | 87 | 77 | +10 |
| 9 | `producao` | 58 | 50 | +8 |
| 10 | `forsythe` | 130 | 122 | +8 |
| 11 | `modelo` | 60 | 53 | +7 |
| 12 | `conhecimento` | 37 | 31 | +6 |
| 13 | `pesquisa` | 41 | 35 | +6 |
| 14 | `cientifico` | 109 | 103 | +6 |
| 15 | `taxa` | 110 | 104 | +6 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `latour` | 0.3168 |
| 2 | `inteligencia` | 0.2138 |
| 3 | `artificial` | 0.2056 |
| 4 | `militar` | 0.1453 |
| 5 | `vocabulario` | 0.1378 |
| 6 | `ciencia` | 0.1331 |
| 7 | `rotulo` | 0.0943 |
| 8 | `capes` | 0.0821 |
| 9 | `rede` | 0.0721 |
| 10 | `catalogo` | 0.0695 |
| 11 | `conceito` | 0.0671 |
| 12 | `analise` | 0.0581 |
| 13 | `figuracoes` | 0.0528 |
| 14 | `humano` | 0.0515 |
| 15 | `teoria` | 0.0505 |
| 16 | `aime` | 0.0492 |
| 17 | `descreve` | 0.0476 |
| 18 | `figuracao` | 0.0465 |
| 19 | `campo` | 0.0455 |
| 20 | `tecnociencia` | 0.0446 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `laboratory` | `life` | 0.871 | 109 |
| 2 | `hope` | `pandora` | 0.869 | 123 |
| 3 | `inteligencia` | `artificial` | 0.828 | 819 |
| 4 | `press` | `university` | 0.818 | 64 |
| 5 | `taxa` | `interna` | 0.803 | 54 |
| 6 | `action` | `science` | 0.790 | 171 |
| 7 | `crawford` | `joler` | 0.740 | 41 |
| 8 | `quadro` | `conclusao` | 0.722 | 62 |
| 9 | `mediacao` | `tecnica` | 0.711 | 96 |
| 10 | `maquina` | `aprendizado` | 0.710 | 126 |
| 11 | `teoria` | `ator` | 0.707 | 152 |
| 12 | `textil` | `topologico` | 0.644 | 46 |
| 13 | `lexicometrica` | `analise` | 0.625 | 95 |
| 14 | `modelo` | `linguagem` | 0.597 | 63 |
| 15 | `ator` | `rede` | 0.591 | 154 |
| 16 | `recalling` | `clarifications` | 0.572 | 27 |
| 17 | `acesso` | `disponivel` | 0.566 | 18 |
| 18 | `traducao` | `brasileira` | 0.563 | 27 |
| 19 | `action` | `pandora` | 0.563 | 54 |
| 20 | `industria` | `militar` | 0.552 | 89 |
| 21 | `publico` | `repositorio` | 0.531 | 33 |
| 22 | `stengers` | `haraway` | 0.528 | 29 |
| 23 | `vocabulario` | `topologico` | 0.519 | 58 |
| 24 | `ciencia` | `humano` | 0.517 | 177 |
| 25 | `lexical` | `catalogo` | 0.512 | 43 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (51 termos): rede, analise, teoria, tecnociencia, ator, descreve
- **Tópico 2** (42 termos): leitura, obras, dado, capes, partir, artigos
- **Tópico 3** (42 termos): latour, militar, rotulo, vocabulario, figuracao, rotulos
- **Tópico 4** (21 termos): artificial, inteligencia, objeto, maquina, pesquisa, tecnica
- **Tópico 5** (17 termos): ciencia, humano, campo, tecnologia, antropologia, estudos
- **Tópico 6** (5 termos): quadro, modos, conclusao, investigacao, grupo
- **Tópico 7** (2 termos): press, university

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 3** [latour, militar, rotulo] e **Tópico 4** [artificial, inteligencia, objeto] — densidade ponderada de ligação = 0.5147
- Lacuna entre **Tópico 3** [latour, militar, rotulo] e **Tópico 5** [ciencia, humano, campo] — densidade ponderada de ligação = 0.5154
- Lacuna entre **Tópico 1** [rede, analise, teoria] e **Tópico 2** [leitura, obras, dado] — densidade ponderada de ligação = 0.5341
- Lacuna entre **Tópico 1** [rede, analise, teoria] e **Tópico 3** [latour, militar, rotulo] — densidade ponderada de ligação = 0.8273
- Lacuna entre **Tópico 2** [leitura, obras, dado] e **Tópico 3** [latour, militar, rotulo] — densidade ponderada de ligação = 0.8770
- Lacuna entre **Tópico 1** [rede, analise, teoria] e **Tópico 5** [ciencia, humano, campo] — densidade ponderada de ligação = 0.9239

## 9. Leitura interpretativa
**O que a rede mostra.** O capítulo trama três vocabulários. O primeiro é
a leitura conceitual das *figurações* em Latour, cujos próprios livros
aparecem como duplas de altíssima associação (NPMI): `laboratory ↔ life`,
`hope ↔ pandora`, `science ↔ action` — *Laboratory Life*, *A Esperança de
Pandora* e *Science in Action* condensados em pares lexicais. O segundo é a
genealogia militar-industrial da IA (`militar`, `industria`, `inteligencia`,
`artificial`). O terceiro é o panorama bibliométrico do campo brasileiro
(`capes`, `scielo`, `producao`, `obras`, `dado`).

**Pontes (`betweenness`).** `latour` é a grande ponte do capítulo
(betweenness 0,33), seguido de `inteligencia`, `artificial`, `ciencia`,
`militar` e `vocabulario`: são os termos que costuram a teoria às
descrições. Que `vocabulario` apareça como ponte é coerente com o gesto do
capítulo, que é ele mesmo um exercício de vocabulário — as figurações.

**Lacunas a desenvolver.** As ligações mais fracas estão entre o tópico
bibliométrico (`obras`, `dado`, `capes`) e o tópico das obras de Latour
lidas no original (`science`, `action`, `pandora`, `hope`); e entre o tópico
da IA (`artificial`, `inteligencia`) e essas mesmas obras. O mapeamento
quantitativo do campo e a leitura cerrada das figurações correm em paralelo
sem se costurarem — um convite a explicitar como a análise lexicométrica das
obras conversa com o panorama bibliométrico do campo.

## 10. Arquivos gerados
**Visões frequentistas**
- `infranodus_cap2_network.png` — rede completa, tamanho por degree.
- `infranodus_cap2_focus.png` — núcleo (top-100, peso ≥ 3).

**Visões informativas**
- `infranodus_cap2_pmi.png` — rede completa, tamanho por **PageRank**,
  arestas filtradas por **NPMI ≥ 0,20**.
- `infranodus_cap2_focus_pmi.png` — núcleo, NPMI ≥ 0,25.

**Dados**
- `infranodus_cap2_metrics.json` — métricas brutas (degree, betweenness,
  PageRank, NPMI, comunidades, lacunas).
- `infranodus_cap2.gexf` / `infranodus_cap2_focus.gexf` — grafos para Gephi
  já com `community`, `frequency`, `degree_weighted`, `betweenness`,
  `pagerank` (nós) e `weight`, `npmi` (arestas).
- `infranodus_cap2_nodes.csv` / `infranodus_cap2_edges.csv` (e `_focus_*`)
  — fallback em planilha; CSVs trazem todas as colunas acima.

## 11. Como abrir no Gephi
1. Instale Gephi (≥ 0.10): https://gephi.org/users/download/
2. `File → Open…` → selecione `infranodus_cap2.gexf` (ou `_focus.gexf`).
3. No painel **Appearance**: já vem com cor por `community` e tamanho por
   `degree_weighted` (embutidos via atributos `viz`). Ajuste se quiser.
4. Em **Layout**: aplique *ForceAtlas 2* (ative *Prevent Overlap* e
   *Dissuade Hubs*) por ~30 s; ou *Fruchterman-Reingold* para algo mais rápido.
5. Em **Statistics**: rode *Modularity* e *Average Path Length* se quiser
   recalcular comunidades dentro do Gephi (resultados serão semelhantes).
6. Em **Preview**: ative *Node Labels*, escolha fonte e exporte para PDF/SVG.
