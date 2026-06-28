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
- Tokens significativos: **17,635**
- Grafo bruto: **5333** nós · **45583** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **2527** arestas
- Tópicos detectados (Louvain): **7**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `claudio` | 791 |
| 2 | `pesquisa` | 663 |
| 3 | `rede` | 599 |
| 4 | `centro` | 509 |
| 5 | `fabio` | 500 |
| 6 | `publico` | 416 |
| 7 | `arranjo` | 407 |
| 8 | `corporacao` | 364 |
| 9 | `seguir` | 360 |
| 10 | `brasil` | 311 |
| 11 | `inteligencia` | 305 |
| 12 | `hollerith` | 300 |
| 13 | `artificial` | 298 |
| 14 | `tecnologia` | 293 |
| 15 | `ator` | 288 |
| 16 | `laboratorio` | 266 |
| 17 | `infraestrutura` | 255 |
| 18 | `ecossistema` | 251 |
| 19 | `empresa` | 243 |
| 20 | `fapesp` | 234 |
| 21 | `maquina` | 233 |
| 22 | `modelo` | 230 |
| 23 | `instituicao` | 230 |
| 24 | `universidade` | 225 |
| 25 | `trajetoria` | 212 |
| 26 | `informacao` | 210 |
| 27 | `campo` | 204 |
| 28 | `encerramento` | 194 |
| 29 | `associacao` | 185 |
| 30 | `verbal` | 184 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `claudio` | 0.0284 |
| 2 | `pesquisa` | 0.0254 |
| 3 | `rede` | 0.0230 |
| 4 | `centro` | 0.0195 |
| 5 | `fabio` | 0.0178 |
| 6 | `publico` | 0.0162 |
| 7 | `arranjo` | 0.0159 |
| 8 | `corporacao` | 0.0146 |
| 9 | `seguir` | 0.0139 |
| 10 | `brasil` | 0.0124 |
| 11 | `tecnologia` | 0.0123 |
| 12 | `hollerith` | 0.0123 |
| 13 | `ator` | 0.0113 |
| 14 | `inteligencia` | 0.0112 |
| 15 | `artificial` | 0.0110 |
| 16 | `infraestrutura` | 0.0106 |
| 17 | `laboratorio` | 0.0104 |
| 18 | `ecossistema` | 0.0100 |
| 19 | `modelo` | 0.0099 |
| 20 | `empresa` | 0.0099 |
| 21 | `maquina` | 0.0096 |
| 22 | `fapesp` | 0.0095 |
| 23 | `instituicao` | 0.0093 |
| 24 | `universidade` | 0.0091 |
| 25 | `trajetoria` | 0.0088 |
| 26 | `campo` | 0.0084 |
| 27 | `dado` | 0.0080 |
| 28 | `encerramento` | 0.0078 |
| 29 | `cientifico` | 0.0077 |
| 30 | `associacao` | 0.0077 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `processamento` | 125 | 110 | +15 |
| 2 | `cadeia` | 97 | 84 | +13 |
| 3 | `translacao` | 89 | 78 | +11 |
| 4 | `conta` | 132 | 121 | +11 |
| 5 | `estados` | 69 | 59 | +10 |
| 6 | `unidos` | 88 | 79 | +9 |
| 7 | `cartoes` | 111 | 103 | +8 |
| 8 | `pratica` | 121 | 113 | +8 |
| 9 | `material` | 90 | 83 | +7 |
| 10 | `censo` | 98 | 91 | +7 |
| 11 | `linguagem` | 157 | 150 | +7 |
| 12 | `tecnica` | 54 | 48 | +6 |
| 13 | `conhecimento` | 83 | 77 | +6 |
| 14 | `lado` | 95 | 89 | +6 |
| 15 | `dependencia` | 99 | 93 | +6 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `centro` | 0.2637 |
| 2 | `rede` | 0.2310 |
| 3 | `pesquisa` | 0.2165 |
| 4 | `claudio` | 0.1761 |
| 5 | `fabio` | 0.1421 |
| 6 | `publico` | 0.1062 |
| 7 | `corporacao` | 0.0963 |
| 8 | `tecnologia` | 0.0835 |
| 9 | `hollerith` | 0.0725 |
| 10 | `seguir` | 0.0668 |
| 11 | `ator` | 0.0610 |
| 12 | `ecossistema` | 0.0522 |
| 13 | `brasil` | 0.0521 |
| 14 | `universidade` | 0.0371 |
| 15 | `cientifico` | 0.0368 |
| 16 | `fapesp` | 0.0352 |
| 17 | `arranjo` | 0.0340 |
| 18 | `inteligencia` | 0.0328 |
| 19 | `modelo` | 0.0318 |
| 20 | `empresa` | 0.0316 |

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
| 4 | `aberto` | `codigo` | 0.747 | 45 |
| 5 | `linguagem` | `processamento` | 0.735 | 30 |
| 6 | `historica` | `investigacao` | 0.622 | 24 |
| 7 | `acesso` | `disponivel` | 0.588 | 27 |
| 8 | `claudio` | `fabio` | 0.588 | 169 |
| 9 | `novembro` | `dezembro` | 0.571 | 23 |
| 10 | `passagem` | `ponto` | 0.570 | 27 |
| 11 | `research` | `brasil` | 0.546 | 38 |
| 12 | `inovacao` | `ecossistema` | 0.526 | 43 |
| 13 | `entrevistas` | `observacao` | 0.507 | 18 |
| 14 | `translacao` | `cadeias` | 0.506 | 12 |
| 15 | `gente` | `dinheiro` | 0.496 | 15 |
| 16 | `research` | `fechamento` | 0.494 | 12 |
| 17 | `hollerith` | `tabulacao` | 0.482 | 36 |
| 18 | `hollerith` | `maquina` | 0.479 | 55 |
| 19 | `grupo` | `obia` | 0.469 | 11 |
| 20 | `inteligencia` | `brasileiro` | 0.469 | 24 |
| 21 | `claudio` | `informacao` | 0.468 | 61 |
| 22 | `cientifico` | `relatorios` | 0.465 | 21 |
| 23 | `comercial` | `tecnica` | 0.463 | 13 |
| 24 | `abertura` | `codigo` | 0.457 | 11 |
| 25 | `comercial` | `interesse` | 0.451 | 9 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (43 termos): claudio, rede, fabio, seguir, ator, informacao
- **Tópico 2** (36 termos): publico, corporacao, tecnologia, infraestrutura, instituicao, universidade
- **Tópico 3** (32 termos): pesquisa, centro, fapesp, cientifico, pesquisador, partir
- **Tópico 4** (31 termos): hollerith, empresa, maquina, trajetoria, tabulacao, ponto
- **Tópico 5** (14 termos): modelo, codigo, aberto, negocio, pratica, processamento
- **Tópico 6** (14 termos): arranjo, brasil, laboratorio, encerramento, acesso, dezembro
- **Tópico 7** (10 termos): inteligencia, artificial, ecossistema, inovacao, brasileiro, obia

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 5** [modelo, codigo, aberto] — densidade ponderada de ligação = 0.2625
- Lacuna entre **Tópico 4** [hollerith, empresa, maquina] e **Tópico 5** [modelo, codigo, aberto] — densidade ponderada de ligação = 0.2765
- Lacuna entre **Tópico 3** [pesquisa, centro, fapesp] e **Tópico 5** [modelo, codigo, aberto] — densidade ponderada de ligação = 0.2835
- Lacuna entre **Tópico 3** [pesquisa, centro, fapesp] e **Tópico 4** [hollerith, empresa, maquina] — densidade ponderada de ligação = 0.2984
- Lacuna entre **Tópico 2** [publico, corporacao, tecnologia] e **Tópico 5** [modelo, codigo, aberto] — densidade ponderada de ligação = 0.3968
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 4** [hollerith, empresa, maquina] — densidade ponderada de ligação = 0.4186

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
