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
- Tokens significativos: **27,711**
- Grafo bruto: **6947** nós · **65265** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **3578** arestas
- Tópicos detectados (Louvain): **9**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `artificial` | 1862 |
| 2 | `inteligencia` | 1855 |
| 3 | `latour` | 1165 |
| 4 | `militar` | 1117 |
| 5 | `ciencia` | 1018 |
| 6 | `rotulo` | 860 |
| 7 | `vocabulario` | 756 |
| 8 | `analise` | 732 |
| 9 | `rede` | 723 |
| 10 | `humano` | 692 |
| 11 | `campo` | 660 |
| 12 | `figuracao` | 616 |
| 13 | `aime` | 539 |
| 14 | `teoria` | 527 |
| 15 | `rotulos` | 525 |
| 16 | `tecnologia` | 511 |
| 17 | `ocorrencias` | 509 |
| 18 | `science` | 481 |
| 19 | `catalogo` | 480 |
| 20 | `ator` | 471 |
| 21 | `tecnociencia` | 471 |
| 22 | `objeto` | 467 |
| 23 | `action` | 456 |
| 24 | `descreve` | 454 |
| 25 | `obras` | 427 |
| 26 | `leitura` | 423 |
| 27 | `figuracoes` | 419 |
| 28 | `dado` | 415 |
| 29 | `capes` | 410 |
| 30 | `densidade` | 407 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `artificial` | 0.0322 |
| 2 | `inteligencia` | 0.0321 |
| 3 | `latour` | 0.0216 |
| 4 | `militar` | 0.0193 |
| 5 | `ciencia` | 0.0186 |
| 6 | `rotulo` | 0.0153 |
| 7 | `analise` | 0.0141 |
| 8 | `rede` | 0.0138 |
| 9 | `vocabulario` | 0.0138 |
| 10 | `humano` | 0.0132 |
| 11 | `campo` | 0.0129 |
| 12 | `figuracao` | 0.0116 |
| 13 | `aime` | 0.0103 |
| 14 | `tecnologia` | 0.0100 |
| 15 | `rotulos` | 0.0098 |
| 16 | `teoria` | 0.0098 |
| 17 | `tecnociencia` | 0.0094 |
| 18 | `ocorrencias` | 0.0094 |
| 19 | `catalogo` | 0.0092 |
| 20 | `objeto` | 0.0092 |
| 21 | `descreve` | 0.0091 |
| 22 | `ator` | 0.0089 |
| 23 | `dado` | 0.0088 |
| 24 | `science` | 0.0088 |
| 25 | `leitura` | 0.0085 |
| 26 | `figuracoes` | 0.0084 |
| 27 | `obras` | 0.0084 |
| 28 | `action` | 0.0083 |
| 29 | `capes` | 0.0082 |
| 30 | `conhecimento` | 0.0081 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `press` | 156 | 99 | +57 |
| 2 | `university` | 168 | 117 | +51 |
| 3 | `joler` | 162 | 140 | +22 |
| 4 | `crawford` | 178 | 158 | +20 |
| 5 | `traducao` | 139 | 122 | +17 |
| 6 | `modelo` | 59 | 47 | +12 |
| 7 | `cadeia` | 95 | 84 | +11 |
| 8 | `collins` | 119 | 108 | +11 |
| 9 | `forsythe` | 129 | 118 | +11 |
| 10 | `sistemas` | 51 | 41 | +10 |
| 11 | `producao` | 58 | 49 | +9 |
| 12 | `quadro` | 86 | 77 | +9 |
| 13 | `claude` | 71 | 63 | +8 |
| 14 | `code` | 118 | 110 | +8 |
| 15 | `pesquisa` | 42 | 36 | +6 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `latour` | 0.3450 |
| 2 | `inteligencia` | 0.2258 |
| 3 | `artificial` | 0.2178 |
| 4 | `ciencia` | 0.1456 |
| 5 | `militar` | 0.1418 |
| 6 | `vocabulario` | 0.1405 |
| 7 | `rotulo` | 0.0887 |
| 8 | `capes` | 0.0811 |
| 9 | `conceito` | 0.0729 |
| 10 | `figuracoes` | 0.0695 |
| 11 | `catalogo` | 0.0584 |
| 12 | `humano` | 0.0544 |
| 13 | `analise` | 0.0540 |
| 14 | `teoria` | 0.0519 |
| 15 | `rede` | 0.0502 |
| 16 | `campo` | 0.0487 |
| 17 | `aime` | 0.0473 |
| 18 | `descreve` | 0.0468 |
| 19 | `figuracao` | 0.0432 |
| 20 | `tecnociencia` | 0.0363 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `laboratory` | `life` | 0.871 | 106 |
| 2 | `hope` | `pandora` | 0.869 | 120 |
| 3 | `inteligencia` | `artificial` | 0.827 | 819 |
| 4 | `press` | `university` | 0.818 | 64 |
| 5 | `taxa` | `interna` | 0.803 | 54 |
| 6 | `action` | `science` | 0.789 | 168 |
| 7 | `code` | `claude` | 0.782 | 92 |
| 8 | `crawford` | `joler` | 0.739 | 41 |
| 9 | `quadro` | `conclusao` | 0.727 | 62 |
| 10 | `mediacao` | `tecnica` | 0.710 | 96 |
| 11 | `maquina` | `aprendizado` | 0.709 | 126 |
| 12 | `teoria` | `ator` | 0.706 | 152 |
| 13 | `refinada` | `contagem` | 0.649 | 46 |
| 14 | `textil` | `topologico` | 0.649 | 46 |
| 15 | `lexicometrica` | `analise` | 0.631 | 95 |
| 16 | `sistemas` | `especialistas` | 0.628 | 50 |
| 17 | `ator` | `rede` | 0.606 | 154 |
| 18 | `modelo` | `linguagem` | 0.596 | 63 |
| 19 | `recalling` | `clarifications` | 0.570 | 27 |
| 20 | `traducao` | `brasileira` | 0.562 | 27 |
| 21 | `action` | `pandora` | 0.558 | 52 |
| 22 | `industria` | `militar` | 0.551 | 89 |
| 23 | `publico` | `repositorio` | 0.539 | 33 |
| 24 | `stengers` | `haraway` | 0.526 | 29 |
| 25 | `vocabulario` | `topologico` | 0.521 | 58 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (44 termos): latour, analise, rede, teoria, tecnociencia, ator
- **Tópico 2** (37 termos): militar, rotulo, vocabulario, figuracao, aime, rotulos
- **Tópico 3** (32 termos): dado, capes, partir, scielo, producao, corpus
- **Tópico 4** (30 termos): artificial, inteligencia, objeto, conhecimento, maquina, pesquisa
- **Tópico 5** (21 termos): ciencia, humano, campo, tecnologia, antropologia, estudos
- **Tópico 6** (7 termos): science, action, pandora, hope, laboratory, life
- **Tópico 7** (5 termos): quadro, modos, conclusao, investigacao, grupo
- **Tópico 8** (2 termos): press, university

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 2** [militar, rotulo, vocabulario] e **Tópico 4** [artificial, inteligencia, objeto] — densidade ponderada de ligação = 0.4315
- Lacuna entre **Tópico 2** [militar, rotulo, vocabulario] e **Tópico 5** [ciencia, humano, campo] — densidade ponderada de ligação = 0.5534
- Lacuna entre **Tópico 1** [latour, analise, rede] e **Tópico 3** [dado, capes, partir] — densidade ponderada de ligação = 0.5575
- Lacuna entre **Tópico 2** [militar, rotulo, vocabulario] e **Tópico 3** [dado, capes, partir] — densidade ponderada de ligação = 0.7213
- Lacuna entre **Tópico 1** [latour, analise, rede] e **Tópico 5** [ciencia, humano, campo] — densidade ponderada de ligação = 0.8939
- Lacuna entre **Tópico 3** [dado, capes, partir] e **Tópico 4** [artificial, inteligencia, objeto] — densidade ponderada de ligação = 0.9563

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
