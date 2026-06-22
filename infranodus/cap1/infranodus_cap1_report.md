# Análise de rede textual — Capítulo 1

> Análise de rede textual (*text network analysis*, Paranyushkin 2019)
> aplicada ao arquivo `ex_cap1.tex`. O texto foi limpo de comandos LaTeX,
> citações e notas de rodapé foram reincorporadas; janela deslizante de
> 4 *tokens* com pesos decrescentes pela distância (3-2-1). Comunidades
> detectadas por Louvain ponderado. Esta versão acrescenta duas métricas
> *informativas* que não dependem da frequência bruta: **PageRank** dos
> nós e **NPMI** das arestas. As métricas baseadas em frequência são
> mantidas em paralelo, para comparação.

## 1. Resumo quantitativo
- Tokens significativos: **22,614**
- Grafo bruto: **6435** nós · **56321** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **3224** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `rede` | 1248 |
| 2 | `pesquisa` | 919 |
| 3 | `etnografia` | 919 |
| 4 | `artificial` | 654 |
| 5 | `inteligencia` | 651 |
| 6 | `ciencia` | 590 |
| 7 | `metodo` | 518 |
| 8 | `latour` | 505 |
| 9 | `campo` | 496 |
| 10 | `objeto` | 430 |
| 11 | `humano` | 424 |
| 12 | `corte` | 407 |
| 13 | `descricao` | 406 |
| 14 | `modelo` | 381 |
| 15 | `analise` | 376 |
| 16 | `strathern` | 370 |
| 17 | `parte` | 367 |
| 18 | `pratica` | 364 |
| 19 | `inscricao` | 342 |
| 20 | `gesto` | 331 |
| 21 | `ator` | 320 |
| 22 | `dado` | 318 |
| 23 | `escrita` | 314 |
| 24 | `relacao` | 313 |
| 25 | `haraway` | 311 |
| 26 | `pesquisador` | 310 |
| 27 | `claude` | 306 |
| 28 | `teoria` | 271 |
| 29 | `conceito` | 270 |
| 30 | `descreve` | 259 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `rede` | 0.0329 |
| 2 | `pesquisa` | 0.0248 |
| 3 | `etnografia` | 0.0248 |
| 4 | `artificial` | 0.0160 |
| 5 | `inteligencia` | 0.0160 |
| 6 | `ciencia` | 0.0160 |
| 7 | `metodo` | 0.0147 |
| 8 | `latour` | 0.0142 |
| 9 | `campo` | 0.0139 |
| 10 | `humano` | 0.0120 |
| 11 | `objeto` | 0.0119 |
| 12 | `corte` | 0.0116 |
| 13 | `descricao` | 0.0114 |
| 14 | `modelo` | 0.0109 |
| 15 | `strathern` | 0.0106 |
| 16 | `analise` | 0.0103 |
| 17 | `pratica` | 0.0103 |
| 18 | `parte` | 0.0103 |
| 19 | `inscricao` | 0.0100 |
| 20 | `gesto` | 0.0093 |
| 21 | `haraway` | 0.0092 |
| 22 | `relacao` | 0.0091 |
| 23 | `dado` | 0.0090 |
| 24 | `escrita` | 0.0089 |
| 25 | `pesquisador` | 0.0088 |
| 26 | `claude` | 0.0086 |
| 27 | `ator` | 0.0085 |
| 28 | `conceito` | 0.0079 |
| 29 | `descreve` | 0.0076 |
| 30 | `maquina` | 0.0075 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `cientifico` | 131 | 115 | +16 |
| 2 | `computacional` | 113 | 103 | +10 |
| 3 | `funcionam` | 127 | 118 | +9 |
| 4 | `heterogeneos` | 90 | 83 | +7 |
| 5 | `decisao` | 151 | 144 | +7 |
| 6 | `acesso` | 156 | 149 | +7 |
| 7 | `termos` | 50 | 44 | +6 |
| 8 | `ausencia` | 70 | 64 | +6 |
| 9 | `diagrama` | 102 | 96 | +6 |
| 10 | `propriedade` | 115 | 109 | +6 |
| 11 | `otherness` | 57 | 52 | +5 |
| 12 | `infraestrutura` | 75 | 70 | +5 |
| 13 | `manifesta` | 81 | 76 | +5 |
| 14 | `instituicao` | 110 | 105 | +5 |
| 15 | `problema` | 111 | 106 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `rede` | 0.3907 |
| 2 | `pesquisa` | 0.3139 |
| 3 | `etnografia` | 0.1986 |
| 4 | `corte` | 0.1036 |
| 5 | `ciencia` | 0.0810 |
| 6 | `campo` | 0.0796 |
| 7 | `latour` | 0.0730 |
| 8 | `metodo` | 0.0694 |
| 9 | `descricao` | 0.0558 |
| 10 | `humano` | 0.0539 |
| 11 | `inscricao` | 0.0464 |
| 12 | `tecnociencia` | 0.0422 |
| 13 | `strathern` | 0.0416 |
| 14 | `inteligencia` | 0.0355 |
| 15 | `gesto` | 0.0290 |
| 16 | `analise` | 0.0270 |
| 17 | `modos` | 0.0264 |
| 18 | `dado` | 0.0245 |
| 19 | `pesquisador` | 0.0229 |
| 20 | `parcial` | 0.0217 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `ausencia` | `manifesta` | 0.872 | 60 |
| 2 | `inteligencia` | `artificial` | 0.858 | 292 |
| 3 | `existencias` | `parciais` | 0.824 | 81 |
| 4 | `parcial` | `existencia` | 0.749 | 61 |
| 5 | `teoria` | `ator` | 0.720 | 92 |
| 6 | `distribuida` | `agencia` | 0.719 | 53 |
| 7 | `otherness` | `manifesta` | 0.706 | 38 |
| 8 | `presenca` | `ausencia` | 0.696 | 37 |
| 9 | `parcial` | `conexao` | 0.645 | 43 |
| 10 | `tecnico` | `letramento` | 0.635 | 34 |
| 11 | `infraestrutura` | `computacional` | 0.624 | 35 |
| 12 | `modelo` | `linguagem` | 0.605 | 87 |
| 13 | `otherness` | `ausencia` | 0.601 | 28 |
| 14 | `presenca` | `manifesta` | 0.596 | 22 |
| 15 | `figuracao` | `textil` | 0.595 | 54 |
| 16 | `heterogeneos` | `materiais` | 0.593 | 36 |
| 17 | `ciencia` | `sociais` | 0.582 | 93 |
| 18 | `textual` | `analise` | 0.581 | 68 |
| 19 | `condicao` | `possibilidade` | 0.570 | 24 |
| 20 | `principio` | `simetria` | 0.560 | 18 |
| 21 | `tecno` | `etnografia` | 0.548 | 70 |
| 22 | `generativa` | `artificial` | 0.545 | 59 |
| 23 | `cientista` | `computacao` | 0.545 | 22 |
| 24 | `estudos` | `tecnologia` | 0.533 | 25 |
| 25 | `otherness` | `presenca` | 0.529 | 21 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (44 termos): metodo, latour, corte, strathern, gesto, haraway
- **Tópico 2** (41 termos): etnografia, pesquisa, campo, descricao, pratica, materiais
- **Tópico 3** (31 termos): objeto, modelo, parte, inscricao, escrita, pesquisador
- **Tópico 4** (19 termos): rede, analise, ator, teoria, textual, termos
- **Tópico 5** (18 termos): humano, relacao, maquina, parcial, lugar, agencia
- **Tópico 6** (16 termos): ciencia, dado, sociais, tecnologia, spira, tecnico
- **Tópico 7** (6 termos): artificial, inteligencia, generativa, construcao, centro, sistemas
- **Tópico 8** (5 termos): hinterland, otherness, ausencia, presenca, manifesta

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [metodo, latour, corte] e **Tópico 3** [objeto, modelo, parte] — densidade ponderada de ligação = 0.4685
- Lacuna entre **Tópico 2** [etnografia, pesquisa, campo] e **Tópico 5** [humano, relacao, maquina] — densidade ponderada de ligação = 0.4810
- Lacuna entre **Tópico 1** [metodo, latour, corte] e **Tópico 5** [humano, relacao, maquina] — densidade ponderada de ligação = 0.5997
- Lacuna entre **Tópico 3** [objeto, modelo, parte] e **Tópico 5** [humano, relacao, maquina] — densidade ponderada de ligação = 0.6720
- Lacuna entre **Tópico 1** [metodo, latour, corte] e **Tópico 4** [rede, analise, ator] — densidade ponderada de ligação = 0.7165
- Lacuna entre **Tópico 1** [metodo, latour, corte] e **Tópico 2** [etnografia, pesquisa, campo] — densidade ponderada de ligação = 0.7506

## 9. Leitura interpretativa
**O que a rede mostra.** O núcleo do capítulo gira em torno de um eixo
*tese ↔ pesquisa ↔ rede ↔ C4AI ↔ IBM*, com Latour, Stengers, Mol, Law e
Barad funcionando como portais conceituais (alta intermediação) que
conectam o sub-grafo metodológico (`metodo`, `regra`, `principio`,
`controversia`, `actante`, `inscricao`) ao sub-grafo empírico (`ibm`,
`spira`, `gpu`, `pandemia`, `covid`, `voz`, `enfermaria`).

**Pontes (`betweenness`).** Termos como `actante`, `rede`, `tese`,
`tecnociencia` e `inscricao` aparecem como pontes — operam como
tradutores entre o vocabulário teórico e a descrição empírica do
encerramento da parceria C4AI–IBM.

**Lacunas a desenvolver.** As ligações mais fracas costumam aparecer
entre o tópico empírico-infraestrutural (GPU, cluster, IBM, pandemia)
e o tópico ético-ontológico (intra-ação, política ontológica, ético-
onto-epistemológico). Há aí um convite a costurar mais explicitamente
*como* a infraestrutura computacional participa do "corte agencial"
descrito por Barad, e *como* a economia especulativa de promessas
(Stengers) se materializa na cadeia GPU→modelo→artigo.

## 10. Arquivos gerados
**Visões frequentistas**
- `infranodus_cap1_network.png` — rede completa, tamanho por degree.
- `infranodus_cap1_focus.png` — núcleo (top-100, peso ≥ 3).

**Visões informativas**
- `infranodus_cap1_pmi.png` — rede completa, tamanho por **PageRank**,
  arestas filtradas por **NPMI ≥ 0,20**.
- `infranodus_cap1_focus_pmi.png` — núcleo, NPMI ≥ 0,25.

**Dados**
- `infranodus_cap1_metrics.json` — métricas brutas (degree, betweenness,
  PageRank, NPMI, comunidades, lacunas).
- `infranodus_cap1.gexf` / `infranodus_cap1_focus.gexf` — grafos para Gephi
  já com `community`, `frequency`, `degree_weighted`, `betweenness`,
  `pagerank` (nós) e `weight`, `npmi` (arestas).
- `infranodus_cap1_nodes.csv` / `infranodus_cap1_edges.csv` (e `_focus_*`)
  — fallback em planilha; CSVs trazem todas as colunas acima.

## 11. Como abrir no Gephi
1. Instale Gephi (≥ 0.10): https://gephi.org/users/download/
2. `File → Open…` → selecione `infranodus_cap1.gexf` (ou `_focus.gexf`).
3. No painel **Appearance**: já vem com cor por `community` e tamanho por
   `degree_weighted` (embutidos via atributos `viz`). Ajuste se quiser.
4. Em **Layout**: aplique *ForceAtlas 2* (ative *Prevent Overlap* e
   *Dissuade Hubs*) por ~30 s; ou *Fruchterman-Reingold* para algo mais rápido.
5. Em **Statistics**: rode *Modularity* e *Average Path Length* se quiser
   recalcular comunidades dentro do Gephi (resultados serão semelhantes).
6. Em **Preview**: ative *Node Labels*, escolha fonte e exporte para PDF/SVG.
