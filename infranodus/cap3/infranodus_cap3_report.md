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
- Tokens significativos: **19,092**
- Grafo bruto: **5739** nós · **49694** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **2647** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `claudio` | 895 |
| 2 | `pesquisa` | 730 |
| 3 | `rede` | 586 |
| 4 | `centro` | 533 |
| 5 | `fabio` | 523 |
| 6 | `publico` | 367 |
| 7 | `inteligencia` | 363 |
| 8 | `artificial` | 362 |
| 9 | `seguir` | 354 |
| 10 | `brasil` | 346 |
| 11 | `corporacao` | 333 |
| 12 | `arranjo` | 331 |
| 13 | `fapesp` | 322 |
| 14 | `tecnologia` | 311 |
| 15 | `maquina` | 306 |
| 16 | `ecossistema` | 301 |
| 17 | `ator` | 285 |
| 18 | `hollerith` | 281 |
| 19 | `laboratorio` | 269 |
| 20 | `modelo` | 262 |
| 21 | `dado` | 260 |
| 22 | `empresa` | 257 |
| 23 | `informacao` | 243 |
| 24 | `universidade` | 232 |
| 25 | `instituicao` | 221 |
| 26 | `trajetoria` | 218 |
| 27 | `verbal` | 218 |
| 28 | `associacao` | 217 |
| 29 | `campo` | 213 |
| 30 | `infraestrutura` | 207 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `claudio` | 0.0300 |
| 2 | `pesquisa` | 0.0261 |
| 3 | `rede` | 0.0212 |
| 4 | `centro` | 0.0189 |
| 5 | `fabio` | 0.0174 |
| 6 | `publico` | 0.0135 |
| 7 | `seguir` | 0.0130 |
| 8 | `brasil` | 0.0129 |
| 9 | `corporacao` | 0.0126 |
| 10 | `inteligencia` | 0.0124 |
| 11 | `artificial` | 0.0124 |
| 12 | `arranjo` | 0.0122 |
| 13 | `fapesp` | 0.0122 |
| 14 | `tecnologia` | 0.0120 |
| 15 | `maquina` | 0.0115 |
| 16 | `hollerith` | 0.0110 |
| 17 | `ecossistema` | 0.0109 |
| 18 | `ator` | 0.0106 |
| 19 | `modelo` | 0.0103 |
| 20 | `dado` | 0.0103 |
| 21 | `laboratorio` | 0.0100 |
| 22 | `empresa` | 0.0097 |
| 23 | `universidade` | 0.0087 |
| 24 | `trajetoria` | 0.0085 |
| 25 | `instituicao` | 0.0084 |
| 26 | `associacao` | 0.0084 |
| 27 | `infraestrutura` | 0.0083 |
| 28 | `campo` | 0.0083 |
| 29 | `informacao` | 0.0082 |
| 30 | `analise` | 0.0077 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `conta` | 156 | 137 | +19 |
| 2 | `mostra` | 143 | 131 | +12 |
| 3 | `indigenas` | 97 | 86 | +11 |
| 4 | `linguas` | 106 | 97 | +9 |
| 5 | `cadeia` | 111 | 102 | +9 |
| 6 | `tecnicas` | 126 | 117 | +9 |
| 7 | `vida` | 170 | 162 | +8 |
| 8 | `estados` | 62 | 55 | +7 |
| 9 | `tecnica` | 67 | 60 | +7 |
| 10 | `maior` | 72 | 65 | +7 |
| 11 | `unidos` | 76 | 69 | +7 |
| 12 | `tecnociencia` | 115 | 108 | +7 |
| 13 | `censo` | 140 | 133 | +7 |
| 14 | `parcerias` | 141 | 134 | +7 |
| 15 | `pessoas` | 172 | 165 | +7 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `pesquisa` | 0.2935 |
| 2 | `centro` | 0.2762 |
| 3 | `rede` | 0.2045 |
| 4 | `claudio` | 0.1907 |
| 5 | `fabio` | 0.1176 |
| 6 | `tecnologia` | 0.0751 |
| 7 | `fapesp` | 0.0731 |
| 8 | `inteligencia` | 0.0646 |
| 9 | `dado` | 0.0638 |
| 10 | `hollerith` | 0.0619 |
| 11 | `ator` | 0.0576 |
| 12 | `corporacao` | 0.0527 |
| 13 | `brasil` | 0.0516 |
| 14 | `publico` | 0.0513 |
| 15 | `seguir` | 0.0503 |
| 16 | `maquina` | 0.0408 |
| 17 | `artificial` | 0.0399 |
| 18 | `ecossistema` | 0.0378 |
| 19 | `arranjo` | 0.0342 |
| 20 | `empresa` | 0.0313 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `informacao` | `verbal` | 0.872 | 86 |
| 2 | `inteligencia` | `artificial` | 0.864 | 156 |
| 3 | `unidos` | `estados` | 0.860 | 54 |
| 4 | `linguas` | `indigenas` | 0.782 | 40 |
| 5 | `linguagem` | `natural` | 0.751 | 46 |
| 6 | `aberto` | `codigo` | 0.734 | 54 |
| 7 | `processamento` | `natural` | 0.696 | 28 |
| 8 | `linguagem` | `processamento` | 0.677 | 40 |
| 9 | `maquina` | `aprendizado` | 0.653 | 56 |
| 10 | `acesso` | `disponivel` | 0.646 | 37 |
| 11 | `historica` | `investigacao` | 0.620 | 24 |
| 12 | `claudio` | `fabio` | 0.578 | 182 |
| 13 | `research` | `brasil` | 0.563 | 51 |
| 14 | `inovacao` | `ecossistema` | 0.539 | 58 |
| 15 | `hollerith` | `tabulacao` | 0.515 | 39 |
| 16 | `laboratorio` | `fechamento` | 0.514 | 34 |
| 17 | `comercial` | `tecnica` | 0.509 | 19 |
| 18 | `passagem` | `ponto` | 0.499 | 18 |
| 19 | `claudio` | `informacao` | 0.496 | 75 |
| 20 | `documentos` | `entrevistas` | 0.493 | 21 |
| 21 | `sistema` | `tabulacao` | 0.488 | 24 |
| 22 | `gente` | `dinheiro` | 0.488 | 15 |
| 23 | `entrevistas` | `observacao` | 0.482 | 20 |
| 24 | `ecossistemas` | `inovacao` | 0.480 | 18 |
| 25 | `fapesp` | `convenio` | 0.478 | 23 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (41 termos): publico, corporacao, tecnologia, dado, universidade, instituicao
- **Tópico 2** (34 termos): pesquisa, centro, arranjo, fapesp, analise, cientifico
- **Tópico 3** (29 termos): rede, seguir, ator, associacao, descrevo, etnografia
- **Tópico 4** (20 termos): inteligencia, artificial, maquina, hollerith, empresa, trajetoria
- **Tópico 5** (19 termos): claudio, fabio, informacao, verbal, campo, entrevistas
- **Tópico 6** (16 termos): modelo, codigo, linguagem, aberto, processamento, natural
- **Tópico 7** (12 termos): brasil, laboratorio, pesquisador, vinculo, research, acesso
- **Tópico 8** (9 termos): ecossistema, inovacao, historica, questao, tornou, investigacao

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 4** [inteligencia, artificial, maquina] e **Tópico 5** [claudio, fabio, informacao] — densidade ponderada de ligação = 0.3342
- Lacuna entre **Tópico 1** [publico, corporacao, tecnologia] e **Tópico 3** [rede, seguir, ator] — densidade ponderada de ligação = 0.3448
- Lacuna entre **Tópico 3** [rede, seguir, ator] e **Tópico 4** [inteligencia, artificial, maquina] — densidade ponderada de ligação = 0.4259
- Lacuna entre **Tópico 1** [publico, corporacao, tecnologia] e **Tópico 5** [claudio, fabio, informacao] — densidade ponderada de ligação = 0.4300
- Lacuna entre **Tópico 1** [publico, corporacao, tecnologia] e **Tópico 4** [inteligencia, artificial, maquina] — densidade ponderada de ligação = 0.4756
- Lacuna entre **Tópico 2** [pesquisa, centro, arranjo] e **Tópico 3** [rede, seguir, ator] — densidade ponderada de ligação = 0.4757

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
