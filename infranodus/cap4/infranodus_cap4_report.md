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
- Tokens significativos: **33,486**
- Grafo bruto: **6835** nós · **79789** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **4074** arestas
- Tópicos detectados (Louvain): **7**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `spira` | 1969 |
| 2 | `covideiro` | 1178 |
| 3 | `inscricao` | 1133 |
| 4 | `rede` | 1048 |
| 5 | `cadeia` | 1036 |
| 6 | `artigo` | 901 |
| 7 | `objeto` | 873 |
| 8 | `respiratoria` | 786 |
| 9 | `insuficiencia` | 748 |
| 10 | `dado` | 742 |
| 11 | `projeto` | 725 |
| 12 | `modelo` | 685 |
| 13 | `marcelo` | 645 |
| 14 | `artigos` | 545 |
| 15 | `espectrograma` | 534 |
| 16 | `coleta` | 514 |
| 17 | `actante` | 468 |
| 18 | `covid` | 451 |
| 19 | `condicoes` | 445 |
| 20 | `cientifico` | 441 |
| 21 | `partir` | 426 |
| 22 | `pratica` | 425 |
| 23 | `audio` | 423 |
| 24 | `pacientes` | 408 |
| 25 | `analise` | 393 |
| 26 | `sinal` | 385 |
| 27 | `ruido` | 374 |
| 28 | `torna` | 358 |
| 29 | `secao` | 356 |
| 30 | `dispositivo` | 351 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `spira` | 0.0378 |
| 2 | `covideiro` | 0.0228 |
| 3 | `inscricao` | 0.0223 |
| 4 | `rede` | 0.0206 |
| 5 | `cadeia` | 0.0203 |
| 6 | `artigo` | 0.0176 |
| 7 | `objeto` | 0.0173 |
| 8 | `dado` | 0.0147 |
| 9 | `respiratoria` | 0.0144 |
| 10 | `projeto` | 0.0143 |
| 11 | `modelo` | 0.0139 |
| 12 | `insuficiencia` | 0.0137 |
| 13 | `marcelo` | 0.0128 |
| 14 | `espectrograma` | 0.0109 |
| 15 | `artigos` | 0.0107 |
| 16 | `coleta` | 0.0105 |
| 17 | `actante` | 0.0096 |
| 18 | `covid` | 0.0091 |
| 19 | `condicoes` | 0.0090 |
| 20 | `pratica` | 0.0089 |
| 21 | `audio` | 0.0088 |
| 22 | `cientifico` | 0.0088 |
| 23 | `partir` | 0.0087 |
| 24 | `pacientes` | 0.0084 |
| 25 | `sinal` | 0.0082 |
| 26 | `ruido` | 0.0081 |
| 27 | `analise` | 0.0079 |
| 28 | `torna` | 0.0078 |
| 29 | `secao` | 0.0075 |
| 30 | `centro` | 0.0075 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `escala` | 79 | 66 | +13 |
| 2 | `parametros` | 141 | 129 | +12 |
| 3 | `clinica` | 86 | 77 | +9 |
| 4 | `resultado` | 94 | 85 | +9 |
| 5 | `processamento` | 77 | 69 | +8 |
| 6 | `mapa` | 147 | 139 | +8 |
| 7 | `analitico` | 161 | 154 | +7 |
| 8 | `acesso` | 90 | 84 | +6 |
| 9 | `movimento` | 95 | 89 | +6 |
| 10 | `carrega` | 118 | 112 | +6 |
| 11 | `frequencia` | 132 | 126 | +6 |
| 12 | `grade` | 140 | 134 | +6 |
| 13 | `diferenca` | 148 | 142 | +6 |
| 14 | `frequencias` | 150 | 144 | +6 |
| 15 | `codigo` | 92 | 87 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `spira` | 0.5488 |
| 2 | `inscricao` | 0.2200 |
| 3 | `covideiro` | 0.2017 |
| 4 | `rede` | 0.1080 |
| 5 | `cadeia` | 0.1043 |
| 6 | `objeto` | 0.0814 |
| 7 | `artigo` | 0.0799 |
| 8 | `respiratoria` | 0.0775 |
| 9 | `modelo` | 0.0740 |
| 10 | `projeto` | 0.0705 |
| 11 | `dado` | 0.0662 |
| 12 | `espectrograma` | 0.0538 |
| 13 | `coleta` | 0.0336 |
| 14 | `marcelo` | 0.0324 |
| 15 | `sinal` | 0.0305 |
| 16 | `insuficiencia` | 0.0274 |
| 17 | `ruido` | 0.0266 |
| 18 | `torna` | 0.0235 |
| 19 | `pratica` | 0.0235 |
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
| 3 | `calculo` | `centro` | 0.737 | 85 |
| 4 | `escuta` | `clinica` | 0.638 | 42 |
| 5 | `neural` | `rede` | 0.597 | 144 |
| 6 | `acao` | `programa` | 0.565 | 38 |
| 7 | `linguagem` | `processamento` | 0.556 | 33 |
| 8 | `sinal` | `acustico` | 0.545 | 61 |
| 9 | `tornou` | `possivel` | 0.533 | 34 |
| 10 | `mapa` | `analitico` | 0.530 | 25 |
| 11 | `acesso` | `disponivel` | 0.510 | 28 |
| 12 | `entrevista` | `marcelo` | 0.502 | 100 |
| 13 | `enfermaria` | `ruido` | 0.486 | 57 |
| 14 | `publico` | `repositorio` | 0.485 | 24 |
| 15 | `torna` | `visivel` | 0.480 | 45 |
| 16 | `modelo` | `treinado` | 0.480 | 58 |
| 17 | `covideiro` | `pandemico` | 0.474 | 97 |
| 18 | `ciencia` | `construcao` | 0.464 | 19 |
| 19 | `fonoaudiologos` | `medicos` | 0.459 | 28 |
| 20 | `tornar` | `visivel` | 0.455 | 20 |
| 21 | `condicoes` | `producao` | 0.453 | 54 |
| 22 | `textual` | `analise` | 0.438 | 27 |
| 23 | `cadeia` | `translacoes` | 0.437 | 51 |
| 24 | `publico` | `saude` | 0.434 | 18 |
| 25 | `controles` | `enfermaria` | 0.426 | 27 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (38 termos): inscricao, cadeia, torna, secao, dispositivo, ponto
- **Tópico 2** (38 termos): spira, artigo, projeto, marcelo, artigos, cientifico
- **Tópico 3** (36 termos): dado, modelo, espectrograma, audio, sinal, arquivo
- **Tópico 4** (30 termos): covideiro, coleta, actante, condicoes, pandemico, virus
- **Tópico 5** (17 termos): respiratoria, insuficiencia, covid, pacientes, ruido, enfermaria
- **Tópico 6** (11 termos): rede, analise, neural, textual, associacao, arquitetura
- **Tópico 7** (10 termos): objeto, pratica, condicao, distintos, distintas, clinica

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [inscricao, cadeia, torna] e **Tópico 5** [respiratoria, insuficiencia, covid] — densidade ponderada de ligação = 0.5093
- Lacuna entre **Tópico 1** [inscricao, cadeia, torna] e **Tópico 3** [dado, modelo, espectrograma] — densidade ponderada de ligação = 0.7763
- Lacuna entre **Tópico 1** [inscricao, cadeia, torna] e **Tópico 4** [covideiro, coleta, actante] — densidade ponderada de ligação = 0.8974
- Lacuna entre **Tópico 2** [spira, artigo, projeto] e **Tópico 3** [dado, modelo, espectrograma] — densidade ponderada de ligação = 0.9371
- Lacuna entre **Tópico 3** [dado, modelo, espectrograma] e **Tópico 4** [covideiro, coleta, actante] — densidade ponderada de ligação = 0.9750
- Lacuna entre **Tópico 2** [spira, artigo, projeto] e **Tópico 5** [respiratoria, insuficiencia, covid] — densidade ponderada de ligação = 1.0480

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
