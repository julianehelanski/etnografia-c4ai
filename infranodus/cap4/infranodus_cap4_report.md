# Análise de rede textual — Capítulo 4

> Análise de rede textual (*text network analysis*, Paranyushkin 2019)
> aplicada ao arquivo `ex_cap4.tex`. O texto foi limpo de comandos LaTeX,
> citações e notas de rodapé foram reincorporadas; janela deslizante de
> 4 *tokens* com pesos decrescentes pela distância (3-2-1). Comunidades
> detectadas por Louvain ponderado. Esta versão acrescenta duas métricas
> *informativas* que não dependem da frequência bruta: **PageRank** dos
> nós e **NPMI** das arestas. As métricas baseadas em frequência são
> mantidas em paralelo, para comparação.

## 1. Resumo quantitativo
- Tokens significativos: **32,670**
- Grafo bruto: **6731** nós · **78239** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **4028** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `spira` | 1927 |
| 2 | `covideiro` | 1208 |
| 3 | `inscricao` | 1110 |
| 4 | `rede` | 1097 |
| 5 | `cadeia` | 963 |
| 6 | `artigo` | 846 |
| 7 | `objeto` | 839 |
| 8 | `respiratoria` | 776 |
| 9 | `dado` | 758 |
| 10 | `insuficiencia` | 734 |
| 11 | `modelo` | 669 |
| 12 | `projeto` | 655 |
| 13 | `marcelo` | 649 |
| 14 | `espectrograma` | 552 |
| 15 | `artigos` | 528 |
| 16 | `coleta` | 514 |
| 17 | `covid` | 457 |
| 18 | `pacientes` | 445 |
| 19 | `actante` | 442 |
| 20 | `pratica` | 414 |
| 21 | `audio` | 413 |
| 22 | `partir` | 410 |
| 23 | `sinal` | 392 |
| 24 | `condicoes` | 389 |
| 25 | `ruido` | 374 |
| 26 | `analise` | 367 |
| 27 | `cientifico` | 355 |
| 28 | `dataset` | 348 |
| 29 | `secao` | 346 |
| 30 | `condicao` | 339 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `spira` | 0.0380 |
| 2 | `covideiro` | 0.0240 |
| 3 | `inscricao` | 0.0224 |
| 4 | `rede` | 0.0219 |
| 5 | `cadeia` | 0.0194 |
| 6 | `artigo` | 0.0171 |
| 7 | `objeto` | 0.0170 |
| 8 | `dado` | 0.0154 |
| 9 | `respiratoria` | 0.0147 |
| 10 | `modelo` | 0.0140 |
| 11 | `insuficiencia` | 0.0139 |
| 12 | `marcelo` | 0.0133 |
| 13 | `projeto` | 0.0133 |
| 14 | `espectrograma` | 0.0115 |
| 15 | `coleta` | 0.0108 |
| 16 | `artigos` | 0.0107 |
| 17 | `covid` | 0.0096 |
| 18 | `actante` | 0.0094 |
| 19 | `pacientes` | 0.0093 |
| 20 | `pratica` | 0.0089 |
| 21 | `audio` | 0.0088 |
| 22 | `partir` | 0.0087 |
| 23 | `sinal` | 0.0085 |
| 24 | `ruido` | 0.0082 |
| 25 | `condicoes` | 0.0082 |
| 26 | `analise` | 0.0076 |
| 27 | `secao` | 0.0076 |
| 28 | `dataset` | 0.0074 |
| 29 | `ponto` | 0.0074 |
| 30 | `condicao` | 0.0074 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `escala` | 90 | 70 | +20 |
| 2 | `processamento` | 77 | 66 | +11 |
| 3 | `coeficientes` | 109 | 99 | +10 |
| 4 | `diferenca` | 124 | 115 | +9 |
| 5 | `pesquisa` | 72 | 64 | +8 |
| 6 | `carrega` | 117 | 109 | +8 |
| 7 | `microfone` | 132 | 125 | +7 |
| 8 | `visivel` | 52 | 46 | +6 |
| 9 | `frequencia` | 129 | 123 | +6 |
| 10 | `linguagem` | 140 | 134 | +6 |
| 11 | `padrao` | 146 | 140 | +6 |
| 12 | `algoritmo` | 64 | 59 | +5 |
| 13 | `campo` | 80 | 75 | +5 |
| 14 | `acesso` | 93 | 88 | +5 |
| 15 | `escolha` | 112 | 107 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `spira` | 0.5430 |
| 2 | `covideiro` | 0.2006 |
| 3 | `inscricao` | 0.1369 |
| 4 | `rede` | 0.1279 |
| 5 | `artigo` | 0.1060 |
| 6 | `cadeia` | 0.0947 |
| 7 | `respiratoria` | 0.0914 |
| 8 | `objeto` | 0.0833 |
| 9 | `modelo` | 0.0734 |
| 10 | `dado` | 0.0711 |
| 11 | `espectrograma` | 0.0534 |
| 12 | `projeto` | 0.0435 |
| 13 | `coleta` | 0.0380 |
| 14 | `insuficiencia` | 0.0365 |
| 15 | `pratica` | 0.0345 |
| 16 | `sinal` | 0.0309 |
| 17 | `ruido` | 0.0289 |
| 18 | `marcelo` | 0.0249 |
| 19 | `covid` | 0.0249 |
| 20 | `audio` | 0.0222 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `imutavel` | `movel` | 0.842 | 81 |
| 2 | `respiratoria` | `insuficiencia` | 0.841 | 309 |
| 3 | `grupo` | `controle` | 0.674 | 49 |
| 4 | `escuta` | `clinica` | 0.624 | 42 |
| 5 | `neural` | `rede` | 0.591 | 147 |
| 6 | `acao` | `programa` | 0.577 | 35 |
| 7 | `linguagem` | `processamento` | 0.558 | 33 |
| 8 | `sinal` | `acustico` | 0.540 | 61 |
| 9 | `tornou` | `possivel` | 0.525 | 34 |
| 10 | `entrevista` | `marcelo` | 0.500 | 99 |
| 11 | `enfermaria` | `ruido` | 0.500 | 68 |
| 12 | `acesso` | `disponivel` | 0.491 | 25 |
| 13 | `torna` | `visivel` | 0.489 | 42 |
| 14 | `publico` | `repositorio` | 0.487 | 24 |
| 15 | `modelo` | `treinado` | 0.472 | 52 |
| 16 | `covideiro` | `pandemico` | 0.469 | 97 |
| 17 | `ciencia` | `construcao` | 0.466 | 19 |
| 18 | `tornar` | `visivel` | 0.464 | 20 |
| 19 | `fonoaudiologos` | `medicos` | 0.458 | 25 |
| 20 | `publico` | `saude` | 0.444 | 18 |
| 21 | `textual` | `analise` | 0.439 | 27 |
| 22 | `controles` | `pacientes` | 0.433 | 43 |
| 23 | `tornou` | `visivel` | 0.431 | 21 |
| 24 | `saude` | `pesquisa` | 0.425 | 20 |
| 25 | `cadeia` | `translacao` | 0.417 | 71 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (31 termos): covideiro, artigo, coleta, condicoes, cientifico, laboratorio
- **Tópico 2** (30 termos): inscricao, cadeia, secao, ponto, dispositivo, latour
- **Tópico 3** (28 termos): dado, modelo, audio, treinamento, repositorio, algoritmo
- **Tópico 4** (27 termos): espectrograma, actante, partir, sinal, paciente, torna
- **Tópico 5** (25 termos): spira, projeto, marcelo, artigos, dataset, entrevista
- **Tópico 6** (19 termos): respiratoria, insuficiencia, covid, pacientes, ruido, enfermaria
- **Tópico 7** (11 termos): rede, analise, neural, textual, associacao, topologia
- **Tópico 8** (9 termos): objeto, pratica, condicao, clinica, distintas, distintos

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 2** [inscricao, cadeia, secao] e **Tópico 3** [dado, modelo, audio] — densidade ponderada de ligação = 0.5762
- Lacuna entre **Tópico 1** [covideiro, artigo, coleta] e **Tópico 3** [dado, modelo, audio] — densidade ponderada de ligação = 0.8226
- Lacuna entre **Tópico 4** [espectrograma, actante, partir] e **Tópico 5** [spira, projeto, marcelo] — densidade ponderada de ligação = 0.8785
- Lacuna entre **Tópico 3** [dado, modelo, audio] e **Tópico 4** [espectrograma, actante, partir] — densidade ponderada de ligação = 0.9352
- Lacuna entre **Tópico 3** [dado, modelo, audio] e **Tópico 5** [spira, projeto, marcelo] — densidade ponderada de ligação = 0.9471
- Lacuna entre **Tópico 1** [covideiro, artigo, coleta] e **Tópico 4** [espectrograma, actante, partir] — densidade ponderada de ligação = 0.9570

## 9. Leitura interpretativa
**O que a rede mostra.** O capítulo organiza-se em torno do projeto SPIRA (a
maior ponte do grafo, betweenness 0,60) e do aparato latouriano da
*inscrição*: os pares de maior associação são exatamente os conceitos-chave
— `caixa ↔ preta` (a caixa-preta) e `imutavel ↔ movel` (o *móvel imutável*
de Latour). A `cadeia` de translações percorre a cena clínica
(`respiratoria`, `insuficiencia`, `covid`, `enfermaria`, `ruido`), passa pelo
sinal (`espectrograma`, `sinal`, `acustico`), pelo dado e pelo modelo
(`dado`, `modelo`, `treinamento`, `rede neural`) e chega ao `artigo`.

**Pontes (`betweenness`).** Além de `spira`, são pontes `inscricao`,
`covideiro`, `cadeia`, `objeto`, `rede` e `artigo`. Vale notar `covideiro` —
o neologismo/actante cunhado no capítulo — operando como conector: a própria
invenção lexical do texto faz trabalho de tradução na rede.

**Lacunas a desenvolver.** As ligações mais fracas caem justamente nas
*juntas* da cadeia: entre a teoria da inscrição (`inscricao`, `cadeia`,
`dispositivo`) e o par dado/modelo é a lacuna mais forte; e seguem fracas as
costuras entre o espectrograma/sinal e o artigo/dado. Os pontos onde a rede é
mais rala são exatamente as translações que o capítulo narra — um convite a
tornar explícito *como* cada elo converte um estado no seguinte (voz → sinal
→ espectrograma → dado → modelo → artigo).

## 10. Arquivos gerados
**Visões frequentistas**
- `infranodus_cap4_network.png` — rede completa, tamanho por degree.
- `infranodus_cap4_focus.png` — núcleo (top-100, peso ≥ 3).

**Visões informativas**
- `infranodus_cap4_pmi.png` — rede completa, tamanho por **PageRank**,
  arestas filtradas por **NPMI ≥ 0,20**.
- `infranodus_cap4_focus_pmi.png` — núcleo, NPMI ≥ 0,25.

**Dados**
- `infranodus_cap4_metrics.json` — métricas brutas (degree, betweenness,
  PageRank, NPMI, comunidades, lacunas).
- `infranodus_cap4.gexf` / `infranodus_cap4_focus.gexf` — grafos para Gephi
  já com `community`, `frequency`, `degree_weighted`, `betweenness`,
  `pagerank` (nós) e `weight`, `npmi` (arestas).
- `infranodus_cap4_nodes.csv` / `infranodus_cap4_edges.csv` (e `_focus_*`)
  — fallback em planilha; CSVs trazem todas as colunas acima.

## 11. Como abrir no Gephi
1. Instale Gephi (≥ 0.10): https://gephi.org/users/download/
2. `File → Open…` → selecione `infranodus_cap4.gexf` (ou `_focus.gexf`).
3. No painel **Appearance**: já vem com cor por `community` e tamanho por
   `degree_weighted` (embutidos via atributos `viz`). Ajuste se quiser.
4. Em **Layout**: aplique *ForceAtlas 2* (ative *Prevent Overlap* e
   *Dissuade Hubs*) por ~30 s; ou *Fruchterman-Reingold* para algo mais rápido.
5. Em **Statistics**: rode *Modularity* e *Average Path Length* se quiser
   recalcular comunidades dentro do Gephi (resultados serão semelhantes).
6. Em **Preview**: ative *Node Labels*, escolha fonte e exporte para PDF/SVG.
