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
- Tokens significativos: **22,547**
- Grafo bruto: **6487** nós · **57005** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **3247** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `rede` | 1201 |
| 2 | `pesquisa` | 966 |
| 3 | `etnografia` | 906 |
| 4 | `artificial` | 678 |
| 5 | `inteligencia` | 665 |
| 6 | `ciencia` | 593 |
| 7 | `latour` | 551 |
| 8 | `metodo` | 512 |
| 9 | `campo` | 509 |
| 10 | `objeto` | 458 |
| 11 | `humano` | 432 |
| 12 | `descricao` | 402 |
| 13 | `corte` | 393 |
| 14 | `modelo` | 387 |
| 15 | `pratica` | 382 |
| 16 | `parte` | 365 |
| 17 | `strathern` | 357 |
| 18 | `inscricao` | 348 |
| 19 | `relacao` | 345 |
| 20 | `claude` | 338 |
| 21 | `analise` | 334 |
| 22 | `dado` | 332 |
| 23 | `gesto` | 326 |
| 24 | `ator` | 320 |
| 25 | `maquina` | 312 |
| 26 | `haraway` | 305 |
| 27 | `escrita` | 289 |
| 28 | `teoria` | 278 |
| 29 | `conceito` | 270 |
| 30 | `sociais` | 260 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `rede` | 0.0316 |
| 2 | `pesquisa` | 0.0258 |
| 3 | `etnografia` | 0.0242 |
| 4 | `artificial` | 0.0164 |
| 5 | `inteligencia` | 0.0161 |
| 6 | `ciencia` | 0.0160 |
| 7 | `latour` | 0.0154 |
| 8 | `metodo` | 0.0144 |
| 9 | `campo` | 0.0141 |
| 10 | `objeto` | 0.0126 |
| 11 | `humano` | 0.0122 |
| 12 | `descricao` | 0.0112 |
| 13 | `corte` | 0.0111 |
| 14 | `modelo` | 0.0110 |
| 15 | `pratica` | 0.0107 |
| 16 | `inscricao` | 0.0103 |
| 17 | `parte` | 0.0102 |
| 18 | `strathern` | 0.0102 |
| 19 | `relacao` | 0.0099 |
| 20 | `claude` | 0.0094 |
| 21 | `analise` | 0.0093 |
| 22 | `dado` | 0.0093 |
| 23 | `gesto` | 0.0091 |
| 24 | `haraway` | 0.0090 |
| 25 | `maquina` | 0.0090 |
| 26 | `ator` | 0.0085 |
| 27 | `escrita` | 0.0082 |
| 28 | `conceito` | 0.0079 |
| 29 | `descreve` | 0.0076 |
| 30 | `teoria` | 0.0075 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `cientifico` | 134 | 117 | +17 |
| 2 | `diagrama` | 105 | 93 | +12 |
| 3 | `computacional` | 110 | 100 | +10 |
| 4 | `manifesta` | 83 | 75 | +8 |
| 5 | `funcionam` | 124 | 116 | +8 |
| 6 | `decisao` | 133 | 126 | +7 |
| 7 | `infraestrutura` | 68 | 62 | +6 |
| 8 | `ausencia` | 69 | 63 | +6 |
| 9 | `instituicao` | 111 | 105 | +6 |
| 10 | `materiais` | 38 | 33 | +5 |
| 11 | `propriedade` | 112 | 107 | +5 |
| 12 | `fato` | 147 | 142 | +5 |
| 13 | `cientista` | 82 | 78 | +4 |
| 14 | `heterogeneos` | 99 | 95 | +4 |
| 15 | `conexoes` | 115 | 111 | +4 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `rede` | 0.3927 |
| 2 | `pesquisa` | 0.3092 |
| 3 | `etnografia` | 0.1860 |
| 4 | `latour` | 0.1103 |
| 5 | `corte` | 0.1087 |
| 6 | `campo` | 0.0813 |
| 7 | `ciencia` | 0.0793 |
| 8 | `metodo` | 0.0718 |
| 9 | `inscricao` | 0.0555 |
| 10 | `humano` | 0.0512 |
| 11 | `descricao` | 0.0504 |
| 12 | `tecnociencia` | 0.0481 |
| 13 | `strathern` | 0.0401 |
| 14 | `inteligencia` | 0.0318 |
| 15 | `maquina` | 0.0287 |
| 16 | `modos` | 0.0265 |
| 17 | `claude` | 0.0230 |
| 18 | `dado` | 0.0226 |
| 19 | `parcial` | 0.0207 |
| 20 | `pesquisador` | 0.0194 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `ausencia` | `manifesta` | 0.872 | 60 |
| 2 | `inteligencia` | `artificial` | 0.857 | 301 |
| 3 | `existencias` | `parciais` | 0.824 | 81 |
| 4 | `parcial` | `existencia` | 0.749 | 61 |
| 5 | `distribuida` | `agencia` | 0.715 | 53 |
| 6 | `teoria` | `ator` | 0.715 | 92 |
| 7 | `otherness` | `manifesta` | 0.706 | 38 |
| 8 | `presenca` | `ausencia` | 0.696 | 37 |
| 9 | `tecnico` | `letramento` | 0.647 | 43 |
| 10 | `parcial` | `conexao` | 0.639 | 43 |
| 11 | `infraestrutura` | `computacional` | 0.629 | 38 |
| 12 | `otherness` | `ausencia` | 0.601 | 28 |
| 13 | `figuracao` | `textil` | 0.598 | 54 |
| 14 | `modelo` | `linguagem` | 0.598 | 84 |
| 15 | `heterogeneos` | `materiais` | 0.598 | 36 |
| 16 | `presenca` | `manifesta` | 0.595 | 22 |
| 17 | `ciencia` | `sociais` | 0.582 | 93 |
| 18 | `textual` | `analise` | 0.580 | 58 |
| 19 | `principio` | `simetria` | 0.560 | 18 |
| 20 | `tecno` | `etnografia` | 0.555 | 73 |
| 21 | `generativa` | `artificial` | 0.548 | 62 |
| 22 | `cientista` | `computacao` | 0.545 | 22 |
| 23 | `condicoes` | `materiais` | 0.538 | 31 |
| 24 | `otherness` | `presenca` | 0.529 | 21 |
| 25 | `estudos` | `tecnologia` | 0.519 | 25 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (52 termos): latour, metodo, corte, strathern, gesto, haraway
- **Tópico 2** (37 termos): pesquisa, etnografia, campo, objeto, descricao, pratica
- **Tópico 3** (23 termos): rede, analise, ator, teoria, pesquisador, actante
- **Tópico 4** (20 termos): humano, relacao, maquina, parcial, plano, agencia
- **Tópico 5** (20 termos): ciencia, dado, sociais, laboratorio, tecnologia, tecnico
- **Tópico 6** (17 termos): modelo, inscricao, tecnociencia, linguagem, infraestrutura, diagrama
- **Tópico 7** (6 termos): artificial, inteligencia, generativa, construcao, descrever, sistemas
- **Tópico 8** (5 termos): hinterland, otherness, ausencia, presenca, manifesta

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [latour, metodo, corte] e **Tópico 5** [ciencia, dado, sociais] — densidade ponderada de ligação = 0.3260
- Lacuna entre **Tópico 4** [humano, relacao, maquina] e **Tópico 5** [ciencia, dado, sociais] — densidade ponderada de ligação = 0.5175
- Lacuna entre **Tópico 1** [latour, metodo, corte] e **Tópico 4** [humano, relacao, maquina] — densidade ponderada de ligação = 0.5298
- Lacuna entre **Tópico 1** [latour, metodo, corte] e **Tópico 3** [rede, analise, ator] — densidade ponderada de ligação = 0.5995
- Lacuna entre **Tópico 2** [pesquisa, etnografia, campo] e **Tópico 4** [humano, relacao, maquina] — densidade ponderada de ligação = 0.6162
- Lacuna entre **Tópico 3** [rede, analise, ator] e **Tópico 4** [humano, relacao, maquina] — densidade ponderada de ligação = 0.6565

## 9. Leitura interpretativa
**O que a rede mostra.** O núcleo do capítulo gira em torno de `rede`,
`etnografia` e `pesquisa`, articulando quatro famílias de termos: a
etnografia e o campo (`etnografia`, `pesquisa`, `campo`, `descricao`,
`pratica`); o método e a teoria ator-rede (`metodo`, `latour`, `corte`,
`strathern`, `haraway`); a inteligência artificial como objeto
(`artificial`, `inteligencia`, `objeto`, `modelo`, `laboratorio`); e a
simetria humano/não-humano (`humano`, `relacao`, `parcial`, `maquina`,
`agencia`). Um pequeno polo teórico denso reúne Law e Mol (`otherness`,
`ausencia`, `presenca`, `manifesta`).

**Pontes (`betweenness`).** As maiores pontes são `rede`, `pesquisa` e
`etnografia` — palavras-coringa que circulam entre os sub-vocabulários —,
seguidas de `corte` (o "corte agencial"), `latour`, `ciencia` e `metodo`. As
associações teoricamente densas aparecem como pares NPMI fortes, ainda que
pouco frequentes: `parcial ↔ existencia` (Strathern, 0,75), `distribuida ↔
agencia` (0,72), `teoria ↔ ator` (0,72), `presenca ↔ ausencia` (Law/Mol,
0,70) e `principio ↔ simetria` (0,56).

**Lacunas a desenvolver.** A ligação mais fraca está entre o tópico do
método/ator-rede (`metodo`, `latour`, `corte`) e o tópico da IA como objeto
(`artificial`, `inteligencia`, `objeto`): o vocabulário com que se promete
descrever e o objeto técnico a descrever ainda não estão suficientemente
costurados. Fraca também é a costura entre a etnografia/campo e a simetria
humano/máquina (`humano`, `parcial`, `agencia`) — exatamente a aposta que o
capítulo seguinte precisa desenvolver.

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
