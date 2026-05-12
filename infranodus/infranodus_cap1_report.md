# Análise de rede textual — Capítulo 1

> Análise de rede textual (*text network analysis*, Paranyushkin 2019)
> aplicada ao arquivo `capitulo1`. O texto foi limpo de comandos LaTeX,
> citações e notas de rodapé foram reincorporadas; janela deslizante de
> 4 *tokens* com pesos decrescentes pela distância (3-2-1). Comunidades
> detectadas por Louvain ponderado. Esta versão acrescenta duas métricas
> *informativas* que não dependem da frequência bruta: **PageRank** dos
> nós e **NPMI** das arestas. As métricas baseadas em frequência são
> mantidas em paralelo, para comparação.

## 1. Resumo quantitativo
- Tokens significativos: **18,005**
- Grafo bruto: **5782** nós · **47055** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **2730** arestas
- Tópicos detectados (Louvain): **9**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `rede` | 735 |
| 2 | `pesquisa` | 678 |
| 3 | `ciencia` | 559 |
| 4 | `etnografia` | 534 |
| 5 | `metodo` | 449 |
| 6 | `inteligencia` | 403 |
| 7 | `artificial` | 393 |
| 8 | `humano` | 346 |
| 9 | `claude` | 323 |
| 10 | `objeto` | 323 |
| 11 | `composicao` | 319 |
| 12 | `campo` | 315 |
| 13 | `modelo` | 301 |
| 14 | `latour` | 292 |
| 15 | `pratica` | 270 |
| 16 | `pesquisador` | 267 |
| 17 | `haraway` | 264 |
| 18 | `sociais` | 262 |
| 19 | `gesto` | 255 |
| 20 | `parte` | 247 |
| 21 | `dado` | 245 |
| 22 | `inscricao` | 245 |
| 23 | `descricao` | 233 |
| 24 | `strathern` | 227 |
| 25 | `vocabulario` | 222 |
| 26 | `corte` | 215 |
| 27 | `escrita` | 215 |
| 28 | `conhecimento` | 215 |
| 29 | `lugar` | 214 |
| 30 | `ator` | 211 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `rede` | 0.0261 |
| 2 | `pesquisa` | 0.0240 |
| 3 | `ciencia` | 0.0197 |
| 4 | `etnografia` | 0.0192 |
| 5 | `metodo` | 0.0166 |
| 6 | `humano` | 0.0133 |
| 7 | `inteligencia` | 0.0132 |
| 8 | `artificial` | 0.0129 |
| 9 | `objeto` | 0.0119 |
| 10 | `campo` | 0.0117 |
| 11 | `claude` | 0.0116 |
| 12 | `composicao` | 0.0116 |
| 13 | `modelo` | 0.0113 |
| 14 | `latour` | 0.0110 |
| 15 | `haraway` | 0.0103 |
| 16 | `pratica` | 0.0103 |
| 17 | `pesquisador` | 0.0099 |
| 18 | `inscricao` | 0.0096 |
| 19 | `gesto` | 0.0096 |
| 20 | `sociais` | 0.0094 |
| 21 | `dado` | 0.0092 |
| 22 | `parte` | 0.0091 |
| 23 | `descricao` | 0.0089 |
| 24 | `strathern` | 0.0088 |
| 25 | `vocabulario` | 0.0084 |
| 26 | `corte` | 0.0084 |
| 27 | `partir` | 0.0082 |
| 28 | `conhecimento` | 0.0082 |
| 29 | `lugar` | 0.0082 |
| 30 | `escrita` | 0.0079 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `heterogeneos` | 121 | 108 | +13 |
| 2 | `cientifico` | 85 | 76 | +9 |
| 3 | `computacional` | 87 | 78 | +9 |
| 4 | `decisao` | 114 | 106 | +8 |
| 5 | `registro` | 119 | 111 | +8 |
| 6 | `condicoes` | 100 | 93 | +7 |
| 7 | `nomeia` | 63 | 58 | +5 |
| 8 | `infraestrutura` | 73 | 68 | +5 |
| 9 | `ontologia` | 101 | 96 | +5 |
| 10 | `situada` | 135 | 130 | +5 |
| 11 | `sistemas` | 142 | 137 | +5 |
| 12 | `inscricao` | 22 | 18 | +4 |
| 13 | `partir` | 31 | 27 | +4 |
| 14 | `pensar` | 37 | 33 | +4 |
| 15 | `materiais` | 45 | 41 | +4 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `pesquisa` | 0.3145 |
| 2 | `rede` | 0.2575 |
| 3 | `etnografia` | 0.1447 |
| 4 | `ciencia` | 0.1400 |
| 5 | `metodo` | 0.1221 |
| 6 | `humano` | 0.0594 |
| 7 | `dado` | 0.0571 |
| 8 | `inteligencia` | 0.0493 |
| 9 | `objeto` | 0.0485 |
| 10 | `claude` | 0.0437 |
| 11 | `pratica` | 0.0431 |
| 12 | `inscricao` | 0.0426 |
| 13 | `latour` | 0.0418 |
| 14 | `sociais` | 0.0404 |
| 15 | `composicao` | 0.0365 |
| 16 | `pesquisador` | 0.0346 |
| 17 | `campo` | 0.0345 |
| 18 | `strathern` | 0.0325 |
| 19 | `tecnociencia` | 0.0314 |
| 20 | `artificial` | 0.0308 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `inteligencia` | `artificial` | 0.855 | 193 |
| 2 | `ausencia` | `manifesta` | 0.851 | 57 |
| 3 | `parciais` | `existencias` | 0.811 | 69 |
| 4 | `existencia` | `parcial` | 0.766 | 34 |
| 5 | `teoria` | `ator` | 0.732 | 57 |
| 6 | `agencia` | `distribuida` | 0.721 | 41 |
| 7 | `otherness` | `manifesta` | 0.692 | 35 |
| 8 | `tecnico` | `letramento` | 0.672 | 47 |
| 9 | `ausencia` | `presenca` | 0.661 | 34 |
| 10 | `computacional` | `infraestrutura` | 0.617 | 35 |
| 11 | `textil` | `figuracao` | 0.604 | 39 |
| 12 | `presenca` | `manifesta` | 0.573 | 20 |
| 13 | `ausencia` | `otherness` | 0.572 | 26 |
| 14 | `materiais` | `heterogeneos` | 0.570 | 24 |
| 15 | `sociais` | `ciencia` | 0.555 | 98 |
| 16 | `computacao` | `cientista` | 0.554 | 28 |
| 17 | `modelo` | `linguagem` | 0.551 | 56 |
| 18 | `costura` | `figuracao` | 0.543 | 21 |
| 19 | `precisa` | `ponto` | 0.541 | 23 |
| 20 | `possibilidade` | `condicao` | 0.537 | 21 |
| 21 | `simetria` | `principio` | 0.524 | 12 |
| 22 | `strathern` | `barad` | 0.523 | 21 |
| 23 | `presenca` | `otherness` | 0.519 | 20 |
| 24 | `tecnologia` | `estudos` | 0.515 | 20 |
| 25 | `parciais` | `conexoes` | 0.510 | 21 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (53 termos): metodo, latour, haraway, gesto, strathern, vocabulario
- **Tópico 2** (29 termos): pesquisa, etnografia, inteligencia, artificial, campo, pratica
- **Tópico 3** (23 termos): ciencia, sociais, dado, tecnico, cientista, tecnologia
- **Tópico 4** (20 termos): claude, composicao, modelo, parte, inscricao, escrita
- **Tópico 5** (15 termos): rede, objeto, pesquisador, ator, actante, teoria
- **Tópico 6** (14 termos): humano, agencia, maquina, distribuida, existencia, termos
- **Tópico 7** (10 termos): infraestrutura, cientifico, computacional, decisao, instituicao, momento
- **Tópico 8** (9 termos): conhecimento, modos, produz, mundo, produzem, pensamento

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [metodo, latour, haraway] e **Tópico 3** [ciencia, sociais, dado] — densidade ponderada de ligação = 0.2986
- Lacuna entre **Tópico 1** [metodo, latour, haraway] e **Tópico 4** [claude, composicao, modelo] — densidade ponderada de ligação = 0.4406
- Lacuna entre **Tópico 3** [ciencia, sociais, dado] e **Tópico 4** [claude, composicao, modelo] — densidade ponderada de ligação = 0.5196
- Lacuna entre **Tópico 1** [metodo, latour, haraway] e **Tópico 5** [rede, objeto, pesquisador] — densidade ponderada de ligação = 0.5535
- Lacuna entre **Tópico 1** [metodo, latour, haraway] e **Tópico 2** [pesquisa, etnografia, inteligencia] — densidade ponderada de ligação = 0.6194
- Lacuna entre **Tópico 3** [ciencia, sociais, dado] e **Tópico 5** [rede, objeto, pesquisador] — densidade ponderada de ligação = 0.6667

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
**Visões frequentistas (mantidas)**
- `infranodus_cap1_network.png` — rede completa, tamanho por degree.
- `infranodus_cap1_focus.png` — núcleo (top-100, peso ≥ 3).

**Visões informativas (novas)**
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
