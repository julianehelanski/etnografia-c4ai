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
- Tokens significativos: **15,706**
- Grafo bruto: **4512** nós · **39361** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **2300** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `pesquisa` | 796 |
| 2 | `claudio` | 622 |
| 3 | `corporacao` | 532 |
| 4 | `centro` | 508 |
| 5 | `instituicao` | 427 |
| 6 | `publico` | 421 |
| 7 | `fabio` | 384 |
| 8 | `tecnologia` | 365 |
| 9 | `inteligencia` | 357 |
| 10 | `artificial` | 353 |
| 11 | `modelo` | 344 |
| 12 | `laboratorio` | 298 |
| 13 | `brasil` | 297 |
| 14 | `ator` | 292 |
| 15 | `cientifico` | 285 |
| 16 | `arranjo` | 278 |
| 17 | `rede` | 275 |
| 18 | `infraestrutura` | 258 |
| 19 | `fapesp` | 240 |
| 20 | `ecossistema` | 238 |
| 21 | `informacao` | 231 |
| 22 | `inovacao` | 227 |
| 23 | `recursos` | 224 |
| 24 | `seguir` | 213 |
| 25 | `universidade` | 210 |
| 26 | `encerramento` | 205 |
| 27 | `pinhanez` | 204 |
| 28 | `verbal` | 200 |
| 29 | `pesquisador` | 187 |
| 30 | `etnografia` | 182 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `pesquisa` | 0.0308 |
| 2 | `claudio` | 0.0234 |
| 3 | `corporacao` | 0.0218 |
| 4 | `centro` | 0.0194 |
| 5 | `publico` | 0.0167 |
| 6 | `instituicao` | 0.0166 |
| 7 | `tecnologia` | 0.0154 |
| 8 | `modelo` | 0.0147 |
| 9 | `fabio` | 0.0145 |
| 10 | `inteligencia` | 0.0130 |
| 11 | `artificial` | 0.0129 |
| 12 | `ator` | 0.0121 |
| 13 | `brasil` | 0.0120 |
| 14 | `laboratorio` | 0.0119 |
| 15 | `cientifico` | 0.0116 |
| 16 | `rede` | 0.0112 |
| 17 | `arranjo` | 0.0110 |
| 18 | `infraestrutura` | 0.0108 |
| 19 | `fapesp` | 0.0098 |
| 20 | `recursos` | 0.0098 |
| 21 | `ecossistema` | 0.0097 |
| 22 | `inovacao` | 0.0093 |
| 23 | `informacao` | 0.0089 |
| 24 | `universidade` | 0.0087 |
| 25 | `seguir` | 0.0087 |
| 26 | `encerramento` | 0.0084 |
| 27 | `pesquisador` | 0.0082 |
| 28 | `hollerith` | 0.0081 |
| 29 | `pinhanez` | 0.0079 |
| 30 | `etnografia` | 0.0079 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `unidos` | 131 | 104 | +27 |
| 2 | `estados` | 125 | 100 | +25 |
| 3 | `estruturais` | 128 | 113 | +15 |
| 4 | `tecnociencia` | 79 | 65 | +14 |
| 5 | `translacao` | 129 | 117 | +12 |
| 6 | `ponto` | 64 | 53 | +11 |
| 7 | `codigo` | 78 | 68 | +10 |
| 8 | `assimetrias` | 142 | 132 | +10 |
| 9 | `maquina` | 80 | 71 | +9 |
| 10 | `capacidade` | 124 | 115 | +9 |
| 11 | `aberto` | 77 | 69 | +8 |
| 12 | `passagem` | 154 | 146 | +8 |
| 13 | `latour` | 49 | 42 | +7 |
| 14 | `estrategias` | 98 | 91 | +7 |
| 15 | `sistema` | 50 | 44 | +6 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `pesquisa` | 0.2890 |
| 2 | `centro` | 0.2175 |
| 3 | `corporacao` | 0.1442 |
| 4 | `claudio` | 0.1386 |
| 5 | `instituicao` | 0.1193 |
| 6 | `tecnologia` | 0.1096 |
| 7 | `publico` | 0.0839 |
| 8 | `modelo` | 0.0641 |
| 9 | `inteligencia` | 0.0566 |
| 10 | `cientifico` | 0.0563 |
| 11 | `fabio` | 0.0561 |
| 12 | `rede` | 0.0546 |
| 13 | `ator` | 0.0490 |
| 14 | `laboratorio` | 0.0432 |
| 15 | `recursos` | 0.0431 |
| 16 | `brasil` | 0.0391 |
| 17 | `infraestrutura` | 0.0382 |
| 18 | `pinhanez` | 0.0321 |
| 19 | `seguir` | 0.0264 |
| 20 | `fapesp` | 0.0262 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `unidos` | `estados` | 0.890 | 48 |
| 2 | `open` | `source` | 0.890 | 51 |
| 3 | `porta` | `voz` | 0.880 | 50 |
| 4 | `inteligencia` | `artificial` | 0.858 | 153 |
| 5 | `informacao` | `verbal` | 0.853 | 81 |
| 6 | `aberto` | `codigo` | 0.796 | 45 |
| 7 | `relatorios` | `anuais` | 0.783 | 44 |
| 8 | `informacao` | `pinhanez` | 0.718 | 57 |
| 9 | `ponto` | `passagem` | 0.715 | 34 |
| 10 | `criar` | `demanda` | 0.714 | 28 |
| 11 | `elaboracao` | `base` | 0.663 | 21 |
| 12 | `servicos` | `demanda` | 0.654 | 33 |
| 13 | `verbal` | `pinhanez` | 0.650 | 40 |
| 14 | `estruturais` | `assimetrias` | 0.635 | 18 |
| 15 | `elaboracao` | `relatorios` | 0.590 | 20 |
| 16 | `torna` | `visivel` | 0.590 | 21 |
| 17 | `fabio` | `claudio` | 0.589 | 139 |
| 18 | `tabulacao` | `sistema` | 0.584 | 30 |
| 19 | `brasil` | `research` | 0.581 | 42 |
| 20 | `brasileiro` | `contexto` | 0.572 | 18 |
| 21 | `relatorios` | `base` | 0.565 | 18 |
| 22 | `partir` | `elaboracao` | 0.559 | 18 |
| 23 | `multiplicacao` | `instituicao` | 0.558 | 54 |
| 24 | `investigacao` | `historica` | 0.533 | 15 |
| 25 | `hollerith` | `tabulacao` | 0.533 | 29 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (38 termos): claudio, fabio, ator, rede, seguir, etnografia
- **Tópico 2** (35 termos): corporacao, publico, infraestrutura, fapesp, recursos, universidade
- **Tópico 3** (29 termos): pesquisa, centro, instituicao, laboratorio, brasil, arranjo
- **Tópico 4** (27 termos): tecnologia, hollerith, tabulacao, ciencia, latour, sistema
- **Tópico 5** (20 termos): inteligencia, artificial, ecossistema, inovacao, brasileiro, ecossistemas
- **Tópico 6** (14 termos): modelo, negocio, open, source, gente, aberto
- **Tópico 7** (11 termos): cientifico, relatorios, producao, registros, anuais, partir
- **Tópico 8** (6 termos): informacao, pinhanez, verbal, estados, unidos, projeto

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 4** [tecnologia, hollerith, tabulacao] e **Tópico 5** [inteligencia, artificial, ecossistema] — densidade ponderada de ligação = 0.2944
- Lacuna entre **Tópico 1** [claudio, fabio, ator] e **Tópico 5** [inteligencia, artificial, ecossistema] — densidade ponderada de ligação = 0.3329
- Lacuna entre **Tópico 2** [corporacao, publico, infraestrutura] e **Tópico 5** [inteligencia, artificial, ecossistema] — densidade ponderada de ligação = 0.3443
- Lacuna entre **Tópico 1** [claudio, fabio, ator] e **Tópico 4** [tecnologia, hollerith, tabulacao] — densidade ponderada de ligação = 0.3470
- Lacuna entre **Tópico 1** [claudio, fabio, ator] e **Tópico 2** [corporacao, publico, infraestrutura] — densidade ponderada de ligação = 0.3699
- Lacuna entre **Tópico 2** [corporacao, publico, infraestrutura] e **Tópico 4** [tecnologia, hollerith, tabulacao] — densidade ponderada de ligação = 0.4095

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
