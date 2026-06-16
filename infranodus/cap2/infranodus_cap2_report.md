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
- Tokens significativos: **27,140**
- Grafo bruto: **6861** nós · **63680** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **3461** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `campo` | 2119 |
| 2 | `artificial` | 1859 |
| 3 | `inteligencia` | 1836 |
| 4 | `latour` | 1122 |
| 5 | `militar` | 1100 |
| 6 | `ciencia` | 941 |
| 7 | `analise` | 727 |
| 8 | `vocabulario` | 723 |
| 9 | `humano` | 702 |
| 10 | `rede` | 650 |
| 11 | `aime` | 533 |
| 12 | `ocorrencias` | 505 |
| 13 | `science` | 497 |
| 14 | `figuracao` | 493 |
| 15 | `teoria` | 493 |
| 16 | `catalogo` | 484 |
| 17 | `action` | 467 |
| 18 | `descreve` | 448 |
| 19 | `objeto` | 446 |
| 20 | `tecnociencia` | 439 |
| 21 | `obras` | 439 |
| 22 | `figuracoes` | 437 |
| 23 | `leitura` | 433 |
| 24 | `tecnologia` | 432 |
| 25 | `ator` | 427 |
| 26 | `dado` | 415 |
| 27 | `capes` | 415 |
| 28 | `densidade` | 414 |
| 29 | `artigos` | 391 |
| 30 | `partir` | 381 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `campo` | 0.0380 |
| 2 | `artificial` | 0.0325 |
| 3 | `inteligencia` | 0.0322 |
| 4 | `latour` | 0.0209 |
| 5 | `militar` | 0.0194 |
| 6 | `ciencia` | 0.0174 |
| 7 | `analise` | 0.0141 |
| 8 | `humano` | 0.0134 |
| 9 | `vocabulario` | 0.0133 |
| 10 | `rede` | 0.0127 |
| 11 | `aime` | 0.0102 |
| 12 | `figuracao` | 0.0097 |
| 13 | `teoria` | 0.0094 |
| 14 | `ocorrencias` | 0.0093 |
| 15 | `catalogo` | 0.0093 |
| 16 | `descreve` | 0.0091 |
| 17 | `science` | 0.0090 |
| 18 | `tecnociencia` | 0.0090 |
| 19 | `figuracoes` | 0.0089 |
| 20 | `objeto` | 0.0088 |
| 21 | `dado` | 0.0088 |
| 22 | `tecnologia` | 0.0088 |
| 23 | `leitura` | 0.0087 |
| 24 | `obras` | 0.0087 |
| 25 | `action` | 0.0084 |
| 26 | `capes` | 0.0084 |
| 27 | `ator` | 0.0083 |
| 28 | `partir` | 0.0080 |
| 29 | `conhecimento` | 0.0080 |
| 30 | `densidade` | 0.0079 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `press` | 160 | 91 | +69 |
| 2 | `university` | 169 | 106 | +63 |
| 3 | `joler` | 163 | 139 | +24 |
| 4 | `crawford` | 175 | 158 | +17 |
| 5 | `modelo` | 56 | 45 | +11 |
| 6 | `collins` | 114 | 104 | +10 |
| 7 | `forsythe` | 131 | 121 | +10 |
| 8 | `claude` | 71 | 62 | +9 |
| 9 | `modos` | 136 | 127 | +9 |
| 10 | `sistemas` | 48 | 40 | +8 |
| 11 | `producao` | 55 | 47 | +8 |
| 12 | `sustenta` | 65 | 57 | +8 |
| 13 | `quadro` | 84 | 76 | +8 |
| 14 | `cientifico` | 120 | 112 | +8 |
| 15 | `etnografia` | 63 | 56 | +7 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `campo` | 0.5087 |
| 2 | `inteligencia` | 0.2703 |
| 3 | `latour` | 0.2096 |
| 4 | `militar` | 0.1963 |
| 5 | `artificial` | 0.1511 |
| 6 | `vocabulario` | 0.1196 |
| 7 | `ciencia` | 0.1157 |
| 8 | `catalogo` | 0.0681 |
| 9 | `capes` | 0.0629 |
| 10 | `figuracao` | 0.0593 |
| 11 | `teoria` | 0.0503 |
| 12 | `figuracoes` | 0.0490 |
| 13 | `analise` | 0.0414 |
| 14 | `descreve` | 0.0398 |
| 15 | `rede` | 0.0394 |
| 16 | `modelo` | 0.0350 |
| 17 | `aime` | 0.0330 |
| 18 | `haraway` | 0.0330 |
| 19 | `tecnociencia` | 0.0304 |
| 20 | `humano` | 0.0281 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `laboratory` | `life` | 0.871 | 109 |
| 2 | `pandora` | `hope` | 0.868 | 123 |
| 3 | `inteligencia` | `artificial` | 0.827 | 807 |
| 4 | `press` | `university` | 0.817 | 64 |
| 5 | `taxa` | `interna` | 0.802 | 54 |
| 6 | `science` | `action` | 0.788 | 171 |
| 7 | `code` | `claude` | 0.785 | 92 |
| 8 | `actor` | `network` | 0.764 | 71 |
| 9 | `crawford` | `joler` | 0.738 | 41 |
| 10 | `quadro` | `conclusao` | 0.726 | 62 |
| 11 | `mediacao` | `tecnica` | 0.716 | 96 |
| 12 | `maquina` | `aprendizado` | 0.706 | 123 |
| 13 | `ator` | `teoria` | 0.701 | 137 |
| 14 | `topologico` | `textil` | 0.665 | 49 |
| 15 | `contagem` | `refinada` | 0.652 | 46 |
| 16 | `lexicometrica` | `analise` | 0.631 | 95 |
| 17 | `sistemas` | `especialistas` | 0.626 | 50 |
| 18 | `ator` | `rede` | 0.614 | 139 |
| 19 | `linguagem` | `modelo` | 0.594 | 63 |
| 20 | `recalling` | `clarifications` | 0.584 | 30 |
| 21 | `pandora` | `action` | 0.564 | 55 |
| 22 | `militar` | `industria` | 0.564 | 89 |
| 23 | `repositorio` | `publico` | 0.537 | 33 |
| 24 | `topologico` | `vocabulario` | 0.533 | 60 |
| 25 | `stengers` | `haraway` | 0.531 | 28 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (50 termos): ciencia, humano, tecnologia, dado, capes, artigos
- **Tópico 2** (40 termos): campo, militar, vocabulario, aime, ocorrencias, figuracao
- **Tópico 3** (39 termos): latour, analise, rede, teoria, descreve, tecnociencia
- **Tópico 4** (35 termos): artificial, inteligencia, objeto, conhecimento, maquina, pesquisa
- **Tópico 5** (7 termos): science, action, pandora, hope, life, laboratory
- **Tópico 6** (5 termos): quadro, conclusao, modos, investigacao, grupo
- **Tópico 7** (2 termos): press, university
- **Tópico 8** (2 termos): joler, crawford

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [ciencia, humano, tecnologia] e **Tópico 5** [science, action, pandora] — densidade ponderada de ligação = 0.3057
- Lacuna entre **Tópico 4** [artificial, inteligencia, objeto] e **Tópico 5** [science, action, pandora] — densidade ponderada de ligação = 0.3061
- Lacuna entre **Tópico 2** [campo, militar, vocabulario] e **Tópico 4** [artificial, inteligencia, objeto] — densidade ponderada de ligação = 0.4829
- Lacuna entre **Tópico 1** [ciencia, humano, tecnologia] e **Tópico 3** [latour, analise, rede] — densidade ponderada de ligação = 0.5795
- Lacuna entre **Tópico 1** [ciencia, humano, tecnologia] e **Tópico 2** [campo, militar, vocabulario] — densidade ponderada de ligação = 0.7790
- Lacuna entre **Tópico 3** [latour, analise, rede] e **Tópico 5** [science, action, pandora] — densidade ponderada de ligação = 0.8388

## 9. Leitura interpretativa
_Leitura interpretativa ainda não escrita para este capítulo. Crie `interpretation_cap2.md` ao lado dos outputs para que o conteúdo seja embutido aqui automaticamente._

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
