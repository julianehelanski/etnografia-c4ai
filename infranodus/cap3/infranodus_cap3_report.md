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
- Tokens significativos: **16,328**
- Grafo bruto: **5091** nós · **42362** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **2290** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `pesquisa` | 668 |
| 2 | `claudio` | 582 |
| 3 | `centro` | 479 |
| 4 | `rede` | 448 |
| 5 | `publico` | 382 |
| 6 | `corporacao` | 375 |
| 7 | `fabio` | 372 |
| 8 | `seguir` | 300 |
| 9 | `inteligencia` | 293 |
| 10 | `tecnologia` | 293 |
| 11 | `hollerith` | 292 |
| 12 | `brasil` | 282 |
| 13 | `artificial` | 280 |
| 14 | `ator` | 272 |
| 15 | `arranjo` | 268 |
| 16 | `laboratorio` | 267 |
| 17 | `instituicao` | 244 |
| 18 | `modelo` | 243 |
| 19 | `cientifico` | 239 |
| 20 | `infraestrutura` | 237 |
| 21 | `fapesp` | 232 |
| 22 | `trajetoria` | 226 |
| 23 | `universidade` | 226 |
| 24 | `maquina` | 207 |
| 25 | `encerramento` | 200 |
| 26 | `ecossistema` | 189 |
| 27 | `dado` | 180 |
| 28 | `empresa` | 178 |
| 29 | `tabulacao` | 174 |
| 30 | `campo` | 173 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `pesquisa` | 0.0270 |
| 2 | `claudio` | 0.0231 |
| 3 | `centro` | 0.0195 |
| 4 | `rede` | 0.0189 |
| 5 | `corporacao` | 0.0159 |
| 6 | `publico` | 0.0158 |
| 7 | `fabio` | 0.0147 |
| 8 | `tecnologia` | 0.0129 |
| 9 | `hollerith` | 0.0127 |
| 10 | `seguir` | 0.0125 |
| 11 | `ator` | 0.0118 |
| 12 | `brasil` | 0.0118 |
| 13 | `inteligencia` | 0.0115 |
| 14 | `laboratorio` | 0.0113 |
| 15 | `arranjo` | 0.0111 |
| 16 | `artificial` | 0.0111 |
| 17 | `modelo` | 0.0108 |
| 18 | `infraestrutura` | 0.0105 |
| 19 | `instituicao` | 0.0103 |
| 20 | `cientifico` | 0.0102 |
| 21 | `trajetoria` | 0.0100 |
| 22 | `fapesp` | 0.0099 |
| 23 | `universidade` | 0.0096 |
| 24 | `maquina` | 0.0091 |
| 25 | `encerramento` | 0.0085 |
| 26 | `dado` | 0.0083 |
| 27 | `ecossistema` | 0.0082 |
| 28 | `empresa` | 0.0079 |
| 29 | `campo` | 0.0078 |
| 30 | `tabulacao` | 0.0078 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `conta` | 126 | 107 | +19 |
| 2 | `source` | 109 | 92 | +17 |
| 3 | `humano` | 79 | 64 | +15 |
| 4 | `open` | 99 | 87 | +12 |
| 5 | `objeto` | 113 | 101 | +12 |
| 6 | `descreve` | 60 | 50 | +10 |
| 7 | `analise` | 69 | 60 | +9 |
| 8 | `estatistica` | 94 | 86 | +8 |
| 9 | `translacao` | 104 | 96 | +8 |
| 10 | `dinheiro` | 107 | 99 | +8 |
| 11 | `pratica` | 121 | 114 | +7 |
| 12 | `cadeias` | 139 | 132 | +7 |
| 13 | `tecnica` | 55 | 49 | +6 |
| 14 | `estados` | 61 | 55 | +6 |
| 15 | `material` | 78 | 72 | +6 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `pesquisa` | 0.2587 |
| 2 | `centro` | 0.2358 |
| 3 | `rede` | 0.1854 |
| 4 | `claudio` | 0.1406 |
| 5 | `corporacao` | 0.1063 |
| 6 | `publico` | 0.0942 |
| 7 | `fabio` | 0.0902 |
| 8 | `tecnologia` | 0.0872 |
| 9 | `hollerith` | 0.0750 |
| 10 | `seguir` | 0.0699 |
| 11 | `ator` | 0.0692 |
| 12 | `cientifico` | 0.0569 |
| 13 | `fapesp` | 0.0466 |
| 14 | `laboratorio` | 0.0460 |
| 15 | `ciencia` | 0.0395 |
| 16 | `inteligencia` | 0.0334 |
| 17 | `instituicao` | 0.0328 |
| 18 | `trajetoria` | 0.0312 |
| 19 | `brasil` | 0.0296 |
| 20 | `infraestrutura` | 0.0296 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `open` | `source` | 0.904 | 42 |
| 2 | `porta` | `voz` | 0.881 | 47 |
| 3 | `inteligencia` | `artificial` | 0.870 | 135 |
| 4 | `informacao` | `verbal` | 0.862 | 68 |
| 5 | `unidos` | `estados` | 0.857 | 57 |
| 6 | `relatorios` | `anuais` | 0.794 | 39 |
| 7 | `aberto` | `codigo` | 0.744 | 45 |
| 8 | `informacao` | `pinhanez` | 0.739 | 45 |
| 9 | `elaboracao` | `fonte` | 0.685 | 21 |
| 10 | `verbal` | `pinhanez` | 0.660 | 30 |
| 11 | `elaboracao` | `base` | 0.656 | 21 |
| 12 | `claudio` | `fabio` | 0.623 | 138 |
| 13 | `passagem` | `ponto` | 0.616 | 33 |
| 14 | `historica` | `investigacao` | 0.611 | 24 |
| 15 | `research` | `brasil` | 0.584 | 43 |
| 16 | `relatorios` | `elaboracao` | 0.581 | 18 |
| 17 | `base` | `fonte` | 0.580 | 14 |
| 18 | `cientifico` | `producao` | 0.576 | 43 |
| 19 | `relatorios` | `base` | 0.572 | 18 |
| 20 | `research` | `fechamento` | 0.553 | 15 |
| 21 | `teoria` | `ator` | 0.548 | 27 |
| 22 | `translacao` | `cadeias` | 0.537 | 15 |
| 23 | `anuais` | `base` | 0.537 | 12 |
| 24 | `fapesp` | `convenio` | 0.522 | 20 |
| 25 | `novembro` | `dezembro` | 0.514 | 17 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (54 termos): claudio, rede, fabio, seguir, ator, campo
- **Tópico 2** (42 termos): publico, corporacao, tecnologia, infraestrutura, universidade, dado
- **Tópico 3** (21 termos): hollerith, trajetoria, maquina, empresa, tabulacao, tecnica
- **Tópico 4** (21 termos): brasil, arranjo, laboratorio, instituicao, fapesp, encerramento
- **Tópico 5** (20 termos): pesquisa, centro, cientifico, relatorios, partir, grupo
- **Tópico 6** (10 termos): modelo, codigo, aberto, negocio, gente, open
- **Tópico 7** (9 termos): inteligencia, artificial, ecossistema, inovacao, brasileiro, obia
- **Tópico 8** (3 termos): informacao, pinhanez, verbal

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 2** [publico, corporacao, tecnologia] — densidade ponderada de ligação = 0.2848
- Lacuna entre **Tópico 3** [hollerith, trajetoria, maquina] e **Tópico 5** [pesquisa, centro, cientifico] — densidade ponderada de ligação = 0.3119
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 4** [brasil, arranjo, laboratorio] — densidade ponderada de ligação = 0.3272
- Lacuna entre **Tópico 3** [hollerith, trajetoria, maquina] e **Tópico 4** [brasil, arranjo, laboratorio] — densidade ponderada de ligação = 0.3560
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 3** [hollerith, trajetoria, maquina] — densidade ponderada de ligação = 0.3660
- Lacuna entre **Tópico 2** [publico, corporacao, tecnologia] e **Tópico 3** [hollerith, trajetoria, maquina] — densidade ponderada de ligação = 0.4320

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
