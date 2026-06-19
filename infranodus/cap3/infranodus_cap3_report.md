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
- Tokens significativos: **16,735**
- Grafo bruto: **5155** nós · **43443** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **2408** arestas
- Tópicos detectados (Louvain): **7**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `claudio` | 752 |
| 2 | `pesquisa` | 685 |
| 3 | `centro` | 501 |
| 4 | `rede` | 449 |
| 5 | `fabio` | 434 |
| 6 | `publico` | 417 |
| 7 | `corporacao` | 394 |
| 8 | `seguir` | 362 |
| 9 | `inteligencia` | 312 |
| 10 | `brasil` | 303 |
| 11 | `artificial` | 301 |
| 12 | `arranjo` | 299 |
| 13 | `tecnologia` | 292 |
| 14 | `hollerith` | 291 |
| 15 | `laboratorio` | 277 |
| 16 | `ator` | 268 |
| 17 | `cientifico` | 258 |
| 18 | `infraestrutura` | 240 |
| 19 | `instituicao` | 238 |
| 20 | `modelo` | 236 |
| 21 | `trajetoria` | 235 |
| 22 | `universidade` | 230 |
| 23 | `ecossistema` | 217 |
| 24 | `maquina` | 215 |
| 25 | `encerramento` | 215 |
| 26 | `fapesp` | 211 |
| 27 | `empresa` | 203 |
| 28 | `informacao` | 200 |
| 29 | `verbal` | 179 |
| 30 | `dado` | 176 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `claudio` | 0.0276 |
| 2 | `pesquisa` | 0.0265 |
| 3 | `centro` | 0.0195 |
| 4 | `rede` | 0.0179 |
| 5 | `publico` | 0.0165 |
| 6 | `corporacao` | 0.0159 |
| 7 | `fabio` | 0.0158 |
| 8 | `seguir` | 0.0142 |
| 9 | `tecnologia` | 0.0124 |
| 10 | `brasil` | 0.0122 |
| 11 | `hollerith` | 0.0121 |
| 12 | `arranjo` | 0.0119 |
| 13 | `inteligencia` | 0.0117 |
| 14 | `artificial` | 0.0113 |
| 15 | `laboratorio` | 0.0111 |
| 16 | `ator` | 0.0109 |
| 17 | `cientifico` | 0.0107 |
| 18 | `infraestrutura` | 0.0102 |
| 19 | `modelo` | 0.0101 |
| 20 | `trajetoria` | 0.0099 |
| 21 | `instituicao` | 0.0096 |
| 22 | `universidade` | 0.0094 |
| 23 | `maquina` | 0.0090 |
| 24 | `ecossistema` | 0.0088 |
| 25 | `encerramento` | 0.0087 |
| 26 | `fapesp` | 0.0087 |
| 27 | `empresa` | 0.0086 |
| 28 | `dado` | 0.0079 |
| 29 | `campo` | 0.0076 |
| 30 | `tabulacao` | 0.0075 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `estatistica` | 109 | 89 | +20 |
| 2 | `conta` | 127 | 107 | +20 |
| 3 | `open` | 110 | 97 | +13 |
| 4 | `computacional` | 140 | 128 | +12 |
| 5 | `source` | 102 | 91 | +11 |
| 6 | `condicao` | 136 | 126 | +10 |
| 7 | `objeto` | 141 | 131 | +10 |
| 8 | `humano` | 73 | 64 | +9 |
| 9 | `deixa` | 84 | 76 | +8 |
| 10 | `censo` | 107 | 99 | +8 |
| 11 | `cadeia` | 113 | 105 | +8 |
| 12 | `lado` | 132 | 124 | +8 |
| 13 | `estados` | 64 | 57 | +7 |
| 14 | `analise` | 78 | 71 | +7 |
| 15 | `unidos` | 86 | 79 | +7 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `pesquisa` | 0.2552 |
| 2 | `centro` | 0.2232 |
| 3 | `rede` | 0.1590 |
| 4 | `claudio` | 0.1566 |
| 5 | `publico` | 0.1160 |
| 6 | `corporacao` | 0.1039 |
| 7 | `seguir` | 0.0871 |
| 8 | `tecnologia` | 0.0832 |
| 9 | `fabio` | 0.0805 |
| 10 | `hollerith` | 0.0704 |
| 11 | `ator` | 0.0639 |
| 12 | `cientifico` | 0.0636 |
| 13 | `brasil` | 0.0629 |
| 14 | `laboratorio` | 0.0345 |
| 15 | `ecossistema` | 0.0325 |
| 16 | `inteligencia` | 0.0317 |
| 17 | `universidade` | 0.0303 |
| 18 | `ciencia` | 0.0297 |
| 19 | `trajetoria` | 0.0293 |
| 20 | `fapesp` | 0.0289 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `open` | `source` | 0.904 | 42 |
| 2 | `informacao` | `verbal` | 0.870 | 77 |
| 3 | `inteligencia` | `artificial` | 0.869 | 144 |
| 4 | `unidos` | `estados` | 0.858 | 57 |
| 5 | `porta` | `voz` | 0.855 | 47 |
| 6 | `relatorios` | `anuais` | 0.780 | 38 |
| 7 | `aberto` | `codigo` | 0.745 | 45 |
| 8 | `elaboracao` | `fonte` | 0.696 | 21 |
| 9 | `elaboracao` | `base` | 0.643 | 21 |
| 10 | `acesso` | `disponivel` | 0.635 | 30 |
| 11 | `historica` | `investigacao` | 0.619 | 24 |
| 12 | `passagem` | `ponto` | 0.589 | 30 |
| 13 | `cientifico` | `producao` | 0.578 | 43 |
| 14 | `claudio` | `fabio` | 0.575 | 152 |
| 15 | `base` | `fonte` | 0.558 | 14 |
| 16 | `relatorios` | `elaboracao` | 0.558 | 16 |
| 17 | `translacao` | `cadeias` | 0.546 | 15 |
| 18 | `relatorios` | `base` | 0.543 | 18 |
| 19 | `research` | `brasil` | 0.542 | 38 |
| 20 | `novembro` | `dezembro` | 0.542 | 21 |
| 21 | `estatistica` | `foucault` | 0.518 | 14 |
| 22 | `anuais` | `base` | 0.516 | 12 |
| 23 | `comercial` | `tecnica` | 0.508 | 13 |
| 24 | `gente` | `dinheiro` | 0.499 | 15 |
| 25 | `research` | `fechamento` | 0.490 | 12 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (43 termos): claudio, rede, fabio, seguir, ator, informacao
- **Tópico 2** (40 termos): publico, corporacao, tecnologia, infraestrutura, instituicao, universidade
- **Tópico 3** (31 termos): hollerith, trajetoria, maquina, empresa, tabulacao, historica
- **Tópico 4** (24 termos): brasil, arranjo, laboratorio, encerramento, fapesp, acesso
- **Tópico 5** (23 termos): pesquisa, centro, cientifico, modelo, campo, relatorios
- **Tópico 6** (13 termos): inteligencia, artificial, ecossistema, inovacao, brasileiro, obia
- **Tópico 7** (6 termos): codigo, aberto, source, open, posicao, servicos

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 3** [hollerith, trajetoria, maquina] e **Tópico 4** [brasil, arranjo, laboratorio] — densidade ponderada de ligação = 0.2688
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 2** [publico, corporacao, tecnologia] — densidade ponderada de ligação = 0.3326
- Lacuna entre **Tópico 3** [hollerith, trajetoria, maquina] e **Tópico 5** [pesquisa, centro, cientifico] — densidade ponderada de ligação = 0.3590
- Lacuna entre **Tópico 2** [publico, corporacao, tecnologia] e **Tópico 3** [hollerith, trajetoria, maquina] — densidade ponderada de ligação = 0.3855
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 3** [hollerith, trajetoria, maquina] — densidade ponderada de ligação = 0.3946
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 4** [brasil, arranjo, laboratorio] — densidade ponderada de ligação = 0.4012

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
