# Análise de rede textual — Capítulo 3

> Análise de rede textual (*text network analysis*, Paranyushkin 2019)
> aplicada ao arquivo `ex_cap3.tex`. O texto foi limpo de comandos LaTeX,
> citações e notas de rodapé foram reincorporadas; janela deslizante de
> 4 *tokens* com pesos decrescentes pela distância (3-2-1). Comunidades
> detectadas por Louvain ponderado. Esta versão acrescenta duas métricas
> *informativas* que não dependem da frequência bruta: **PageRank** dos
> nós e **NPMI** das arestas. As métricas baseadas em frequência são
> mantidas em paralelo, para comparação.

## 1. Resumo quantitativo
- Tokens significativos: **17,227**
- Grafo bruto: **5307** nós · **44831** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **2492** arestas
- Tópicos detectados (Louvain): **7**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `claudio` | 751 |
| 2 | `pesquisa` | 636 |
| 3 | `rede` | 570 |
| 4 | `centro` | 497 |
| 5 | `fabio` | 493 |
| 6 | `arranjo` | 399 |
| 7 | `publico` | 383 |
| 8 | `seguir` | 351 |
| 9 | `corporacao` | 343 |
| 10 | `brasil` | 310 |
| 11 | `inteligencia` | 305 |
| 12 | `hollerith` | 303 |
| 13 | `artificial` | 302 |
| 14 | `tecnologia` | 282 |
| 15 | `empresa` | 280 |
| 16 | `ator` | 274 |
| 17 | `ecossistema` | 255 |
| 18 | `universidade` | 253 |
| 19 | `laboratorio` | 251 |
| 20 | `maquina` | 239 |
| 21 | `instituicao` | 233 |
| 22 | `infraestrutura` | 230 |
| 23 | `modelo` | 227 |
| 24 | `fapesp` | 219 |
| 25 | `trajetoria` | 200 |
| 26 | `informacao` | 200 |
| 27 | `encerramento` | 188 |
| 28 | `campo` | 185 |
| 29 | `verbal` | 184 |
| 30 | `associacao` | 180 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `claudio` | 0.0269 |
| 2 | `pesquisa` | 0.0248 |
| 3 | `rede` | 0.0221 |
| 4 | `centro` | 0.0193 |
| 5 | `fabio` | 0.0175 |
| 6 | `arranjo` | 0.0158 |
| 7 | `publico` | 0.0151 |
| 8 | `corporacao` | 0.0141 |
| 9 | `seguir` | 0.0135 |
| 10 | `hollerith` | 0.0127 |
| 11 | `brasil` | 0.0124 |
| 12 | `tecnologia` | 0.0122 |
| 13 | `empresa` | 0.0114 |
| 14 | `inteligencia` | 0.0113 |
| 15 | `artificial` | 0.0112 |
| 16 | `ator` | 0.0109 |
| 17 | `universidade` | 0.0103 |
| 18 | `ecossistema` | 0.0102 |
| 19 | `maquina` | 0.0100 |
| 20 | `laboratorio` | 0.0100 |
| 21 | `infraestrutura` | 0.0099 |
| 22 | `modelo` | 0.0098 |
| 23 | `instituicao` | 0.0096 |
| 24 | `fapesp` | 0.0090 |
| 25 | `trajetoria` | 0.0085 |
| 26 | `campo` | 0.0079 |
| 27 | `encerramento` | 0.0076 |
| 28 | `associacao` | 0.0075 |
| 29 | `dado` | 0.0075 |
| 30 | `informacao` | 0.0072 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `linguagem` | 93 | 67 | +26 |
| 2 | `processamento` | 88 | 66 | +22 |
| 3 | `natural` | 119 | 102 | +17 |
| 4 | `cadeia` | 87 | 71 | +16 |
| 5 | `estados` | 90 | 77 | +13 |
| 6 | `estatistica` | 100 | 87 | +13 |
| 7 | `unidos` | 91 | 81 | +10 |
| 8 | `censo` | 110 | 100 | +10 |
| 9 | `conta` | 124 | 114 | +10 |
| 10 | `codigo` | 48 | 42 | +6 |
| 11 | `translacao` | 107 | 101 | +6 |
| 12 | `inscricao` | 140 | 134 | +6 |
| 13 | `mostra` | 150 | 144 | +6 |
| 14 | `leio` | 159 | 153 | +6 |
| 15 | `tecnica` | 55 | 50 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `centro` | 0.2357 |
| 2 | `pesquisa` | 0.2280 |
| 3 | `rede` | 0.2054 |
| 4 | `claudio` | 0.1716 |
| 5 | `fabio` | 0.1294 |
| 6 | `tecnologia` | 0.0843 |
| 7 | `corporacao` | 0.0714 |
| 8 | `hollerith` | 0.0626 |
| 9 | `ator` | 0.0600 |
| 10 | `seguir` | 0.0598 |
| 11 | `brasil` | 0.0594 |
| 12 | `publico` | 0.0555 |
| 13 | `empresa` | 0.0554 |
| 14 | `arranjo` | 0.0531 |
| 15 | `ecossistema` | 0.0469 |
| 16 | `inteligencia` | 0.0377 |
| 17 | `universidade` | 0.0355 |
| 18 | `modelo` | 0.0324 |
| 19 | `trajetoria` | 0.0277 |
| 20 | `dado` | 0.0261 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `informacao` | `verbal` | 0.877 | 80 |
| 2 | `inteligencia` | `artificial` | 0.863 | 144 |
| 3 | `unidos` | `estados` | 0.856 | 48 |
| 4 | `porta` | `voz` | 0.840 | 47 |
| 5 | `linguagem` | `natural` | 0.829 | 39 |
| 6 | `linguagem` | `processamento` | 0.753 | 30 |
| 7 | `aberto` | `codigo` | 0.732 | 45 |
| 8 | `processamento` | `natural` | 0.675 | 20 |
| 9 | `historica` | `investigacao` | 0.614 | 24 |
| 10 | `acesso` | `disponivel` | 0.596 | 27 |
| 11 | `claudio` | `fabio` | 0.586 | 169 |
| 12 | `novembro` | `dezembro` | 0.562 | 20 |
| 13 | `research` | `brasil` | 0.552 | 41 |
| 14 | `passagem` | `ponto` | 0.548 | 24 |
| 15 | `inovacao` | `ecossistema` | 0.547 | 46 |
| 16 | `translacao` | `cadeias` | 0.527 | 12 |
| 17 | `comercial` | `tecnica` | 0.511 | 19 |
| 18 | `hollerith` | `tabulacao` | 0.507 | 39 |
| 19 | `entrevistas` | `observacao` | 0.506 | 18 |
| 20 | `gente` | `dinheiro` | 0.501 | 15 |
| 21 | `cientifico` | `relatorios` | 0.489 | 21 |
| 22 | `research` | `fechamento` | 0.485 | 12 |
| 23 | `sistema` | `tabulacao` | 0.480 | 24 |
| 24 | `claudio` | `informacao` | 0.474 | 61 |
| 25 | `fontes` | `financiamento` | 0.470 | 16 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (46 termos): claudio, rede, fabio, seguir, ator, informacao
- **Tópico 2** (30 termos): pesquisa, centro, fapesp, cientifico, pesquisador, partir
- **Tópico 3** (30 termos): publico, corporacao, empresa, ecossistema, universidade, instituicao
- **Tópico 4** (29 termos): tecnologia, dado, parte, ciencia, escala, tecnica
- **Tópico 5** (21 termos): arranjo, brasil, inteligencia, artificial, laboratorio, encerramento
- **Tópico 6** (13 termos): hollerith, maquina, ponto, tabulacao, sistema, estados
- **Tópico 7** (11 termos): modelo, codigo, aberto, negocio, processamento, linguagem

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 4** [tecnologia, dado, parte] e **Tópico 5** [arranjo, brasil, inteligencia] — densidade ponderada de ligação = 0.3186
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 4** [tecnologia, dado, parte] — densidade ponderada de ligação = 0.3193
- Lacuna entre **Tópico 2** [pesquisa, centro, fapesp] e **Tópico 4** [tecnologia, dado, parte] — densidade ponderada de ligação = 0.3437
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 5** [arranjo, brasil, inteligencia] — densidade ponderada de ligação = 0.4441
- Lacuna entre **Tópico 3** [publico, corporacao, empresa] e **Tópico 4** [tecnologia, dado, parte] — densidade ponderada de ligação = 0.4460
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 2** [pesquisa, centro, fapesp] — densidade ponderada de ligação = 0.4623

## 9. Leitura interpretativa
**O que a rede mostra.** O capítulo segue o arranjo do C4AI em três planos
que o grafo separa nitidamente. Há a infraestrutura histórica (`tecnologia`,
`hollerith`, `infraestrutura`, `empresa`, `maquina`, `trajetoria`) — a longa
trajetória das máquinas até a IBM; há o arranjo público-privado do presente
(`publico`, `arranjo`, `corporacao`, `universidade`, `brasil`); e há o
vocabulário do método (`rede`, `ator`, `associacao`, `sigo`, `descrevo`),
que forma comunidade própria — o gesto de "seguir os atores" é lexicalmente
distinto. Os atores seguidos no campo aparecem como uma dupla forte:
`claudio ↔ fabio` (NPMI 0,58).

**Pontes (`betweenness`).** `centro` e `pesquisa` são as maiores pontes,
seguidas de `rede`, `claudio`, `publico`, `corporacao` e `fabio`. O centro e
a pesquisa funcionam como termos-coringa que circulam entre a história
infraestrutural, o arranjo institucional e o trabalho de campo.

**Lacunas a desenvolver.** A ligação mais fraca está entre o vocabulário do
centro de pesquisa (`pesquisa`, `centro`, `cientifico`, `fapesp`) e o
vocabulário do método ator-rede (`rede`, `ator`, `associacao`): a instituição
descrita e o método que a descreve correm lado a lado. Fraca também é a
costura entre a infraestrutura histórica IBM/Hollerith e o centro do presente
— a história profunda das máquinas e o presente etnográfico pedem uma ponte
mais explícita.

## 10. Arquivos gerados
**Visões frequentistas**
- `infranodus_cap3_network.png` — rede completa, tamanho por degree.
- `infranodus_cap3_focus.png` — núcleo (top-100, peso ≥ 3).

**Visões informativas**
- `infranodus_cap3_pmi.png` — rede completa, tamanho por **PageRank**,
  arestas filtradas por **NPMI ≥ 0,20**.
- `infranodus_cap3_focus_pmi.png` — núcleo, NPMI ≥ 0,25.

**Dados**
- `infranodus_cap3_metrics.json` — métricas brutas (degree, betweenness,
  PageRank, NPMI, comunidades, lacunas).
- `infranodus_cap3.gexf` / `infranodus_cap3_focus.gexf` — grafos para Gephi
  já com `community`, `frequency`, `degree_weighted`, `betweenness`,
  `pagerank` (nós) e `weight`, `npmi` (arestas).
- `infranodus_cap3_nodes.csv` / `infranodus_cap3_edges.csv` (e `_focus_*`)
  — fallback em planilha; CSVs trazem todas as colunas acima.

## 11. Como abrir no Gephi
1. Instale Gephi (≥ 0.10): https://gephi.org/users/download/
2. `File → Open…` → selecione `infranodus_cap3.gexf` (ou `_focus.gexf`).
3. No painel **Appearance**: já vem com cor por `community` e tamanho por
   `degree_weighted` (embutidos via atributos `viz`). Ajuste se quiser.
4. Em **Layout**: aplique *ForceAtlas 2* (ative *Prevent Overlap* e
   *Dissuade Hubs*) por ~30 s; ou *Fruchterman-Reingold* para algo mais rápido.
5. Em **Statistics**: rode *Modularity* e *Average Path Length* se quiser
   recalcular comunidades dentro do Gephi (resultados serão semelhantes).
6. Em **Preview**: ative *Node Labels*, escolha fonte e exporte para PDF/SVG.
