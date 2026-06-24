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
- Tokens significativos: **17,786**
- Grafo bruto: **5347** nós · **45841** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **2531** arestas
- Tópicos detectados (Louvain): **7**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `claudio` | 764 |
| 2 | `pesquisa` | 734 |
| 3 | `rede` | 581 |
| 4 | `centro` | 519 |
| 5 | `fabio` | 491 |
| 6 | `publico` | 421 |
| 7 | `arranjo` | 409 |
| 8 | `corporacao` | 366 |
| 9 | `seguir` | 353 |
| 10 | `brasil` | 311 |
| 11 | `inteligencia` | 305 |
| 12 | `hollerith` | 300 |
| 13 | `artificial` | 298 |
| 14 | `tecnologia` | 297 |
| 15 | `ator` | 286 |
| 16 | `laboratorio` | 266 |
| 17 | `infraestrutura` | 255 |
| 18 | `ecossistema` | 251 |
| 19 | `empresa` | 243 |
| 20 | `cientifico` | 239 |
| 21 | `fapesp` | 239 |
| 22 | `maquina` | 233 |
| 23 | `instituicao` | 230 |
| 24 | `modelo` | 228 |
| 25 | `universidade` | 225 |
| 26 | `trajetoria` | 212 |
| 27 | `campo` | 208 |
| 28 | `informacao` | 208 |
| 29 | `encerramento` | 194 |
| 30 | `associacao` | 183 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `pesquisa` | 0.0274 |
| 2 | `claudio` | 0.0267 |
| 3 | `rede` | 0.0218 |
| 4 | `centro` | 0.0194 |
| 5 | `fabio` | 0.0171 |
| 6 | `publico` | 0.0160 |
| 7 | `arranjo` | 0.0156 |
| 8 | `corporacao` | 0.0144 |
| 9 | `seguir` | 0.0133 |
| 10 | `tecnologia` | 0.0123 |
| 11 | `brasil` | 0.0121 |
| 12 | `hollerith` | 0.0121 |
| 13 | `ator` | 0.0110 |
| 14 | `inteligencia` | 0.0110 |
| 15 | `artificial` | 0.0108 |
| 16 | `infraestrutura` | 0.0105 |
| 17 | `laboratorio` | 0.0102 |
| 18 | `ecossistema` | 0.0098 |
| 19 | `empresa` | 0.0097 |
| 20 | `modelo` | 0.0096 |
| 21 | `maquina` | 0.0095 |
| 22 | `cientifico` | 0.0095 |
| 23 | `fapesp` | 0.0095 |
| 24 | `instituicao` | 0.0091 |
| 25 | `universidade` | 0.0090 |
| 26 | `trajetoria` | 0.0086 |
| 27 | `campo` | 0.0084 |
| 28 | `dado` | 0.0078 |
| 29 | `encerramento` | 0.0076 |
| 30 | `associacao` | 0.0074 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `processamento` | 127 | 111 | +16 |
| 2 | `conta` | 142 | 128 | +14 |
| 3 | `cadeia` | 101 | 88 | +13 |
| 4 | `translacao` | 99 | 87 | +12 |
| 5 | `cartoes` | 116 | 106 | +10 |
| 6 | `tecnica` | 59 | 51 | +8 |
| 7 | `estados` | 80 | 72 | +8 |
| 8 | `conhecimento` | 87 | 79 | +8 |
| 9 | `unidos` | 91 | 83 | +8 |
| 10 | `dinheiro` | 115 | 107 | +8 |
| 11 | `secao` | 98 | 91 | +7 |
| 12 | `estatistica` | 119 | 112 | +7 |
| 13 | `mostra` | 162 | 155 | +7 |
| 14 | `negocio` | 86 | 80 | +6 |
| 15 | `material` | 92 | 86 | +6 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `centro` | 0.2453 |
| 2 | `pesquisa` | 0.2435 |
| 3 | `rede` | 0.2145 |
| 4 | `claudio` | 0.1617 |
| 5 | `fabio` | 0.1294 |
| 6 | `publico` | 0.1108 |
| 7 | `corporacao` | 0.0949 |
| 8 | `tecnologia` | 0.0844 |
| 9 | `hollerith` | 0.0705 |
| 10 | `ator` | 0.0581 |
| 11 | `seguir` | 0.0537 |
| 12 | `cientifico` | 0.0531 |
| 13 | `ecossistema` | 0.0515 |
| 14 | `brasil` | 0.0485 |
| 15 | `arranjo` | 0.0375 |
| 16 | `universidade` | 0.0374 |
| 17 | `fapesp` | 0.0355 |
| 18 | `modelo` | 0.0317 |
| 19 | `empresa` | 0.0316 |
| 20 | `inteligencia` | 0.0287 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `informacao` | `verbal` | 0.871 | 80 |
| 2 | `inteligencia` | `artificial` | 0.864 | 144 |
| 3 | `unidos` | `estados` | 0.859 | 57 |
| 4 | `relatorios` | `anuais` | 0.775 | 46 |
| 5 | `aberto` | `codigo` | 0.748 | 45 |
| 6 | `linguagem` | `processamento` | 0.736 | 30 |
| 7 | `historica` | `investigacao` | 0.622 | 24 |
| 8 | `elaboracao` | `base` | 0.616 | 21 |
| 9 | `claudio` | `fabio` | 0.589 | 169 |
| 10 | `acesso` | `disponivel` | 0.589 | 27 |
| 11 | `novembro` | `dezembro` | 0.571 | 23 |
| 12 | `passagem` | `ponto` | 0.570 | 27 |
| 13 | `research` | `brasil` | 0.547 | 38 |
| 14 | `inovacao` | `ecossistema` | 0.527 | 43 |
| 15 | `cientifico` | `producao` | 0.510 | 34 |
| 16 | `entrevistas` | `observacao` | 0.508 | 18 |
| 17 | `translacao` | `cadeias` | 0.507 | 12 |
| 18 | `mapa` | `problemas` | 0.506 | 12 |
| 19 | `relatorios` | `base` | 0.498 | 18 |
| 20 | `gente` | `dinheiro` | 0.497 | 15 |
| 21 | `relatorios` | `elaboracao` | 0.496 | 14 |
| 22 | `research` | `fechamento` | 0.494 | 12 |
| 23 | `hollerith` | `tabulacao` | 0.482 | 36 |
| 24 | `hollerith` | `maquina` | 0.479 | 55 |
| 25 | `anuais` | `base` | 0.476 | 12 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (47 termos): hollerith, tecnologia, infraestrutura, empresa, maquina, trajetoria
- **Tópico 2** (39 termos): claudio, rede, fabio, seguir, ator, informacao
- **Tópico 3** (34 termos): pesquisa, centro, cientifico, fapesp, relatorios, partir
- **Tópico 4** (26 termos): publico, arranjo, corporacao, brasil, laboratorio, instituicao
- **Tópico 5** (12 termos): modelo, codigo, aberto, negocio, processamento, torna
- **Tópico 6** (12 termos): parte, escala, historica, maior, estados, investigacao
- **Tópico 7** (10 termos): inteligencia, artificial, ecossistema, inovacao, brasileiro, obia

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 3** [pesquisa, centro, cientifico] e **Tópico 5** [modelo, codigo, aberto] — densidade ponderada de ligação = 0.2647
- Lacuna entre **Tópico 2** [claudio, rede, fabio] e **Tópico 5** [modelo, codigo, aberto] — densidade ponderada de ligação = 0.2692
- Lacuna entre **Tópico 1** [hollerith, tecnologia, infraestrutura] e **Tópico 5** [modelo, codigo, aberto] — densidade ponderada de ligação = 0.3209
- Lacuna entre **Tópico 1** [hollerith, tecnologia, infraestrutura] e **Tópico 3** [pesquisa, centro, cientifico] — densidade ponderada de ligação = 0.3254
- Lacuna entre **Tópico 4** [publico, arranjo, corporacao] e **Tópico 5** [modelo, codigo, aberto] — densidade ponderada de ligação = 0.3526
- Lacuna entre **Tópico 1** [hollerith, tecnologia, infraestrutura] e **Tópico 2** [claudio, rede, fabio] — densidade ponderada de ligação = 0.4103

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
