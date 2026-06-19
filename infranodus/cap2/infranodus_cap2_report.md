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
- Tokens significativos: **27,738**
- Grafo bruto: **6951** nós · **65308** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **3583** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `artificial` | 1863 |
| 2 | `inteligencia` | 1854 |
| 3 | `latour` | 1166 |
| 4 | `militar` | 1117 |
| 5 | `ciencia` | 1017 |
| 6 | `rotulo` | 862 |
| 7 | `vocabulario` | 757 |
| 8 | `analise` | 735 |
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
| 20 | `tecnociencia` | 472 |
| 21 | `ator` | 471 |
| 22 | `objeto` | 467 |
| 23 | `action` | 456 |
| 24 | `descreve` | 456 |
| 25 | `leitura` | 434 |
| 26 | `obras` | 427 |
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
| 1 | `artificial` | 0.0321 |
| 2 | `inteligencia` | 0.0321 |
| 3 | `latour` | 0.0216 |
| 4 | `militar` | 0.0193 |
| 5 | `ciencia` | 0.0185 |
| 6 | `rotulo` | 0.0153 |
| 7 | `analise` | 0.0142 |
| 8 | `rede` | 0.0138 |
| 9 | `vocabulario` | 0.0138 |
| 10 | `humano` | 0.0131 |
| 11 | `campo` | 0.0129 |
| 12 | `figuracao` | 0.0116 |
| 13 | `aime` | 0.0103 |
| 14 | `tecnologia` | 0.0100 |
| 15 | `rotulos` | 0.0098 |
| 16 | `teoria` | 0.0097 |
| 17 | `tecnociencia` | 0.0094 |
| 18 | `ocorrencias` | 0.0093 |
| 19 | `catalogo` | 0.0092 |
| 20 | `objeto` | 0.0092 |
| 21 | `descreve` | 0.0091 |
| 22 | `ator` | 0.0089 |
| 23 | `dado` | 0.0088 |
| 24 | `science` | 0.0088 |
| 25 | `leitura` | 0.0087 |
| 26 | `figuracoes` | 0.0084 |
| 27 | `obras` | 0.0084 |
| 28 | `action` | 0.0083 |
| 29 | `capes` | 0.0082 |
| 30 | `partir` | 0.0081 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `press` | 156 | 98 | +58 |
| 2 | `university` | 169 | 117 | +52 |
| 3 | `joler` | 163 | 139 | +24 |
| 4 | `crawford` | 178 | 158 | +20 |
| 5 | `traducao` | 139 | 124 | +15 |
| 6 | `modelo` | 59 | 47 | +12 |
| 7 | `collins` | 119 | 108 | +11 |
| 8 | `forsythe` | 127 | 116 | +11 |
| 9 | `sistemas` | 51 | 41 | +10 |
| 10 | `cadeia` | 97 | 87 | +10 |
| 11 | `producao` | 58 | 49 | +9 |
| 12 | `quadro` | 86 | 77 | +9 |
| 13 | `code` | 118 | 110 | +8 |
| 14 | `pesquisa` | 42 | 35 | +7 |
| 15 | `claude` | 71 | 64 | +7 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `latour` | 0.3440 |
| 2 | `inteligencia` | 0.2246 |
| 3 | `artificial` | 0.2162 |
| 4 | `ciencia` | 0.1480 |
| 5 | `militar` | 0.1411 |
| 6 | `vocabulario` | 0.1407 |
| 7 | `rotulo` | 0.0883 |
| 8 | `capes` | 0.0811 |
| 9 | `figuracoes` | 0.0696 |
| 10 | `conceito` | 0.0670 |
| 11 | `catalogo` | 0.0580 |
| 12 | `humano` | 0.0546 |
| 13 | `analise` | 0.0537 |
| 14 | `teoria` | 0.0519 |
| 15 | `rede` | 0.0500 |
| 16 | `campo` | 0.0489 |
| 17 | `descreve` | 0.0481 |
| 18 | `aime` | 0.0472 |
| 19 | `figuracao` | 0.0426 |
| 20 | `tecnociencia` | 0.0362 |

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
| 10 | `maquina` | `aprendizado` | 0.709 | 126 |
| 11 | `mediacao` | `tecnica` | 0.708 | 96 |
| 12 | `teoria` | `ator` | 0.706 | 152 |
| 13 | `refinada` | `contagem` | 0.650 | 46 |
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
| 25 | `vocabulario` | `topologico` | 0.520 | 58 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (48 termos): artificial, inteligencia, ciencia, humano, campo, tecnologia
- **Tópico 2** (39 termos): latour, rede, teoria, tecnociencia, ator, descreve
- **Tópico 3** (35 termos): leitura, dado, capes, partir, artigos, distribuicao
- **Tópico 4** (32 termos): militar, rotulo, vocabulario, figuracao, aime, rotulos
- **Tópico 5** (15 termos): analise, figuracoes, secao, claude, lexicometrica, quadro
- **Tópico 6** (7 termos): science, action, pandora, hope, laboratory, life
- **Tópico 7** (2 termos): press, university
- **Tópico 8** (2 termos): joler, crawford

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [artificial, inteligencia, ciencia] e **Tópico 4** [militar, rotulo, vocabulario] — densidade ponderada de ligação = 0.3861
- Lacuna entre **Tópico 2** [latour, rede, teoria] e **Tópico 3** [leitura, dado, capes] — densidade ponderada de ligação = 0.5187
- Lacuna entre **Tópico 3** [leitura, dado, capes] e **Tópico 5** [analise, figuracoes, secao] — densidade ponderada de ligação = 0.6095
- Lacuna entre **Tópico 1** [artificial, inteligencia, ciencia] e **Tópico 5** [analise, figuracoes, secao] — densidade ponderada de ligação = 0.6222
- Lacuna entre **Tópico 2** [latour, rede, teoria] e **Tópico 5** [analise, figuracoes, secao] — densidade ponderada de ligação = 0.8803
- Lacuna entre **Tópico 3** [leitura, dado, capes] e **Tópico 4** [militar, rotulo, vocabulario] — densidade ponderada de ligação = 0.9402

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
