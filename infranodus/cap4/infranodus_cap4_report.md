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
- Tokens significativos: **33,456**
- Grafo bruto: **6832** nós · **79722** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **4072** arestas
- Tópicos detectados (Louvain): **7**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `spira` | 1968 |
| 2 | `covideiro` | 1178 |
| 3 | `inscricao` | 1144 |
| 4 | `rede` | 1046 |
| 5 | `cadeia` | 995 |
| 6 | `artigo` | 900 |
| 7 | `objeto` | 882 |
| 8 | `respiratoria` | 786 |
| 9 | `insuficiencia` | 748 |
| 10 | `dado` | 738 |
| 11 | `projeto` | 723 |
| 12 | `modelo` | 691 |
| 13 | `marcelo` | 639 |
| 14 | `espectrograma` | 543 |
| 15 | `artigos` | 540 |
| 16 | `coleta` | 516 |
| 17 | `actante` | 465 |
| 18 | `covid` | 451 |
| 19 | `condicoes` | 437 |
| 20 | `cientifico` | 429 |
| 21 | `partir` | 426 |
| 22 | `pratica` | 423 |
| 23 | `audio` | 420 |
| 24 | `pacientes` | 408 |
| 25 | `sinal` | 390 |
| 26 | `analise` | 390 |
| 27 | `ruido` | 377 |
| 28 | `secao` | 361 |
| 29 | `torna` | 353 |
| 30 | `dispositivo` | 350 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `spira` | 0.0379 |
| 2 | `covideiro` | 0.0229 |
| 3 | `inscricao` | 0.0226 |
| 4 | `rede` | 0.0206 |
| 5 | `cadeia` | 0.0195 |
| 6 | `artigo` | 0.0176 |
| 7 | `objeto` | 0.0175 |
| 8 | `dado` | 0.0147 |
| 9 | `respiratoria` | 0.0145 |
| 10 | `projeto` | 0.0144 |
| 11 | `modelo` | 0.0141 |
| 12 | `insuficiencia` | 0.0137 |
| 13 | `marcelo` | 0.0128 |
| 14 | `espectrograma` | 0.0111 |
| 15 | `artigos` | 0.0106 |
| 16 | `coleta` | 0.0106 |
| 17 | `actante` | 0.0096 |
| 18 | `covid` | 0.0092 |
| 19 | `pratica` | 0.0089 |
| 20 | `condicoes` | 0.0089 |
| 21 | `partir` | 0.0088 |
| 22 | `audio` | 0.0087 |
| 23 | `cientifico` | 0.0086 |
| 24 | `pacientes` | 0.0084 |
| 25 | `sinal` | 0.0083 |
| 26 | `ruido` | 0.0082 |
| 27 | `analise` | 0.0079 |
| 28 | `torna` | 0.0077 |
| 29 | `secao` | 0.0077 |
| 30 | `ponto` | 0.0074 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `escala` | 88 | 68 | +20 |
| 2 | `pesquisa` | 77 | 67 | +10 |
| 3 | `analitico` | 158 | 148 | +10 |
| 4 | `clinica` | 87 | 78 | +9 |
| 5 | `momento` | 100 | 91 | +9 |
| 6 | `disponivel` | 114 | 105 | +9 |
| 7 | `parametros` | 137 | 128 | +9 |
| 8 | `processamento` | 73 | 65 | +8 |
| 9 | `mapa` | 144 | 136 | +8 |
| 10 | `codigo` | 94 | 88 | +6 |
| 11 | `carrega` | 120 | 114 | +6 |
| 12 | `frequencia` | 129 | 123 | +6 |
| 13 | `grade` | 140 | 134 | +6 |
| 14 | `argumento` | 92 | 87 | +5 |
| 15 | `coeficientes` | 103 | 98 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `spira` | 0.5541 |
| 2 | `inscricao` | 0.2188 |
| 3 | `covideiro` | 0.2011 |
| 4 | `rede` | 0.1094 |
| 5 | `cadeia` | 0.0942 |
| 6 | `objeto` | 0.0929 |
| 7 | `artigo` | 0.0794 |
| 8 | `respiratoria` | 0.0776 |
| 9 | `modelo` | 0.0740 |
| 10 | `projeto` | 0.0706 |
| 11 | `dado` | 0.0653 |
| 12 | `espectrograma` | 0.0541 |
| 13 | `coleta` | 0.0330 |
| 14 | `marcelo` | 0.0325 |
| 15 | `sinal` | 0.0305 |
| 16 | `insuficiencia` | 0.0273 |
| 17 | `ruido` | 0.0263 |
| 18 | `pratica` | 0.0238 |
| 19 | `torna` | 0.0231 |
| 20 | `audio` | 0.0207 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `respiratoria` | `insuficiencia` | 0.844 | 317 |
| 2 | `imutavel` | `movel` | 0.843 | 81 |
| 3 | `escuta` | `clinica` | 0.638 | 42 |
| 4 | `neural` | `rede` | 0.599 | 147 |
| 5 | `acao` | `programa` | 0.565 | 38 |
| 6 | `linguagem` | `processamento` | 0.560 | 33 |
| 7 | `sinal` | `acustico` | 0.545 | 61 |
| 8 | `tornou` | `possivel` | 0.533 | 34 |
| 9 | `mapa` | `analitico` | 0.530 | 25 |
| 10 | `entrevista` | `marcelo` | 0.502 | 100 |
| 11 | `acesso` | `disponivel` | 0.493 | 25 |
| 12 | `publico` | `repositorio` | 0.488 | 24 |
| 13 | `enfermaria` | `ruido` | 0.486 | 57 |
| 14 | `torna` | `visivel` | 0.482 | 45 |
| 15 | `modelo` | `treinado` | 0.480 | 58 |
| 16 | `covideiro` | `pandemico` | 0.475 | 97 |
| 17 | `ciencia` | `construcao` | 0.459 | 19 |
| 18 | `fonoaudiologos` | `medicos` | 0.459 | 28 |
| 19 | `condicoes` | `producao` | 0.457 | 54 |
| 20 | `tornar` | `visivel` | 0.455 | 20 |
| 21 | `textual` | `analise` | 0.439 | 27 |
| 22 | `publico` | `saude` | 0.436 | 18 |
| 23 | `controles` | `enfermaria` | 0.426 | 27 |
| 24 | `conceito` | `referencia` | 0.424 | 16 |
| 25 | `tornou` | `visivel` | 0.421 | 21 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (40 termos): dado, modelo, espectrograma, audio, sinal, arquivo
- **Tópico 2** (39 termos): inscricao, cadeia, secao, torna, dispositivo, ponto
- **Tópico 3** (33 termos): spira, artigo, projeto, marcelo, artigos, cientifico
- **Tópico 4** (32 termos): respiratoria, insuficiencia, coleta, covid, condicoes, pacientes
- **Tópico 5** (15 termos): covideiro, actante, pandemico, virus, sistema, humano
- **Tópico 6** (11 termos): rede, analise, neural, textual, associacao, arquitetura
- **Tópico 7** (10 termos): objeto, pratica, produz, distintas, distintos, diferentes

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 2** [inscricao, cadeia, secao] e **Tópico 4** [respiratoria, insuficiencia, coleta] — densidade ponderada de ligação = 0.6050
- Lacuna entre **Tópico 1** [dado, modelo, espectrograma] e **Tópico 2** [inscricao, cadeia, secao] — densidade ponderada de ligação = 0.7051
- Lacuna entre **Tópico 1** [dado, modelo, espectrograma] e **Tópico 4** [respiratoria, insuficiencia, coleta] — densidade ponderada de ligação = 0.8883
- Lacuna entre **Tópico 1** [dado, modelo, espectrograma] e **Tópico 3** [spira, artigo, projeto] — densidade ponderada de ligação = 0.9402
- Lacuna entre **Tópico 3** [spira, artigo, projeto] e **Tópico 4** [respiratoria, insuficiencia, coleta] — densidade ponderada de ligação = 1.0909
- Lacuna entre **Tópico 2** [inscricao, cadeia, secao] e **Tópico 5** [covideiro, actante, pandemico] — densidade ponderada de ligação = 1.1179

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
