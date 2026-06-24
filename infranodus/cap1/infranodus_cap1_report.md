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
- Tokens significativos: **22,133**
- Grafo bruto: **6416** nós · **56025** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **3223** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `rede` | 1204 |
| 2 | `pesquisa` | 963 |
| 3 | `etnografia` | 887 |
| 4 | `artificial` | 676 |
| 5 | `inteligencia` | 666 |
| 6 | `ciencia` | 594 |
| 7 | `latour` | 537 |
| 8 | `campo` | 513 |
| 9 | `metodo` | 501 |
| 10 | `objeto` | 458 |
| 11 | `humano` | 432 |
| 12 | `descricao` | 402 |
| 13 | `corte` | 385 |
| 14 | `pratica` | 384 |
| 15 | `strathern` | 360 |
| 16 | `modelo` | 355 |
| 17 | `relacao` | 345 |
| 18 | `inscricao` | 338 |
| 19 | `analise` | 330 |
| 20 | `parte` | 325 |
| 21 | `dado` | 324 |
| 22 | `ator` | 316 |
| 23 | `maquina` | 312 |
| 24 | `gesto` | 308 |
| 25 | `haraway` | 305 |
| 26 | `claude` | 283 |
| 27 | `teoria` | 278 |
| 28 | `descreve` | 263 |
| 29 | `conceito` | 260 |
| 30 | `sociais` | 260 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `rede` | 0.0321 |
| 2 | `pesquisa` | 0.0261 |
| 3 | `etnografia` | 0.0240 |
| 4 | `artificial` | 0.0165 |
| 5 | `inteligencia` | 0.0163 |
| 6 | `ciencia` | 0.0161 |
| 7 | `latour` | 0.0152 |
| 8 | `campo` | 0.0144 |
| 9 | `metodo` | 0.0144 |
| 10 | `objeto` | 0.0127 |
| 11 | `humano` | 0.0123 |
| 12 | `descricao` | 0.0113 |
| 13 | `corte` | 0.0111 |
| 14 | `pratica` | 0.0109 |
| 15 | `strathern` | 0.0104 |
| 16 | `modelo` | 0.0103 |
| 17 | `relacao` | 0.0100 |
| 18 | `inscricao` | 0.0100 |
| 19 | `parte` | 0.0094 |
| 20 | `analise` | 0.0094 |
| 21 | `dado` | 0.0092 |
| 22 | `haraway` | 0.0091 |
| 23 | `maquina` | 0.0091 |
| 24 | `gesto` | 0.0088 |
| 25 | `ator` | 0.0085 |
| 26 | `claude` | 0.0082 |
| 27 | `conceito` | 0.0078 |
| 28 | `descreve` | 0.0077 |
| 29 | `teoria` | 0.0076 |
| 30 | `partir` | 0.0075 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `cientifico` | 131 | 115 | +16 |
| 2 | `computacional` | 108 | 99 | +9 |
| 3 | `actante` | 54 | 46 | +8 |
| 4 | `hinterland` | 55 | 48 | +7 |
| 5 | `manifesta` | 80 | 74 | +6 |
| 6 | `pensamento` | 119 | 113 | +6 |
| 7 | `funcionam` | 124 | 118 | +6 |
| 8 | `notas` | 162 | 156 | +6 |
| 9 | `materiais` | 37 | 32 | +5 |
| 10 | `otherness` | 58 | 53 | +5 |
| 11 | `infraestrutura` | 66 | 61 | +5 |
| 12 | `instituicao` | 109 | 104 | +5 |
| 13 | `propriedade` | 110 | 105 | +5 |
| 14 | `conexoes` | 116 | 111 | +5 |
| 15 | `decisao` | 129 | 124 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `rede` | 0.4004 |
| 2 | `pesquisa` | 0.3107 |
| 3 | `etnografia` | 0.1816 |
| 4 | `corte` | 0.1062 |
| 5 | `latour` | 0.1047 |
| 6 | `campo` | 0.0832 |
| 7 | `ciencia` | 0.0799 |
| 8 | `metodo` | 0.0699 |
| 9 | `descricao` | 0.0546 |
| 10 | `humano` | 0.0516 |
| 11 | `inscricao` | 0.0459 |
| 12 | `tecnociencia` | 0.0411 |
| 13 | `strathern` | 0.0396 |
| 14 | `inteligencia` | 0.0319 |
| 15 | `maquina` | 0.0286 |
| 16 | `modos` | 0.0276 |
| 17 | `objeto` | 0.0259 |
| 18 | `relacao` | 0.0252 |
| 19 | `parcial` | 0.0209 |
| 20 | `pesquisador` | 0.0207 |

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
| 4 | `parcial` | `existencia` | 0.748 | 61 |
| 5 | `distribuida` | `agencia` | 0.722 | 50 |
| 6 | `teoria` | `ator` | 0.718 | 92 |
| 7 | `otherness` | `manifesta` | 0.705 | 38 |
| 8 | `presenca` | `ausencia` | 0.695 | 37 |
| 9 | `tecnico` | `letramento` | 0.648 | 46 |
| 10 | `parcial` | `conexao` | 0.638 | 43 |
| 11 | `infraestrutura` | `computacional` | 0.628 | 38 |
| 12 | `modelo` | `linguagem` | 0.601 | 78 |
| 13 | `otherness` | `ausencia` | 0.600 | 28 |
| 14 | `figuracao` | `textil` | 0.597 | 54 |
| 15 | `heterogeneos` | `materiais` | 0.597 | 36 |
| 16 | `presenca` | `manifesta` | 0.594 | 22 |
| 17 | `ciencia` | `sociais` | 0.580 | 93 |
| 18 | `textual` | `analise` | 0.579 | 58 |
| 19 | `principio` | `simetria` | 0.559 | 18 |
| 20 | `generativa` | `artificial` | 0.557 | 62 |
| 21 | `tecno` | `etnografia` | 0.555 | 73 |
| 22 | `cientista` | `computacao` | 0.543 | 22 |
| 23 | `condicoes` | `materiais` | 0.537 | 31 |
| 24 | `otherness` | `presenca` | 0.528 | 21 |
| 25 | `estudos` | `tecnologia` | 0.518 | 25 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (35 termos): latour, corte, strathern, gesto, haraway, conceito
- **Tópico 2** (33 termos): pesquisa, campo, pratica, materiais, escrita, conhecimento
- **Tópico 3** (29 termos): artificial, inteligencia, objeto, modelo, claude, pesquisador
- **Tópico 4** (24 termos): etnografia, metodo, descricao, parte, descreve, parciais
- **Tópico 5** (21 termos): humano, relacao, maquina, parcial, plano, lugar
- **Tópico 6** (19 termos): rede, inscricao, analise, ator, teoria, tecnociencia
- **Tópico 7** (14 termos): ciencia, dado, sociais, tecnico, tecnologia, letramento
- **Tópico 8** (5 termos): hinterland, otherness, ausencia, presenca, manifesta

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [latour, corte, strathern] e **Tópico 3** [artificial, inteligencia, objeto] — densidade ponderada de ligação = 0.3172
- Lacuna entre **Tópico 2** [pesquisa, campo, pratica] e **Tópico 5** [humano, relacao, maquina] — densidade ponderada de ligação = 0.4444
- Lacuna entre **Tópico 1** [latour, corte, strathern] e **Tópico 5** [humano, relacao, maquina] — densidade ponderada de ligação = 0.5483
- Lacuna entre **Tópico 3** [artificial, inteligencia, objeto] e **Tópico 4** [etnografia, metodo, descricao] — densidade ponderada de ligação = 0.5819
- Lacuna entre **Tópico 1** [latour, corte, strathern] e **Tópico 2** [pesquisa, campo, pratica] — densidade ponderada de ligação = 0.6260
- Lacuna entre **Tópico 3** [artificial, inteligencia, objeto] e **Tópico 5** [humano, relacao, maquina] — densidade ponderada de ligação = 0.6437

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
