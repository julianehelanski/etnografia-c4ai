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
- Tokens significativos: **18,848**
- Grafo bruto: **5670** nós · **48998** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **2637** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `claudio` | 859 |
| 2 | `pesquisa` | 765 |
| 3 | `rede` | 571 |
| 4 | `centro` | 549 |
| 5 | `fabio` | 526 |
| 6 | `publico` | 380 |
| 7 | `seguir` | 363 |
| 8 | `arranjo` | 357 |
| 9 | `artificial` | 347 |
| 10 | `inteligencia` | 346 |
| 11 | `brasil` | 338 |
| 12 | `corporacao` | 336 |
| 13 | `hollerith` | 289 |
| 14 | `ator` | 289 |
| 15 | `maquina` | 283 |
| 16 | `tecnologia` | 276 |
| 17 | `empresa` | 276 |
| 18 | `fapesp` | 263 |
| 19 | `laboratorio` | 262 |
| 20 | `ecossistema` | 253 |
| 21 | `modelo` | 248 |
| 22 | `instituicao` | 241 |
| 23 | `dado` | 232 |
| 24 | `universidade` | 225 |
| 25 | `informacao` | 223 |
| 26 | `infraestrutura` | 221 |
| 27 | `campo` | 221 |
| 28 | `trajetoria` | 216 |
| 29 | `vinculo` | 216 |
| 30 | `verbal` | 206 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `claudio` | 0.0293 |
| 2 | `pesquisa` | 0.0280 |
| 3 | `rede` | 0.0210 |
| 4 | `centro` | 0.0198 |
| 5 | `fabio` | 0.0178 |
| 6 | `publico` | 0.0141 |
| 7 | `seguir` | 0.0134 |
| 8 | `arranjo` | 0.0134 |
| 9 | `corporacao` | 0.0129 |
| 10 | `brasil` | 0.0128 |
| 11 | `artificial` | 0.0121 |
| 12 | `inteligencia` | 0.0120 |
| 13 | `hollerith` | 0.0115 |
| 14 | `tecnologia` | 0.0110 |
| 15 | `maquina` | 0.0110 |
| 16 | `ator` | 0.0109 |
| 17 | `empresa` | 0.0106 |
| 18 | `fapesp` | 0.0101 |
| 19 | `modelo` | 0.0101 |
| 20 | `laboratorio` | 0.0099 |
| 21 | `ecossistema` | 0.0095 |
| 22 | `dado` | 0.0094 |
| 23 | `instituicao` | 0.0092 |
| 24 | `infraestrutura` | 0.0089 |
| 25 | `campo` | 0.0088 |
| 26 | `universidade` | 0.0086 |
| 27 | `trajetoria` | 0.0085 |
| 28 | `vinculo` | 0.0083 |
| 29 | `analise` | 0.0079 |
| 30 | `pergunta` | 0.0078 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `conta` | 140 | 121 | +19 |
| 2 | `indigenas` | 106 | 93 | +13 |
| 3 | `mostra` | 142 | 129 | +13 |
| 4 | `estados` | 156 | 143 | +13 |
| 5 | `linguas` | 112 | 100 | +12 |
| 6 | `pratica` | 99 | 88 | +11 |
| 7 | `processamento` | 91 | 81 | +10 |
| 8 | `material` | 85 | 76 | +9 |
| 9 | `tecnociencia` | 118 | 109 | +9 |
| 10 | `comercial` | 83 | 75 | +8 |
| 11 | `logica` | 152 | 144 | +8 |
| 12 | `tecnica` | 68 | 61 | +7 |
| 13 | `vida` | 172 | 165 | +7 |
| 14 | `cadeia` | 110 | 104 | +6 |
| 15 | `acao` | 116 | 110 | +6 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `centro` | 0.3347 |
| 2 | `pesquisa` | 0.2839 |
| 3 | `claudio` | 0.2302 |
| 4 | `rede` | 0.1698 |
| 5 | `fabio` | 0.1380 |
| 6 | `seguir` | 0.0768 |
| 7 | `brasil` | 0.0676 |
| 8 | `inteligencia` | 0.0635 |
| 9 | `fapesp` | 0.0609 |
| 10 | `hollerith` | 0.0599 |
| 11 | `tecnologia` | 0.0581 |
| 12 | `ator` | 0.0572 |
| 13 | `corporacao` | 0.0534 |
| 14 | `publico` | 0.0460 |
| 15 | `dado` | 0.0460 |
| 16 | `empresa` | 0.0441 |
| 17 | `artificial` | 0.0328 |
| 18 | `modelo` | 0.0319 |
| 19 | `maquina` | 0.0311 |
| 20 | `ecossistema` | 0.0302 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `informacao` | `verbal` | 0.878 | 83 |
| 2 | `inteligencia` | `artificial` | 0.864 | 156 |
| 3 | `linguas` | `indigenas` | 0.782 | 40 |
| 4 | `aberto` | `codigo` | 0.734 | 51 |
| 5 | `linguagem` | `processamento` | 0.692 | 36 |
| 6 | `maquina` | `aprendizado` | 0.628 | 44 |
| 7 | `acesso` | `disponivel` | 0.626 | 34 |
| 8 | `historica` | `investigacao` | 0.619 | 24 |
| 9 | `claudio` | `fabio` | 0.581 | 182 |
| 10 | `research` | `brasil` | 0.580 | 50 |
| 11 | `inovacao` | `ecossistema` | 0.556 | 46 |
| 12 | `passagem` | `ponto` | 0.539 | 24 |
| 13 | `novembro` | `dezembro` | 0.539 | 15 |
| 14 | `hollerith` | `tabulacao` | 0.514 | 39 |
| 15 | `comercial` | `tecnica` | 0.513 | 19 |
| 16 | `laboratorio` | `fechamento` | 0.505 | 31 |
| 17 | `gente` | `dinheiro` | 0.498 | 15 |
| 18 | `entrevistas` | `observacao` | 0.496 | 20 |
| 19 | `sistema` | `tabulacao` | 0.483 | 24 |
| 20 | `claudio` | `informacao` | 0.483 | 67 |
| 21 | `linguas` | `projeto` | 0.469 | 12 |
| 22 | `cadeia` | `translacao` | 0.467 | 12 |
| 23 | `research` | `fechamento` | 0.463 | 13 |
| 24 | `inteligencia` | `brasileiro` | 0.462 | 24 |
| 25 | `pessoas` | `vida` | 0.462 | 9 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (48 termos): rede, seguir, arranjo, ator, campo, trajetoria
- **Tópico 2** (36 termos): pesquisa, centro, fapesp, analise, financiamento, cientifico
- **Tópico 3** (28 termos): hollerith, maquina, tecnologia, tabulacao, ciencia, escala
- **Tópico 4** (17 termos): brasil, laboratorio, vinculo, pesquisador, acesso, research
- **Tópico 5** (16 termos): modelo, dado, codigo, aberto, questao, linguagem
- **Tópico 6** (13 termos): claudio, fabio, informacao, verbal, pergunta, entrevistas
- **Tópico 7** (12 termos): publico, corporacao, instituicao, universidade, infraestrutura, decisao
- **Tópico 8** (10 termos): artificial, inteligencia, empresa, ecossistema, inovacao, brasileiro

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [rede, seguir, arranjo] e **Tópico 5** [modelo, dado, codigo] — densidade ponderada de ligação = 0.2656
- Lacuna entre **Tópico 3** [hollerith, maquina, tecnologia] e **Tópico 4** [brasil, laboratorio, vinculo] — densidade ponderada de ligação = 0.2752
- Lacuna entre **Tópico 2** [pesquisa, centro, fapesp] e **Tópico 3** [hollerith, maquina, tecnologia] — densidade ponderada de ligação = 0.3264
- Lacuna entre **Tópico 4** [brasil, laboratorio, vinculo] e **Tópico 5** [modelo, dado, codigo] — densidade ponderada de ligação = 0.3272
- Lacuna entre **Tópico 1** [rede, seguir, arranjo] e **Tópico 3** [hollerith, maquina, tecnologia] — densidade ponderada de ligação = 0.3564
- Lacuna entre **Tópico 1** [rede, seguir, arranjo] e **Tópico 4** [brasil, laboratorio, vinculo] — densidade ponderada de ligação = 0.3591

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
