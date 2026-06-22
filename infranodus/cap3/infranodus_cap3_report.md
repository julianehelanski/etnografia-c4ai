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
- Tokens significativos: **17,896**
- Grafo bruto: **5358** nós · **46094** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **2579** arestas
- Tópicos detectados (Louvain): **7**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `claudio` | 796 |
| 2 | `pesquisa` | 715 |
| 3 | `rede` | 590 |
| 4 | `centro` | 531 |
| 5 | `fabio` | 498 |
| 6 | `publico` | 429 |
| 7 | `arranjo` | 400 |
| 8 | `seguir` | 393 |
| 9 | `corporacao` | 361 |
| 10 | `inteligencia` | 323 |
| 11 | `artificial` | 320 |
| 12 | `brasil` | 315 |
| 13 | `hollerith` | 301 |
| 14 | `tecnologia` | 301 |
| 15 | `ator` | 297 |
| 16 | `laboratorio` | 289 |
| 17 | `infraestrutura` | 255 |
| 18 | `ecossistema` | 253 |
| 19 | `fapesp` | 244 |
| 20 | `empresa` | 241 |
| 21 | `universidade` | 241 |
| 22 | `cientifico` | 240 |
| 23 | `instituicao` | 232 |
| 24 | `maquina` | 232 |
| 25 | `trajetoria` | 229 |
| 26 | `modelo` | 228 |
| 27 | `associacao` | 211 |
| 28 | `informacao` | 208 |
| 29 | `campo` | 206 |
| 30 | `encerramento` | 197 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `claudio` | 0.0271 |
| 2 | `pesquisa` | 0.0260 |
| 3 | `rede` | 0.0216 |
| 4 | `centro` | 0.0193 |
| 5 | `fabio` | 0.0169 |
| 6 | `publico` | 0.0160 |
| 7 | `arranjo` | 0.0150 |
| 8 | `seguir` | 0.0142 |
| 9 | `corporacao` | 0.0138 |
| 10 | `tecnologia` | 0.0122 |
| 11 | `brasil` | 0.0120 |
| 12 | `hollerith` | 0.0119 |
| 13 | `inteligencia` | 0.0114 |
| 14 | `artificial` | 0.0113 |
| 15 | `ator` | 0.0112 |
| 16 | `laboratorio` | 0.0108 |
| 17 | `infraestrutura` | 0.0103 |
| 18 | `ecossistema` | 0.0096 |
| 19 | `fapesp` | 0.0095 |
| 20 | `modelo` | 0.0094 |
| 21 | `empresa` | 0.0094 |
| 22 | `universidade` | 0.0094 |
| 23 | `cientifico` | 0.0093 |
| 24 | `maquina` | 0.0093 |
| 25 | `trajetoria` | 0.0090 |
| 26 | `instituicao` | 0.0090 |
| 27 | `associacao` | 0.0082 |
| 28 | `campo` | 0.0082 |
| 29 | `dado` | 0.0078 |
| 30 | `encerramento` | 0.0076 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `conta` | 136 | 122 | +14 |
| 2 | `pratica` | 118 | 105 | +13 |
| 3 | `processamento` | 126 | 114 | +12 |
| 4 | `estatistica` | 96 | 85 | +11 |
| 5 | `tecnica` | 62 | 53 | +9 |
| 6 | `objeto` | 145 | 136 | +9 |
| 7 | `mostra` | 170 | 161 | +9 |
| 8 | `unidos` | 92 | 84 | +8 |
| 9 | `dependencia` | 98 | 90 | +8 |
| 10 | `lado` | 101 | 93 | +8 |
| 11 | `censo` | 104 | 96 | +8 |
| 12 | `translacao` | 111 | 104 | +7 |
| 13 | `tecnociencia` | 140 | 133 | +7 |
| 14 | `linguagem` | 161 | 154 | +7 |
| 15 | `modelo` | 26 | 20 | +6 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `centro` | 0.2402 |
| 2 | `pesquisa` | 0.2203 |
| 3 | `rede` | 0.2088 |
| 4 | `claudio` | 0.1755 |
| 5 | `fabio` | 0.1256 |
| 6 | `publico` | 0.1105 |
| 7 | `tecnologia` | 0.0873 |
| 8 | `corporacao` | 0.0867 |
| 9 | `seguir` | 0.0793 |
| 10 | `ator` | 0.0686 |
| 11 | `hollerith` | 0.0657 |
| 12 | `cientifico` | 0.0532 |
| 13 | `ecossistema` | 0.0532 |
| 14 | `brasil` | 0.0490 |
| 15 | `universidade` | 0.0373 |
| 16 | `fapesp` | 0.0343 |
| 17 | `modelo` | 0.0319 |
| 18 | `inteligencia` | 0.0311 |
| 19 | `empresa` | 0.0308 |
| 20 | `trajetoria` | 0.0307 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `informacao` | `verbal` | 0.871 | 80 |
| 2 | `inteligencia` | `artificial` | 0.864 | 150 |
| 3 | `unidos` | `estados` | 0.859 | 57 |
| 4 | `porta` | `voz` | 0.858 | 53 |
| 5 | `relatorios` | `anuais` | 0.765 | 43 |
| 6 | `aberto` | `codigo` | 0.748 | 45 |
| 7 | `linguagem` | `processamento` | 0.736 | 30 |
| 8 | `historica` | `investigacao` | 0.631 | 24 |
| 9 | `elaboracao` | `base` | 0.610 | 21 |
| 10 | `passagem` | `ponto` | 0.589 | 30 |
| 11 | `claudio` | `fabio` | 0.583 | 166 |
| 12 | `acesso` | `disponivel` | 0.583 | 27 |
| 13 | `novembro` | `dezembro` | 0.565 | 23 |
| 14 | `research` | `brasil` | 0.545 | 38 |
| 15 | `inovacao` | `ecossistema` | 0.532 | 46 |
| 16 | `translacao` | `cadeias` | 0.531 | 15 |
| 17 | `cientifico` | `producao` | 0.508 | 34 |
| 18 | `mapa` | `problemas` | 0.506 | 12 |
| 19 | `gente` | `dinheiro` | 0.497 | 15 |
| 20 | `relatorios` | `elaboracao` | 0.497 | 14 |
| 21 | `relatorios` | `base` | 0.493 | 18 |
| 22 | `research` | `fechamento` | 0.488 | 12 |
| 23 | `anuais` | `base` | 0.478 | 12 |
| 24 | `hollerith` | `tabulacao` | 0.478 | 36 |
| 25 | `hollerith` | `maquina` | 0.475 | 54 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (39 termos): claudio, rede, fabio, seguir, ator, associacao
- **Tópico 2** (36 termos): hollerith, empresa, maquina, trajetoria, tabulacao, ponto
- **Tópico 3** (36 termos): publico, corporacao, tecnologia, infraestrutura, universidade, instituicao
- **Tópico 4** (30 termos): pesquisa, centro, fapesp, cientifico, partir, relatorios
- **Tópico 5** (16 termos): arranjo, brasil, laboratorio, encerramento, acesso, novembro
- **Tópico 6** (12 termos): inteligencia, artificial, ecossistema, inovacao, brasileiro, obia
- **Tópico 7** (11 termos): modelo, codigo, aberto, negocio, processamento, abertura

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 2** [hollerith, empresa, maquina] e **Tópico 4** [pesquisa, centro, fapesp] — densidade ponderada de ligação = 0.2889
- Lacuna entre **Tópico 2** [hollerith, empresa, maquina] e **Tópico 5** [arranjo, brasil, laboratorio] — densidade ponderada de ligação = 0.3542
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 3** [publico, corporacao, tecnologia] — densidade ponderada de ligação = 0.4330
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 2** [hollerith, empresa, maquina] — densidade ponderada de ligação = 0.4523
- Lacuna entre **Tópico 2** [hollerith, empresa, maquina] e **Tópico 3** [publico, corporacao, tecnologia] — densidade ponderada de ligação = 0.4630
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 4** [pesquisa, centro, fapesp] — densidade ponderada de ligação = 0.5222

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
