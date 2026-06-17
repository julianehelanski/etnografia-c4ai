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
- Tokens significativos: **22,375**
- Grafo bruto: **6420** nós · **56140** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **3214** arestas
- Tópicos detectados (Louvain): **9**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `rede` | 1219 |
| 2 | `pesquisa` | 912 |
| 3 | `etnografia` | 904 |
| 4 | `artificial` | 644 |
| 5 | `inteligencia` | 643 |
| 6 | `ciencia` | 584 |
| 7 | `metodo` | 518 |
| 8 | `latour` | 515 |
| 9 | `campo` | 481 |
| 10 | `objeto` | 424 |
| 11 | `humano` | 424 |
| 12 | `corte` | 407 |
| 13 | `descricao` | 396 |
| 14 | `strathern` | 373 |
| 15 | `modelo` | 370 |
| 16 | `analise` | 363 |
| 17 | `pratica` | 361 |
| 18 | `parte` | 341 |
| 19 | `gesto` | 328 |
| 20 | `relacao` | 326 |
| 21 | `ator` | 322 |
| 22 | `dado` | 318 |
| 23 | `haraway` | 317 |
| 24 | `pesquisador` | 312 |
| 25 | `inscricao` | 311 |
| 26 | `claude` | 304 |
| 27 | `escrita` | 301 |
| 28 | `teoria` | 273 |
| 29 | `conceito` | 272 |
| 30 | `descreve` | 254 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `rede` | 0.0324 |
| 2 | `pesquisa` | 0.0249 |
| 3 | `etnografia` | 0.0246 |
| 4 | `ciencia` | 0.0160 |
| 5 | `inteligencia` | 0.0160 |
| 6 | `artificial` | 0.0159 |
| 7 | `metodo` | 0.0148 |
| 8 | `latour` | 0.0147 |
| 9 | `campo` | 0.0136 |
| 10 | `humano` | 0.0122 |
| 11 | `objeto` | 0.0119 |
| 12 | `corte` | 0.0117 |
| 13 | `descricao` | 0.0112 |
| 14 | `strathern` | 0.0108 |
| 15 | `modelo` | 0.0107 |
| 16 | `pratica` | 0.0103 |
| 17 | `analise` | 0.0102 |
| 18 | `relacao` | 0.0097 |
| 19 | `parte` | 0.0097 |
| 20 | `haraway` | 0.0094 |
| 21 | `gesto` | 0.0093 |
| 22 | `inscricao` | 0.0091 |
| 23 | `dado` | 0.0091 |
| 24 | `pesquisador` | 0.0090 |
| 25 | `claude` | 0.0087 |
| 26 | `escrita` | 0.0087 |
| 27 | `ator` | 0.0087 |
| 28 | `conceito` | 0.0081 |
| 29 | `maquina` | 0.0076 |
| 30 | `descreve` | 0.0075 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `computacional` | 113 | 97 | +16 |
| 2 | `cientifico` | 130 | 115 | +15 |
| 3 | `momento` | 122 | 111 | +11 |
| 4 | `decisao` | 143 | 133 | +10 |
| 5 | `funcionam` | 129 | 120 | +9 |
| 6 | `conexoes` | 114 | 106 | +8 |
| 7 | `termos` | 49 | 42 | +7 |
| 8 | `diagrama` | 115 | 108 | +7 |
| 9 | `hinterland` | 54 | 48 | +6 |
| 10 | `infraestrutura` | 75 | 69 | +6 |
| 11 | `condicoes` | 109 | 103 | +6 |
| 12 | `heterogeneos` | 94 | 89 | +5 |
| 13 | `propriedade` | 106 | 101 | +5 |
| 14 | `textil` | 51 | 47 | +4 |
| 15 | `otherness` | 59 | 55 | +4 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `rede` | 0.3849 |
| 2 | `pesquisa` | 0.3298 |
| 3 | `etnografia` | 0.2003 |
| 4 | `corte` | 0.1122 |
| 5 | `latour` | 0.0900 |
| 6 | `ciencia` | 0.0836 |
| 7 | `campo` | 0.0788 |
| 8 | `metodo` | 0.0759 |
| 9 | `humano` | 0.0557 |
| 10 | `descricao` | 0.0546 |
| 11 | `strathern` | 0.0420 |
| 12 | `inteligencia` | 0.0357 |
| 13 | `modos` | 0.0266 |
| 14 | `tecnociencia` | 0.0257 |
| 15 | `inscricao` | 0.0251 |
| 16 | `dado` | 0.0242 |
| 17 | `pesquisador` | 0.0233 |
| 18 | `parcial` | 0.0220 |
| 19 | `hinterland` | 0.0217 |
| 20 | `maquina` | 0.0212 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `ausencia` | `manifesta` | 0.872 | 60 |
| 2 | `inteligencia` | `artificial` | 0.858 | 289 |
| 3 | `existencias` | `parciais` | 0.824 | 81 |
| 4 | `parcial` | `existencia` | 0.748 | 61 |
| 5 | `teoria` | `ator` | 0.719 | 92 |
| 6 | `distribuida` | `agencia` | 0.719 | 53 |
| 7 | `otherness` | `manifesta` | 0.706 | 38 |
| 8 | `presenca` | `ausencia` | 0.702 | 37 |
| 9 | `parcial` | `conexao` | 0.645 | 43 |
| 10 | `tecnico` | `letramento` | 0.634 | 34 |
| 11 | `infraestrutura` | `computacional` | 0.623 | 35 |
| 12 | `modelo` | `linguagem` | 0.603 | 84 |
| 13 | `presenca` | `manifesta` | 0.601 | 22 |
| 14 | `otherness` | `ausencia` | 0.600 | 28 |
| 15 | `heterogeneos` | `materiais` | 0.598 | 36 |
| 16 | `figuracao` | `textil` | 0.598 | 54 |
| 17 | `textual` | `analise` | 0.589 | 68 |
| 18 | `ciencia` | `sociais` | 0.577 | 90 |
| 19 | `condicao` | `possibilidade` | 0.569 | 24 |
| 20 | `principio` | `simetria` | 0.559 | 18 |
| 21 | `tecno` | `etnografia` | 0.550 | 70 |
| 22 | `generativa` | `artificial` | 0.546 | 59 |
| 23 | `cientista` | `computacao` | 0.544 | 22 |
| 24 | `otherness` | `presenca` | 0.534 | 21 |
| 25 | `estudos` | `tecnologia` | 0.532 | 25 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (43 termos): metodo, latour, corte, strathern, gesto, haraway
- **Tópico 2** (38 termos): pesquisa, campo, objeto, pratica, materiais, lugar
- **Tópico 3** (28 termos): artificial, inteligencia, ciencia, dado, pesquisador, sociais
- **Tópico 4** (20 termos): humano, relacao, maquina, parcial, nomeia, agencia
- **Tópico 5** (16 termos): rede, analise, ator, teoria, textual, actante
- **Tópico 6** (11 termos): infraestrutura, ponto, instituicao, computacional, momento, precisa
- **Tópico 7** (11 termos): modelo, parte, inscricao, claude, escrita, tecnociencia
- **Tópico 8** (8 termos): etnografia, descricao, sustenta, torna, possivel, tecno

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [metodo, latour, corte] e **Tópico 3** [artificial, inteligencia, ciencia] — densidade ponderada de ligação = 0.3414
- Lacuna entre **Tópico 2** [pesquisa, campo, objeto] e **Tópico 4** [humano, relacao, maquina] — densidade ponderada de ligação = 0.4382
- Lacuna entre **Tópico 3** [artificial, inteligencia, ciencia] e **Tópico 4** [humano, relacao, maquina] — densidade ponderada de ligação = 0.5696
- Lacuna entre **Tópico 1** [metodo, latour, corte] e **Tópico 4** [humano, relacao, maquina] — densidade ponderada de ligação = 0.6198
- Lacuna entre **Tópico 1** [metodo, latour, corte] e **Tópico 2** [pesquisa, campo, objeto] — densidade ponderada de ligação = 0.6322
- Lacuna entre **Tópico 1** [metodo, latour, corte] e **Tópico 5** [rede, analise, ator] — densidade ponderada de ligação = 0.7340

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
