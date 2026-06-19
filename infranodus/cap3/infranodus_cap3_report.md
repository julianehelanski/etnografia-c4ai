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
- Tokens significativos: **17,551**
- Grafo bruto: **5247** nós · **44973** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **2414** arestas
- Tópicos detectados (Louvain): **7**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `pesquisa` | 713 |
| 2 | `claudio` | 623 |
| 3 | `centro` | 524 |
| 4 | `rede` | 451 |
| 5 | `corporacao` | 440 |
| 6 | `publico` | 434 |
| 7 | `fabio` | 406 |
| 8 | `seguir` | 327 |
| 9 | `inteligencia` | 311 |
| 10 | `instituicao` | 306 |
| 11 | `hollerith` | 302 |
| 12 | `tecnologia` | 302 |
| 13 | `arranjo` | 299 |
| 14 | `artificial` | 296 |
| 15 | `infraestrutura` | 292 |
| 16 | `ator` | 284 |
| 17 | `brasil` | 281 |
| 18 | `laboratorio` | 277 |
| 19 | `modelo` | 268 |
| 20 | `universidade` | 263 |
| 21 | `trajetoria` | 245 |
| 22 | `fapesp` | 237 |
| 23 | `cientifico` | 235 |
| 24 | `encerramento` | 212 |
| 25 | `maquina` | 210 |
| 26 | `ecossistema` | 196 |
| 27 | `pergunta` | 195 |
| 28 | `porta` | 193 |
| 29 | `ponto` | 189 |
| 30 | `dado` | 184 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `pesquisa` | 0.0273 |
| 2 | `claudio` | 0.0232 |
| 3 | `centro` | 0.0201 |
| 4 | `rede` | 0.0177 |
| 5 | `corporacao` | 0.0175 |
| 6 | `publico` | 0.0166 |
| 7 | `fabio` | 0.0150 |
| 8 | `seguir` | 0.0127 |
| 9 | `tecnologia` | 0.0125 |
| 10 | `hollerith` | 0.0124 |
| 11 | `instituicao` | 0.0121 |
| 12 | `infraestrutura` | 0.0119 |
| 13 | `inteligencia` | 0.0115 |
| 14 | `arranjo` | 0.0115 |
| 15 | `ator` | 0.0114 |
| 16 | `modelo` | 0.0113 |
| 17 | `brasil` | 0.0111 |
| 18 | `artificial` | 0.0111 |
| 19 | `laboratorio` | 0.0110 |
| 20 | `universidade` | 0.0105 |
| 21 | `trajetoria` | 0.0101 |
| 22 | `fapesp` | 0.0095 |
| 23 | `cientifico` | 0.0095 |
| 24 | `maquina` | 0.0088 |
| 25 | `encerramento` | 0.0086 |
| 26 | `ponto` | 0.0081 |
| 27 | `ecossistema` | 0.0080 |
| 28 | `pergunta` | 0.0080 |
| 29 | `dado` | 0.0080 |
| 30 | `tabulacao` | 0.0078 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `conta` | 143 | 129 | +14 |
| 2 | `estados` | 69 | 58 | +11 |
| 3 | `pratica` | 119 | 109 | +10 |
| 4 | `humano` | 79 | 70 | +9 |
| 5 | `censo` | 88 | 79 | +9 |
| 6 | `translacao` | 117 | 108 | +9 |
| 7 | `dinheiro` | 122 | 113 | +9 |
| 8 | `actante` | 68 | 62 | +6 |
| 9 | `cadeias` | 98 | 92 | +6 |
| 10 | `lado` | 130 | 124 | +6 |
| 11 | `objeto` | 133 | 127 | +6 |
| 12 | `escala` | 62 | 57 | +5 |
| 13 | `analise` | 65 | 60 | +5 |
| 14 | `material` | 78 | 73 | +5 |
| 15 | `deixa` | 89 | 84 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `pesquisa` | 0.2404 |
| 2 | `centro` | 0.1980 |
| 3 | `claudio` | 0.1624 |
| 4 | `rede` | 0.1606 |
| 5 | `corporacao` | 0.1402 |
| 6 | `publico` | 0.1285 |
| 7 | `fabio` | 0.1019 |
| 8 | `tecnologia` | 0.0808 |
| 9 | `ator` | 0.0766 |
| 10 | `seguir` | 0.0756 |
| 11 | `hollerith` | 0.0731 |
| 12 | `infraestrutura` | 0.0467 |
| 13 | `cientifico` | 0.0452 |
| 14 | `trajetoria` | 0.0432 |
| 15 | `universidade` | 0.0385 |
| 16 | `arranjo` | 0.0380 |
| 17 | `laboratorio` | 0.0369 |
| 18 | `inteligencia` | 0.0326 |
| 19 | `fapesp` | 0.0312 |
| 20 | `instituicao` | 0.0292 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `porta` | `voz` | 0.881 | 68 |
| 2 | `inteligencia` | `artificial` | 0.871 | 144 |
| 3 | `informacao` | `verbal` | 0.864 | 77 |
| 4 | `unidos` | `estados` | 0.859 | 57 |
| 5 | `relatorios` | `anuais` | 0.796 | 39 |
| 6 | `aberto` | `codigo` | 0.752 | 48 |
| 7 | `informacao` | `pinhanez` | 0.736 | 48 |
| 8 | `elaboracao` | `base` | 0.660 | 21 |
| 9 | `verbal` | `pinhanez` | 0.653 | 32 |
| 10 | `claudio` | `fabio` | 0.624 | 150 |
| 11 | `historica` | `investigacao` | 0.615 | 24 |
| 12 | `relatorios` | `elaboracao` | 0.585 | 18 |
| 13 | `research` | `brasil` | 0.584 | 43 |
| 14 | `passagem` | `ponto` | 0.581 | 33 |
| 15 | `relatorios` | `base` | 0.576 | 18 |
| 16 | `cientifico` | `producao` | 0.566 | 43 |
| 17 | `funcionamento` | `condicao` | 0.544 | 21 |
| 18 | `anuais` | `base` | 0.541 | 12 |
| 19 | `research` | `fechamento` | 0.541 | 15 |
| 20 | `novembro` | `dezembro` | 0.525 | 20 |
| 21 | `hollerith` | `tabulacao` | 0.493 | 39 |
| 22 | `translacao` | `cadeias` | 0.493 | 15 |
| 23 | `instituicao` | `multiplicacao` | 0.491 | 27 |
| 24 | `gente` | `dinheiro` | 0.486 | 15 |
| 25 | `publicacoes` | `datasets` | 0.486 | 14 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (52 termos): claudio, rede, fabio, seguir, ator, pergunta
- **Tópico 2** (51 termos): corporacao, publico, instituicao, tecnologia, infraestrutura, modelo
- **Tópico 3** (28 termos): hollerith, trajetoria, maquina, tabulacao, empresa, historica
- **Tópico 4** (24 termos): pesquisa, centro, cientifico, relatorios, pesquisador, partir
- **Tópico 5** (11 termos): inteligencia, artificial, ecossistema, inovacao, brasileiro, valor
- **Tópico 6** (10 termos): arranjo, brasil, laboratorio, encerramento, dezembro, novembro
- **Tópico 7** (4 termos): informacao, verbal, pinhanez, projeto

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 5** [inteligencia, artificial, ecossistema] — densidade ponderada de ligação = 0.2657
- Lacuna entre **Tópico 3** [hollerith, trajetoria, maquina] e **Tópico 4** [pesquisa, centro, cientifico] — densidade ponderada de ligação = 0.3199
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 2** [corporacao, publico, instituicao] — densidade ponderada de ligação = 0.3443
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 3** [hollerith, trajetoria, maquina] — densidade ponderada de ligação = 0.3647
- Lacuna entre **Tópico 2** [corporacao, publico, instituicao] e **Tópico 3** [hollerith, trajetoria, maquina] — densidade ponderada de ligação = 0.3971
- Lacuna entre **Tópico 3** [hollerith, trajetoria, maquina] e **Tópico 5** [inteligencia, artificial, ecossistema] — densidade ponderada de ligação = 0.4578

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
