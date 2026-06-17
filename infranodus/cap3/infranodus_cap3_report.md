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
- Tokens significativos: **17,474**
- Grafo bruto: **5240** nós · **44940** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **2377** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `pesquisa` | 705 |
| 2 | `claudio` | 610 |
| 3 | `centro` | 503 |
| 4 | `publico` | 438 |
| 5 | `corporacao` | 432 |
| 6 | `rede` | 426 |
| 7 | `fabio` | 376 |
| 8 | `instituicao` | 326 |
| 9 | `arranjo` | 320 |
| 10 | `inteligencia` | 319 |
| 11 | `seguir` | 312 |
| 12 | `tecnologia` | 311 |
| 13 | `artificial` | 309 |
| 14 | `infraestrutura` | 288 |
| 15 | `hollerith` | 278 |
| 16 | `modelo` | 275 |
| 17 | `laboratorio` | 273 |
| 18 | `ator` | 270 |
| 19 | `brasil` | 259 |
| 20 | `universidade` | 252 |
| 21 | `fapesp` | 240 |
| 22 | `trajetoria` | 238 |
| 23 | `cientifico` | 237 |
| 24 | `encerramento` | 199 |
| 25 | `informacao` | 196 |
| 26 | `maquina` | 195 |
| 27 | `ecossistema` | 190 |
| 28 | `parte` | 186 |
| 29 | `porta` | 183 |
| 30 | `etnografia` | 181 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `pesquisa` | 0.0275 |
| 2 | `claudio` | 0.0229 |
| 3 | `centro` | 0.0195 |
| 4 | `corporacao` | 0.0174 |
| 5 | `publico` | 0.0170 |
| 6 | `rede` | 0.0169 |
| 7 | `fabio` | 0.0141 |
| 8 | `instituicao` | 0.0131 |
| 9 | `tecnologia` | 0.0130 |
| 10 | `arranjo` | 0.0125 |
| 11 | `seguir` | 0.0124 |
| 12 | `infraestrutura` | 0.0121 |
| 13 | `inteligencia` | 0.0120 |
| 14 | `hollerith` | 0.0118 |
| 15 | `artificial` | 0.0117 |
| 16 | `modelo` | 0.0117 |
| 17 | `laboratorio` | 0.0111 |
| 18 | `ator` | 0.0109 |
| 19 | `brasil` | 0.0106 |
| 20 | `universidade` | 0.0103 |
| 21 | `trajetoria` | 0.0102 |
| 22 | `fapesp` | 0.0098 |
| 23 | `cientifico` | 0.0097 |
| 24 | `maquina` | 0.0085 |
| 25 | `encerramento` | 0.0081 |
| 26 | `parte` | 0.0080 |
| 27 | `ecossistema` | 0.0080 |
| 28 | `informacao` | 0.0078 |
| 29 | `etnografia` | 0.0077 |
| 30 | `relatorios` | 0.0075 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `conta` | 111 | 82 | +29 |
| 2 | `estados` | 88 | 68 | +20 |
| 3 | `estatistica` | 102 | 83 | +19 |
| 4 | `unidos` | 114 | 101 | +13 |
| 5 | `tecnociencia` | 131 | 119 | +12 |
| 6 | `escala` | 86 | 75 | +11 |
| 7 | `pratica` | 127 | 117 | +10 |
| 8 | `vida` | 151 | 141 | +10 |
| 9 | `computacional` | 89 | 81 | +8 |
| 10 | `translacao` | 117 | 109 | +8 |
| 11 | `objeto` | 126 | 118 | +8 |
| 12 | `gesto` | 154 | 146 | +8 |
| 13 | `lado` | 107 | 100 | +7 |
| 14 | `conjunto` | 160 | 153 | +7 |
| 15 | `comercial` | 85 | 79 | +6 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `pesquisa` | 0.2546 |
| 2 | `centro` | 0.2015 |
| 3 | `rede` | 0.1690 |
| 4 | `corporacao` | 0.1590 |
| 5 | `claudio` | 0.1452 |
| 6 | `publico` | 0.1212 |
| 7 | `tecnologia` | 0.0848 |
| 8 | `fabio` | 0.0782 |
| 9 | `ator` | 0.0655 |
| 10 | `hollerith` | 0.0642 |
| 11 | `infraestrutura` | 0.0631 |
| 12 | `seguir` | 0.0569 |
| 13 | `trajetoria` | 0.0563 |
| 14 | `instituicao` | 0.0498 |
| 15 | `cientifico` | 0.0414 |
| 16 | `universidade` | 0.0402 |
| 17 | `arranjo` | 0.0381 |
| 18 | `laboratorio` | 0.0370 |
| 19 | `inteligencia` | 0.0349 |
| 20 | `fapesp` | 0.0313 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `voz` | `porta` | 0.881 | 68 |
| 2 | `artificial` | `inteligencia` | 0.871 | 144 |
| 3 | `estados` | `unidos` | 0.857 | 51 |
| 4 | `informacao` | `verbal` | 0.855 | 72 |
| 5 | `relatorios` | `anuais` | 0.786 | 41 |
| 6 | `aberto` | `codigo` | 0.745 | 48 |
| 7 | `informacao` | `pinhanez` | 0.731 | 51 |
| 8 | `pinhanez` | `verbal` | 0.670 | 36 |
| 9 | `elaboracao` | `base` | 0.660 | 21 |
| 10 | `fabio` | `claudio` | 0.616 | 138 |
| 11 | `historica` | `investigacao` | 0.615 | 24 |
| 12 | `ponto` | `passagem` | 0.592 | 33 |
| 13 | `relatorios` | `elaboracao` | 0.588 | 20 |
| 14 | `relatorios` | `base` | 0.572 | 18 |
| 15 | `cientifico` | `producao` | 0.572 | 43 |
| 16 | `disponivel` | `acesso` | 0.553 | 21 |
| 17 | `research` | `brasil` | 0.550 | 33 |
| 18 | `base` | `anuais` | 0.540 | 12 |
| 19 | `novembro` | `dezembro` | 0.517 | 18 |
| 20 | `dezembro` | `encerramento` | 0.517 | 34 |
| 21 | `comercial` | `tecnica` | 0.514 | 16 |
| 22 | `cadeias` | `translacao` | 0.513 | 15 |
| 23 | `instituicao` | `multiplicacao` | 0.508 | 30 |
| 24 | `foucault` | `estatistica` | 0.506 | 14 |
| 25 | `funcionamento` | `condicao` | 0.500 | 15 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (38 termos): claudio, rede, fabio, seguir, ator, porta
- **Tópico 2** (36 termos): publico, corporacao, instituicao, tecnologia, infraestrutura, universidade
- **Tópico 3** (29 termos): pesquisa, centro, cientifico, etnografia, relatorios, pergunta
- **Tópico 4** (26 termos): hollerith, trajetoria, maquina, tabulacao, empresa, historica
- **Tópico 5** (18 termos): arranjo, laboratorio, brasil, encerramento, parte, dezembro
- **Tópico 6** (13 termos): inteligencia, artificial, ecossistema, inovacao, acesso, brasileiro
- **Tópico 7** (12 termos): fapesp, informacao, verbal, pinhanez, gente, acordo
- **Tópico 8** (8 termos): modelo, dado, codigo, aberto, negocio, conhecimento

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 4** [hollerith, trajetoria, maquina] e **Tópico 5** [arranjo, laboratorio, brasil] — densidade ponderada de ligação = 0.2842
- Lacuna entre **Tópico 3** [pesquisa, centro, cientifico] e **Tópico 4** [hollerith, trajetoria, maquina] — densidade ponderada de ligação = 0.3408
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 2** [publico, corporacao, instituicao] — densidade ponderada de ligação = 0.3582
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 4** [hollerith, trajetoria, maquina] — densidade ponderada de ligação = 0.3634
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 5** [arranjo, laboratorio, brasil] — densidade ponderada de ligação = 0.3860
- Lacuna entre **Tópico 2** [publico, corporacao, instituicao] e **Tópico 4** [hollerith, trajetoria, maquina] — densidade ponderada de ligação = 0.4626

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
