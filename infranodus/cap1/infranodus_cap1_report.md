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
- Tokens significativos: **22,342**
- Grafo bruto: **6419** nós · **56055** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **3218** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `rede` | 1237 |
| 2 | `pesquisa` | 921 |
| 3 | `etnografia` | 907 |
| 4 | `artificial` | 644 |
| 5 | `inteligencia` | 643 |
| 6 | `ciencia` | 584 |
| 7 | `metodo` | 512 |
| 8 | `latour` | 494 |
| 9 | `campo` | 486 |
| 10 | `objeto` | 430 |
| 11 | `humano` | 424 |
| 12 | `corte` | 407 |
| 13 | `descricao` | 398 |
| 14 | `modelo` | 371 |
| 15 | `strathern` | 370 |
| 16 | `pratica` | 364 |
| 17 | `analise` | 363 |
| 18 | `parte` | 349 |
| 19 | `gesto` | 325 |
| 20 | `ator` | 320 |
| 21 | `relacao` | 319 |
| 22 | `dado` | 318 |
| 23 | `inscricao` | 315 |
| 24 | `pesquisador` | 312 |
| 25 | `haraway` | 311 |
| 26 | `escrita` | 301 |
| 27 | `claude` | 301 |
| 28 | `teoria` | 273 |
| 29 | `conceito` | 270 |
| 30 | `descreve` | 257 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `rede` | 0.0330 |
| 2 | `pesquisa` | 0.0252 |
| 3 | `etnografia` | 0.0247 |
| 4 | `ciencia` | 0.0160 |
| 5 | `inteligencia` | 0.0159 |
| 6 | `artificial` | 0.0159 |
| 7 | `metodo` | 0.0146 |
| 8 | `latour` | 0.0140 |
| 9 | `campo` | 0.0137 |
| 10 | `humano` | 0.0121 |
| 11 | `objeto` | 0.0121 |
| 12 | `corte` | 0.0117 |
| 13 | `descricao` | 0.0113 |
| 14 | `modelo` | 0.0107 |
| 15 | `strathern` | 0.0107 |
| 16 | `pratica` | 0.0104 |
| 17 | `analise` | 0.0102 |
| 18 | `parte` | 0.0099 |
| 19 | `relacao` | 0.0095 |
| 20 | `inscricao` | 0.0093 |
| 21 | `haraway` | 0.0093 |
| 22 | `gesto` | 0.0092 |
| 23 | `dado` | 0.0091 |
| 24 | `pesquisador` | 0.0090 |
| 25 | `escrita` | 0.0087 |
| 26 | `ator` | 0.0086 |
| 27 | `claude` | 0.0086 |
| 28 | `conceito` | 0.0080 |
| 29 | `descreve` | 0.0076 |
| 30 | `maquina` | 0.0076 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `cientifico` | 130 | 115 | +15 |
| 2 | `computacional` | 113 | 99 | +14 |
| 3 | `funcionam` | 128 | 119 | +9 |
| 4 | `momento` | 125 | 117 | +8 |
| 5 | `decisao` | 143 | 135 | +8 |
| 6 | `termos` | 50 | 43 | +7 |
| 7 | `ausencia` | 69 | 62 | +7 |
| 8 | `propriedade` | 115 | 108 | +7 |
| 9 | `hinterland` | 54 | 48 | +6 |
| 10 | `heterogeneos` | 91 | 85 | +6 |
| 11 | `diagrama` | 110 | 104 | +6 |
| 12 | `problema` | 112 | 106 | +6 |
| 13 | `otherness` | 57 | 52 | +5 |
| 14 | `infraestrutura` | 74 | 69 | +5 |
| 15 | `haraway` | 25 | 21 | +4 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `rede` | 0.3890 |
| 2 | `pesquisa` | 0.3293 |
| 3 | `etnografia` | 0.1993 |
| 4 | `corte` | 0.1125 |
| 5 | `ciencia` | 0.0817 |
| 6 | `campo` | 0.0769 |
| 7 | `metodo` | 0.0751 |
| 8 | `latour` | 0.0709 |
| 9 | `descricao` | 0.0548 |
| 10 | `humano` | 0.0545 |
| 11 | `strathern` | 0.0422 |
| 12 | `inteligencia` | 0.0358 |
| 13 | `inscricao` | 0.0313 |
| 14 | `tecnociencia` | 0.0295 |
| 15 | `modos` | 0.0266 |
| 16 | `dado` | 0.0242 |
| 17 | `pesquisador` | 0.0234 |
| 18 | `parcial` | 0.0220 |
| 19 | `hinterland` | 0.0218 |
| 20 | `escrita` | 0.0210 |

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
| 16 | `figuracao` | `textil` | 0.597 | 54 |
| 17 | `textual` | `analise` | 0.589 | 68 |
| 18 | `ciencia` | `sociais` | 0.577 | 90 |
| 19 | `condicao` | `possibilidade` | 0.569 | 24 |
| 20 | `principio` | `simetria` | 0.559 | 18 |
| 21 | `tecno` | `etnografia` | 0.551 | 70 |
| 22 | `generativa` | `artificial` | 0.546 | 59 |
| 23 | `cientista` | `computacao` | 0.543 | 22 |
| 24 | `otherness` | `presenca` | 0.534 | 21 |
| 25 | `estudos` | `tecnologia` | 0.532 | 25 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (50 termos): metodo, latour, corte, strathern, gesto, haraway
- **Tópico 2** (41 termos): pesquisa, etnografia, campo, objeto, descricao, pratica
- **Tópico 3** (23 termos): modelo, parte, inscricao, claude, escrita, descreve
- **Tópico 4** (18 termos): rede, analise, ator, teoria, textual, actante
- **Tópico 5** (17 termos): humano, relacao, maquina, parcial, agencia, existencia
- **Tópico 6** (17 termos): ciencia, pesquisador, sociais, laboratorio, tecnologia, tecnico
- **Tópico 7** (8 termos): sustenta, hinterland, otherness, ausencia, manifesta, presenca
- **Tópico 8** (6 termos): artificial, inteligencia, generativa, construcao, descrever, sistemas

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [metodo, latour, corte] e **Tópico 3** [modelo, parte, inscricao] — densidade ponderada de ligação = 0.4713
- Lacuna entre **Tópico 2** [pesquisa, etnografia, campo] e **Tópico 5** [humano, relacao, maquina] — densidade ponderada de ligação = 0.5194
- Lacuna entre **Tópico 1** [metodo, latour, corte] e **Tópico 5** [humano, relacao, maquina] — densidade ponderada de ligação = 0.5565
- Lacuna entre **Tópico 3** [modelo, parte, inscricao] e **Tópico 5** [humano, relacao, maquina] — densidade ponderada de ligação = 0.5831
- Lacuna entre **Tópico 1** [metodo, latour, corte] e **Tópico 4** [rede, analise, ator] — densidade ponderada de ligação = 0.6144
- Lacuna entre **Tópico 1** [metodo, latour, corte] e **Tópico 2** [pesquisa, etnografia, campo] — densidade ponderada de ligação = 0.6927

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
