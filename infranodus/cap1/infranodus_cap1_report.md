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
- Tokens significativos: **22,790**
- Grafo bruto: **6514** nós · **57529** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **3250** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `rede` | 1276 |
| 2 | `pesquisa` | 965 |
| 3 | `etnografia` | 920 |
| 4 | `artificial` | 698 |
| 5 | `inteligencia` | 693 |
| 6 | `ciencia` | 599 |
| 7 | `latour` | 597 |
| 8 | `campo` | 537 |
| 9 | `metodo` | 518 |
| 10 | `objeto` | 485 |
| 11 | `corte` | 463 |
| 12 | `humano` | 429 |
| 13 | `descricao` | 414 |
| 14 | `inscricao` | 392 |
| 15 | `pratica` | 388 |
| 16 | `strathern` | 372 |
| 17 | `modelo` | 357 |
| 18 | `relacao` | 346 |
| 19 | `analise` | 345 |
| 20 | `ator` | 336 |
| 21 | `dado` | 328 |
| 22 | `maquina` | 322 |
| 23 | `gesto` | 318 |
| 24 | `parte` | 313 |
| 25 | `haraway` | 308 |
| 26 | `teoria` | 302 |
| 27 | `conceito` | 277 |
| 28 | `descreve` | 276 |
| 29 | `sociais` | 270 |
| 30 | `escrita` | 255 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `rede` | 0.0330 |
| 2 | `pesquisa` | 0.0254 |
| 3 | `etnografia` | 0.0242 |
| 4 | `artificial` | 0.0165 |
| 5 | `inteligencia` | 0.0165 |
| 6 | `latour` | 0.0161 |
| 7 | `ciencia` | 0.0157 |
| 8 | `campo` | 0.0145 |
| 9 | `metodo` | 0.0142 |
| 10 | `objeto` | 0.0130 |
| 11 | `corte` | 0.0127 |
| 12 | `humano` | 0.0120 |
| 13 | `descricao` | 0.0113 |
| 14 | `inscricao` | 0.0112 |
| 15 | `pratica` | 0.0107 |
| 16 | `strathern` | 0.0104 |
| 17 | `modelo` | 0.0102 |
| 18 | `relacao` | 0.0097 |
| 19 | `analise` | 0.0094 |
| 20 | `maquina` | 0.0091 |
| 21 | `dado` | 0.0090 |
| 22 | `haraway` | 0.0089 |
| 23 | `parte` | 0.0089 |
| 24 | `gesto` | 0.0088 |
| 25 | `ator` | 0.0086 |
| 26 | `conceito` | 0.0080 |
| 27 | `descreve` | 0.0079 |
| 28 | `teoria` | 0.0078 |
| 29 | `sociais` | 0.0075 |
| 30 | `escrita` | 0.0073 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `cientifico` | 140 | 126 | +14 |
| 2 | `computacional` | 111 | 99 | +12 |
| 3 | `instituicao` | 95 | 84 | +11 |
| 4 | `diagrama` | 106 | 95 | +11 |
| 5 | `infraestrutura` | 73 | 64 | +9 |
| 6 | `acesso` | 119 | 110 | +9 |
| 7 | `funcionam` | 124 | 115 | +9 |
| 8 | `decisao` | 139 | 132 | +7 |
| 9 | `termos` | 52 | 46 | +6 |
| 10 | `cortes` | 102 | 96 | +6 |
| 11 | `actante` | 53 | 48 | +5 |
| 12 | `conexoes` | 116 | 111 | +5 |
| 13 | `fato` | 141 | 136 | +5 |
| 14 | `disponivel` | 154 | 149 | +5 |
| 15 | `materiais` | 38 | 34 | +4 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `rede` | 0.4029 |
| 2 | `pesquisa` | 0.2594 |
| 3 | `etnografia` | 0.1947 |
| 4 | `latour` | 0.1607 |
| 5 | `corte` | 0.1183 |
| 6 | `campo` | 0.0879 |
| 7 | `ciencia` | 0.0743 |
| 8 | `inscricao` | 0.0722 |
| 9 | `metodo` | 0.0615 |
| 10 | `descricao` | 0.0587 |
| 11 | `humano` | 0.0476 |
| 12 | `strathern` | 0.0400 |
| 13 | `objeto` | 0.0322 |
| 14 | `maquina` | 0.0312 |
| 15 | `dado` | 0.0266 |
| 16 | `modos` | 0.0254 |
| 17 | `parcial` | 0.0227 |
| 18 | `hinterland` | 0.0208 |
| 19 | `laboratorio` | 0.0202 |
| 20 | `pratica` | 0.0201 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `ausencia` | `manifesta` | 0.864 | 67 |
| 2 | `inteligencia` | `artificial` | 0.857 | 310 |
| 3 | `existencias` | `parciais` | 0.825 | 81 |
| 4 | `parcial` | `existencia` | 0.744 | 59 |
| 5 | `teoria` | `ator` | 0.727 | 101 |
| 6 | `distribuida` | `agencia` | 0.726 | 52 |
| 7 | `presenca` | `ausencia` | 0.706 | 43 |
| 8 | `otherness` | `manifesta` | 0.683 | 40 |
| 9 | `tecnico` | `letramento` | 0.654 | 46 |
| 10 | `parcial` | `conexao` | 0.639 | 43 |
| 11 | `pergunta` | `responde` | 0.635 | 36 |
| 12 | `infraestrutura` | `computacional` | 0.630 | 38 |
| 13 | `presenca` | `manifesta` | 0.621 | 28 |
| 14 | `otherness` | `ausencia` | 0.616 | 34 |
| 15 | `modelo` | `linguagem` | 0.611 | 84 |
| 16 | `figuracao` | `textil` | 0.599 | 54 |
| 17 | `heterogeneos` | `materiais` | 0.598 | 36 |
| 18 | `ciencia` | `sociais` | 0.580 | 94 |
| 19 | `textual` | `analise` | 0.566 | 56 |
| 20 | `generativa` | `artificial` | 0.554 | 62 |
| 21 | `tecno` | `etnografia` | 0.554 | 73 |
| 22 | `cientista` | `computacao` | 0.550 | 22 |
| 23 | `principio` | `simetria` | 0.547 | 18 |
| 24 | `acesso` | `disponivel` | 0.544 | 18 |
| 25 | `otherness` | `presenca` | 0.543 | 25 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (49 termos): latour, metodo, corte, strathern, gesto, haraway
- **Tópico 2** (34 termos): pesquisa, artificial, inteligencia, objeto, pratica, modelo
- **Tópico 3** (27 termos): etnografia, descricao, inscricao, parte, descreve, tecnociencia
- **Tópico 4** (20 termos): humano, relacao, maquina, parcial, plano, agencia
- **Tópico 5** (19 termos): rede, analise, ator, teoria, termos, actante
- **Tópico 6** (15 termos): ciencia, campo, dado, sociais, escrita, tecnologia
- **Tópico 7** (9 termos): materiais, ponto, condicoes, heterogeneos, precisa, momento
- **Tópico 8** (7 termos): otherness, hinterland, ausencia, presenca, manifesta, palavra

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [latour, metodo, corte] e **Tópico 2** [pesquisa, artificial, inteligencia] — densidade ponderada de ligação = 0.5582
- Lacuna entre **Tópico 1** [latour, metodo, corte] e **Tópico 4** [humano, relacao, maquina] — densidade ponderada de ligação = 0.5827
- Lacuna entre **Tópico 2** [pesquisa, artificial, inteligencia] e **Tópico 4** [humano, relacao, maquina] — densidade ponderada de ligação = 0.5956
- Lacuna entre **Tópico 3** [etnografia, descricao, inscricao] e **Tópico 4** [humano, relacao, maquina] — densidade ponderada de ligação = 0.5963
- Lacuna entre **Tópico 4** [humano, relacao, maquina] e **Tópico 5** [rede, analise, ator] — densidade ponderada de ligação = 0.6553
- Lacuna entre **Tópico 1** [latour, metodo, corte] e **Tópico 5** [rede, analise, ator] — densidade ponderada de ligação = 0.6681

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
