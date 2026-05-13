# Análise de rede textual — Capítulo 2

> Análise de rede textual (*text network analysis*, Paranyushkin 2019)
> aplicada ao arquivo `ex_cap2.tex`. O texto foi limpo de comandos LaTeX,
> citações e notas de rodapé foram reincorporadas; janela deslizante de
> 4 *tokens* com pesos decrescentes pela distância (3-2-1). Comunidades
> detectadas por Louvain ponderado. Esta versão acrescenta duas métricas
> *informativas* que não dependem da frequência bruta: **PageRank** dos
> nós e **NPMI** das arestas. As métricas baseadas em frequência são
> mantidas em paralelo, para comparação.

## 1. Resumo quantitativo
- Tokens significativos: **7,088**
- Grafo bruto: **2978** nós · **18553** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **1376** arestas
- Tópicos detectados (Louvain): **10**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `inteligencia` | 601 |
| 2 | `artificial` | 566 |
| 3 | `ciencia` | 464 |
| 4 | `tecnologia` | 263 |
| 5 | `latour` | 221 |
| 6 | `sociais` | 218 |
| 7 | `humano` | 217 |
| 8 | `estudos` | 216 |
| 9 | `campo` | 193 |
| 10 | `sistemas` | 167 |
| 11 | `etnografia` | 159 |
| 12 | `capes` | 153 |
| 13 | `antropologia` | 146 |
| 14 | `pesquisa` | 143 |
| 15 | `dado` | 138 |
| 16 | `rede` | 128 |
| 17 | `tecnica` | 127 |
| 18 | `social` | 125 |
| 19 | `mediacao` | 123 |
| 20 | `vocabulario` | 119 |
| 21 | `conhecimento` | 117 |
| 22 | `press` | 113 |
| 23 | `analise` | 112 |
| 24 | `producao` | 111 |
| 25 | `ator` | 107 |
| 26 | `objeto` | 103 |
| 27 | `scielo` | 102 |
| 28 | `pratica` | 101 |
| 29 | `area` | 97 |
| 30 | `torna` | 95 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `inteligencia` | 0.0370 |
| 2 | `artificial` | 0.0345 |
| 3 | `ciencia` | 0.0297 |
| 4 | `tecnologia` | 0.0178 |
| 5 | `latour` | 0.0166 |
| 6 | `humano` | 0.0151 |
| 7 | `campo` | 0.0145 |
| 8 | `sociais` | 0.0143 |
| 9 | `estudos` | 0.0141 |
| 10 | `sistemas` | 0.0126 |
| 11 | `etnografia` | 0.0120 |
| 12 | `vocabulario` | 0.0108 |
| 13 | `capes` | 0.0108 |
| 14 | `dado` | 0.0106 |
| 15 | `social` | 0.0106 |
| 16 | `pesquisa` | 0.0106 |
| 17 | `antropologia` | 0.0101 |
| 18 | `rede` | 0.0101 |
| 19 | `tecnica` | 0.0100 |
| 20 | `mediacao` | 0.0100 |
| 21 | `press` | 0.0096 |
| 22 | `conhecimento` | 0.0091 |
| 23 | `analise` | 0.0089 |
| 24 | `producao` | 0.0085 |
| 25 | `pratica` | 0.0085 |
| 26 | `ator` | 0.0083 |
| 27 | `torna` | 0.0080 |
| 28 | `infraestrutura` | 0.0080 |
| 29 | `university` | 0.0077 |
| 30 | `scielo` | 0.0075 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `technology` | 143 | 115 | +28 |
| 2 | `johnson` | 82 | 57 | +25 |
| 3 | `importa` | 88 | 65 | +23 |
| 4 | `knowledge` | 164 | 144 | +20 |
| 5 | `lenhard` | 91 | 73 | +18 |
| 6 | `scientific` | 177 | 160 | +17 |
| 7 | `computacional` | 64 | 49 | +15 |
| 8 | `figural` | 102 | 87 | +15 |
| 9 | `cientifico` | 60 | 46 | +14 |
| 10 | `engenharia` | 68 | 54 | +14 |
| 11 | `opera` | 136 | 122 | +14 |
| 12 | `ponto` | 141 | 127 | +14 |
| 13 | `agencia` | 67 | 55 | +12 |
| 14 | `posicao` | 106 | 94 | +12 |
| 15 | `mundo` | 101 | 90 | +11 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `ciencia` | 0.3744 |
| 2 | `inteligencia` | 0.3440 |
| 3 | `artificial` | 0.3393 |
| 4 | `humano` | 0.1420 |
| 5 | `latour` | 0.1406 |
| 6 | `tecnologia` | 0.0908 |
| 7 | `antropologia` | 0.0903 |
| 8 | `sistemas` | 0.0787 |
| 9 | `sociais` | 0.0726 |
| 10 | `campo` | 0.0654 |
| 11 | `social` | 0.0615 |
| 12 | `vocabulario` | 0.0588 |
| 13 | `pesquisa` | 0.0428 |
| 14 | `capes` | 0.0428 |
| 15 | `etnografia` | 0.0408 |
| 16 | `rede` | 0.0401 |
| 17 | `producao` | 0.0398 |
| 18 | `pratica` | 0.0390 |
| 19 | `relacoes` | 0.0384 |
| 20 | `conhecimento` | 0.0361 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `teses` | `dissertacoes` | 0.901 | 21 |
| 2 | `catalogo` | `teses` | 0.878 | 21 |
| 3 | `johnson` | `lenhard` | 0.829 | 26 |
| 4 | `tecnica` | `mediacao` | 0.814 | 45 |
| 5 | `university` | `press` | 0.812 | 50 |
| 6 | `inteligencia` | `artificial` | 0.807 | 244 |
| 7 | `crawford` | `joler` | 0.786 | 19 |
| 8 | `catalogo` | `dissertacoes` | 0.756 | 14 |
| 9 | `historias` | `importa` | 0.748 | 16 |
| 10 | `central` | `foco` | 0.734 | 20 |
| 11 | `teoria` | `ator` | 0.719 | 18 |
| 12 | `capes` | `dissertacoes` | 0.706 | 21 |
| 13 | `science` | `studies` | 0.679 | 21 |
| 14 | `stengers` | `haraway` | 0.669 | 27 |
| 15 | `numero` | `maior` | 0.669 | 15 |
| 16 | `bruno` | `latour` | 0.663 | 43 |
| 17 | `recusa` | `posicao` | 0.660 | 9 |
| 18 | `emergente` | `brasil` | 0.656 | 11 |
| 19 | `infraestrutura` | `computacional` | 0.656 | 22 |
| 20 | `possiveis` | `figuracao` | 0.650 | 13 |
| 21 | `bibliometrica` | `analise` | 0.646 | 18 |
| 22 | `disponivel` | `acesso` | 0.644 | 17 |
| 23 | `educacao` | `revista` | 0.641 | 12 |
| 24 | `especialistas` | `sistemas` | 0.627 | 30 |
| 25 | `engenheiro` | `cientista` | 0.626 | 9 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (41 termos): campo, etnografia, vocabulario, analise, laboratorio, haraway
- **Tópico 2** (39 termos): pratica, torna, infraestrutura, relacoes, cientifico, acesso
- **Tópico 3** (34 termos): humano, capes, dado, conhecimento, producao, scielo
- **Tópico 4** (16 termos): ciencia, tecnologia, sociais, estudos, antropologia, acao
- **Tópico 5** (14 termos): latour, rede, ator, bruno, seguir, propoe
- **Tópico 6** (12 termos): social, science, collins, forsythe, studies, argumento
- **Tópico 7** (10 termos): inteligencia, artificial, sistemas, pesquisa, objeto, partir
- **Tópico 8** (6 termos): press, university, traducao, chicago, material, pergunta

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 2** [pratica, torna, infraestrutura] e **Tópico 3** [humano, capes, dado] — densidade ponderada de ligação = 0.1184
- Lacuna entre **Tópico 1** [campo, etnografia, vocabulario] e **Tópico 3** [humano, capes, dado] — densidade ponderada de ligação = 0.1212
- Lacuna entre **Tópico 1** [campo, etnografia, vocabulario] e **Tópico 2** [pratica, torna, infraestrutura] — densidade ponderada de ligação = 0.1263
- Lacuna entre **Tópico 2** [pratica, torna, infraestrutura] e **Tópico 5** [latour, rede, ator] — densidade ponderada de ligação = 0.1392
- Lacuna entre **Tópico 2** [pratica, torna, infraestrutura] e **Tópico 4** [ciencia, tecnologia, sociais] — densidade ponderada de ligação = 0.1635
- Lacuna entre **Tópico 3** [humano, capes, dado] e **Tópico 5** [latour, rede, ator] — densidade ponderada de ligação = 0.1954

## 9. Leitura interpretativa
_Leitura interpretativa ainda não escrita para este capítulo. Crie `interpretation_cap2.md` ao lado dos outputs para que o conteúdo seja embutido aqui automaticamente._

## 10. Arquivos gerados
**Visões frequentistas**
- `infranodus_cap2_network.png` — rede completa, tamanho por degree.
- `infranodus_cap2_focus.png` — núcleo (top-100, peso ≥ 3).

**Visões informativas**
- `infranodus_cap2_pmi.png` — rede completa, tamanho por **PageRank**,
  arestas filtradas por **NPMI ≥ 0,20**.
- `infranodus_cap2_focus_pmi.png` — núcleo, NPMI ≥ 0,25.

**Dados**
- `infranodus_cap2_metrics.json` — métricas brutas (degree, betweenness,
  PageRank, NPMI, comunidades, lacunas).
- `infranodus_cap2.gexf` / `infranodus_cap2_focus.gexf` — grafos para Gephi
  já com `community`, `frequency`, `degree_weighted`, `betweenness`,
  `pagerank` (nós) e `weight`, `npmi` (arestas).
- `infranodus_cap2_nodes.csv` / `infranodus_cap2_edges.csv` (e `_focus_*`)
  — fallback em planilha; CSVs trazem todas as colunas acima.

## 11. Como abrir no Gephi
1. Instale Gephi (≥ 0.10): https://gephi.org/users/download/
2. `File → Open…` → selecione `infranodus_cap2.gexf` (ou `_focus.gexf`).
3. No painel **Appearance**: já vem com cor por `community` e tamanho por
   `degree_weighted` (embutidos via atributos `viz`). Ajuste se quiser.
4. Em **Layout**: aplique *ForceAtlas 2* (ative *Prevent Overlap* e
   *Dissuade Hubs*) por ~30 s; ou *Fruchterman-Reingold* para algo mais rápido.
5. Em **Statistics**: rode *Modularity* e *Average Path Length* se quiser
   recalcular comunidades dentro do Gephi (resultados serão semelhantes).
6. Em **Preview**: ative *Node Labels*, escolha fonte e exporte para PDF/SVG.
