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
- Tokens significativos: **16,879**
- Grafo bruto: **5157** nós · **43733** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **2470** arestas
- Tópicos detectados (Louvain): **7**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `claudio` | 782 |
| 2 | `pesquisa` | 674 |
| 3 | `centro` | 499 |
| 4 | `rede` | 478 |
| 5 | `fabio` | 473 |
| 6 | `publico` | 441 |
| 7 | `corporacao` | 419 |
| 8 | `seguir` | 381 |
| 9 | `arranjo` | 348 |
| 10 | `inteligencia` | 314 |
| 11 | `tecnologia` | 306 |
| 12 | `artificial` | 302 |
| 13 | `brasil` | 299 |
| 14 | `hollerith` | 293 |
| 15 | `laboratorio` | 281 |
| 16 | `ator` | 276 |
| 17 | `cientifico` | 257 |
| 18 | `infraestrutura` | 253 |
| 19 | `instituicao` | 240 |
| 20 | `modelo` | 230 |
| 21 | `ecossistema` | 230 |
| 22 | `universidade` | 230 |
| 23 | `trajetoria` | 229 |
| 24 | `encerramento` | 221 |
| 25 | `fapesp` | 218 |
| 26 | `maquina` | 216 |
| 27 | `empresa` | 208 |
| 28 | `informacao` | 200 |
| 29 | `campo` | 195 |
| 30 | `dado` | 190 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `claudio` | 0.0283 |
| 2 | `pesquisa` | 0.0257 |
| 3 | `centro` | 0.0192 |
| 4 | `rede` | 0.0187 |
| 5 | `publico` | 0.0172 |
| 6 | `fabio` | 0.0170 |
| 7 | `corporacao` | 0.0168 |
| 8 | `seguir` | 0.0147 |
| 9 | `arranjo` | 0.0137 |
| 10 | `tecnologia` | 0.0127 |
| 11 | `hollerith` | 0.0120 |
| 12 | `brasil` | 0.0118 |
| 13 | `inteligencia` | 0.0116 |
| 14 | `artificial` | 0.0112 |
| 15 | `ator` | 0.0111 |
| 16 | `laboratorio` | 0.0110 |
| 17 | `infraestrutura` | 0.0106 |
| 18 | `cientifico` | 0.0105 |
| 19 | `modelo` | 0.0098 |
| 20 | `instituicao` | 0.0095 |
| 21 | `trajetoria` | 0.0095 |
| 22 | `universidade` | 0.0093 |
| 23 | `ecossistema` | 0.0091 |
| 24 | `maquina` | 0.0089 |
| 25 | `fapesp` | 0.0088 |
| 26 | `encerramento` | 0.0088 |
| 27 | `empresa` | 0.0087 |
| 28 | `dado` | 0.0084 |
| 29 | `campo` | 0.0082 |
| 30 | `associacao` | 0.0076 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `conta` | 142 | 121 | +21 |
| 2 | `estados` | 68 | 57 | +11 |
| 3 | `humano` | 91 | 80 | +11 |
| 4 | `estatistica` | 98 | 87 | +11 |
| 5 | `computacional` | 126 | 115 | +11 |
| 6 | `conhecimento` | 92 | 82 | +10 |
| 7 | `pratica` | 120 | 110 | +10 |
| 8 | `censo` | 104 | 95 | +9 |
| 9 | `translacao` | 122 | 113 | +9 |
| 10 | `cadeia` | 110 | 102 | +8 |
| 11 | `mostra` | 162 | 154 | +8 |
| 12 | `unidos` | 88 | 81 | +7 |
| 13 | `acao` | 118 | 111 | +7 |
| 14 | `condicao` | 136 | 129 | +7 |
| 15 | `codigo` | 55 | 49 | +6 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `pesquisa` | 0.2233 |
| 2 | `centro` | 0.2228 |
| 3 | `rede` | 0.1806 |
| 4 | `claudio` | 0.1754 |
| 5 | `publico` | 0.1190 |
| 6 | `corporacao` | 0.1042 |
| 7 | `fabio` | 0.0958 |
| 8 | `seguir` | 0.0916 |
| 9 | `tecnologia` | 0.0852 |
| 10 | `ator` | 0.0708 |
| 11 | `cientifico` | 0.0663 |
| 12 | `hollerith` | 0.0646 |
| 13 | `arranjo` | 0.0547 |
| 14 | `brasil` | 0.0476 |
| 15 | `trajetoria` | 0.0342 |
| 16 | `laboratorio` | 0.0331 |
| 17 | `ecossistema` | 0.0322 |
| 18 | `inteligencia` | 0.0311 |
| 19 | `infraestrutura` | 0.0308 |
| 20 | `dado` | 0.0297 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `informacao` | `verbal` | 0.870 | 77 |
| 2 | `inteligencia` | `artificial` | 0.870 | 144 |
| 3 | `unidos` | `estados` | 0.858 | 57 |
| 4 | `porta` | `voz` | 0.857 | 53 |
| 5 | `relatorios` | `anuais` | 0.780 | 38 |
| 6 | `aberto` | `codigo` | 0.746 | 45 |
| 7 | `elaboracao` | `base` | 0.651 | 21 |
| 8 | `acesso` | `disponivel` | 0.627 | 30 |
| 9 | `historica` | `investigacao` | 0.619 | 24 |
| 10 | `passagem` | `ponto` | 0.593 | 30 |
| 11 | `claudio` | `fabio` | 0.585 | 164 |
| 12 | `cientifico` | `producao` | 0.579 | 43 |
| 13 | `relatorios` | `elaboracao` | 0.559 | 16 |
| 14 | `relatorios` | `base` | 0.551 | 18 |
| 15 | `research` | `brasil` | 0.543 | 38 |
| 16 | `novembro` | `dezembro` | 0.543 | 21 |
| 17 | `translacao` | `cadeias` | 0.540 | 15 |
| 18 | `anuais` | `base` | 0.523 | 12 |
| 19 | `estatistica` | `foucault` | 0.509 | 14 |
| 20 | `comercial` | `tecnica` | 0.509 | 13 |
| 21 | `gente` | `dinheiro` | 0.500 | 15 |
| 22 | `inovacao` | `ecossistema` | 0.497 | 41 |
| 23 | `hollerith` | `maquina` | 0.494 | 54 |
| 24 | `research` | `fechamento` | 0.484 | 12 |
| 25 | `hollerith` | `tabulacao` | 0.478 | 36 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (42 termos): tecnologia, hollerith, trajetoria, maquina, empresa, dado
- **Tópico 2** (37 termos): rede, seguir, ator, campo, associacao, porta
- **Tópico 3** (34 termos): publico, corporacao, arranjo, brasil, laboratorio, infraestrutura
- **Tópico 4** (29 termos): pesquisa, centro, cientifico, fapesp, relatorios, partir
- **Tópico 5** (17 termos): inteligencia, artificial, ecossistema, inovacao, brasileiro, historica
- **Tópico 6** (15 termos): claudio, fabio, informacao, verbal, pergunta, entrevistas
- **Tópico 7** (6 termos): modelo, codigo, aberto, negocio, expertise, software

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 2** [rede, seguir, ator] e **Tópico 5** [inteligencia, artificial, ecossistema] — densidade ponderada de ligação = 0.2957
- Lacuna entre **Tópico 2** [rede, seguir, ator] e **Tópico 4** [pesquisa, centro, cientifico] — densidade ponderada de ligação = 0.3271
- Lacuna entre **Tópico 1** [tecnologia, hollerith, trajetoria] e **Tópico 4** [pesquisa, centro, cientifico] — densidade ponderada de ligação = 0.3292
- Lacuna entre **Tópico 1** [tecnologia, hollerith, trajetoria] e **Tópico 2** [rede, seguir, ator] — densidade ponderada de ligação = 0.3404
- Lacuna entre **Tópico 1** [tecnologia, hollerith, trajetoria] e **Tópico 5** [inteligencia, artificial, ecossistema] — densidade ponderada de ligação = 0.3627
- Lacuna entre **Tópico 2** [rede, seguir, ator] e **Tópico 3** [publico, corporacao, arranjo] — densidade ponderada de ligação = 0.4356

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
