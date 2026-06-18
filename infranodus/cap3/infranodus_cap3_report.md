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
- Grafo bruto: **5237** nós · **44898** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **2375** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `pesquisa` | 700 |
| 2 | `claudio` | 624 |
| 3 | `centro` | 516 |
| 4 | `rede` | 443 |
| 5 | `corporacao` | 434 |
| 6 | `publico` | 431 |
| 7 | `fabio` | 403 |
| 8 | `seguir` | 318 |
| 9 | `inteligencia` | 311 |
| 10 | `instituicao` | 310 |
| 11 | `tecnologia` | 301 |
| 12 | `artificial` | 301 |
| 13 | `arranjo` | 299 |
| 14 | `hollerith` | 284 |
| 15 | `infraestrutura` | 282 |
| 16 | `laboratorio` | 273 |
| 17 | `ator` | 270 |
| 18 | `modelo` | 269 |
| 19 | `brasil` | 268 |
| 20 | `universidade` | 257 |
| 21 | `trajetoria` | 245 |
| 22 | `fapesp` | 224 |
| 23 | `cientifico` | 222 |
| 24 | `encerramento` | 198 |
| 25 | `maquina` | 196 |
| 26 | `ecossistema` | 187 |
| 27 | `ponto` | 187 |
| 28 | `tabulacao` | 184 |
| 29 | `dado` | 183 |
| 30 | `informacao` | 183 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `pesquisa` | 0.0275 |
| 2 | `claudio` | 0.0238 |
| 3 | `centro` | 0.0203 |
| 4 | `rede` | 0.0178 |
| 5 | `corporacao` | 0.0177 |
| 6 | `publico` | 0.0169 |
| 7 | `fabio` | 0.0152 |
| 8 | `tecnologia` | 0.0127 |
| 9 | `seguir` | 0.0126 |
| 10 | `instituicao` | 0.0125 |
| 11 | `hollerith` | 0.0120 |
| 12 | `infraestrutura` | 0.0118 |
| 13 | `arranjo` | 0.0118 |
| 14 | `inteligencia` | 0.0118 |
| 15 | `modelo` | 0.0116 |
| 16 | `artificial` | 0.0115 |
| 17 | `laboratorio` | 0.0111 |
| 18 | `ator` | 0.0111 |
| 19 | `brasil` | 0.0110 |
| 20 | `universidade` | 0.0106 |
| 21 | `trajetoria` | 0.0104 |
| 22 | `fapesp` | 0.0092 |
| 23 | `cientifico` | 0.0092 |
| 24 | `maquina` | 0.0085 |
| 25 | `encerramento` | 0.0082 |
| 26 | `ponto` | 0.0082 |
| 27 | `dado` | 0.0081 |
| 28 | `tabulacao` | 0.0080 |
| 29 | `etnografia` | 0.0079 |
| 30 | `ecossistema` | 0.0078 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `conta` | 133 | 109 | +24 |
| 2 | `source` | 111 | 92 | +19 |
| 3 | `open` | 92 | 78 | +14 |
| 4 | `pratica` | 119 | 107 | +12 |
| 5 | `translacao` | 113 | 104 | +9 |
| 6 | `cadeias` | 117 | 108 | +9 |
| 7 | `dinheiro` | 109 | 102 | +7 |
| 8 | `estados` | 71 | 65 | +6 |
| 9 | `unidos` | 91 | 85 | +6 |
| 10 | `objeto` | 135 | 129 | +6 |
| 11 | `latour` | 55 | 50 | +5 |
| 12 | `censo` | 86 | 81 | +5 |
| 13 | `cadeia` | 94 | 89 | +5 |
| 14 | `computacional` | 98 | 93 | +5 |
| 15 | `lado` | 130 | 125 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `pesquisa` | 0.2329 |
| 2 | `centro` | 0.2114 |
| 3 | `rede` | 0.1772 |
| 4 | `claudio` | 0.1675 |
| 5 | `corporacao` | 0.1498 |
| 6 | `publico` | 0.1338 |
| 7 | `fabio` | 0.1026 |
| 8 | `tecnologia` | 0.0795 |
| 9 | `seguir` | 0.0739 |
| 10 | `ator` | 0.0686 |
| 11 | `hollerith` | 0.0668 |
| 12 | `trajetoria` | 0.0483 |
| 13 | `infraestrutura` | 0.0478 |
| 14 | `universidade` | 0.0458 |
| 15 | `instituicao` | 0.0411 |
| 16 | `arranjo` | 0.0378 |
| 17 | `laboratorio` | 0.0371 |
| 18 | `cientifico` | 0.0358 |
| 19 | `fapesp` | 0.0326 |
| 20 | `inteligencia` | 0.0323 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `open` | `source` | 0.893 | 42 |
| 2 | `porta` | `voz` | 0.881 | 65 |
| 3 | `inteligencia` | `artificial` | 0.870 | 144 |
| 4 | `informacao` | `verbal` | 0.864 | 77 |
| 5 | `unidos` | `estados` | 0.858 | 54 |
| 6 | `aberto` | `codigo` | 0.752 | 48 |
| 7 | `informacao` | `pinhanez` | 0.735 | 48 |
| 8 | `elaboracao` | `base` | 0.668 | 21 |
| 9 | `verbal` | `pinhanez` | 0.653 | 32 |
| 10 | `claudio` | `fabio` | 0.623 | 150 |
| 11 | `historica` | `investigacao` | 0.614 | 24 |
| 12 | `relatorios` | `elaboracao` | 0.584 | 18 |
| 13 | `relatorios` | `base` | 0.584 | 18 |
| 14 | `passagem` | `ponto` | 0.584 | 33 |
| 15 | `cientifico` | `producao` | 0.571 | 43 |
| 16 | `research` | `brasil` | 0.558 | 35 |
| 17 | `novembro` | `dezembro` | 0.525 | 19 |
| 18 | `research` | `fechamento` | 0.515 | 12 |
| 19 | `translacao` | `cadeias` | 0.507 | 15 |
| 20 | `hollerith` | `tabulacao` | 0.498 | 39 |
| 21 | `funcionamento` | `condicao` | 0.494 | 15 |
| 22 | `dezembro` | `encerramento` | 0.490 | 30 |
| 23 | `instituicao` | `multiplicacao` | 0.489 | 27 |
| 24 | `comercial` | `tecnica` | 0.489 | 13 |
| 25 | `gente` | `dinheiro` | 0.486 | 15 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (49 termos): claudio, rede, fabio, seguir, ator, ponto
- **Tópico 2** (37 termos): corporacao, publico, instituicao, tecnologia, infraestrutura, universidade
- **Tópico 3** (23 termos): hollerith, trajetoria, maquina, tabulacao, empresa, historia
- **Tópico 4** (21 termos): pesquisa, centro, cientifico, pesquisador, partir, producao
- **Tópico 5** (17 termos): arranjo, laboratorio, brasil, encerramento, parte, dezembro
- **Tópico 6** (14 termos): fapesp, informacao, verbal, pinhanez, recursos, financiamento
- **Tópico 7** (11 termos): inteligencia, artificial, ecossistema, inovacao, brasileiro, valor
- **Tópico 8** (8 termos): modelo, codigo, aberto, negocio, open, source

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 3** [hollerith, trajetoria, maquina] e **Tópico 5** [arranjo, laboratorio, brasil] — densidade ponderada de ligação = 0.3018
- Lacuna entre **Tópico 3** [hollerith, trajetoria, maquina] e **Tópico 4** [pesquisa, centro, cientifico] — densidade ponderada de ligação = 0.3043
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 2** [corporacao, publico, instituicao] — densidade ponderada de ligação = 0.3591
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 3** [hollerith, trajetoria, maquina] — densidade ponderada de ligação = 0.3691
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 5** [arranjo, laboratorio, brasil] — densidade ponderada de ligação = 0.4226
- Lacuna entre **Tópico 2** [corporacao, publico, instituicao] e **Tópico 3** [hollerith, trajetoria, maquina] — densidade ponderada de ligação = 0.4595

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
