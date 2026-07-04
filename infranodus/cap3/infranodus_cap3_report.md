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
- Tokens significativos: **18,745**
- Grafo bruto: **5658** nós · **48799** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **2605** arestas
- Tópicos detectados (Louvain): **7**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `claudio` | 848 |
| 2 | `pesquisa` | 723 |
| 3 | `rede` | 562 |
| 4 | `centro` | 535 |
| 5 | `fabio` | 520 |
| 6 | `seguir` | 366 |
| 7 | `publico` | 362 |
| 8 | `artificial` | 343 |
| 9 | `inteligencia` | 342 |
| 10 | `brasil` | 332 |
| 11 | `corporacao` | 327 |
| 12 | `arranjo` | 325 |
| 13 | `ator` | 297 |
| 14 | `maquina` | 282 |
| 15 | `hollerith` | 278 |
| 16 | `tecnologia` | 272 |
| 17 | `empresa` | 261 |
| 18 | `fapesp` | 258 |
| 19 | `ecossistema` | 247 |
| 20 | `modelo` | 245 |
| 21 | `laboratorio` | 244 |
| 22 | `instituicao` | 240 |
| 23 | `dado` | 230 |
| 24 | `campo` | 222 |
| 25 | `universidade` | 217 |
| 26 | `informacao` | 216 |
| 27 | `associacao` | 213 |
| 28 | `infraestrutura` | 213 |
| 29 | `trajetoria` | 204 |
| 30 | `vinculo` | 201 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `claudio` | 0.0295 |
| 2 | `pesquisa` | 0.0269 |
| 3 | `rede` | 0.0209 |
| 4 | `centro` | 0.0196 |
| 5 | `fabio` | 0.0179 |
| 6 | `seguir` | 0.0138 |
| 7 | `publico` | 0.0137 |
| 8 | `brasil` | 0.0129 |
| 9 | `corporacao` | 0.0128 |
| 10 | `arranjo` | 0.0125 |
| 11 | `artificial` | 0.0121 |
| 12 | `inteligencia` | 0.0120 |
| 13 | `ator` | 0.0114 |
| 14 | `hollerith` | 0.0112 |
| 15 | `maquina` | 0.0111 |
| 16 | `tecnologia` | 0.0110 |
| 17 | `empresa` | 0.0102 |
| 18 | `fapesp` | 0.0101 |
| 19 | `modelo` | 0.0101 |
| 20 | `dado` | 0.0095 |
| 21 | `laboratorio` | 0.0094 |
| 22 | `ecossistema` | 0.0094 |
| 23 | `instituicao` | 0.0094 |
| 24 | `campo` | 0.0089 |
| 25 | `infraestrutura` | 0.0088 |
| 26 | `associacao` | 0.0085 |
| 27 | `universidade` | 0.0084 |
| 28 | `trajetoria` | 0.0082 |
| 29 | `analise` | 0.0080 |
| 30 | `vinculo` | 0.0079 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `conta` | 147 | 125 | +22 |
| 2 | `linguas` | 110 | 96 | +14 |
| 3 | `indigenas` | 104 | 92 | +12 |
| 4 | `mostra` | 141 | 129 | +12 |
| 5 | `estados` | 67 | 57 | +10 |
| 6 | `comercial` | 83 | 74 | +9 |
| 7 | `tecnociencia` | 116 | 107 | +9 |
| 8 | `vida` | 173 | 164 | +9 |
| 9 | `unidos` | 79 | 71 | +8 |
| 10 | `pratica` | 88 | 80 | +8 |
| 11 | `logica` | 152 | 144 | +8 |
| 12 | `pessoas` | 171 | 163 | +8 |
| 13 | `recursos` | 60 | 54 | +6 |
| 14 | `secao` | 62 | 56 | +6 |
| 15 | `tecnica` | 64 | 58 | +6 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `centro` | 0.3307 |
| 2 | `pesquisa` | 0.2797 |
| 3 | `claudio` | 0.2162 |
| 4 | `rede` | 0.1666 |
| 5 | `fabio` | 0.1204 |
| 6 | `brasil` | 0.0700 |
| 7 | `seguir` | 0.0665 |
| 8 | `inteligencia` | 0.0657 |
| 9 | `fapesp` | 0.0642 |
| 10 | `tecnologia` | 0.0576 |
| 11 | `ator` | 0.0567 |
| 12 | `hollerith` | 0.0566 |
| 13 | `publico` | 0.0521 |
| 14 | `dado` | 0.0511 |
| 15 | `corporacao` | 0.0483 |
| 16 | `artificial` | 0.0414 |
| 17 | `empresa` | 0.0405 |
| 18 | `maquina` | 0.0378 |
| 19 | `modelo` | 0.0320 |
| 20 | `ecossistema` | 0.0319 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `informacao` | `verbal` | 0.878 | 80 |
| 2 | `inteligencia` | `artificial` | 0.864 | 153 |
| 3 | `unidos` | `estados` | 0.858 | 48 |
| 4 | `linguas` | `indigenas` | 0.782 | 40 |
| 5 | `aberto` | `codigo` | 0.740 | 51 |
| 6 | `linguagem` | `processamento` | 0.691 | 36 |
| 7 | `maquina` | `aprendizado` | 0.636 | 47 |
| 8 | `acesso` | `disponivel` | 0.635 | 34 |
| 9 | `historica` | `investigacao` | 0.619 | 24 |
| 10 | `claudio` | `fabio` | 0.580 | 179 |
| 11 | `research` | `brasil` | 0.567 | 47 |
| 12 | `inovacao` | `ecossistema` | 0.551 | 46 |
| 13 | `passagem` | `ponto` | 0.523 | 21 |
| 14 | `novembro` | `dezembro` | 0.520 | 12 |
| 15 | `laboratorio` | `fechamento` | 0.517 | 31 |
| 16 | `hollerith` | `tabulacao` | 0.516 | 39 |
| 17 | `comercial` | `tecnica` | 0.513 | 19 |
| 18 | `gente` | `dinheiro` | 0.497 | 15 |
| 19 | `entrevistas` | `observacao` | 0.495 | 20 |
| 20 | `documentos` | `entrevistas` | 0.492 | 21 |
| 21 | `sistema` | `tabulacao` | 0.487 | 24 |
| 22 | `claudio` | `informacao` | 0.478 | 63 |
| 23 | `linguas` | `projeto` | 0.468 | 12 |
| 24 | `cadeia` | `translacao` | 0.466 | 12 |
| 25 | `pessoas` | `vida` | 0.461 | 9 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (53 termos): pesquisa, centro, publico, corporacao, fapesp, instituicao
- **Tópico 2** (42 termos): rede, seguir, arranjo, ator, campo, associacao
- **Tópico 3** (25 termos): tecnologia, modelo, dado, codigo, aberto, ciencia
- **Tópico 4** (20 termos): maquina, hollerith, tabulacao, tecnica, estados, escala
- **Tópico 5** (16 termos): brasil, laboratorio, vinculo, pesquisador, acesso, research
- **Tópico 6** (14 termos): claudio, fabio, informacao, verbal, pergunta, entrevistas
- **Tópico 7** (10 termos): artificial, inteligencia, empresa, ecossistema, inovacao, brasileiro

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 4** [maquina, hollerith, tabulacao] e **Tópico 5** [brasil, laboratorio, vinculo] — densidade ponderada de ligação = 0.2562
- Lacuna entre **Tópico 1** [pesquisa, centro, publico] e **Tópico 4** [maquina, hollerith, tabulacao] — densidade ponderada de ligação = 0.3170
- Lacuna entre **Tópico 2** [rede, seguir, arranjo] e **Tópico 3** [tecnologia, modelo, dado] — densidade ponderada de ligação = 0.3219
- Lacuna entre **Tópico 2** [rede, seguir, arranjo] e **Tópico 4** [maquina, hollerith, tabulacao] — densidade ponderada de ligação = 0.3500
- Lacuna entre **Tópico 3** [tecnologia, modelo, dado] e **Tópico 5** [brasil, laboratorio, vinculo] — densidade ponderada de ligação = 0.3525
- Lacuna entre **Tópico 3** [tecnologia, modelo, dado] e **Tópico 4** [maquina, hollerith, tabulacao] — densidade ponderada de ligação = 0.3900

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
