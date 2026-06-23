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
- Tokens significativos: **17,696**
- Grafo bruto: **5334** nós · **45609** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **2526** arestas
- Tópicos detectados (Louvain): **7**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `claudio` | 761 |
| 2 | `pesquisa` | 734 |
| 3 | `rede` | 572 |
| 4 | `centro` | 519 |
| 5 | `fabio` | 488 |
| 6 | `publico` | 421 |
| 7 | `arranjo` | 404 |
| 8 | `corporacao` | 360 |
| 9 | `seguir` | 353 |
| 10 | `brasil` | 311 |
| 11 | `inteligencia` | 305 |
| 12 | `artificial` | 298 |
| 13 | `tecnologia` | 297 |
| 14 | `hollerith` | 295 |
| 15 | `ator` | 286 |
| 16 | `laboratorio` | 266 |
| 17 | `infraestrutura` | 255 |
| 18 | `ecossistema` | 251 |
| 19 | `empresa` | 243 |
| 20 | `cientifico` | 239 |
| 21 | `fapesp` | 239 |
| 22 | `maquina` | 233 |
| 23 | `modelo` | 228 |
| 24 | `instituicao` | 225 |
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
| 1 | `pesquisa` | 0.0275 |
| 2 | `claudio` | 0.0267 |
| 3 | `rede` | 0.0216 |
| 4 | `centro` | 0.0195 |
| 5 | `fabio` | 0.0171 |
| 6 | `publico` | 0.0161 |
| 7 | `arranjo` | 0.0155 |
| 8 | `corporacao` | 0.0142 |
| 9 | `seguir` | 0.0133 |
| 10 | `tecnologia` | 0.0123 |
| 11 | `brasil` | 0.0122 |
| 12 | `hollerith` | 0.0120 |
| 13 | `ator` | 0.0111 |
| 14 | `inteligencia` | 0.0110 |
| 15 | `artificial` | 0.0108 |
| 16 | `infraestrutura` | 0.0105 |
| 17 | `laboratorio` | 0.0103 |
| 18 | `ecossistema` | 0.0098 |
| 19 | `empresa` | 0.0097 |
| 20 | `modelo` | 0.0097 |
| 21 | `maquina` | 0.0096 |
| 22 | `cientifico` | 0.0095 |
| 23 | `fapesp` | 0.0095 |
| 24 | `universidade` | 0.0090 |
| 25 | `instituicao` | 0.0090 |
| 26 | `trajetoria` | 0.0087 |
| 27 | `campo` | 0.0084 |
| 28 | `dado` | 0.0079 |
| 29 | `encerramento` | 0.0077 |
| 30 | `associacao` | 0.0075 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `processamento` | 126 | 112 | +14 |
| 2 | `conta` | 140 | 126 | +14 |
| 3 | `translacao` | 98 | 88 | +10 |
| 4 | `cartoes` | 115 | 105 | +10 |
| 5 | `cadeia` | 94 | 85 | +9 |
| 6 | `tecnica` | 59 | 51 | +8 |
| 7 | `estados` | 80 | 72 | +8 |
| 8 | `mostra` | 162 | 154 | +8 |
| 9 | `conhecimento` | 86 | 79 | +7 |
| 10 | `unidos` | 90 | 83 | +7 |
| 11 | `dinheiro` | 114 | 107 | +7 |
| 12 | `estatistica` | 118 | 111 | +7 |
| 13 | `secao` | 97 | 91 | +6 |
| 14 | `corte` | 116 | 110 | +6 |
| 15 | `codigo` | 51 | 46 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `centro` | 0.2496 |
| 2 | `pesquisa` | 0.2462 |
| 3 | `rede` | 0.2128 |
| 4 | `claudio` | 0.1623 |
| 5 | `fabio` | 0.1292 |
| 6 | `publico` | 0.1161 |
| 7 | `corporacao` | 0.0937 |
| 8 | `tecnologia` | 0.0846 |
| 9 | `hollerith` | 0.0703 |
| 10 | `ator` | 0.0580 |
| 11 | `seguir` | 0.0543 |
| 12 | `cientifico` | 0.0533 |
| 13 | `ecossistema` | 0.0516 |
| 14 | `brasil` | 0.0486 |
| 15 | `universidade` | 0.0383 |
| 16 | `fapesp` | 0.0355 |
| 17 | `arranjo` | 0.0341 |
| 18 | `modelo` | 0.0317 |
| 19 | `empresa` | 0.0317 |
| 20 | `inteligencia` | 0.0289 |

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
| 8 | `elaboracao` | `base` | 0.615 | 21 |
| 9 | `acesso` | `disponivel` | 0.589 | 27 |
| 10 | `claudio` | `fabio` | 0.586 | 166 |
| 11 | `novembro` | `dezembro` | 0.571 | 23 |
| 12 | `passagem` | `ponto` | 0.570 | 27 |
| 13 | `research` | `brasil` | 0.546 | 38 |
| 14 | `inovacao` | `ecossistema` | 0.527 | 43 |
| 15 | `cientifico` | `producao` | 0.510 | 34 |
| 16 | `entrevistas` | `observacao` | 0.507 | 18 |
| 17 | `translacao` | `cadeias` | 0.506 | 12 |
| 18 | `mapa` | `problemas` | 0.505 | 12 |
| 19 | `relatorios` | `base` | 0.498 | 18 |
| 20 | `gente` | `dinheiro` | 0.497 | 15 |
| 21 | `relatorios` | `elaboracao` | 0.496 | 14 |
| 22 | `research` | `fechamento` | 0.494 | 12 |
| 23 | `hollerith` | `maquina` | 0.482 | 55 |
| 24 | `anuais` | `base` | 0.475 | 12 |
| 25 | `claudio` | `informacao` | 0.469 | 61 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (45 termos): tecnologia, hollerith, infraestrutura, empresa, maquina, trajetoria
- **Tópico 2** (39 termos): claudio, rede, fabio, seguir, ator, informacao
- **Tópico 3** (36 termos): pesquisa, centro, cientifico, fapesp, relatorios, partir
- **Tópico 4** (26 termos): publico, arranjo, corporacao, brasil, laboratorio, universidade
- **Tópico 5** (12 termos): modelo, codigo, aberto, negocio, processamento, torna
- **Tópico 6** (12 termos): parte, escala, historica, maior, estados, investigacao
- **Tópico 7** (10 termos): inteligencia, artificial, ecossistema, inovacao, brasileiro, obia

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 3** [pesquisa, centro, cientifico] e **Tópico 5** [modelo, codigo, aberto] — densidade ponderada de ligação = 0.2500
- Lacuna entre **Tópico 2** [claudio, rede, fabio] e **Tópico 5** [modelo, codigo, aberto] — densidade ponderada de ligação = 0.2692
- Lacuna entre **Tópico 1** [tecnologia, hollerith, infraestrutura] e **Tópico 3** [pesquisa, centro, cientifico] — densidade ponderada de ligação = 0.3315
- Lacuna entre **Tópico 1** [tecnologia, hollerith, infraestrutura] e **Tópico 5** [modelo, codigo, aberto] — densidade ponderada de ligação = 0.3352
- Lacuna entre **Tópico 4** [publico, arranjo, corporacao] e **Tópico 5** [modelo, codigo, aberto] — densidade ponderada de ligação = 0.3526
- Lacuna entre **Tópico 1** [tecnologia, hollerith, infraestrutura] e **Tópico 2** [claudio, rede, fabio] — densidade ponderada de ligação = 0.4091

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
