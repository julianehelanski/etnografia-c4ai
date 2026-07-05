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
- Tokens significativos: **22,606**
- Grafo bruto: **6503** nós · **57156** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **3248** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `rede` | 1256 |
| 2 | `pesquisa` | 969 |
| 3 | `etnografia` | 921 |
| 4 | `artificial` | 693 |
| 5 | `inteligencia` | 683 |
| 6 | `ciencia` | 590 |
| 7 | `latour` | 556 |
| 8 | `campo` | 528 |
| 9 | `metodo` | 498 |
| 10 | `objeto` | 478 |
| 11 | `humano` | 435 |
| 12 | `corte` | 425 |
| 13 | `descricao` | 403 |
| 14 | `pratica` | 377 |
| 15 | `modelo` | 364 |
| 16 | `strathern` | 363 |
| 17 | `inscricao` | 345 |
| 18 | `relacao` | 326 |
| 19 | `analise` | 325 |
| 20 | `ator` | 320 |
| 21 | `dado` | 317 |
| 22 | `parte` | 313 |
| 23 | `maquina` | 312 |
| 24 | `gesto` | 311 |
| 25 | `haraway` | 299 |
| 26 | `teoria` | 276 |
| 27 | `conceito` | 267 |
| 28 | `descreve` | 266 |
| 29 | `sociais` | 263 |
| 30 | `claude` | 250 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `rede` | 0.0331 |
| 2 | `pesquisa` | 0.0259 |
| 3 | `etnografia` | 0.0247 |
| 4 | `artificial` | 0.0167 |
| 5 | `inteligencia` | 0.0165 |
| 6 | `ciencia` | 0.0158 |
| 7 | `latour` | 0.0153 |
| 8 | `campo` | 0.0146 |
| 9 | `metodo` | 0.0140 |
| 10 | `objeto` | 0.0130 |
| 11 | `humano` | 0.0123 |
| 12 | `corte` | 0.0119 |
| 13 | `descricao` | 0.0112 |
| 14 | `pratica` | 0.0106 |
| 15 | `modelo` | 0.0104 |
| 16 | `strathern` | 0.0104 |
| 17 | `inscricao` | 0.0101 |
| 18 | `relacao` | 0.0093 |
| 19 | `analise` | 0.0091 |
| 20 | `parte` | 0.0090 |
| 21 | `maquina` | 0.0090 |
| 22 | `dado` | 0.0089 |
| 23 | `haraway` | 0.0088 |
| 24 | `gesto` | 0.0087 |
| 25 | `ator` | 0.0085 |
| 26 | `conceito` | 0.0078 |
| 27 | `descreve` | 0.0078 |
| 28 | `teoria` | 0.0074 |
| 29 | `sociais` | 0.0074 |
| 30 | `partir` | 0.0073 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `computacional` | 110 | 97 | +13 |
| 2 | `cientifico` | 135 | 123 | +12 |
| 3 | `cortes` | 104 | 94 | +10 |
| 4 | `manifesta` | 83 | 75 | +8 |
| 5 | `diagrama` | 91 | 84 | +7 |
| 6 | `acesso` | 116 | 109 | +7 |
| 7 | `materiais` | 38 | 32 | +6 |
| 8 | `otherness` | 56 | 50 | +6 |
| 9 | `infraestrutura` | 70 | 64 | +6 |
| 10 | `condicoes` | 105 | 99 | +6 |
| 11 | `funcionam` | 123 | 117 | +6 |
| 12 | `hinterland` | 51 | 46 | +5 |
| 13 | `ausencia` | 68 | 63 | +5 |
| 14 | `cientista` | 86 | 81 | +5 |
| 15 | `instituicao` | 92 | 87 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `rede` | 0.4125 |
| 2 | `pesquisa` | 0.2895 |
| 3 | `etnografia` | 0.1890 |
| 4 | `latour` | 0.1166 |
| 5 | `corte` | 0.1151 |
| 6 | `campo` | 0.0839 |
| 7 | `ciencia` | 0.0758 |
| 8 | `metodo` | 0.0557 |
| 9 | `descricao` | 0.0544 |
| 10 | `humano` | 0.0531 |
| 11 | `inscricao` | 0.0526 |
| 12 | `tecnociencia` | 0.0475 |
| 13 | `strathern` | 0.0396 |
| 14 | `inteligencia` | 0.0300 |
| 15 | `maquina` | 0.0294 |
| 16 | `modos` | 0.0268 |
| 17 | `objeto` | 0.0259 |
| 18 | `pratica` | 0.0216 |
| 19 | `parcial` | 0.0207 |
| 20 | `pesquisador` | 0.0198 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `ausencia` | `manifesta` | 0.872 | 60 |
| 2 | `inteligencia` | `artificial` | 0.857 | 307 |
| 3 | `existencias` | `parciais` | 0.824 | 81 |
| 4 | `parcial` | `existencia` | 0.749 | 61 |
| 5 | `distribuida` | `agencia` | 0.723 | 53 |
| 6 | `teoria` | `ator` | 0.715 | 92 |
| 7 | `otherness` | `manifesta` | 0.706 | 38 |
| 8 | `presenca` | `ausencia` | 0.696 | 37 |
| 9 | `tecnico` | `letramento` | 0.649 | 46 |
| 10 | `parcial` | `conexao` | 0.639 | 43 |
| 11 | `infraestrutura` | `computacional` | 0.630 | 38 |
| 12 | `modelo` | `linguagem` | 0.608 | 84 |
| 13 | `otherness` | `ausencia` | 0.601 | 28 |
| 14 | `figuracao` | `textil` | 0.598 | 54 |
| 15 | `heterogeneos` | `materiais` | 0.598 | 36 |
| 16 | `presenca` | `manifesta` | 0.596 | 22 |
| 17 | `ciencia` | `sociais` | 0.582 | 93 |
| 18 | `textual` | `analise` | 0.565 | 54 |
| 19 | `principio` | `simetria` | 0.560 | 18 |
| 20 | `generativa` | `artificial` | 0.555 | 62 |
| 21 | `tecno` | `etnografia` | 0.554 | 73 |
| 22 | `cientista` | `computacao` | 0.545 | 22 |
| 23 | `acesso` | `disponivel` | 0.543 | 18 |
| 24 | `condicoes` | `materiais` | 0.538 | 31 |
| 25 | `otherness` | `presenca` | 0.529 | 21 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (52 termos): latour, metodo, corte, strathern, gesto, haraway
- **Tópico 2** (27 termos): pesquisa, artificial, inteligencia, objeto, modelo, claude
- **Tópico 3** (24 termos): ciencia, campo, dado, sociais, escrita, conhecimento
- **Tópico 4** (20 termos): etnografia, descricao, pratica, materiais, material, sustenta
- **Tópico 5** (20 termos): humano, relacao, maquina, parcial, plano, agencia
- **Tópico 6** (17 termos): rede, analise, ator, teoria, termos, actante
- **Tópico 7** (13 termos): inscricao, parte, descreve, tecnociencia, modos, diagrama
- **Tópico 8** (7 termos): hinterland, otherness, ausencia, presenca, manifesta, palavra

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [latour, metodo, corte] e **Tópico 2** [pesquisa, artificial, inteligencia] — densidade ponderada de ligação = 0.5178
- Lacuna entre **Tópico 1** [latour, metodo, corte] e **Tópico 3** [ciencia, campo, dado] — densidade ponderada de ligação = 0.5208
- Lacuna entre **Tópico 4** [etnografia, descricao, pratica] e **Tópico 5** [humano, relacao, maquina] — densidade ponderada de ligação = 0.5425
- Lacuna entre **Tópico 3** [ciencia, campo, dado] e **Tópico 5** [humano, relacao, maquina] — densidade ponderada de ligação = 0.5625
- Lacuna entre **Tópico 1** [latour, metodo, corte] e **Tópico 5** [humano, relacao, maquina] — densidade ponderada de ligação = 0.5875
- Lacuna entre **Tópico 2** [pesquisa, artificial, inteligencia] e **Tópico 5** [humano, relacao, maquina] — densidade ponderada de ligação = 0.7352

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
