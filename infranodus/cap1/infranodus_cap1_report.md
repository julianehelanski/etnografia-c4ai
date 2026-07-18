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
- Tokens significativos: **23,245**
- Grafo bruto: **6603** nós · **58712** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **3291** arestas
- Tópicos detectados (Louvain): **9**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `rede` | 1280 |
| 2 | `pesquisa` | 980 |
| 3 | `etnografia` | 850 |
| 4 | `artificial` | 703 |
| 5 | `inteligencia` | 692 |
| 6 | `ciencia` | 613 |
| 7 | `latour` | 607 |
| 8 | `campo` | 584 |
| 9 | `metodo` | 538 |
| 10 | `objeto` | 489 |
| 11 | `corte` | 473 |
| 12 | `humano` | 445 |
| 13 | `descricao` | 415 |
| 14 | `inscricao` | 407 |
| 15 | `pratica` | 398 |
| 16 | `strathern` | 385 |
| 17 | `modelo` | 369 |
| 18 | `ator` | 350 |
| 19 | `relacao` | 344 |
| 20 | `analise` | 343 |
| 21 | `gesto` | 337 |
| 22 | `dado` | 325 |
| 23 | `parte` | 322 |
| 24 | `maquina` | 319 |
| 25 | `haraway` | 308 |
| 26 | `teoria` | 305 |
| 27 | `conceito` | 304 |
| 28 | `escrita` | 286 |
| 29 | `descreve` | 275 |
| 30 | `sociais` | 270 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `rede` | 0.0326 |
| 2 | `pesquisa` | 0.0254 |
| 3 | `etnografia` | 0.0223 |
| 4 | `artificial` | 0.0165 |
| 5 | `inteligencia` | 0.0162 |
| 6 | `latour` | 0.0161 |
| 7 | `ciencia` | 0.0160 |
| 8 | `campo` | 0.0157 |
| 9 | `metodo` | 0.0146 |
| 10 | `objeto` | 0.0130 |
| 11 | `corte` | 0.0128 |
| 12 | `humano` | 0.0123 |
| 13 | `inscricao` | 0.0114 |
| 14 | `descricao` | 0.0112 |
| 15 | `pratica` | 0.0109 |
| 16 | `strathern` | 0.0107 |
| 17 | `modelo` | 0.0103 |
| 18 | `relacao` | 0.0096 |
| 19 | `analise` | 0.0092 |
| 20 | `gesto` | 0.0092 |
| 21 | `parte` | 0.0090 |
| 22 | `maquina` | 0.0090 |
| 23 | `dado` | 0.0088 |
| 24 | `haraway` | 0.0088 |
| 25 | `ator` | 0.0088 |
| 26 | `conceito` | 0.0087 |
| 27 | `escrita` | 0.0081 |
| 28 | `descreve` | 0.0078 |
| 29 | `teoria` | 0.0077 |
| 30 | `sociais` | 0.0074 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `cientifico` | 143 | 126 | +17 |
| 2 | `tecnica` | 107 | 95 | +12 |
| 3 | `computacional` | 114 | 102 | +12 |
| 4 | `instituicao` | 96 | 86 | +10 |
| 5 | `diagrama` | 97 | 87 | +10 |
| 6 | `infraestrutura` | 74 | 65 | +9 |
| 7 | `cortes` | 108 | 100 | +8 |
| 8 | `funcionam` | 117 | 111 | +6 |
| 9 | `acesso` | 119 | 113 | +6 |
| 10 | `spira` | 62 | 57 | +5 |
| 11 | `termos` | 45 | 41 | +4 |
| 12 | `actante` | 51 | 47 | +4 |
| 13 | `ausencia` | 55 | 51 | +4 |
| 14 | `tecnico` | 58 | 54 | +4 |
| 15 | `manifesta` | 70 | 66 | +4 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `rede` | 0.3832 |
| 2 | `pesquisa` | 0.2676 |
| 3 | `etnografia` | 0.1791 |
| 4 | `latour` | 0.1627 |
| 5 | `campo` | 0.1170 |
| 6 | `corte` | 0.1145 |
| 7 | `ciencia` | 0.0732 |
| 8 | `metodo` | 0.0686 |
| 9 | `inscricao` | 0.0645 |
| 10 | `descricao` | 0.0562 |
| 11 | `humano` | 0.0559 |
| 12 | `strathern` | 0.0418 |
| 13 | `maquina` | 0.0375 |
| 14 | `objeto` | 0.0328 |
| 15 | `modos` | 0.0254 |
| 16 | `dado` | 0.0244 |
| 17 | `parcial` | 0.0227 |
| 18 | `pratica` | 0.0203 |
| 19 | `hinterland` | 0.0192 |
| 20 | `haraway` | 0.0191 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `ausencia` | `manifesta` | 0.864 | 67 |
| 2 | `inteligencia` | `artificial` | 0.857 | 313 |
| 3 | `existencias` | `parciais` | 0.826 | 84 |
| 4 | `parcial` | `existencia` | 0.745 | 59 |
| 5 | `teoria` | `ator` | 0.728 | 104 |
| 6 | `distribuida` | `agencia` | 0.727 | 52 |
| 7 | `presenca` | `ausencia` | 0.707 | 43 |
| 8 | `otherness` | `manifesta` | 0.684 | 40 |
| 9 | `tecnico` | `letramento` | 0.655 | 46 |
| 10 | `parcial` | `conexao` | 0.634 | 43 |
| 11 | `infraestrutura` | `computacional` | 0.631 | 38 |
| 12 | `presenca` | `manifesta` | 0.622 | 28 |
| 13 | `otherness` | `ausencia` | 0.617 | 34 |
| 14 | `modelo` | `linguagem` | 0.616 | 87 |
| 15 | `heterogeneos` | `materiais` | 0.600 | 36 |
| 16 | `figuracao` | `textil` | 0.597 | 54 |
| 17 | `ciencia` | `sociais` | 0.578 | 94 |
| 18 | `textual` | `analise` | 0.565 | 56 |
| 19 | `generativa` | `artificial` | 0.554 | 62 |
| 20 | `principio` | `simetria` | 0.548 | 18 |
| 21 | `otherness` | `hinterland` | 0.546 | 36 |
| 22 | `acesso` | `disponivel` | 0.545 | 18 |
| 23 | `otherness` | `presenca` | 0.545 | 25 |
| 24 | `antropologia` | `tecnica` | 0.544 | 21 |
| 25 | `condicoes` | `materiais` | 0.540 | 31 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (42 termos): pesquisa, etnografia, campo, metodo, descricao, pratica
- **Tópico 2** (36 termos): latour, corte, strathern, gesto, haraway, conceito
- **Tópico 3** (21 termos): humano, relacao, maquina, parcial, plano, agencia
- **Tópico 4** (17 termos): rede, ator, analise, teoria, termos, actante
- **Tópico 5** (17 termos): artificial, inteligencia, objeto, modelo, claude, laboratorio
- **Tópico 6** (16 termos): ciencia, dado, sociais, tecnologia, lugar, tecnico
- **Tópico 7** (15 termos): inscricao, descreve, tecnociencia, modos, diagrama, cadeia
- **Tópico 8** (9 termos): infraestrutura, instituicao, computacional, decisao, cientifico, arranjo

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 2** [latour, corte, strathern] e **Tópico 5** [artificial, inteligencia, objeto] — densidade ponderada de ligação = 0.4984
- Lacuna entre **Tópico 1** [pesquisa, etnografia, campo] e **Tópico 3** [humano, relacao, maquina] — densidade ponderada de ligação = 0.5102
- Lacuna entre **Tópico 2** [latour, corte, strathern] e **Tópico 3** [humano, relacao, maquina] — densidade ponderada de ligação = 0.5899
- Lacuna entre **Tópico 3** [humano, relacao, maquina] e **Tópico 4** [rede, ator, analise] — densidade ponderada de ligação = 0.6078
- Lacuna entre **Tópico 2** [latour, corte, strathern] e **Tópico 4** [rede, ator, analise] — densidade ponderada de ligação = 0.7843
- Lacuna entre **Tópico 3** [humano, relacao, maquina] e **Tópico 5** [artificial, inteligencia, objeto] — densidade ponderada de ligação = 0.7899

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
