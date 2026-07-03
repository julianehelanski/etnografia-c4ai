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
- Tokens significativos: **19,011**
- Grafo bruto: **5670** nós · **49024** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **2652** arestas
- Tópicos detectados (Louvain): **7**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `claudio` | 867 |
| 2 | `pesquisa` | 812 |
| 3 | `rede` | 571 |
| 4 | `centro` | 557 |
| 5 | `fabio` | 528 |
| 6 | `publico` | 383 |
| 7 | `seguir` | 363 |
| 8 | `arranjo` | 359 |
| 9 | `artificial` | 347 |
| 10 | `inteligencia` | 346 |
| 11 | `brasil` | 338 |
| 12 | `corporacao` | 336 |
| 13 | `ator` | 291 |
| 14 | `hollerith` | 287 |
| 15 | `maquina` | 283 |
| 16 | `empresa` | 276 |
| 17 | `fapesp` | 271 |
| 18 | `tecnologia` | 271 |
| 19 | `dado` | 263 |
| 20 | `laboratorio` | 260 |
| 21 | `modelo` | 245 |
| 22 | `ecossistema` | 245 |
| 23 | `instituicao` | 241 |
| 24 | `informacao` | 223 |
| 25 | `universidade` | 222 |
| 26 | `infraestrutura` | 221 |
| 27 | `campo` | 217 |
| 28 | `vinculo` | 216 |
| 29 | `relatorios` | 214 |
| 30 | `trajetoria` | 207 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `claudio` | 0.0291 |
| 2 | `pesquisa` | 0.0288 |
| 3 | `rede` | 0.0206 |
| 4 | `centro` | 0.0195 |
| 5 | `fabio` | 0.0176 |
| 6 | `publico` | 0.0139 |
| 7 | `seguir` | 0.0132 |
| 8 | `arranjo` | 0.0132 |
| 9 | `corporacao` | 0.0126 |
| 10 | `brasil` | 0.0125 |
| 11 | `artificial` | 0.0118 |
| 12 | `inteligencia` | 0.0118 |
| 13 | `hollerith` | 0.0112 |
| 14 | `maquina` | 0.0109 |
| 15 | `ator` | 0.0108 |
| 16 | `tecnologia` | 0.0106 |
| 17 | `empresa` | 0.0104 |
| 18 | `dado` | 0.0104 |
| 19 | `fapesp` | 0.0100 |
| 20 | `modelo` | 0.0098 |
| 21 | `laboratorio` | 0.0096 |
| 22 | `instituicao` | 0.0090 |
| 23 | `ecossistema` | 0.0089 |
| 24 | `infraestrutura` | 0.0088 |
| 25 | `campo` | 0.0084 |
| 26 | `universidade` | 0.0083 |
| 27 | `vinculo` | 0.0081 |
| 28 | `relatorios` | 0.0081 |
| 29 | `trajetoria` | 0.0080 |
| 30 | `pesquisador` | 0.0080 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `conta` | 143 | 124 | +19 |
| 2 | `indigenas` | 107 | 89 | +18 |
| 3 | `linguas` | 110 | 93 | +17 |
| 4 | `pratica` | 106 | 92 | +14 |
| 5 | `mostra` | 145 | 131 | +14 |
| 6 | `estados` | 160 | 146 | +14 |
| 7 | `processamento` | 93 | 82 | +11 |
| 8 | `tecnica` | 72 | 62 | +10 |
| 9 | `cadeia` | 114 | 105 | +9 |
| 10 | `tecnociencia` | 121 | 113 | +8 |
| 11 | `comercial` | 84 | 77 | +7 |
| 12 | `material` | 89 | 83 | +6 |
| 13 | `humano` | 97 | 91 | +6 |
| 14 | `censo` | 129 | 123 | +6 |
| 15 | `cartoes` | 134 | 128 | +6 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `pesquisa` | 0.3464 |
| 2 | `centro` | 0.3318 |
| 3 | `claudio` | 0.2284 |
| 4 | `rede` | 0.1577 |
| 5 | `fabio` | 0.1351 |
| 6 | `seguir` | 0.0740 |
| 7 | `dado` | 0.0687 |
| 8 | `brasil` | 0.0669 |
| 9 | `fapesp` | 0.0611 |
| 10 | `hollerith` | 0.0587 |
| 11 | `ator` | 0.0549 |
| 12 | `inteligencia` | 0.0547 |
| 13 | `tecnologia` | 0.0511 |
| 14 | `corporacao` | 0.0455 |
| 15 | `publico` | 0.0435 |
| 16 | `empresa` | 0.0394 |
| 17 | `modelo` | 0.0344 |
| 18 | `maquina` | 0.0303 |
| 19 | `artificial` | 0.0298 |
| 20 | `pergunta` | 0.0296 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `informacao` | `verbal` | 0.879 | 83 |
| 2 | `inteligencia` | `artificial` | 0.864 | 156 |
| 3 | `linguas` | `indigenas` | 0.782 | 40 |
| 4 | `relatorios` | `anuais` | 0.739 | 45 |
| 5 | `aberto` | `codigo` | 0.734 | 51 |
| 6 | `linguagem` | `processamento` | 0.692 | 36 |
| 7 | `maquina` | `aprendizado` | 0.629 | 44 |
| 8 | `acesso` | `disponivel` | 0.627 | 34 |
| 9 | `historica` | `investigacao` | 0.620 | 24 |
| 10 | `claudio` | `fabio` | 0.582 | 182 |
| 11 | `research` | `brasil` | 0.580 | 50 |
| 12 | `inovacao` | `ecossistema` | 0.557 | 46 |
| 13 | `passagem` | `ponto` | 0.539 | 24 |
| 14 | `novembro` | `dezembro` | 0.539 | 15 |
| 15 | `hollerith` | `tabulacao` | 0.515 | 39 |
| 16 | `comercial` | `tecnica` | 0.514 | 19 |
| 17 | `laboratorio` | `fechamento` | 0.506 | 31 |
| 18 | `equipe` | `relatorio` | 0.500 | 20 |
| 19 | `cientifico` | `anuais` | 0.500 | 19 |
| 20 | `gente` | `dinheiro` | 0.498 | 15 |
| 21 | `entrevistas` | `observacao` | 0.496 | 20 |
| 22 | `sistema` | `tabulacao` | 0.483 | 24 |
| 23 | `claudio` | `informacao` | 0.483 | 67 |
| 24 | `linguas` | `projeto` | 0.469 | 12 |
| 25 | `cadeia` | `translacao` | 0.467 | 12 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (47 termos): claudio, rede, fabio, seguir, ator, informacao
- **Tópico 2** (37 termos): hollerith, maquina, tecnologia, trajetoria, tabulacao, ciencia
- **Tópico 3** (32 termos): pesquisa, centro, fapesp, relatorios, cientifico, analise
- **Tópico 4** (22 termos): publico, arranjo, corporacao, instituicao, universidade, infraestrutura
- **Tópico 5** (17 termos): brasil, laboratorio, vinculo, pesquisador, research, acesso
- **Tópico 6** (15 termos): dado, modelo, codigo, aberto, linguagem, processamento
- **Tópico 7** (10 termos): artificial, inteligencia, empresa, ecossistema, inovacao, brasileiro

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 2** [hollerith, maquina, tecnologia] e **Tópico 5** [brasil, laboratorio, vinculo] — densidade ponderada de ligação = 0.2846
- Lacuna entre **Tópico 2** [hollerith, maquina, tecnologia] e **Tópico 3** [pesquisa, centro, fapesp] — densidade ponderada de ligação = 0.3691
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 2** [hollerith, maquina, tecnologia] — densidade ponderada de ligação = 0.3882
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 5** [brasil, laboratorio, vinculo] — densidade ponderada de ligação = 0.3955
- Lacuna entre **Tópico 2** [hollerith, maquina, tecnologia] e **Tópico 4** [publico, arranjo, corporacao] — densidade ponderada de ligação = 0.4754
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 3** [pesquisa, centro, fapesp] — densidade ponderada de ligação = 0.4860

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
