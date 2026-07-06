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
- Tokens significativos: **18,874**
- Grafo bruto: **5692** nós · **49140** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **2601** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `claudio` | 897 |
| 2 | `pesquisa` | 724 |
| 3 | `rede` | 551 |
| 4 | `fabio` | 532 |
| 5 | `centro` | 503 |
| 6 | `seguir` | 358 |
| 7 | `inteligencia` | 346 |
| 8 | `artificial` | 345 |
| 9 | `arranjo` | 342 |
| 10 | `publico` | 341 |
| 11 | `corporacao` | 333 |
| 12 | `brasil` | 329 |
| 13 | `tecnologia` | 322 |
| 14 | `maquina` | 300 |
| 15 | `fapesp` | 298 |
| 16 | `ecossistema` | 293 |
| 17 | `ator` | 283 |
| 18 | `laboratorio` | 271 |
| 19 | `hollerith` | 268 |
| 20 | `dado` | 265 |
| 21 | `modelo` | 264 |
| 22 | `empresa` | 257 |
| 23 | `informacao` | 236 |
| 24 | `universidade` | 230 |
| 25 | `instituicao` | 215 |
| 26 | `campo` | 215 |
| 27 | `associacao` | 211 |
| 28 | `verbal` | 208 |
| 29 | `infraestrutura` | 207 |
| 30 | `inovacao` | 203 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `claudio` | 0.0307 |
| 2 | `pesquisa` | 0.0264 |
| 3 | `rede` | 0.0204 |
| 4 | `centro` | 0.0183 |
| 5 | `fabio` | 0.0181 |
| 6 | `seguir` | 0.0133 |
| 7 | `arranjo` | 0.0130 |
| 8 | `corporacao` | 0.0128 |
| 9 | `publico` | 0.0128 |
| 10 | `tecnologia` | 0.0128 |
| 11 | `brasil` | 0.0125 |
| 12 | `inteligencia` | 0.0121 |
| 13 | `artificial` | 0.0121 |
| 14 | `fapesp` | 0.0116 |
| 15 | `maquina` | 0.0115 |
| 16 | `ecossistema` | 0.0108 |
| 17 | `ator` | 0.0108 |
| 18 | `dado` | 0.0107 |
| 19 | `hollerith` | 0.0107 |
| 20 | `modelo` | 0.0105 |
| 21 | `laboratorio` | 0.0102 |
| 22 | `empresa` | 0.0100 |
| 23 | `universidade` | 0.0088 |
| 24 | `campo` | 0.0085 |
| 25 | `instituicao` | 0.0084 |
| 26 | `infraestrutura` | 0.0084 |
| 27 | `associacao` | 0.0083 |
| 28 | `informacao` | 0.0081 |
| 29 | `trajetoria` | 0.0081 |
| 30 | `pergunta` | 0.0080 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `conta` | 145 | 126 | +19 |
| 2 | `vida` | 170 | 158 | +12 |
| 3 | `estados` | 67 | 58 | +9 |
| 4 | `estatistica` | 110 | 101 | +9 |
| 5 | `linguas` | 107 | 99 | +8 |
| 6 | `mostra` | 135 | 127 | +8 |
| 7 | `tecnica` | 64 | 57 | +7 |
| 8 | `humano` | 89 | 82 | +7 |
| 9 | `indigenas` | 101 | 94 | +7 |
| 10 | `objeto` | 147 | 140 | +7 |
| 11 | `pratica` | 84 | 78 | +6 |
| 12 | `actante` | 69 | 64 | +5 |
| 13 | `unidos` | 72 | 67 | +5 |
| 14 | `material` | 79 | 74 | +5 |
| 15 | `comercial` | 80 | 75 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `pesquisa` | 0.3143 |
| 2 | `centro` | 0.2578 |
| 3 | `claudio` | 0.2185 |
| 4 | `rede` | 0.1737 |
| 5 | `fabio` | 0.1353 |
| 6 | `tecnologia` | 0.0826 |
| 7 | `dado` | 0.0728 |
| 8 | `inteligencia` | 0.0697 |
| 9 | `fapesp` | 0.0668 |
| 10 | `seguir` | 0.0644 |
| 11 | `ator` | 0.0585 |
| 12 | `hollerith` | 0.0556 |
| 13 | `brasil` | 0.0503 |
| 14 | `ecossistema` | 0.0475 |
| 15 | `corporacao` | 0.0441 |
| 16 | `empresa` | 0.0411 |
| 17 | `artificial` | 0.0395 |
| 18 | `maquina` | 0.0374 |
| 19 | `arranjo` | 0.0342 |
| 20 | `entrevistas` | 0.0331 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `informacao` | `verbal` | 0.872 | 83 |
| 2 | `inteligencia` | `artificial` | 0.864 | 150 |
| 3 | `unidos` | `estados` | 0.860 | 54 |
| 4 | `linguas` | `indigenas` | 0.782 | 40 |
| 5 | `linguagem` | `natural` | 0.750 | 46 |
| 6 | `aberto` | `codigo` | 0.733 | 54 |
| 7 | `processamento` | `natural` | 0.695 | 28 |
| 8 | `linguagem` | `processamento` | 0.676 | 40 |
| 9 | `acesso` | `disponivel` | 0.654 | 40 |
| 10 | `maquina` | `aprendizado` | 0.648 | 53 |
| 11 | `historica` | `investigacao` | 0.619 | 24 |
| 12 | `claudio` | `fabio` | 0.580 | 183 |
| 13 | `research` | `brasil` | 0.576 | 51 |
| 14 | `inovacao` | `ecossistema` | 0.550 | 58 |
| 15 | `laboratorio` | `fechamento` | 0.516 | 34 |
| 16 | `hollerith` | `tabulacao` | 0.514 | 39 |
| 17 | `brasileiro` | `contexto` | 0.508 | 12 |
| 18 | `comercial` | `tecnica` | 0.508 | 19 |
| 19 | `claudio` | `informacao` | 0.490 | 72 |
| 20 | `sistema` | `tabulacao` | 0.487 | 24 |
| 21 | `gente` | `dinheiro` | 0.487 | 15 |
| 22 | `documentos` | `entrevistas` | 0.485 | 21 |
| 23 | `fapesp` | `convenio` | 0.484 | 23 |
| 24 | `entrevistas` | `observacao` | 0.482 | 20 |
| 25 | `cadeia` | `translacao` | 0.466 | 12 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (48 termos): pesquisa, centro, arranjo, publico, corporacao, fapesp
- **Tópico 2** (36 termos): rede, seguir, ator, campo, associacao, descrevo
- **Tópico 3** (26 termos): tecnologia, maquina, hollerith, tabulacao, ciencia, aprendizado
- **Tópico 4** (18 termos): dado, modelo, codigo, linguagem, aberto, processamento
- **Tópico 5** (18 termos): ecossistema, empresa, inovacao, trajetoria, descreve, historica
- **Tópico 6** (16 termos): claudio, fabio, informacao, verbal, pergunta, entrevistas
- **Tópico 7** (12 termos): inteligencia, artificial, brasil, laboratorio, vinculo, research
- **Tópico 8** (6 termos): acesso, estados, unidos, disponivel, sustenta, decisao

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 2** [rede, seguir, ator] e **Tópico 4** [dado, modelo, codigo] — densidade ponderada de ligação = 0.2130
- Lacuna entre **Tópico 2** [rede, seguir, ator] e **Tópico 3** [tecnologia, maquina, hollerith] — densidade ponderada de ligação = 0.3419
- Lacuna entre **Tópico 3** [tecnologia, maquina, hollerith] e **Tópico 4** [dado, modelo, codigo] — densidade ponderada de ligação = 0.3526
- Lacuna entre **Tópico 4** [dado, modelo, codigo] e **Tópico 5** [ecossistema, empresa, inovacao] — densidade ponderada de ligação = 0.3735
- Lacuna entre **Tópico 2** [rede, seguir, ator] e **Tópico 5** [ecossistema, empresa, inovacao] — densidade ponderada de ligação = 0.4074
- Lacuna entre **Tópico 1** [pesquisa, centro, arranjo] e **Tópico 2** [rede, seguir, ator] — densidade ponderada de ligação = 0.4161

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
