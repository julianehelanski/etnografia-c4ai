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
- Tokens significativos: **18,647**
- Grafo bruto: **5647** nós · **48576** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **2592** arestas
- Tópicos detectados (Louvain): **7**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `claudio` | 840 |
| 2 | `pesquisa` | 720 |
| 3 | `rede` | 559 |
| 4 | `centro` | 534 |
| 5 | `fabio` | 520 |
| 6 | `seguir` | 364 |
| 7 | `publico` | 353 |
| 8 | `artificial` | 341 |
| 9 | `inteligencia` | 338 |
| 10 | `brasil` | 329 |
| 11 | `corporacao` | 325 |
| 12 | `arranjo` | 316 |
| 13 | `ator` | 287 |
| 14 | `maquina` | 285 |
| 15 | `hollerith` | 278 |
| 16 | `tecnologia` | 270 |
| 17 | `fapesp` | 259 |
| 18 | `empresa` | 256 |
| 19 | `laboratorio` | 247 |
| 20 | `modelo` | 245 |
| 21 | `ecossistema` | 242 |
| 22 | `instituicao` | 231 |
| 23 | `dado` | 228 |
| 24 | `campo` | 219 |
| 25 | `informacao` | 218 |
| 26 | `universidade` | 217 |
| 27 | `associacao` | 213 |
| 28 | `infraestrutura` | 209 |
| 29 | `trajetoria` | 207 |
| 30 | `verbal` | 202 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `claudio` | 0.0293 |
| 2 | `pesquisa` | 0.0268 |
| 3 | `rede` | 0.0208 |
| 4 | `centro` | 0.0196 |
| 5 | `fabio` | 0.0179 |
| 6 | `seguir` | 0.0137 |
| 7 | `publico` | 0.0133 |
| 8 | `brasil` | 0.0128 |
| 9 | `corporacao` | 0.0127 |
| 10 | `arranjo` | 0.0121 |
| 11 | `artificial` | 0.0120 |
| 12 | `inteligencia` | 0.0118 |
| 13 | `hollerith` | 0.0112 |
| 14 | `maquina` | 0.0111 |
| 15 | `ator` | 0.0110 |
| 16 | `tecnologia` | 0.0109 |
| 17 | `fapesp` | 0.0102 |
| 18 | `empresa` | 0.0100 |
| 19 | `modelo` | 0.0100 |
| 20 | `laboratorio` | 0.0096 |
| 21 | `dado` | 0.0094 |
| 22 | `ecossistema` | 0.0092 |
| 23 | `instituicao` | 0.0090 |
| 24 | `campo` | 0.0088 |
| 25 | `infraestrutura` | 0.0087 |
| 26 | `associacao` | 0.0085 |
| 27 | `universidade` | 0.0084 |
| 28 | `trajetoria` | 0.0083 |
| 29 | `analise` | 0.0081 |
| 30 | `vinculo` | 0.0078 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `conta` | 146 | 123 | +23 |
| 2 | `linguas` | 100 | 87 | +13 |
| 3 | `indigenas` | 101 | 88 | +13 |
| 4 | `mostra` | 140 | 127 | +13 |
| 5 | `estados` | 69 | 59 | +10 |
| 6 | `logica` | 153 | 144 | +9 |
| 7 | `pessoas` | 172 | 163 | +9 |
| 8 | `vida` | 173 | 164 | +9 |
| 9 | `tecnociencia` | 116 | 108 | +8 |
| 10 | `censo` | 138 | 130 | +8 |
| 11 | `latour` | 102 | 95 | +7 |
| 12 | `inscricao` | 152 | 145 | +7 |
| 13 | `tecnica` | 66 | 60 | +6 |
| 14 | `pratica` | 91 | 85 | +6 |
| 15 | `codigo` | 45 | 40 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `centro` | 0.3197 |
| 2 | `pesquisa` | 0.2762 |
| 3 | `claudio` | 0.2063 |
| 4 | `rede` | 0.1728 |
| 5 | `fabio` | 0.1243 |
| 6 | `publico` | 0.0647 |
| 7 | `inteligencia` | 0.0644 |
| 8 | `seguir` | 0.0635 |
| 9 | `fapesp` | 0.0627 |
| 10 | `brasil` | 0.0615 |
| 11 | `tecnologia` | 0.0584 |
| 12 | `hollerith` | 0.0579 |
| 13 | `ator` | 0.0572 |
| 14 | `dado` | 0.0516 |
| 15 | `corporacao` | 0.0507 |
| 16 | `artificial` | 0.0397 |
| 17 | `modelo` | 0.0393 |
| 18 | `empresa` | 0.0381 |
| 19 | `maquina` | 0.0379 |
| 20 | `ecossistema` | 0.0321 |

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
| 5 | `linguagem` | `natural` | 0.760 | 43 |
| 6 | `aberto` | `codigo` | 0.740 | 51 |
| 7 | `linguagem` | `processamento` | 0.691 | 36 |
| 8 | `processamento` | `natural` | 0.688 | 24 |
| 9 | `maquina` | `aprendizado` | 0.636 | 47 |
| 10 | `acesso` | `disponivel` | 0.635 | 34 |
| 11 | `historica` | `investigacao` | 0.618 | 24 |
| 12 | `claudio` | `fabio` | 0.579 | 179 |
| 13 | `research` | `brasil` | 0.566 | 47 |
| 14 | `inovacao` | `ecossistema` | 0.550 | 46 |
| 15 | `novembro` | `dezembro` | 0.528 | 12 |
| 16 | `passagem` | `ponto` | 0.523 | 21 |
| 17 | `laboratorio` | `fechamento` | 0.517 | 31 |
| 18 | `hollerith` | `tabulacao` | 0.516 | 39 |
| 19 | `comercial` | `tecnica` | 0.512 | 19 |
| 20 | `entrevistas` | `observacao` | 0.499 | 20 |
| 21 | `gente` | `dinheiro` | 0.497 | 15 |
| 22 | `sistema` | `tabulacao` | 0.486 | 24 |
| 23 | `documentos` | `entrevistas` | 0.481 | 21 |
| 24 | `claudio` | `informacao` | 0.477 | 63 |
| 25 | `linguas` | `projeto` | 0.468 | 12 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (49 termos): claudio, rede, fabio, seguir, ator, campo
- **Tópico 2** (33 termos): tecnologia, modelo, dado, codigo, linguagem, aberto
- **Tópico 3** (32 termos): pesquisa, centro, analise, pesquisador, cientifico, parte
- **Tópico 4** (32 termos): publico, corporacao, arranjo, fapesp, instituicao, universidade
- **Tópico 5** (18 termos): artificial, inteligencia, maquina, hollerith, empresa, ecossistema
- **Tópico 6** (12 termos): brasil, laboratorio, acesso, research, fechamento, estados
- **Tópico 7** (4 termos): trajetoria, historica, leitura, investigacao

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 2** [tecnologia, modelo, dado] — densidade ponderada de ligação = 0.2764
- Lacuna entre **Tópico 2** [tecnologia, modelo, dado] e **Tópico 4** [publico, corporacao, arranjo] — densidade ponderada de ligação = 0.3693
- Lacuna entre **Tópico 2** [tecnologia, modelo, dado] e **Tópico 3** [pesquisa, centro, analise] — densidade ponderada de ligação = 0.3996
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 5** [artificial, inteligencia, maquina] — densidade ponderada de ligação = 0.4014
- Lacuna entre **Tópico 4** [publico, corporacao, arranjo] e **Tópico 5** [artificial, inteligencia, maquina] — densidade ponderada de ligação = 0.4149
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 4** [publico, corporacao, arranjo] — densidade ponderada de ligação = 0.4758

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
