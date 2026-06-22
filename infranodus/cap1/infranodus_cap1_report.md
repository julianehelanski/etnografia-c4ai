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
- Tokens significativos: **22,332**
- Grafo bruto: **6432** nós · **56176** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **3231** arestas
- Tópicos detectados (Louvain): **9**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `rede` | 1214 |
| 2 | `pesquisa` | 919 |
| 3 | `etnografia` | 907 |
| 4 | `artificial` | 652 |
| 5 | `inteligencia` | 651 |
| 6 | `ciencia` | 584 |
| 7 | `metodo` | 518 |
| 8 | `latour` | 509 |
| 9 | `campo` | 492 |
| 10 | `objeto` | 430 |
| 11 | `humano` | 424 |
| 12 | `corte` | 407 |
| 13 | `descricao` | 398 |
| 14 | `modelo` | 374 |
| 15 | `strathern` | 373 |
| 16 | `pratica` | 364 |
| 17 | `parte` | 359 |
| 18 | `analise` | 340 |
| 19 | `gesto` | 326 |
| 20 | `ator` | 324 |
| 21 | `inscricao` | 323 |
| 22 | `haraway` | 320 |
| 23 | `dado` | 318 |
| 24 | `relacao` | 315 |
| 25 | `pesquisador` | 310 |
| 26 | `escrita` | 301 |
| 27 | `claude` | 301 |
| 28 | `conceito` | 275 |
| 29 | `teoria` | 271 |
| 30 | `descreve` | 259 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `rede` | 0.0324 |
| 2 | `pesquisa` | 0.0250 |
| 3 | `etnografia` | 0.0246 |
| 4 | `inteligencia` | 0.0161 |
| 5 | `artificial` | 0.0160 |
| 6 | `ciencia` | 0.0159 |
| 7 | `metodo` | 0.0148 |
| 8 | `latour` | 0.0144 |
| 9 | `campo` | 0.0138 |
| 10 | `humano` | 0.0121 |
| 11 | `objeto` | 0.0120 |
| 12 | `corte` | 0.0116 |
| 13 | `descricao` | 0.0112 |
| 14 | `modelo` | 0.0108 |
| 15 | `strathern` | 0.0107 |
| 16 | `pratica` | 0.0104 |
| 17 | `parte` | 0.0102 |
| 18 | `analise` | 0.0096 |
| 19 | `haraway` | 0.0095 |
| 20 | `inscricao` | 0.0095 |
| 21 | `relacao` | 0.0092 |
| 22 | `gesto` | 0.0092 |
| 23 | `dado` | 0.0091 |
| 24 | `pesquisador` | 0.0088 |
| 25 | `ator` | 0.0087 |
| 26 | `escrita` | 0.0087 |
| 27 | `claude` | 0.0086 |
| 28 | `conceito` | 0.0081 |
| 29 | `descreve` | 0.0076 |
| 30 | `maquina` | 0.0075 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `cientifico` | 131 | 116 | +15 |
| 2 | `computacional` | 113 | 100 | +13 |
| 3 | `funcionam` | 127 | 119 | +8 |
| 4 | `diagrama` | 111 | 104 | +7 |
| 5 | `conexoes` | 114 | 107 | +7 |
| 6 | `propriedade` | 116 | 109 | +7 |
| 7 | `decisao` | 151 | 144 | +7 |
| 8 | `otherness` | 57 | 51 | +6 |
| 9 | `infraestrutura` | 75 | 69 | +6 |
| 10 | `manifesta` | 81 | 75 | +6 |
| 11 | `termos` | 51 | 46 | +5 |
| 12 | `hinterland` | 53 | 48 | +5 |
| 13 | `ausencia` | 69 | 64 | +5 |
| 14 | `instituicao` | 108 | 103 | +5 |
| 15 | `notas` | 161 | 156 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `rede` | 0.3963 |
| 2 | `pesquisa` | 0.3234 |
| 3 | `etnografia` | 0.1971 |
| 4 | `corte` | 0.1091 |
| 5 | `ciencia` | 0.0817 |
| 6 | `latour` | 0.0812 |
| 7 | `campo` | 0.0799 |
| 8 | `metodo` | 0.0693 |
| 9 | `descricao` | 0.0547 |
| 10 | `humano` | 0.0542 |
| 11 | `strathern` | 0.0426 |
| 12 | `inteligencia` | 0.0357 |
| 13 | `inscricao` | 0.0313 |
| 14 | `tecnociencia` | 0.0299 |
| 15 | `modos` | 0.0265 |
| 16 | `dado` | 0.0240 |
| 17 | `pesquisador` | 0.0240 |
| 18 | `parcial` | 0.0218 |
| 19 | `haraway` | 0.0218 |
| 20 | `laboratorio` | 0.0205 |

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
| 4 | `parcial` | `existencia` | 0.748 | 61 |
| 5 | `teoria` | `ator` | 0.719 | 92 |
| 6 | `distribuida` | `agencia` | 0.719 | 53 |
| 7 | `otherness` | `manifesta` | 0.706 | 38 |
| 8 | `presenca` | `ausencia` | 0.696 | 37 |
| 9 | `parcial` | `conexao` | 0.645 | 43 |
| 10 | `tecnico` | `letramento` | 0.634 | 34 |
| 11 | `infraestrutura` | `computacional` | 0.623 | 35 |
| 12 | `modelo` | `linguagem` | 0.601 | 84 |
| 13 | `otherness` | `ausencia` | 0.600 | 28 |
| 14 | `heterogeneos` | `materiais` | 0.598 | 36 |
| 15 | `figuracao` | `textil` | 0.597 | 54 |
| 16 | `presenca` | `manifesta` | 0.595 | 22 |
| 17 | `textual` | `analise` | 0.577 | 60 |
| 18 | `ciencia` | `sociais` | 0.577 | 90 |
| 19 | `condicao` | `possibilidade` | 0.569 | 24 |
| 20 | `principio` | `simetria` | 0.559 | 18 |
| 21 | `tecno` | `etnografia` | 0.551 | 70 |
| 22 | `generativa` | `artificial` | 0.544 | 59 |
| 23 | `cientista` | `computacao` | 0.544 | 22 |
| 24 | `estudos` | `tecnologia` | 0.532 | 25 |
| 25 | `otherness` | `presenca` | 0.528 | 21 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (50 termos): metodo, latour, corte, strathern, gesto, haraway
- **Tópico 2** (35 termos): pesquisa, campo, pratica, materiais, lugar, conhecimento
- **Tópico 3** (24 termos): objeto, modelo, parte, pesquisador, claude, escrita
- **Tópico 4** (17 termos): humano, relacao, maquina, parcial, agencia, existencia
- **Tópico 5** (17 termos): rede, analise, ator, inscricao, teoria, tecnociencia
- **Tópico 6** (16 termos): ciencia, dado, sociais, tecnologia, spira, tecnico
- **Tópico 7** (10 termos): etnografia, descricao, torna, ponto, possivel, tecno
- **Tópico 8** (6 termos): artificial, inteligencia, generativa, construcao, centro, sistemas

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 2** [pesquisa, campo, pratica] e **Tópico 4** [humano, relacao, maquina] — densidade ponderada de ligação = 0.3479
- Lacuna entre **Tópico 1** [metodo, latour, corte] e **Tópico 3** [objeto, modelo, parte] — densidade ponderada de ligação = 0.4492
- Lacuna entre **Tópico 1** [metodo, latour, corte] e **Tópico 4** [humano, relacao, maquina] — densidade ponderada de ligação = 0.5729
- Lacuna entre **Tópico 1** [metodo, latour, corte] e **Tópico 2** [pesquisa, campo, pratica] — densidade ponderada de ligação = 0.6034
- Lacuna entre **Tópico 3** [objeto, modelo, parte] e **Tópico 4** [humano, relacao, maquina] — densidade ponderada de ligação = 0.6348
- Lacuna entre **Tópico 1** [metodo, latour, corte] e **Tópico 5** [rede, analise, ator] — densidade ponderada de ligação = 0.7294

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
