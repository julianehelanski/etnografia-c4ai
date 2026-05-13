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
- Tokens significativos: **18,794**
- Grafo bruto: **5978** nós · **49023** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **2763** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `rede` | 745 |
| 2 | `pesquisa` | 689 |
| 3 | `ciencia` | 562 |
| 4 | `etnografia` | 533 |
| 5 | `metodo` | 451 |
| 6 | `inteligencia` | 402 |
| 7 | `artificial` | 393 |
| 8 | `humano` | 334 |
| 9 | `claude` | 330 |
| 10 | `composicao` | 324 |
| 11 | `objeto` | 320 |
| 12 | `campo` | 312 |
| 13 | `modelo` | 311 |
| 14 | `latour` | 288 |
| 15 | `pesquisador` | 277 |
| 16 | `pratica` | 270 |
| 17 | `sociais` | 258 |
| 18 | `parte` | 255 |
| 19 | `inscricao` | 254 |
| 20 | `gesto` | 251 |
| 21 | `dado` | 245 |
| 22 | `haraway` | 237 |
| 23 | `descricao` | 232 |
| 24 | `escrita` | 221 |
| 25 | `partir` | 220 |
| 26 | `corte` | 218 |
| 27 | `conhecimento` | 217 |
| 28 | `lugar` | 214 |
| 29 | `ator` | 212 |
| 30 | `strathern` | 209 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `rede` | 0.0264 |
| 2 | `pesquisa` | 0.0243 |
| 3 | `ciencia` | 0.0197 |
| 4 | `etnografia` | 0.0189 |
| 5 | `metodo` | 0.0166 |
| 6 | `inteligencia` | 0.0130 |
| 7 | `artificial` | 0.0128 |
| 8 | `humano` | 0.0128 |
| 9 | `claude` | 0.0118 |
| 10 | `objeto` | 0.0117 |
| 11 | `composicao` | 0.0117 |
| 12 | `modelo` | 0.0116 |
| 13 | `campo` | 0.0114 |
| 14 | `latour` | 0.0108 |
| 15 | `pratica` | 0.0102 |
| 16 | `pesquisador` | 0.0102 |
| 17 | `inscricao` | 0.0099 |
| 18 | `gesto` | 0.0094 |
| 19 | `parte` | 0.0093 |
| 20 | `sociais` | 0.0092 |
| 21 | `haraway` | 0.0092 |
| 22 | `dado` | 0.0092 |
| 23 | `descricao` | 0.0087 |
| 24 | `partir` | 0.0085 |
| 25 | `corte` | 0.0084 |
| 26 | `conhecimento` | 0.0082 |
| 27 | `lugar` | 0.0082 |
| 28 | `escrita` | 0.0081 |
| 29 | `strathern` | 0.0080 |
| 30 | `figuracao` | 0.0079 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `computacional` | 88 | 76 | +12 |
| 2 | `cientifico` | 86 | 75 | +11 |
| 3 | `termos` | 53 | 45 | +8 |
| 4 | `modos` | 64 | 56 | +8 |
| 5 | `decisao` | 116 | 109 | +7 |
| 6 | `actante` | 49 | 43 | +6 |
| 7 | `diagrama` | 84 | 78 | +6 |
| 8 | `condicoes` | 102 | 96 | +6 |
| 9 | `heterogeneos` | 107 | 101 | +6 |
| 10 | `registro` | 122 | 116 | +6 |
| 11 | `nocao` | 133 | 128 | +5 |
| 12 | `pensar` | 37 | 33 | +4 |
| 13 | `conceito` | 66 | 62 | +4 |
| 14 | `infraestrutura` | 73 | 69 | +4 |
| 15 | `funcionam` | 85 | 81 | +4 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `pesquisa` | 0.3339 |
| 2 | `rede` | 0.2539 |
| 3 | `ciencia` | 0.1459 |
| 4 | `etnografia` | 0.1443 |
| 5 | `metodo` | 0.1185 |
| 6 | `dado` | 0.0539 |
| 7 | `humano` | 0.0524 |
| 8 | `inteligencia` | 0.0480 |
| 9 | `objeto` | 0.0444 |
| 10 | `pratica` | 0.0437 |
| 11 | `sociais` | 0.0435 |
| 12 | `latour` | 0.0420 |
| 13 | `inscricao` | 0.0415 |
| 14 | `pesquisador` | 0.0415 |
| 15 | `composicao` | 0.0403 |
| 16 | `claude` | 0.0386 |
| 17 | `tecnociencia` | 0.0341 |
| 18 | `campo` | 0.0336 |
| 19 | `artificial` | 0.0281 |
| 20 | `figuracao` | 0.0257 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `inteligencia` | `artificial` | 0.857 | 193 |
| 2 | `ausencia` | `manifesta` | 0.852 | 57 |
| 3 | `existencias` | `parciais` | 0.813 | 69 |
| 4 | `existencia` | `parcial` | 0.768 | 34 |
| 5 | `teoria` | `ator` | 0.734 | 57 |
| 6 | `agencia` | `distribuida` | 0.723 | 41 |
| 7 | `otherness` | `manifesta` | 0.694 | 35 |
| 8 | `letramento` | `tecnico` | 0.675 | 47 |
| 9 | `ausencia` | `presenca` | 0.657 | 34 |
| 10 | `computacional` | `infraestrutura` | 0.620 | 35 |
| 11 | `figuracao` | `textil` | 0.606 | 39 |
| 12 | `ausencia` | `otherness` | 0.575 | 26 |
| 13 | `manifesta` | `presenca` | 0.570 | 20 |
| 14 | `maior` | `termos` | 0.566 | 31 |
| 15 | `heterogeneos` | `materiais` | 0.566 | 24 |
| 16 | `modelo` | `linguagem` | 0.561 | 59 |
| 17 | `ciencia` | `sociais` | 0.557 | 98 |
| 18 | `cientista` | `computacao` | 0.557 | 28 |
| 19 | `costura` | `figuracao` | 0.546 | 21 |
| 20 | `possibilidade` | `condicao` | 0.540 | 21 |
| 21 | `simetria` | `principio` | 0.535 | 12 |
| 22 | `precisa` | `ponto` | 0.521 | 23 |
| 23 | `estudos` | `tecnologia` | 0.519 | 20 |
| 24 | `otherness` | `presenca` | 0.516 | 20 |
| 25 | `contexto` | `palavra` | 0.511 | 14 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (39 termos): gesto, haraway, partir, corte, strathern, figuracao
- **Tópico 2** (36 termos): pesquisa, etnografia, inteligencia, artificial, campo, pratica
- **Tópico 3** (25 termos): rede, latour, ator, agencia, teoria, actante
- **Tópico 4** (24 termos): ciencia, sociais, inscricao, tecnico, cientista, tecnologia
- **Tópico 5** (23 termos): claude, composicao, objeto, modelo, pesquisador, parte
- **Tópico 6** (14 termos): humano, maquina, termos, existencia, parcial, decisoes
- **Tópico 7** (11 termos): metodo, sustenta, experiencia, posicao, regra, simetria
- **Tópico 8** (8 termos): hinterland, ausencia, otherness, manifesta, presenca, presente

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [gesto, haraway, partir] e **Tópico 4** [ciencia, sociais, inscricao] — densidade ponderada de ligação = 0.2030
- Lacuna entre **Tópico 1** [gesto, haraway, partir] e **Tópico 5** [claude, composicao, objeto] — densidade ponderada de ligação = 0.4158
- Lacuna entre **Tópico 1** [gesto, haraway, partir] e **Tópico 3** [rede, latour, ator] — densidade ponderada de ligação = 0.5118
- Lacuna entre **Tópico 3** [rede, latour, ator] e **Tópico 4** [ciencia, sociais, inscricao] — densidade ponderada de ligação = 0.5167
- Lacuna entre **Tópico 2** [pesquisa, etnografia, inteligencia] e **Tópico 3** [rede, latour, ator] — densidade ponderada de ligação = 0.5300
- Lacuna entre **Tópico 1** [gesto, haraway, partir] e **Tópico 2** [pesquisa, etnografia, inteligencia] — densidade ponderada de ligação = 0.5627

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
