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
- Tokens significativos: **32,805**
- Grafo bruto: **6746** nós · **78070** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **4026** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `spira` | 1961 |
| 2 | `covideiro` | 1159 |
| 3 | `inscricao` | 1128 |
| 4 | `cadeia` | 1030 |
| 5 | `rede` | 938 |
| 6 | `objeto` | 903 |
| 7 | `artigo` | 887 |
| 8 | `respiratoria` | 778 |
| 9 | `insuficiencia` | 745 |
| 10 | `dado` | 728 |
| 11 | `projeto` | 671 |
| 12 | `modelo` | 654 |
| 13 | `marcelo` | 627 |
| 14 | `artigos` | 527 |
| 15 | `espectrograma` | 510 |
| 16 | `coleta` | 506 |
| 17 | `actante` | 470 |
| 18 | `pratica` | 454 |
| 19 | `condicoes` | 437 |
| 20 | `cientifico` | 432 |
| 21 | `covid` | 418 |
| 22 | `audio` | 410 |
| 23 | `sinal` | 389 |
| 24 | `partir` | 389 |
| 25 | `pacientes` | 388 |
| 26 | `analise` | 381 |
| 27 | `secao` | 379 |
| 28 | `ruido` | 374 |
| 29 | `torna` | 355 |
| 30 | `dispositivo` | 351 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `spira` | 0.0383 |
| 2 | `covideiro` | 0.0229 |
| 3 | `inscricao` | 0.0227 |
| 4 | `cadeia` | 0.0207 |
| 5 | `rede` | 0.0190 |
| 6 | `objeto` | 0.0181 |
| 7 | `artigo` | 0.0177 |
| 8 | `dado` | 0.0147 |
| 9 | `respiratoria` | 0.0146 |
| 10 | `insuficiencia` | 0.0139 |
| 11 | `modelo` | 0.0137 |
| 12 | `projeto` | 0.0136 |
| 13 | `marcelo` | 0.0127 |
| 14 | `espectrograma` | 0.0107 |
| 15 | `coleta` | 0.0106 |
| 16 | `artigos` | 0.0105 |
| 17 | `actante` | 0.0098 |
| 18 | `pratica` | 0.0096 |
| 19 | `condicoes` | 0.0091 |
| 20 | `cientifico` | 0.0088 |
| 21 | `audio` | 0.0088 |
| 22 | `covid` | 0.0088 |
| 23 | `sinal` | 0.0084 |
| 24 | `ruido` | 0.0083 |
| 25 | `partir` | 0.0082 |
| 26 | `pacientes` | 0.0082 |
| 27 | `secao` | 0.0081 |
| 28 | `analise` | 0.0079 |
| 29 | `torna` | 0.0078 |
| 30 | `laboratorio` | 0.0076 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `escala` | 77 | 62 | +15 |
| 2 | `disponivel` | 108 | 97 | +11 |
| 3 | `coeficientes` | 104 | 94 | +10 |
| 4 | `momento` | 107 | 99 | +8 |
| 5 | `pesquisa` | 73 | 66 | +7 |
| 6 | `processamento` | 78 | 71 | +7 |
| 7 | `escolha` | 115 | 108 | +7 |
| 8 | `mapa` | 145 | 138 | +7 |
| 9 | `parametros` | 153 | 146 | +7 |
| 10 | `grade` | 135 | 129 | +6 |
| 11 | `repositorio` | 72 | 67 | +5 |
| 12 | `relatorios` | 92 | 87 | +5 |
| 13 | `grupo` | 109 | 104 | +5 |
| 14 | `onda` | 116 | 111 | +5 |
| 15 | `pessoas` | 123 | 118 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `spira` | 0.5903 |
| 2 | `inscricao` | 0.2425 |
| 3 | `covideiro` | 0.1851 |
| 4 | `cadeia` | 0.1396 |
| 5 | `rede` | 0.1085 |
| 6 | `objeto` | 0.0972 |
| 7 | `artigo` | 0.0949 |
| 8 | `modelo` | 0.0748 |
| 9 | `respiratoria` | 0.0738 |
| 10 | `dado` | 0.0539 |
| 11 | `espectrograma` | 0.0495 |
| 12 | `projeto` | 0.0485 |
| 13 | `torna` | 0.0335 |
| 14 | `ruido` | 0.0289 |
| 15 | `coleta` | 0.0272 |
| 16 | `sinal` | 0.0264 |
| 17 | `pratica` | 0.0241 |
| 18 | `marcelo` | 0.0229 |
| 19 | `insuficiencia` | 0.0229 |
| 20 | `instituicao` | 0.0215 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `imutavel` | `movel` | 0.845 | 82 |
| 2 | `respiratoria` | `insuficiencia` | 0.844 | 317 |
| 3 | `calculo` | `centro` | 0.772 | 85 |
| 4 | `escuta` | `clinica` | 0.610 | 39 |
| 5 | `neural` | `rede` | 0.585 | 121 |
| 6 | `acao` | `programa` | 0.567 | 38 |
| 7 | `sinal` | `acustico` | 0.548 | 61 |
| 8 | `mapa` | `analitico` | 0.547 | 27 |
| 9 | `tornou` | `possivel` | 0.538 | 34 |
| 10 | `linguagem` | `processamento` | 0.521 | 27 |
| 11 | `publico` | `saude` | 0.502 | 22 |
| 12 | `acesso` | `disponivel` | 0.500 | 24 |
| 13 | `publico` | `repositorio` | 0.497 | 24 |
| 14 | `entrevista` | `marcelo` | 0.493 | 100 |
| 15 | `torna` | `visivel` | 0.490 | 48 |
| 16 | `enfermaria` | `ruido` | 0.488 | 57 |
| 17 | `covideiro` | `pandemico` | 0.476 | 97 |
| 18 | `condicoes` | `producao` | 0.471 | 51 |
| 19 | `ciencia` | `construcao` | 0.471 | 19 |
| 20 | `modelo` | `treinado` | 0.460 | 49 |
| 21 | `fonoaudiologos` | `medicos` | 0.457 | 28 |
| 22 | `cadeia` | `translacoes` | 0.454 | 57 |
| 23 | `tornar` | `visivel` | 0.451 | 20 |
| 24 | `conceito` | `referencia` | 0.432 | 16 |
| 25 | `controles` | `enfermaria` | 0.425 | 27 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (44 termos): dado, modelo, espectrograma, audio, sinal, paciente
- **Tópico 2** (38 termos): inscricao, cadeia, analise, secao, torna, dispositivo
- **Tópico 3** (25 termos): covideiro, actante, condicoes, laboratorio, pandemico, humano
- **Tópico 4** (24 termos): respiratoria, insuficiencia, coleta, covid, pacientes, ruido
- **Tópico 5** (24 termos): spira, artigo, projeto, marcelo, artigos, cientifico
- **Tópico 6** (9 termos): rede, partir, neural, associacao, arquitetura, ator
- **Tópico 7** (9 termos): objeto, pratica, distintas, distintos, diferentes, produzido
- **Tópico 8** (7 termos): virus, aparece, ausencia, carrega, presenca, microfone

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 2** [inscricao, cadeia, analise] e **Tópico 4** [respiratoria, insuficiencia, coleta] — densidade ponderada de ligação = 0.6096
- Lacuna entre **Tópico 1** [dado, modelo, espectrograma] e **Tópico 3** [covideiro, actante, condicoes] — densidade ponderada de ligação = 0.7509
- Lacuna entre **Tópico 1** [dado, modelo, espectrograma] e **Tópico 2** [inscricao, cadeia, analise] — densidade ponderada de ligação = 0.7638
- Lacuna entre **Tópico 1** [dado, modelo, espectrograma] e **Tópico 4** [respiratoria, insuficiencia, coleta] — densidade ponderada de ligação = 0.9129
- Lacuna entre **Tópico 2** [inscricao, cadeia, analise] e **Tópico 3** [covideiro, actante, condicoes] — densidade ponderada de ligação = 0.9747
- Lacuna entre **Tópico 1** [dado, modelo, espectrograma] e **Tópico 5** [spira, artigo, projeto] — densidade ponderada de ligação = 1.0009

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
