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
- Tokens significativos: **23,272**
- Grafo bruto: **6604** nós · **58753** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **3297** arestas
- Tópicos detectados (Louvain): **7**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `rede` | 1283 |
| 2 | `pesquisa` | 981 |
| 3 | `etnografia` | 849 |
| 4 | `artificial` | 701 |
| 5 | `inteligencia` | 692 |
| 6 | `ciencia` | 614 |
| 7 | `latour` | 604 |
| 8 | `campo` | 580 |
| 9 | `metodo` | 535 |
| 10 | `objeto` | 492 |
| 11 | `corte` | 477 |
| 12 | `humano` | 439 |
| 13 | `inscricao` | 419 |
| 14 | `descricao` | 417 |
| 15 | `pratica` | 396 |
| 16 | `strathern` | 385 |
| 17 | `modelo` | 374 |
| 18 | `ator` | 350 |
| 19 | `relacao` | 345 |
| 20 | `gesto` | 343 |
| 21 | `analise` | 343 |
| 22 | `dado` | 325 |
| 23 | `parte` | 316 |
| 24 | `maquina` | 314 |
| 25 | `haraway` | 308 |
| 26 | `teoria` | 305 |
| 27 | `conceito` | 305 |
| 28 | `escrita` | 286 |
| 29 | `descreve` | 275 |
| 30 | `sociais` | 268 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `rede` | 0.0326 |
| 2 | `pesquisa` | 0.0254 |
| 3 | `etnografia` | 0.0222 |
| 4 | `artificial` | 0.0164 |
| 5 | `inteligencia` | 0.0162 |
| 6 | `latour` | 0.0160 |
| 7 | `ciencia` | 0.0159 |
| 8 | `campo` | 0.0155 |
| 9 | `metodo` | 0.0145 |
| 10 | `objeto` | 0.0130 |
| 11 | `corte` | 0.0129 |
| 12 | `humano` | 0.0120 |
| 13 | `inscricao` | 0.0117 |
| 14 | `descricao` | 0.0113 |
| 15 | `pratica` | 0.0108 |
| 16 | `strathern` | 0.0107 |
| 17 | `modelo` | 0.0104 |
| 18 | `relacao` | 0.0096 |
| 19 | `gesto` | 0.0093 |
| 20 | `analise` | 0.0092 |
| 21 | `parte` | 0.0088 |
| 22 | `haraway` | 0.0088 |
| 23 | `dado` | 0.0088 |
| 24 | `ator` | 0.0088 |
| 25 | `maquina` | 0.0088 |
| 26 | `conceito` | 0.0087 |
| 27 | `escrita` | 0.0080 |
| 28 | `descreve` | 0.0078 |
| 29 | `teoria` | 0.0077 |
| 30 | `sociais` | 0.0073 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `cientifico` | 144 | 128 | +16 |
| 2 | `computacional` | 114 | 100 | +14 |
| 3 | `infraestrutura` | 75 | 65 | +10 |
| 4 | `instituicao` | 96 | 86 | +10 |
| 5 | `diagrama` | 97 | 87 | +10 |
| 6 | `cortes` | 107 | 98 | +9 |
| 7 | `spira` | 64 | 57 | +7 |
| 8 | `formula` | 105 | 99 | +6 |
| 9 | `tecnica` | 110 | 104 | +6 |
| 10 | `funcionam` | 117 | 111 | +6 |
| 11 | `acesso` | 119 | 113 | +6 |
| 12 | `termos` | 46 | 41 | +5 |
| 13 | `manifesta` | 71 | 66 | +5 |
| 14 | `condicoes` | 106 | 101 | +5 |
| 15 | `palavra` | 153 | 148 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `rede` | 0.3891 |
| 2 | `pesquisa` | 0.2598 |
| 3 | `etnografia` | 0.1758 |
| 4 | `latour` | 0.1578 |
| 5 | `corte` | 0.1156 |
| 6 | `campo` | 0.1028 |
| 7 | `ciencia` | 0.0772 |
| 8 | `inscricao` | 0.0729 |
| 9 | `metodo` | 0.0707 |
| 10 | `descricao` | 0.0554 |
| 11 | `humano` | 0.0519 |
| 12 | `strathern` | 0.0418 |
| 13 | `objeto` | 0.0329 |
| 14 | `maquina` | 0.0313 |
| 15 | `dado` | 0.0255 |
| 16 | `modos` | 0.0252 |
| 17 | `parcial` | 0.0227 |
| 18 | `hinterland` | 0.0202 |
| 19 | `pratica` | 0.0201 |
| 20 | `laboratorio` | 0.0196 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `ausencia` | `manifesta` | 0.864 | 67 |
| 2 | `inteligencia` | `artificial` | 0.857 | 313 |
| 3 | `existencias` | `parciais` | 0.827 | 84 |
| 4 | `parcial` | `existencia` | 0.745 | 59 |
| 5 | `teoria` | `ator` | 0.728 | 104 |
| 6 | `distribuida` | `agencia` | 0.727 | 52 |
| 7 | `presenca` | `ausencia` | 0.707 | 43 |
| 8 | `otherness` | `manifesta` | 0.684 | 40 |
| 9 | `tecnico` | `letramento` | 0.655 | 46 |
| 10 | `parcial` | `conexao` | 0.634 | 43 |
| 11 | `infraestrutura` | `computacional` | 0.631 | 38 |
| 12 | `pergunta` | `responde` | 0.626 | 36 |
| 13 | `presenca` | `manifesta` | 0.622 | 28 |
| 14 | `otherness` | `ausencia` | 0.618 | 34 |
| 15 | `modelo` | `linguagem` | 0.614 | 87 |
| 16 | `heterogeneos` | `materiais` | 0.600 | 36 |
| 17 | `figuracao` | `textil` | 0.597 | 54 |
| 18 | `ciencia` | `sociais` | 0.578 | 94 |
| 19 | `textual` | `analise` | 0.565 | 56 |
| 20 | `generativa` | `artificial` | 0.554 | 62 |
| 21 | `principio` | `simetria` | 0.548 | 18 |
| 22 | `otherness` | `hinterland` | 0.546 | 36 |
| 23 | `acesso` | `disponivel` | 0.545 | 18 |
| 24 | `otherness` | `presenca` | 0.545 | 25 |
| 25 | `antropologia` | `tecnica` | 0.544 | 21 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (48 termos): pesquisa, campo, objeto, pratica, modelo, escrita
- **Tópico 2** (39 termos): latour, corte, strathern, gesto, haraway, conceito
- **Tópico 3** (27 termos): etnografia, metodo, inscricao, descricao, parte, descreve
- **Tópico 4** (24 termos): artificial, inteligencia, ciencia, dado, sociais, laboratorio
- **Tópico 5** (18 termos): humano, relacao, maquina, parcial, plano, agencia
- **Tópico 6** (17 termos): rede, ator, analise, teoria, termos, actante
- **Tópico 7** (7 termos): otherness, hinterland, ausencia, manifesta, presenca, palavra

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 2** [latour, corte, strathern] e **Tópico 4** [artificial, inteligencia, ciencia] — densidade ponderada de ligação = 0.3451
- Lacuna entre **Tópico 1** [pesquisa, campo, objeto] e **Tópico 5** [humano, relacao, maquina] — densidade ponderada de ligação = 0.4618
- Lacuna entre **Tópico 4** [artificial, inteligencia, ciencia] e **Tópico 5** [humano, relacao, maquina] — densidade ponderada de ligação = 0.5486
- Lacuna entre **Tópico 1** [pesquisa, campo, objeto] e **Tópico 2** [latour, corte, strathern] — densidade ponderada de ligação = 0.5801
- Lacuna entre **Tópico 2** [latour, corte, strathern] e **Tópico 5** [humano, relacao, maquina] — densidade ponderada de ligação = 0.6111
- Lacuna entre **Tópico 3** [etnografia, metodo, inscricao] e **Tópico 5** [humano, relacao, maquina] — densidade ponderada de ligação = 0.6523

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
