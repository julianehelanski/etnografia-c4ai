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
- Tokens significativos: **17,643**
- Grafo bruto: **5336** nós · **45603** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **2530** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `claudio` | 788 |
| 2 | `pesquisa` | 666 |
| 3 | `rede` | 597 |
| 4 | `centro` | 509 |
| 5 | `fabio` | 500 |
| 6 | `publico` | 416 |
| 7 | `arranjo` | 407 |
| 8 | `corporacao` | 364 |
| 9 | `seguir` | 353 |
| 10 | `brasil` | 311 |
| 11 | `inteligencia` | 305 |
| 12 | `hollerith` | 300 |
| 13 | `artificial` | 298 |
| 14 | `tecnologia` | 296 |
| 15 | `ator` | 288 |
| 16 | `laboratorio` | 266 |
| 17 | `infraestrutura` | 255 |
| 18 | `ecossistema` | 254 |
| 19 | `empresa` | 245 |
| 20 | `modelo` | 234 |
| 21 | `fapesp` | 234 |
| 22 | `maquina` | 233 |
| 23 | `instituicao` | 232 |
| 24 | `universidade` | 225 |
| 25 | `trajetoria` | 211 |
| 26 | `informacao` | 210 |
| 27 | `campo` | 206 |
| 28 | `encerramento` | 194 |
| 29 | `verbal` | 184 |
| 30 | `associacao` | 183 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `claudio` | 0.0283 |
| 2 | `pesquisa` | 0.0255 |
| 3 | `rede` | 0.0228 |
| 4 | `centro` | 0.0195 |
| 5 | `fabio` | 0.0178 |
| 6 | `publico` | 0.0162 |
| 7 | `arranjo` | 0.0158 |
| 8 | `corporacao` | 0.0146 |
| 9 | `seguir` | 0.0135 |
| 10 | `tecnologia` | 0.0125 |
| 11 | `brasil` | 0.0123 |
| 12 | `hollerith` | 0.0123 |
| 13 | `ator` | 0.0113 |
| 14 | `inteligencia` | 0.0112 |
| 15 | `artificial` | 0.0110 |
| 16 | `infraestrutura` | 0.0106 |
| 17 | `laboratorio` | 0.0104 |
| 18 | `ecossistema` | 0.0101 |
| 19 | `modelo` | 0.0100 |
| 20 | `empresa` | 0.0099 |
| 21 | `maquina` | 0.0096 |
| 22 | `fapesp` | 0.0095 |
| 23 | `instituicao` | 0.0094 |
| 24 | `universidade` | 0.0091 |
| 25 | `trajetoria` | 0.0087 |
| 26 | `campo` | 0.0085 |
| 27 | `dado` | 0.0080 |
| 28 | `encerramento` | 0.0078 |
| 29 | `informacao` | 0.0076 |
| 30 | `pergunta` | 0.0076 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `cadeia` | 97 | 83 | +14 |
| 2 | `estados` | 73 | 60 | +13 |
| 3 | `processamento` | 126 | 113 | +13 |
| 4 | `conta` | 138 | 126 | +12 |
| 5 | `descreve` | 76 | 68 | +8 |
| 6 | `translacao` | 87 | 79 | +8 |
| 7 | `censo` | 98 | 90 | +8 |
| 8 | `secao` | 104 | 96 | +8 |
| 9 | `cartoes` | 112 | 104 | +8 |
| 10 | `pratica` | 123 | 115 | +8 |
| 11 | `mostra` | 153 | 145 | +8 |
| 12 | `lado` | 95 | 88 | +7 |
| 13 | `dependencia` | 99 | 92 | +7 |
| 14 | `linguagem` | 158 | 151 | +7 |
| 15 | `expertise` | 168 | 161 | +7 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `centro` | 0.2636 |
| 2 | `rede` | 0.2295 |
| 3 | `pesquisa` | 0.2211 |
| 4 | `claudio` | 0.1746 |
| 5 | `fabio` | 0.1390 |
| 6 | `publico` | 0.1075 |
| 7 | `corporacao` | 0.0960 |
| 8 | `tecnologia` | 0.0859 |
| 9 | `hollerith` | 0.0722 |
| 10 | `ator` | 0.0583 |
| 11 | `seguir` | 0.0552 |
| 12 | `ecossistema` | 0.0543 |
| 13 | `brasil` | 0.0520 |
| 14 | `universidade` | 0.0381 |
| 15 | `cientifico` | 0.0366 |
| 16 | `fapesp` | 0.0353 |
| 17 | `arranjo` | 0.0340 |
| 18 | `inteligencia` | 0.0328 |
| 19 | `modelo` | 0.0320 |
| 20 | `empresa` | 0.0311 |

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
- **Tópico 1** (33 termos): pesquisa, centro, fapesp, cientifico, parte, pesquisador
- **Tópico 2** (32 termos): publico, corporacao, tecnologia, infraestrutura, instituicao, universidade
- **Tópico 3** (31 termos): rede, ator, analise, sigo, historica, actante
- **Tópico 4** (24 termos): claudio, fabio, seguir, informacao, campo, verbal
- **Tópico 5** (22 termos): hollerith, empresa, maquina, trajetoria, tabulacao, ponto
- **Tópico 6** (16 termos): arranjo, brasil, laboratorio, encerramento, acesso, dezembro
- **Tópico 7** (12 termos): modelo, codigo, aberto, negocio, processamento, torna
- **Tópico 8** (10 termos): inteligencia, artificial, ecossistema, inovacao, brasileiro, obia

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [pesquisa, centro, fapesp] e **Tópico 5** [hollerith, empresa, maquina] — densidade ponderada de ligação = 0.3209
- Lacuna entre **Tópico 1** [pesquisa, centro, fapesp] e **Tópico 3** [rede, ator, analise] — densidade ponderada de ligação = 0.3304
- Lacuna entre **Tópico 2** [publico, corporacao, tecnologia] e **Tópico 4** [claudio, fabio, seguir] — densidade ponderada de ligação = 0.3346
- Lacuna entre **Tópico 3** [rede, ator, analise] e **Tópico 5** [hollerith, empresa, maquina] — densidade ponderada de ligação = 0.3783
- Lacuna entre **Tópico 2** [publico, corporacao, tecnologia] e **Tópico 3** [rede, ator, analise] — densidade ponderada de ligação = 0.4073
- Lacuna entre **Tópico 4** [claudio, fabio, seguir] e **Tópico 5** [hollerith, empresa, maquina] — densidade ponderada de ligação = 0.4583

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
