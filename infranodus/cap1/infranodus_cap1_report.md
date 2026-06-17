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
- Tokens significativos: **21,915**
- Grafo bruto: **6436** nós · **55909** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **3169** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `rede` | 1122 |
| 2 | `pesquisa` | 890 |
| 3 | `etnografia` | 869 |
| 4 | `artificial` | 573 |
| 5 | `inteligencia` | 571 |
| 6 | `ciencia` | 538 |
| 7 | `metodo` | 500 |
| 8 | `latour` | 487 |
| 9 | `campo` | 454 |
| 10 | `humano` | 422 |
| 11 | `objeto` | 411 |
| 12 | `descricao` | 385 |
| 13 | `modelo` | 376 |
| 14 | `corte` | 370 |
| 15 | `pratica` | 367 |
| 16 | `gesto` | 349 |
| 17 | `parte` | 343 |
| 18 | `ator` | 321 |
| 19 | `strathern` | 319 |
| 20 | `analise` | 318 |
| 21 | `claude` | 314 |
| 22 | `escrita` | 310 |
| 23 | `inscricao` | 307 |
| 24 | `dado` | 307 |
| 25 | `relacao` | 300 |
| 26 | `pesquisador` | 289 |
| 27 | `haraway` | 275 |
| 28 | `conceito` | 264 |
| 29 | `teoria` | 256 |
| 30 | `descreve` | 245 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `rede` | 0.0313 |
| 2 | `pesquisa` | 0.0253 |
| 3 | `etnografia` | 0.0245 |
| 4 | `ciencia` | 0.0155 |
| 5 | `artificial` | 0.0149 |
| 6 | `metodo` | 0.0149 |
| 7 | `inteligencia` | 0.0149 |
| 8 | `latour` | 0.0145 |
| 9 | `campo` | 0.0133 |
| 10 | `humano` | 0.0127 |
| 11 | `objeto` | 0.0120 |
| 12 | `descricao` | 0.0113 |
| 13 | `modelo` | 0.0111 |
| 14 | `corte` | 0.0109 |
| 15 | `pratica` | 0.0109 |
| 16 | `gesto` | 0.0103 |
| 17 | `parte` | 0.0101 |
| 18 | `strathern` | 0.0096 |
| 19 | `inscricao` | 0.0094 |
| 20 | `analise` | 0.0094 |
| 21 | `claude` | 0.0093 |
| 22 | `escrita` | 0.0092 |
| 23 | `relacao` | 0.0092 |
| 24 | `ator` | 0.0091 |
| 25 | `dado` | 0.0091 |
| 26 | `pesquisador` | 0.0088 |
| 27 | `haraway` | 0.0086 |
| 28 | `conceito` | 0.0082 |
| 29 | `descreve` | 0.0075 |
| 30 | `parcial` | 0.0074 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `cientifico` | 114 | 98 | +16 |
| 2 | `computacional` | 111 | 101 | +10 |
| 3 | `momento` | 127 | 117 | +10 |
| 4 | `mobiliza` | 128 | 118 | +10 |
| 5 | `funcionam` | 122 | 114 | +8 |
| 6 | `manifesta` | 82 | 75 | +7 |
| 7 | `condicoes` | 107 | 100 | +7 |
| 8 | `conexoes` | 118 | 111 | +7 |
| 9 | `diagrama` | 101 | 95 | +6 |
| 10 | `social` | 152 | 146 | +6 |
| 11 | `hinterland` | 51 | 46 | +5 |
| 12 | `infraestrutura` | 72 | 67 | +5 |
| 13 | `presenca` | 90 | 85 | +5 |
| 14 | `tecnica` | 126 | 121 | +5 |
| 15 | `decisao` | 144 | 139 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `rede` | 0.3707 |
| 2 | `pesquisa` | 0.2902 |
| 3 | `etnografia` | 0.1892 |
| 4 | `corte` | 0.0953 |
| 5 | `latour` | 0.0878 |
| 6 | `ciencia` | 0.0760 |
| 7 | `metodo` | 0.0738 |
| 8 | `campo` | 0.0636 |
| 9 | `humano` | 0.0585 |
| 10 | `gesto` | 0.0460 |
| 11 | `descricao` | 0.0394 |
| 12 | `inscricao` | 0.0361 |
| 13 | `dado` | 0.0358 |
| 14 | `strathern` | 0.0340 |
| 15 | `inteligencia` | 0.0309 |
| 16 | `tecnociencia` | 0.0304 |
| 17 | `modos` | 0.0259 |
| 18 | `haraway` | 0.0214 |
| 19 | `parcial` | 0.0212 |
| 20 | `pesquisador` | 0.0210 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `ausencia` | `manifesta` | 0.871 | 57 |
| 2 | `inteligencia` | `artificial` | 0.858 | 261 |
| 3 | `existencias` | `parciais` | 0.819 | 72 |
| 4 | `parcial` | `existencia` | 0.747 | 61 |
| 5 | `teoria` | `ator` | 0.719 | 89 |
| 6 | `distribuida` | `agencia` | 0.717 | 50 |
| 7 | `manifesta` | `otherness` | 0.702 | 35 |
| 8 | `ausencia` | `presenca` | 0.692 | 34 |
| 9 | `parcial` | `conexao` | 0.634 | 40 |
| 10 | `letramento` | `tecnico` | 0.628 | 31 |
| 11 | `heterogeneos` | `materiais` | 0.607 | 33 |
| 12 | `infraestrutura` | `computacional` | 0.604 | 32 |
| 13 | `linguagem` | `modelo` | 0.600 | 84 |
| 14 | `ausencia` | `otherness` | 0.598 | 26 |
| 15 | `presenca` | `manifesta` | 0.591 | 20 |
| 16 | `sociais` | `ciencia` | 0.572 | 84 |
| 17 | `analise` | `textual` | 0.555 | 50 |
| 18 | `computacao` | `cientista` | 0.550 | 22 |
| 19 | `condicao` | `possibilidade` | 0.550 | 21 |
| 20 | `etnografia` | `tecno` | 0.543 | 63 |
| 21 | `textil` | `figuracao` | 0.540 | 36 |
| 22 | `simetria` | `principio` | 0.540 | 15 |
| 23 | `presenca` | `otherness` | 0.538 | 20 |
| 24 | `condicoes` | `materiais` | 0.532 | 24 |
| 25 | `estudos` | `tecnologia` | 0.526 | 23 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (54 termos): metodo, latour, corte, gesto, strathern, haraway
- **Tópico 2** (26 termos): pesquisa, artificial, inteligencia, pratica, conhecimento, materiais
- **Tópico 3** (26 termos): campo, objeto, modelo, parte, claude, escrita
- **Tópico 4** (23 termos): rede, ator, analise, pesquisador, teoria, actante
- **Tópico 5** (19 termos): humano, relacao, parcial, maquina, lugar, agencia
- **Tópico 6** (17 termos): ciencia, dado, sociais, tecnologia, laboratorio, tecnico
- **Tópico 7** (10 termos): etnografia, descricao, torna, possivel, condicao, possibilidade
- **Tópico 8** (5 termos): hinterland, otherness, ausencia, manifesta, presenca

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [metodo, latour, corte] e **Tópico 2** [pesquisa, artificial, inteligencia] — densidade ponderada de ligação = 0.4387
- Lacuna entre **Tópico 2** [pesquisa, artificial, inteligencia] e **Tópico 5** [humano, relacao, parcial] — densidade ponderada de ligação = 0.4413
- Lacuna entre **Tópico 1** [metodo, latour, corte] e **Tópico 4** [rede, ator, analise] — densidade ponderada de ligação = 0.5459
- Lacuna entre **Tópico 1** [metodo, latour, corte] e **Tópico 5** [humano, relacao, parcial] — densidade ponderada de ligação = 0.5585
- Lacuna entre **Tópico 1** [metodo, latour, corte] e **Tópico 3** [campo, objeto, modelo] — densidade ponderada de ligação = 0.6204
- Lacuna entre **Tópico 3** [campo, objeto, modelo] e **Tópico 5** [humano, relacao, parcial] — densidade ponderada de ligação = 0.7227

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
