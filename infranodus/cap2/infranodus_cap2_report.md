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
- Tokens significativos: **28,131**
- Grafo bruto: **7053** nós · **66266** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **3598** arestas
- Tópicos detectados (Louvain): **9**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `artificial` | 1861 |
| 2 | `inteligencia` | 1851 |
| 3 | `latour` | 1156 |
| 4 | `militar` | 1113 |
| 5 | `ciencia` | 1028 |
| 6 | `rotulo` | 872 |
| 7 | `rede` | 826 |
| 8 | `analise` | 776 |
| 9 | `vocabulario` | 759 |
| 10 | `humano` | 690 |
| 11 | `campo` | 660 |
| 12 | `figuracao` | 616 |
| 13 | `aime` | 555 |
| 14 | `rotulos` | 546 |
| 15 | `teoria` | 529 |
| 16 | `catalogo` | 521 |
| 17 | `ocorrencias` | 516 |
| 18 | `tecnologia` | 513 |
| 19 | `science` | 484 |
| 20 | `ator` | 475 |
| 21 | `tecnociencia` | 466 |
| 22 | `action` | 459 |
| 23 | `objeto` | 450 |
| 24 | `descreve` | 449 |
| 25 | `leitura` | 428 |
| 26 | `obras` | 427 |
| 27 | `dado` | 417 |
| 28 | `figuracoes` | 412 |
| 29 | `densidade` | 410 |
| 30 | `capes` | 410 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `artificial` | 0.0319 |
| 2 | `inteligencia` | 0.0319 |
| 3 | `latour` | 0.0212 |
| 4 | `militar` | 0.0191 |
| 5 | `ciencia` | 0.0187 |
| 6 | `rede` | 0.0157 |
| 7 | `rotulo` | 0.0154 |
| 8 | `analise` | 0.0147 |
| 9 | `vocabulario` | 0.0138 |
| 10 | `humano` | 0.0130 |
| 11 | `campo` | 0.0128 |
| 12 | `figuracao` | 0.0115 |
| 13 | `aime` | 0.0106 |
| 14 | `rotulos` | 0.0101 |
| 15 | `tecnologia` | 0.0100 |
| 16 | `catalogo` | 0.0099 |
| 17 | `teoria` | 0.0098 |
| 18 | `ocorrencias` | 0.0095 |
| 19 | `tecnociencia` | 0.0093 |
| 20 | `ator` | 0.0089 |
| 21 | `descreve` | 0.0089 |
| 22 | `dado` | 0.0088 |
| 23 | `science` | 0.0088 |
| 24 | `objeto` | 0.0087 |
| 25 | `leitura` | 0.0086 |
| 26 | `obras` | 0.0084 |
| 27 | `action` | 0.0083 |
| 28 | `figuracoes` | 0.0082 |
| 29 | `capes` | 0.0082 |
| 30 | `partir` | 0.0080 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `press` | 155 | 96 | +59 |
| 2 | `university` | 171 | 120 | +51 |
| 3 | `traducao` | 135 | 112 | +23 |
| 4 | `crawford` | 178 | 156 | +22 |
| 5 | `joler` | 163 | 142 | +21 |
| 6 | `quadro` | 82 | 72 | +10 |
| 7 | `brasileira` | 84 | 74 | +10 |
| 8 | `producao` | 58 | 49 | +9 |
| 9 | `modelo` | 60 | 52 | +8 |
| 10 | `cientifico` | 111 | 104 | +7 |
| 11 | `investigacao` | 142 | 135 | +7 |
| 12 | `conhecimento` | 37 | 31 | +6 |
| 13 | `pesquisa` | 41 | 35 | +6 |
| 14 | `cadeia` | 87 | 81 | +6 |
| 15 | `brasil` | 117 | 111 | +6 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `latour` | 0.3175 |
| 2 | `inteligencia` | 0.2155 |
| 3 | `artificial` | 0.2075 |
| 4 | `ciencia` | 0.1432 |
| 5 | `militar` | 0.1426 |
| 6 | `vocabulario` | 0.1363 |
| 7 | `rotulo` | 0.0947 |
| 8 | `capes` | 0.0839 |
| 9 | `rede` | 0.0825 |
| 10 | `catalogo` | 0.0709 |
| 11 | `conceito` | 0.0669 |
| 12 | `analise` | 0.0599 |
| 13 | `teoria` | 0.0549 |
| 14 | `humano` | 0.0531 |
| 15 | `figuracoes` | 0.0524 |
| 16 | `aime` | 0.0475 |
| 17 | `campo` | 0.0460 |
| 18 | `figuracao` | 0.0443 |
| 19 | `descreve` | 0.0432 |
| 20 | `tecnociencia` | 0.0355 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `laboratory` | `life` | 0.871 | 106 |
| 2 | `hope` | `pandora` | 0.869 | 120 |
| 3 | `inteligencia` | `artificial` | 0.828 | 819 |
| 4 | `press` | `university` | 0.818 | 64 |
| 5 | `taxa` | `interna` | 0.803 | 54 |
| 6 | `action` | `science` | 0.789 | 168 |
| 7 | `crawford` | `joler` | 0.740 | 41 |
| 8 | `quadro` | `conclusao` | 0.722 | 62 |
| 9 | `mediacao` | `tecnica` | 0.711 | 96 |
| 10 | `maquina` | `aprendizado` | 0.710 | 126 |
| 11 | `teoria` | `ator` | 0.707 | 152 |
| 12 | `refinada` | `contagem` | 0.644 | 46 |
| 13 | `textil` | `topologico` | 0.644 | 46 |
| 14 | `lexicometrica` | `analise` | 0.626 | 95 |
| 15 | `modelo` | `linguagem` | 0.597 | 63 |
| 16 | `ator` | `rede` | 0.592 | 154 |
| 17 | `recalling` | `clarifications` | 0.571 | 27 |
| 18 | `acesso` | `disponivel` | 0.565 | 18 |
| 19 | `traducao` | `brasileira` | 0.563 | 27 |
| 20 | `action` | `pandora` | 0.559 | 52 |
| 21 | `industria` | `militar` | 0.552 | 89 |
| 22 | `publico` | `repositorio` | 0.530 | 33 |
| 23 | `stengers` | `haraway` | 0.527 | 29 |
| 24 | `vocabulario` | `topologico` | 0.521 | 58 |
| 25 | `lexical` | `catalogo` | 0.518 | 43 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (40 termos): latour, rede, analise, teoria, ator, tecnociencia
- **Tópico 2** (40 termos): militar, rotulo, vocabulario, figuracao, aime, rotulos
- **Tópico 3** (32 termos): ciencia, humano, campo, tecnologia, antropologia, conhecimento
- **Tópico 4** (27 termos): obras, dado, capes, partir, scielo, corpus
- **Tópico 5** (25 termos): artificial, inteligencia, objeto, maquina, pesquisa, tecnica
- **Tópico 6** (7 termos): science, action, pandora, hope, laboratory, life
- **Tópico 7** (5 termos): quadro, modos, conclusao, investigacao, grupo
- **Tópico 8** (2 termos): press, university

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 2** [militar, rotulo, vocabulario] e **Tópico 5** [artificial, inteligencia, objeto] — densidade ponderada de ligação = 0.4690
- Lacuna entre **Tópico 2** [militar, rotulo, vocabulario] e **Tópico 3** [ciencia, humano, campo] — densidade ponderada de ligação = 0.4961
- Lacuna entre **Tópico 1** [latour, rede, analise] e **Tópico 4** [obras, dado, capes] — densidade ponderada de ligação = 0.5926
- Lacuna entre **Tópico 1** [latour, rede, analise] e **Tópico 3** [ciencia, humano, campo] — densidade ponderada de ligação = 0.8047
- Lacuna entre **Tópico 2** [militar, rotulo, vocabulario] e **Tópico 4** [obras, dado, capes] — densidade ponderada de ligação = 0.8417
- Lacuna entre **Tópico 3** [ciencia, humano, campo] e **Tópico 4** [obras, dado, capes] — densidade ponderada de ligação = 0.9259

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
