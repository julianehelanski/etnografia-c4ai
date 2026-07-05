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
- Tokens significativos: **28,180**
- Grafo bruto: **7059** nós · **66341** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **3600** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `artificial` | 1861 |
| 2 | `inteligencia` | 1854 |
| 3 | `latour` | 1149 |
| 4 | `militar` | 1114 |
| 5 | `ciencia` | 1025 |
| 6 | `rotulo` | 879 |
| 7 | `rede` | 817 |
| 8 | `analise` | 774 |
| 9 | `vocabulario` | 764 |
| 10 | `humano` | 690 |
| 11 | `campo` | 660 |
| 12 | `figuracao` | 616 |
| 13 | `aime` | 552 |
| 14 | `rotulos` | 546 |
| 15 | `teoria` | 527 |
| 16 | `catalogo` | 521 |
| 17 | `ocorrencias` | 515 |
| 18 | `tecnologia` | 511 |
| 19 | `science` | 489 |
| 20 | `ator` | 466 |
| 21 | `tecnociencia` | 466 |
| 22 | `action` | 465 |
| 23 | `objeto` | 450 |
| 24 | `descreve` | 449 |
| 25 | `obras` | 444 |
| 26 | `leitura` | 424 |
| 27 | `dado` | 417 |
| 28 | `densidade` | 413 |
| 29 | `figuracoes` | 412 |
| 30 | `capes` | 410 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `artificial` | 0.0319 |
| 2 | `inteligencia` | 0.0319 |
| 3 | `latour` | 0.0210 |
| 4 | `militar` | 0.0191 |
| 5 | `ciencia` | 0.0186 |
| 6 | `rotulo` | 0.0156 |
| 7 | `rede` | 0.0154 |
| 8 | `analise` | 0.0147 |
| 9 | `vocabulario` | 0.0139 |
| 10 | `humano` | 0.0130 |
| 11 | `campo` | 0.0128 |
| 12 | `figuracao` | 0.0115 |
| 13 | `aime` | 0.0105 |
| 14 | `rotulos` | 0.0101 |
| 15 | `tecnologia` | 0.0099 |
| 16 | `catalogo` | 0.0099 |
| 17 | `teoria` | 0.0097 |
| 18 | `ocorrencias` | 0.0094 |
| 19 | `tecnociencia` | 0.0093 |
| 20 | `descreve` | 0.0089 |
| 21 | `science` | 0.0088 |
| 22 | `dado` | 0.0088 |
| 23 | `obras` | 0.0087 |
| 24 | `objeto` | 0.0087 |
| 25 | `ator` | 0.0087 |
| 26 | `leitura` | 0.0085 |
| 27 | `action` | 0.0084 |
| 28 | `figuracoes` | 0.0082 |
| 29 | `capes` | 0.0082 |
| 30 | `partir` | 0.0080 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `press` | 155 | 97 | +58 |
| 2 | `university` | 171 | 119 | +52 |
| 3 | `traducao` | 135 | 112 | +23 |
| 4 | `joler` | 163 | 142 | +21 |
| 5 | `crawford` | 178 | 157 | +21 |
| 6 | `quadro` | 82 | 72 | +10 |
| 7 | `modelo` | 60 | 51 | +9 |
| 8 | `brasileira` | 84 | 75 | +9 |
| 9 | `producao` | 58 | 50 | +8 |
| 10 | `cadeia` | 91 | 83 | +8 |
| 11 | `cientifico` | 111 | 103 | +8 |
| 12 | `brasil` | 118 | 111 | +7 |
| 13 | `conhecimento` | 37 | 31 | +6 |
| 14 | `taxa` | 110 | 104 | +6 |
| 15 | `argumento` | 126 | 120 | +6 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `latour` | 0.3214 |
| 2 | `inteligencia` | 0.2148 |
| 3 | `artificial` | 0.2086 |
| 4 | `ciencia` | 0.1434 |
| 5 | `militar` | 0.1426 |
| 6 | `vocabulario` | 0.1364 |
| 7 | `rotulo` | 0.0948 |
| 8 | `capes` | 0.0838 |
| 9 | `rede` | 0.0729 |
| 10 | `catalogo` | 0.0706 |
| 11 | `conceito` | 0.0683 |
| 12 | `analise` | 0.0585 |
| 13 | `humano` | 0.0531 |
| 14 | `figuracoes` | 0.0523 |
| 15 | `teoria` | 0.0504 |
| 16 | `aime` | 0.0475 |
| 17 | `campo` | 0.0459 |
| 18 | `figuracao` | 0.0443 |
| 19 | `descreve` | 0.0436 |
| 20 | `tecnociencia` | 0.0357 |

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
| 12 | `refinada` | `contagem` | 0.647 | 46 |
| 13 | `textil` | `topologico` | 0.644 | 46 |
| 14 | `lexicometrica` | `analise` | 0.626 | 95 |
| 15 | `modelo` | `linguagem` | 0.597 | 63 |
| 16 | `ator` | `rede` | 0.592 | 154 |
| 17 | `recalling` | `clarifications` | 0.571 | 27 |
| 18 | `acesso` | `disponivel` | 0.565 | 18 |
| 19 | `traducao` | `brasileira` | 0.563 | 27 |
| 20 | `action` | `pandora` | 0.562 | 54 |
| 21 | `industria` | `militar` | 0.552 | 89 |
| 22 | `publico` | `repositorio` | 0.530 | 33 |
| 23 | `stengers` | `haraway` | 0.527 | 29 |
| 24 | `vocabulario` | `topologico` | 0.521 | 58 |
| 25 | `lexical` | `catalogo` | 0.518 | 43 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (52 termos): ciencia, humano, campo, tecnologia, dado, capes
- **Tópico 2** (45 termos): latour, rede, analise, teoria, tecnociencia, ator
- **Tópico 3** (41 termos): militar, rotulo, vocabulario, figuracao, aime, rotulos
- **Tópico 4** (27 termos): artificial, inteligencia, objeto, pesquisa, maquina, tecnica
- **Tópico 5** (6 termos): science, action, pandora, hope, laboratory, life
- **Tópico 6** (5 termos): quadro, modos, conclusao, investigacao, grupo
- **Tópico 7** (2 termos): press, university
- **Tópico 8** (2 termos): joler, crawford

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [ciencia, humano, campo] e **Tópico 5** [science, action, pandora] — densidade ponderada de ligação = 0.1795
- Lacuna entre **Tópico 4** [artificial, inteligencia, objeto] e **Tópico 5** [science, action, pandora] — densidade ponderada de ligação = 0.2099
- Lacuna entre **Tópico 3** [militar, rotulo, vocabulario] e **Tópico 4** [artificial, inteligencia, objeto] — densidade ponderada de ligação = 0.3975
- Lacuna entre **Tópico 1** [ciencia, humano, campo] e **Tópico 3** [militar, rotulo, vocabulario] — densidade ponderada de ligação = 0.6008
- Lacuna entre **Tópico 1** [ciencia, humano, campo] e **Tópico 2** [latour, rede, analise] — densidade ponderada de ligação = 0.7333
- Lacuna entre **Tópico 2** [latour, rede, analise] e **Tópico 5** [science, action, pandora] — densidade ponderada de ligação = 0.8704

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
