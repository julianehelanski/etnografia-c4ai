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
- Tokens significativos: **17,359**
- Grafo bruto: **5227** nós · **44846** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **2529** arestas
- Tópicos detectados (Louvain): **7**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `claudio` | 774 |
| 2 | `pesquisa` | 707 |
| 3 | `rede` | 547 |
| 4 | `centro` | 503 |
| 5 | `fabio` | 495 |
| 6 | `publico` | 436 |
| 7 | `arranjo` | 388 |
| 8 | `corporacao` | 387 |
| 9 | `seguir` | 378 |
| 10 | `inteligencia` | 317 |
| 11 | `brasil` | 302 |
| 12 | `artificial` | 302 |
| 13 | `hollerith` | 293 |
| 14 | `tecnologia` | 293 |
| 15 | `laboratorio` | 281 |
| 16 | `ator` | 270 |
| 17 | `infraestrutura` | 256 |
| 18 | `cientifico` | 253 |
| 19 | `fapesp` | 249 |
| 20 | `ecossistema` | 236 |
| 21 | `modelo` | 235 |
| 22 | `instituicao` | 235 |
| 23 | `universidade` | 227 |
| 24 | `trajetoria` | 219 |
| 25 | `maquina` | 219 |
| 26 | `campo` | 217 |
| 27 | `empresa` | 217 |
| 28 | `informacao` | 215 |
| 29 | `encerramento` | 215 |
| 30 | `dado` | 189 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `claudio` | 0.0270 |
| 2 | `pesquisa` | 0.0261 |
| 3 | `rede` | 0.0207 |
| 4 | `centro` | 0.0187 |
| 5 | `fabio` | 0.0172 |
| 6 | `publico` | 0.0164 |
| 7 | `corporacao` | 0.0149 |
| 8 | `arranjo` | 0.0148 |
| 9 | `seguir` | 0.0141 |
| 10 | `tecnologia` | 0.0118 |
| 11 | `hollerith` | 0.0117 |
| 12 | `brasil` | 0.0116 |
| 13 | `inteligencia` | 0.0114 |
| 14 | `artificial` | 0.0109 |
| 15 | `laboratorio` | 0.0107 |
| 16 | `ator` | 0.0105 |
| 17 | `infraestrutura` | 0.0104 |
| 18 | `cientifico` | 0.0100 |
| 19 | `modelo` | 0.0098 |
| 20 | `fapesp` | 0.0097 |
| 21 | `ecossistema` | 0.0092 |
| 22 | `instituicao` | 0.0091 |
| 23 | `universidade` | 0.0089 |
| 24 | `maquina` | 0.0088 |
| 25 | `trajetoria` | 0.0088 |
| 26 | `campo` | 0.0088 |
| 27 | `empresa` | 0.0087 |
| 28 | `encerramento` | 0.0084 |
| 29 | `dado` | 0.0082 |
| 30 | `informacao` | 0.0076 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `conta` | 156 | 134 | +22 |
| 2 | `linguagem` | 83 | 65 | +18 |
| 3 | `natural` | 111 | 96 | +15 |
| 4 | `estados` | 80 | 68 | +12 |
| 5 | `processamento` | 92 | 82 | +10 |
| 6 | `censo` | 110 | 101 | +9 |
| 7 | `pratica` | 115 | 106 | +9 |
| 8 | `tecnica` | 70 | 62 | +8 |
| 9 | `projetos` | 127 | 119 | +8 |
| 10 | `lado` | 146 | 138 | +8 |
| 11 | `fontes` | 147 | 139 | +8 |
| 12 | `codigo` | 61 | 54 | +7 |
| 13 | `tecnociencia` | 116 | 109 | +7 |
| 14 | `mostra` | 168 | 161 | +7 |
| 15 | `descreve` | 66 | 60 | +6 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `pesquisa` | 0.2259 |
| 2 | `centro` | 0.2216 |
| 3 | `rede` | 0.2144 |
| 4 | `claudio` | 0.1717 |
| 5 | `fabio` | 0.1289 |
| 6 | `publico` | 0.1073 |
| 7 | `corporacao` | 0.0869 |
| 8 | `seguir` | 0.0721 |
| 9 | `ator` | 0.0692 |
| 10 | `tecnologia` | 0.0688 |
| 11 | `cientifico` | 0.0664 |
| 12 | `hollerith` | 0.0649 |
| 13 | `brasil` | 0.0438 |
| 14 | `modelo` | 0.0432 |
| 15 | `arranjo` | 0.0389 |
| 16 | `ecossistema` | 0.0344 |
| 17 | `laboratorio` | 0.0327 |
| 18 | `dado` | 0.0324 |
| 19 | `infraestrutura` | 0.0321 |
| 20 | `inteligencia` | 0.0311 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `inteligencia` | `artificial` | 0.870 | 147 |
| 2 | `informacao` | `verbal` | 0.864 | 80 |
| 3 | `unidos` | `estados` | 0.859 | 57 |
| 4 | `porta` | `voz` | 0.858 | 53 |
| 5 | `linguagem` | `natural` | 0.823 | 42 |
| 6 | `relatorios` | `anuais` | 0.772 | 40 |
| 7 | `aberto` | `codigo` | 0.747 | 45 |
| 8 | `linguagem` | `processamento` | 0.727 | 30 |
| 9 | `processamento` | `natural` | 0.656 | 20 |
| 10 | `historica` | `investigacao` | 0.621 | 24 |
| 11 | `acesso` | `disponivel` | 0.615 | 30 |
| 12 | `elaboracao` | `base` | 0.599 | 21 |
| 13 | `passagem` | `ponto` | 0.595 | 30 |
| 14 | `claudio` | `fabio` | 0.583 | 162 |
| 15 | `novembro` | `dezembro` | 0.550 | 21 |
| 16 | `research` | `brasil` | 0.545 | 38 |
| 17 | `translacao` | `cadeias` | 0.543 | 15 |
| 18 | `relatorios` | `elaboracao` | 0.531 | 16 |
| 19 | `cientifico` | `producao` | 0.509 | 37 |
| 20 | `relatorios` | `base` | 0.507 | 18 |
| 21 | `gente` | `dinheiro` | 0.502 | 15 |
| 22 | `inovacao` | `ecossistema` | 0.500 | 41 |
| 23 | `mapa` | `problemas` | 0.499 | 12 |
| 24 | `hollerith` | `maquina` | 0.490 | 54 |
| 25 | `comercial` | `tecnica` | 0.488 | 13 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (42 termos): claudio, rede, fabio, seguir, ator, informacao
- **Tópico 2** (41 termos): publico, arranjo, corporacao, brasil, tecnologia, laboratorio
- **Tópico 3** (30 termos): hollerith, trajetoria, maquina, empresa, tabulacao, ponto
- **Tópico 4** (27 termos): pesquisa, centro, cientifico, campo, relatorios, pergunta
- **Tópico 5** (16 termos): modelo, dado, codigo, aberto, linguagem, negocio
- **Tópico 6** (13 termos): inteligencia, artificial, ecossistema, inovacao, brasileiro, obia
- **Tópico 7** (11 termos): fapesp, recursos, financiamento, gente, dinheiro, acordo

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 5** [modelo, dado, codigo] — densidade ponderada de ligação = 0.2500
- Lacuna entre **Tópico 4** [pesquisa, centro, cientifico] e **Tópico 5** [modelo, dado, codigo] — densidade ponderada de ligação = 0.3032
- Lacuna entre **Tópico 3** [hollerith, trajetoria, maquina] e **Tópico 5** [modelo, dado, codigo] — densidade ponderada de ligação = 0.3208
- Lacuna entre **Tópico 2** [publico, arranjo, corporacao] e **Tópico 5** [modelo, dado, codigo] — densidade ponderada de ligação = 0.3582
- Lacuna entre **Tópico 3** [hollerith, trajetoria, maquina] e **Tópico 4** [pesquisa, centro, cientifico] — densidade ponderada de ligação = 0.3691
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 3** [hollerith, trajetoria, maquina] — densidade ponderada de ligação = 0.3825

## 9. Leitura interpretativa
_Leitura interpretativa ainda não escrita para este capítulo. Crie `interpretation_cap3.md` ao lado dos outputs para que o conteúdo seja embutido aqui automaticamente._

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
