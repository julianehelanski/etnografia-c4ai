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
- Tokens significativos: **16,910**
- Grafo bruto: **5158** nós · **43809** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **2482** arestas
- Tópicos detectados (Louvain): **6**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `claudio` | 786 |
| 2 | `pesquisa` | 675 |
| 3 | `centro` | 503 |
| 4 | `rede` | 494 |
| 5 | `fabio` | 484 |
| 6 | `publico` | 438 |
| 7 | `corporacao` | 417 |
| 8 | `seguir` | 383 |
| 9 | `arranjo` | 366 |
| 10 | `inteligencia` | 314 |
| 11 | `tecnologia` | 306 |
| 12 | `artificial` | 302 |
| 13 | `brasil` | 299 |
| 14 | `hollerith` | 293 |
| 15 | `laboratorio` | 281 |
| 16 | `ator` | 277 |
| 17 | `cientifico` | 261 |
| 18 | `infraestrutura` | 253 |
| 19 | `instituicao` | 240 |
| 20 | `modelo` | 230 |
| 21 | `ecossistema` | 230 |
| 22 | `universidade` | 230 |
| 23 | `trajetoria` | 222 |
| 24 | `encerramento` | 221 |
| 25 | `fapesp` | 218 |
| 26 | `maquina` | 213 |
| 27 | `empresa` | 208 |
| 28 | `informacao` | 200 |
| 29 | `campo` | 194 |
| 30 | `dado` | 188 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `claudio` | 0.0282 |
| 2 | `pesquisa` | 0.0256 |
| 3 | `centro` | 0.0192 |
| 4 | `rede` | 0.0191 |
| 5 | `fabio` | 0.0172 |
| 6 | `publico` | 0.0170 |
| 7 | `corporacao` | 0.0166 |
| 8 | `seguir` | 0.0147 |
| 9 | `arranjo` | 0.0143 |
| 10 | `tecnologia` | 0.0127 |
| 11 | `hollerith` | 0.0120 |
| 12 | `brasil` | 0.0118 |
| 13 | `inteligencia` | 0.0115 |
| 14 | `artificial` | 0.0112 |
| 15 | `ator` | 0.0110 |
| 16 | `laboratorio` | 0.0109 |
| 17 | `cientifico` | 0.0106 |
| 18 | `infraestrutura` | 0.0105 |
| 19 | `modelo` | 0.0097 |
| 20 | `instituicao` | 0.0095 |
| 21 | `universidade` | 0.0092 |
| 22 | `trajetoria` | 0.0092 |
| 23 | `ecossistema` | 0.0091 |
| 24 | `fapesp` | 0.0088 |
| 25 | `maquina` | 0.0088 |
| 26 | `encerramento` | 0.0088 |
| 27 | `empresa` | 0.0087 |
| 28 | `dado` | 0.0082 |
| 29 | `campo` | 0.0081 |
| 30 | `associacao` | 0.0076 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `conta` | 143 | 122 | +21 |
| 2 | `estatistica` | 100 | 87 | +13 |
| 3 | `estados` | 68 | 56 | +12 |
| 4 | `pratica` | 110 | 99 | +11 |
| 5 | `humano` | 90 | 80 | +10 |
| 6 | `censo` | 107 | 97 | +10 |
| 7 | `lado` | 134 | 124 | +10 |
| 8 | `objeto` | 137 | 127 | +10 |
| 9 | `computacional` | 126 | 117 | +9 |
| 10 | `codigo` | 56 | 48 | +8 |
| 11 | `unidos` | 89 | 81 | +8 |
| 12 | `conhecimento` | 91 | 84 | +7 |
| 13 | `translacao` | 109 | 102 | +7 |
| 14 | `mostra` | 163 | 156 | +7 |
| 15 | `deixa` | 77 | 71 | +6 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `centro` | 0.2288 |
| 2 | `pesquisa` | 0.2192 |
| 3 | `rede` | 0.1842 |
| 4 | `claudio` | 0.1682 |
| 5 | `publico` | 0.1173 |
| 6 | `corporacao` | 0.1037 |
| 7 | `fabio` | 0.0960 |
| 8 | `seguir` | 0.0893 |
| 9 | `tecnologia` | 0.0857 |
| 10 | `cientifico` | 0.0748 |
| 11 | `ator` | 0.0706 |
| 12 | `hollerith` | 0.0655 |
| 13 | `arranjo` | 0.0561 |
| 14 | `brasil` | 0.0437 |
| 15 | `laboratorio` | 0.0334 |
| 16 | `ecossistema` | 0.0322 |
| 17 | `trajetoria` | 0.0321 |
| 18 | `inteligencia` | 0.0309 |
| 19 | `infraestrutura` | 0.0306 |
| 20 | `dado` | 0.0301 |

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
| 5 | `relatorios` | `anuais` | 0.773 | 38 |
| 6 | `aberto` | `codigo` | 0.746 | 45 |
| 7 | `elaboracao` | `base` | 0.651 | 21 |
| 8 | `acesso` | `disponivel` | 0.627 | 30 |
| 9 | `historica` | `investigacao` | 0.619 | 24 |
| 10 | `passagem` | `ponto` | 0.593 | 30 |
| 11 | `claudio` | `fabio` | 0.587 | 167 |
| 12 | `cientifico` | `producao` | 0.579 | 43 |
| 13 | `relatorios` | `elaboracao` | 0.553 | 16 |
| 14 | `relatorios` | `base` | 0.545 | 18 |
| 15 | `research` | `brasil` | 0.543 | 38 |
| 16 | `novembro` | `dezembro` | 0.543 | 21 |
| 17 | `translacao` | `cadeias` | 0.533 | 15 |
| 18 | `anuais` | `base` | 0.523 | 12 |
| 19 | `estatistica` | `foucault` | 0.509 | 14 |
| 20 | `comercial` | `tecnica` | 0.509 | 13 |
| 21 | `gente` | `dinheiro` | 0.500 | 15 |
| 22 | `inovacao` | `ecossistema` | 0.497 | 41 |
| 23 | `hollerith` | `maquina` | 0.494 | 54 |
| 24 | `research` | `fechamento` | 0.484 | 12 |
| 25 | `hollerith` | `tabulacao` | 0.478 | 36 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (49 termos): claudio, rede, fabio, seguir, ator, informacao
- **Tópico 2** (45 termos): pesquisa, centro, arranjo, brasil, laboratorio, cientifico
- **Tópico 3** (35 termos): publico, corporacao, tecnologia, infraestrutura, universidade, escala
- **Tópico 4** (27 termos): hollerith, trajetoria, maquina, empresa, tabulacao, ponto
- **Tópico 5** (14 termos): modelo, dado, codigo, aberto, negocio, conhecimento
- **Tópico 6** (10 termos): inteligencia, artificial, ecossistema, inovacao, brasileiro, obia

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 5** [modelo, dado, codigo] — densidade ponderada de ligação = 0.2216
- Lacuna entre **Tópico 2** [pesquisa, centro, arranjo] e **Tópico 4** [hollerith, trajetoria, maquina] — densidade ponderada de ligação = 0.3243
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 3** [publico, corporacao, tecnologia] — densidade ponderada de ligação = 0.3324
- Lacuna entre **Tópico 2** [pesquisa, centro, arranjo] e **Tópico 5** [modelo, dado, codigo] — densidade ponderada de ligação = 0.3635
- Lacuna entre **Tópico 4** [hollerith, trajetoria, maquina] e **Tópico 5** [modelo, dado, codigo] — densidade ponderada de ligação = 0.3942
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 4** [hollerith, trajetoria, maquina] — densidade ponderada de ligação = 0.4157

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
