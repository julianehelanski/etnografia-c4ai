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
- Tokens significativos: **17,498**
- Grafo bruto: **5226** nós · **45067** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **2568** arestas
- Tópicos detectados (Louvain): **7**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `claudio` | 794 |
| 2 | `pesquisa` | 714 |
| 3 | `rede` | 568 |
| 4 | `centro` | 536 |
| 5 | `fabio` | 501 |
| 6 | `publico` | 441 |
| 7 | `arranjo` | 396 |
| 8 | `seguir` | 389 |
| 9 | `corporacao` | 369 |
| 10 | `inteligencia` | 317 |
| 11 | `brasil` | 313 |
| 12 | `artificial` | 304 |
| 13 | `tecnologia` | 301 |
| 14 | `hollerith` | 299 |
| 15 | `ator` | 295 |
| 16 | `laboratorio` | 286 |
| 17 | `infraestrutura` | 255 |
| 18 | `ecossistema` | 248 |
| 19 | `cientifico` | 243 |
| 20 | `universidade` | 243 |
| 21 | `empresa` | 242 |
| 22 | `fapesp` | 238 |
| 23 | `instituicao` | 232 |
| 24 | `modelo` | 228 |
| 25 | `maquina` | 228 |
| 26 | `trajetoria` | 220 |
| 27 | `associacao` | 211 |
| 28 | `informacao` | 208 |
| 29 | `campo` | 205 |
| 30 | `encerramento` | 200 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `claudio` | 0.0270 |
| 2 | `pesquisa` | 0.0259 |
| 3 | `rede` | 0.0209 |
| 4 | `centro` | 0.0195 |
| 5 | `fabio` | 0.0170 |
| 6 | `publico` | 0.0164 |
| 7 | `arranjo` | 0.0147 |
| 8 | `corporacao` | 0.0141 |
| 9 | `seguir` | 0.0141 |
| 10 | `tecnologia` | 0.0122 |
| 11 | `brasil` | 0.0119 |
| 12 | `hollerith` | 0.0118 |
| 13 | `inteligencia` | 0.0112 |
| 14 | `ator` | 0.0111 |
| 15 | `artificial` | 0.0108 |
| 16 | `laboratorio` | 0.0107 |
| 17 | `infraestrutura` | 0.0103 |
| 18 | `empresa` | 0.0095 |
| 19 | `universidade` | 0.0095 |
| 20 | `cientifico` | 0.0094 |
| 21 | `ecossistema` | 0.0093 |
| 22 | `modelo` | 0.0093 |
| 23 | `fapesp` | 0.0092 |
| 24 | `maquina` | 0.0092 |
| 25 | `instituicao` | 0.0090 |
| 26 | `trajetoria` | 0.0087 |
| 27 | `associacao` | 0.0083 |
| 28 | `campo` | 0.0081 |
| 29 | `dado` | 0.0078 |
| 30 | `encerramento` | 0.0077 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `natural` | 117 | 97 | +20 |
| 2 | `conta` | 139 | 121 | +18 |
| 3 | `linguagem` | 84 | 69 | +15 |
| 4 | `estatistica` | 99 | 88 | +11 |
| 5 | `pratica` | 119 | 108 | +11 |
| 6 | `dependencia` | 101 | 91 | +10 |
| 7 | `tecnica` | 68 | 59 | +9 |
| 8 | `processamento` | 90 | 82 | +8 |
| 9 | `unidos` | 95 | 87 | +8 |
| 10 | `mostra` | 170 | 162 | +8 |
| 11 | `cadeia` | 92 | 85 | +7 |
| 12 | `projetos` | 127 | 120 | +7 |
| 13 | `codigo` | 62 | 56 | +6 |
| 14 | `humano` | 81 | 75 | +6 |
| 15 | `conhecimento` | 96 | 90 | +6 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `centro` | 0.2397 |
| 2 | `pesquisa` | 0.2210 |
| 3 | `rede` | 0.2087 |
| 4 | `claudio` | 0.1708 |
| 5 | `publico` | 0.1225 |
| 6 | `fabio` | 0.1222 |
| 7 | `corporacao` | 0.0913 |
| 8 | `tecnologia` | 0.0871 |
| 9 | `seguir` | 0.0758 |
| 10 | `ator` | 0.0746 |
| 11 | `hollerith` | 0.0660 |
| 12 | `cientifico` | 0.0544 |
| 13 | `brasil` | 0.0468 |
| 14 | `ecossistema` | 0.0446 |
| 15 | `modelo` | 0.0416 |
| 16 | `universidade` | 0.0372 |
| 17 | `fapesp` | 0.0338 |
| 18 | `arranjo` | 0.0321 |
| 19 | `inteligencia` | 0.0303 |
| 20 | `empresa` | 0.0297 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `informacao` | `verbal` | 0.871 | 80 |
| 2 | `inteligencia` | `artificial` | 0.870 | 147 |
| 3 | `unidos` | `estados` | 0.859 | 57 |
| 4 | `porta` | `voz` | 0.858 | 53 |
| 5 | `linguagem` | `natural` | 0.823 | 42 |
| 6 | `relatorios` | `anuais` | 0.759 | 43 |
| 7 | `aberto` | `codigo` | 0.747 | 45 |
| 8 | `linguagem` | `processamento` | 0.727 | 30 |
| 9 | `processamento` | `natural` | 0.657 | 20 |
| 10 | `historica` | `investigacao` | 0.629 | 24 |
| 11 | `acesso` | `disponivel` | 0.624 | 30 |
| 12 | `elaboracao` | `base` | 0.599 | 21 |
| 13 | `passagem` | `ponto` | 0.591 | 30 |
| 14 | `claudio` | `fabio` | 0.581 | 168 |
| 15 | `novembro` | `dezembro` | 0.564 | 23 |
| 16 | `research` | `brasil` | 0.543 | 38 |
| 17 | `inovacao` | `ecossistema` | 0.530 | 46 |
| 18 | `translacao` | `cadeias` | 0.529 | 15 |
| 19 | `cientifico` | `producao` | 0.518 | 37 |
| 20 | `relatorios` | `elaboracao` | 0.510 | 16 |
| 21 | `mapa` | `problemas` | 0.505 | 12 |
| 22 | `gente` | `dinheiro` | 0.496 | 15 |
| 23 | `research` | `fechamento` | 0.486 | 12 |
| 24 | `relatorios` | `base` | 0.486 | 18 |
| 25 | `hollerith` | `maquina` | 0.479 | 54 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (52 termos): claudio, rede, fabio, seguir, ator, associacao
- **Tópico 2** (37 termos): tecnologia, hollerith, infraestrutura, empresa, maquina, trajetoria
- **Tópico 3** (28 termos): pesquisa, centro, cientifico, fapesp, partir, relatorios
- **Tópico 4** (27 termos): publico, arranjo, corporacao, brasil, laboratorio, universidade
- **Tópico 5** (15 termos): ponto, parte, escala, historica, deixa, estados
- **Tópico 6** (14 termos): modelo, dado, codigo, aberto, negocio, linguagem
- **Tópico 7** (7 termos): inteligencia, artificial, ecossistema, inovacao, brasileiro, obia

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 2** [tecnologia, hollerith, infraestrutura] e **Tópico 3** [pesquisa, centro, cientifico] — densidade ponderada de ligação = 0.3398
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 2** [tecnologia, hollerith, infraestrutura] — densidade ponderada de ligação = 0.3540
- Lacuna entre **Tópico 3** [pesquisa, centro, cientifico] e **Tópico 5** [ponto, parte, escala] — densidade ponderada de ligação = 0.3976
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 5** [ponto, parte, escala] — densidade ponderada de ligação = 0.4115
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 3** [pesquisa, centro, cientifico] — densidade ponderada de ligação = 0.4519
- Lacuna entre **Tópico 2** [tecnologia, hollerith, infraestrutura] e **Tópico 5** [ponto, parte, escala] — densidade ponderada de ligação = 0.4667

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
