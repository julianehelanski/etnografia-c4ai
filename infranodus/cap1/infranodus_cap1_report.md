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
- Tokens significativos: **22,735**
- Grafo bruto: **6520** nós · **57422** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **3243** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `rede` | 1228 |
| 2 | `pesquisa` | 974 |
| 3 | `etnografia` | 907 |
| 4 | `artificial` | 692 |
| 5 | `inteligencia` | 681 |
| 6 | `ciencia` | 591 |
| 7 | `latour` | 565 |
| 8 | `campo` | 528 |
| 9 | `metodo` | 523 |
| 10 | `objeto` | 484 |
| 11 | `humano` | 430 |
| 12 | `corte` | 423 |
| 13 | `descricao` | 407 |
| 14 | `modelo` | 391 |
| 15 | `pratica` | 380 |
| 16 | `parte` | 371 |
| 17 | `strathern` | 363 |
| 18 | `inscricao` | 348 |
| 19 | `relacao` | 337 |
| 20 | `claude` | 335 |
| 21 | `dado` | 327 |
| 22 | `analise` | 327 |
| 23 | `gesto` | 325 |
| 24 | `ator` | 320 |
| 25 | `maquina` | 310 |
| 26 | `escrita` | 304 |
| 27 | `haraway` | 299 |
| 28 | `teoria` | 276 |
| 29 | `conceito` | 271 |
| 30 | `descreve` | 263 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `rede` | 0.0321 |
| 2 | `pesquisa` | 0.0259 |
| 3 | `etnografia` | 0.0241 |
| 4 | `artificial` | 0.0166 |
| 5 | `inteligencia` | 0.0164 |
| 6 | `ciencia` | 0.0157 |
| 7 | `latour` | 0.0156 |
| 8 | `metodo` | 0.0147 |
| 9 | `campo` | 0.0145 |
| 10 | `objeto` | 0.0131 |
| 11 | `humano` | 0.0121 |
| 12 | `corte` | 0.0118 |
| 13 | `descricao` | 0.0113 |
| 14 | `modelo` | 0.0111 |
| 15 | `pratica` | 0.0106 |
| 16 | `parte` | 0.0103 |
| 17 | `strathern` | 0.0103 |
| 18 | `inscricao` | 0.0102 |
| 19 | `relacao` | 0.0096 |
| 20 | `claude` | 0.0093 |
| 21 | `dado` | 0.0091 |
| 22 | `analise` | 0.0090 |
| 23 | `gesto` | 0.0090 |
| 24 | `maquina` | 0.0089 |
| 25 | `haraway` | 0.0088 |
| 26 | `escrita` | 0.0085 |
| 27 | `ator` | 0.0084 |
| 28 | `conceito` | 0.0079 |
| 29 | `descreve` | 0.0076 |
| 30 | `teoria` | 0.0074 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `diagrama` | 107 | 94 | +13 |
| 2 | `cientifico` | 131 | 118 | +13 |
| 3 | `instituicao` | 100 | 88 | +12 |
| 4 | `manifesta` | 84 | 73 | +11 |
| 5 | `computacional` | 111 | 102 | +9 |
| 6 | `funcionam` | 125 | 116 | +9 |
| 7 | `otherness` | 58 | 50 | +8 |
| 8 | `infraestrutura` | 68 | 62 | +6 |
| 9 | `cientista` | 86 | 80 | +6 |
| 10 | `decisao` | 130 | 124 | +6 |
| 11 | `acesso` | 139 | 133 | +6 |
| 12 | `materiais` | 38 | 33 | +5 |
| 13 | `ausencia` | 69 | 64 | +5 |
| 14 | `seguir` | 92 | 87 | +5 |
| 15 | `formula` | 95 | 90 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `rede` | 0.3829 |
| 2 | `pesquisa` | 0.2961 |
| 3 | `etnografia` | 0.1833 |
| 4 | `latour` | 0.1262 |
| 5 | `corte` | 0.1159 |
| 6 | `campo` | 0.0847 |
| 7 | `ciencia` | 0.0761 |
| 8 | `metodo` | 0.0683 |
| 9 | `inscricao` | 0.0554 |
| 10 | `descricao` | 0.0506 |
| 11 | `humano` | 0.0493 |
| 12 | `tecnociencia` | 0.0480 |
| 13 | `strathern` | 0.0416 |
| 14 | `objeto` | 0.0328 |
| 15 | `claude` | 0.0308 |
| 16 | `inteligencia` | 0.0299 |
| 17 | `maquina` | 0.0294 |
| 18 | `modos` | 0.0264 |
| 19 | `dado` | 0.0217 |
| 20 | `pratica` | 0.0209 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `ausencia` | `manifesta` | 0.872 | 60 |
| 2 | `inteligencia` | `artificial` | 0.857 | 307 |
| 3 | `existencias` | `parciais` | 0.825 | 81 |
| 4 | `parcial` | `existencia` | 0.749 | 61 |
| 5 | `distribuida` | `agencia` | 0.716 | 53 |
| 6 | `teoria` | `ator` | 0.716 | 92 |
| 7 | `otherness` | `manifesta` | 0.706 | 38 |
| 8 | `presenca` | `ausencia` | 0.697 | 37 |
| 9 | `tecnico` | `letramento` | 0.650 | 46 |
| 10 | `parcial` | `conexao` | 0.639 | 43 |
| 11 | `infraestrutura` | `computacional` | 0.630 | 38 |
| 12 | `modelo` | `linguagem` | 0.605 | 87 |
| 13 | `otherness` | `ausencia` | 0.601 | 28 |
| 14 | `figuracao` | `textil` | 0.599 | 54 |
| 15 | `heterogeneos` | `materiais` | 0.598 | 36 |
| 16 | `presenca` | `manifesta` | 0.596 | 22 |
| 17 | `ciencia` | `sociais` | 0.582 | 93 |
| 18 | `textual` | `analise` | 0.580 | 58 |
| 19 | `principio` | `simetria` | 0.560 | 18 |
| 20 | `tecno` | `etnografia` | 0.553 | 73 |
| 21 | `cientista` | `computacao` | 0.545 | 22 |
| 22 | `generativa` | `artificial` | 0.545 | 62 |
| 23 | `condicoes` | `materiais` | 0.539 | 31 |
| 24 | `otherness` | `presenca` | 0.530 | 21 |
| 25 | `haraway` | `barad` | 0.517 | 29 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (51 termos): latour, metodo, corte, strathern, gesto, haraway
- **Tópico 2** (39 termos): etnografia, objeto, descricao, modelo, pratica, parte
- **Tópico 3** (20 termos): humano, relacao, maquina, parcial, plano, agencia
- **Tópico 4** (19 termos): ciencia, campo, dado, sociais, conhecimento, spira
- **Tópico 5** (15 termos): rede, analise, ator, teoria, actante, termos
- **Tópico 6** (15 termos): materiais, infraestrutura, ponto, instituicao, condicoes, heterogeneos
- **Tópico 7** (14 termos): pesquisa, artificial, inteligencia, pesquisador, laboratorio, generativa
- **Tópico 8** (7 termos): hinterland, otherness, ausencia, presenca, manifesta, palavra

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [latour, metodo, corte] e **Tópico 4** [ciencia, campo, dado] — densidade ponderada de ligação = 0.4881
- Lacuna entre **Tópico 3** [humano, relacao, maquina] e **Tópico 4** [ciencia, campo, dado] — densidade ponderada de ligação = 0.5842
- Lacuna entre **Tópico 1** [latour, metodo, corte] e **Tópico 3** [humano, relacao, maquina] — densidade ponderada de ligação = 0.5922
- Lacuna entre **Tópico 2** [etnografia, objeto, descricao] e **Tópico 3** [humano, relacao, maquina] — densidade ponderada de ligação = 0.6192
- Lacuna entre **Tópico 1** [latour, metodo, corte] e **Tópico 2** [etnografia, objeto, descricao] — densidade ponderada de ligação = 0.6893
- Lacuna entre **Tópico 1** [latour, metodo, corte] e **Tópico 5** [rede, analise, ator] — densidade ponderada de ligação = 0.6941

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
