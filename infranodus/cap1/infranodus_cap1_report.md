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
- Tokens significativos: **22,688**
- Grafo bruto: **6429** nós · **56278** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **3206** arestas
- Tópicos detectados (Louvain): **7**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `rede` | 1264 |
| 2 | `etnografia` | 915 |
| 3 | `pesquisa` | 907 |
| 4 | `artificial` | 654 |
| 5 | `inteligencia` | 649 |
| 6 | `ciencia` | 588 |
| 7 | `metodo` | 521 |
| 8 | `latour` | 512 |
| 9 | `campo` | 494 |
| 10 | `objeto` | 433 |
| 11 | `humano` | 426 |
| 12 | `descricao` | 408 |
| 13 | `corte` | 407 |
| 14 | `analise` | 395 |
| 15 | `modelo` | 383 |
| 16 | `parte` | 370 |
| 17 | `strathern` | 368 |
| 18 | `pratica` | 366 |
| 19 | `inscricao` | 363 |
| 20 | `relacao` | 344 |
| 21 | `claude` | 338 |
| 22 | `gesto` | 334 |
| 23 | `dado` | 323 |
| 24 | `ator` | 320 |
| 25 | `pesquisador` | 313 |
| 26 | `haraway` | 309 |
| 27 | `escrita` | 308 |
| 28 | `parcial` | 272 |
| 29 | `teoria` | 271 |
| 30 | `conceito` | 270 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `rede` | 0.0330 |
| 2 | `etnografia` | 0.0245 |
| 3 | `pesquisa` | 0.0244 |
| 4 | `artificial` | 0.0160 |
| 5 | `inteligencia` | 0.0159 |
| 6 | `ciencia` | 0.0158 |
| 7 | `metodo` | 0.0146 |
| 8 | `latour` | 0.0144 |
| 9 | `campo` | 0.0137 |
| 10 | `humano` | 0.0120 |
| 11 | `objeto` | 0.0120 |
| 12 | `corte` | 0.0115 |
| 13 | `descricao` | 0.0114 |
| 14 | `modelo` | 0.0110 |
| 15 | `analise` | 0.0107 |
| 16 | `inscricao` | 0.0105 |
| 17 | `strathern` | 0.0105 |
| 18 | `pratica` | 0.0103 |
| 19 | `parte` | 0.0103 |
| 20 | `relacao` | 0.0099 |
| 21 | `claude` | 0.0095 |
| 22 | `gesto` | 0.0093 |
| 23 | `haraway` | 0.0091 |
| 24 | `dado` | 0.0091 |
| 25 | `pesquisador` | 0.0089 |
| 26 | `escrita` | 0.0087 |
| 27 | `ator` | 0.0085 |
| 28 | `conceito` | 0.0079 |
| 29 | `parcial` | 0.0078 |
| 30 | `descreve` | 0.0076 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `cientifico` | 130 | 114 | +16 |
| 2 | `computacional` | 114 | 102 | +12 |
| 3 | `diagrama` | 101 | 90 | +11 |
| 4 | `manifesta` | 82 | 73 | +9 |
| 5 | `funcionam` | 125 | 117 | +8 |
| 6 | `conexoes` | 115 | 108 | +7 |
| 7 | `entidade` | 156 | 149 | +7 |
| 8 | `efeitos` | 158 | 151 | +7 |
| 9 | `ausencia` | 69 | 63 | +6 |
| 10 | `heterogeneos` | 93 | 87 | +6 |
| 11 | `decisao` | 148 | 142 | +6 |
| 12 | `termos` | 50 | 45 | +5 |
| 13 | `actante` | 53 | 48 | +5 |
| 14 | `otherness` | 58 | 53 | +5 |
| 15 | `nocao` | 136 | 131 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `rede` | 0.3914 |
| 2 | `pesquisa` | 0.2966 |
| 3 | `etnografia` | 0.2007 |
| 4 | `corte` | 0.0979 |
| 5 | `latour` | 0.0813 |
| 6 | `ciencia` | 0.0808 |
| 7 | `campo` | 0.0754 |
| 8 | `metodo` | 0.0708 |
| 9 | `descricao` | 0.0703 |
| 10 | `humano` | 0.0555 |
| 11 | `inscricao` | 0.0484 |
| 12 | `strathern` | 0.0415 |
| 13 | `tecnociencia` | 0.0397 |
| 14 | `inteligencia` | 0.0352 |
| 15 | `analise` | 0.0310 |
| 16 | `gesto` | 0.0267 |
| 17 | `modos` | 0.0262 |
| 18 | `dado` | 0.0257 |
| 19 | `claude` | 0.0237 |
| 20 | `parcial` | 0.0225 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `ausencia` | `manifesta` | 0.872 | 60 |
| 2 | `inteligencia` | `artificial` | 0.858 | 292 |
| 3 | `existencias` | `parciais` | 0.825 | 81 |
| 4 | `parcial` | `existencia` | 0.754 | 68 |
| 5 | `distribuida` | `agencia` | 0.724 | 56 |
| 6 | `teoria` | `ator` | 0.720 | 92 |
| 7 | `otherness` | `manifesta` | 0.706 | 38 |
| 8 | `presenca` | `ausencia` | 0.697 | 37 |
| 9 | `parcial` | `conexao` | 0.656 | 49 |
| 10 | `tecnico` | `letramento` | 0.635 | 34 |
| 11 | `infraestrutura` | `computacional` | 0.624 | 35 |
| 12 | `modelo` | `linguagem` | 0.605 | 87 |
| 13 | `otherness` | `ausencia` | 0.601 | 28 |
| 14 | `presenca` | `manifesta` | 0.596 | 22 |
| 15 | `figuracao` | `textil` | 0.595 | 54 |
| 16 | `heterogeneos` | `materiais` | 0.593 | 36 |
| 17 | `textual` | `analise` | 0.586 | 72 |
| 18 | `ciencia` | `sociais` | 0.582 | 93 |
| 19 | `principio` | `simetria` | 0.560 | 18 |
| 20 | `tecno` | `etnografia` | 0.549 | 70 |
| 21 | `generativa` | `artificial` | 0.545 | 59 |
| 22 | `cientista` | `computacao` | 0.545 | 22 |
| 23 | `estudos` | `tecnologia` | 0.533 | 25 |
| 24 | `otherness` | `presenca` | 0.529 | 21 |
| 25 | `strathern` | `barad` | 0.527 | 30 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (49 termos): etnografia, pesquisa, campo, descricao, parte, pratica
- **Tópico 2** (48 termos): metodo, latour, corte, strathern, gesto, haraway
- **Tópico 3** (28 termos): artificial, inteligencia, objeto, modelo, pesquisador, laboratorio
- **Tópico 4** (19 termos): humano, relacao, parcial, maquina, agencia, lugar
- **Tópico 5** (17 termos): rede, analise, ator, teoria, textual, termos
- **Tópico 6** (14 termos): ciencia, dado, sociais, tecnologia, tecnico, termo
- **Tópico 7** (5 termos): hinterland, otherness, ausencia, presenca, manifesta

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 2** [metodo, latour, corte] e **Tópico 3** [artificial, inteligencia, objeto] — densidade ponderada de ligação = 0.3318
- Lacuna entre **Tópico 1** [etnografia, pesquisa, campo] e **Tópico 4** [humano, relacao, parcial] — densidade ponderada de ligação = 0.5403
- Lacuna entre **Tópico 2** [metodo, latour, corte] e **Tópico 4** [humano, relacao, parcial] — densidade ponderada de ligação = 0.5954
- Lacuna entre **Tópico 3** [artificial, inteligencia, objeto] e **Tópico 4** [humano, relacao, parcial] — densidade ponderada de ligação = 0.6335
- Lacuna entre **Tópico 3** [artificial, inteligencia, objeto] e **Tópico 5** [rede, analise, ator] — densidade ponderada de ligação = 0.7269
- Lacuna entre **Tópico 2** [metodo, latour, corte] e **Tópico 5** [rede, analise, ator] — densidade ponderada de ligação = 0.7304

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
