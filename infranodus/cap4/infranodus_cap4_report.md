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
- Tokens significativos: **32,888**
- Grafo bruto: **6764** nós · **78421** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **4030** arestas
- Tópicos detectados (Louvain): **7**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `spira` | 1911 |
| 2 | `covideiro` | 1179 |
| 3 | `inscricao` | 1128 |
| 4 | `cadeia` | 1047 |
| 5 | `rede` | 1004 |
| 6 | `artigo` | 895 |
| 7 | `objeto` | 885 |
| 8 | `respiratoria` | 763 |
| 9 | `dado` | 732 |
| 10 | `insuficiencia` | 726 |
| 11 | `modelo` | 664 |
| 12 | `projeto` | 658 |
| 13 | `marcelo` | 617 |
| 14 | `artigos` | 535 |
| 15 | `espectrograma` | 533 |
| 16 | `coleta` | 503 |
| 17 | `actante` | 463 |
| 18 | `condicoes` | 436 |
| 19 | `cientifico` | 432 |
| 20 | `pratica` | 422 |
| 21 | `covid` | 422 |
| 22 | `audio` | 414 |
| 23 | `partir` | 406 |
| 24 | `analise` | 392 |
| 25 | `pacientes` | 385 |
| 26 | `sinal` | 384 |
| 27 | `ruido` | 376 |
| 28 | `secao` | 362 |
| 29 | `dispositivo` | 351 |
| 30 | `laboratorio` | 350 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `spira` | 0.0373 |
| 2 | `covideiro` | 0.0232 |
| 3 | `inscricao` | 0.0226 |
| 4 | `cadeia` | 0.0209 |
| 5 | `rede` | 0.0201 |
| 6 | `artigo` | 0.0178 |
| 7 | `objeto` | 0.0178 |
| 8 | `dado` | 0.0148 |
| 9 | `respiratoria` | 0.0143 |
| 10 | `modelo` | 0.0138 |
| 11 | `insuficiencia` | 0.0136 |
| 12 | `projeto` | 0.0132 |
| 13 | `marcelo` | 0.0125 |
| 14 | `espectrograma` | 0.0111 |
| 15 | `artigos` | 0.0107 |
| 16 | `coleta` | 0.0105 |
| 17 | `actante` | 0.0097 |
| 18 | `pratica` | 0.0090 |
| 19 | `condicoes` | 0.0090 |
| 20 | `audio` | 0.0088 |
| 21 | `covid` | 0.0088 |
| 22 | `cientifico` | 0.0088 |
| 23 | `partir` | 0.0085 |
| 24 | `sinal` | 0.0083 |
| 25 | `ruido` | 0.0083 |
| 26 | `pacientes` | 0.0081 |
| 27 | `analise` | 0.0081 |
| 28 | `secao` | 0.0078 |
| 29 | `torna` | 0.0077 |
| 30 | `laboratorio` | 0.0076 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `escala` | 82 | 69 | +13 |
| 2 | `clinica` | 89 | 79 | +10 |
| 3 | `pesquisa` | 74 | 65 | +9 |
| 4 | `disponivel` | 108 | 99 | +9 |
| 5 | `algoritmo` | 71 | 63 | +8 |
| 6 | `processamento` | 80 | 73 | +7 |
| 7 | `resultado` | 88 | 81 | +7 |
| 8 | `coeficientes` | 98 | 91 | +7 |
| 9 | `grade` | 139 | 132 | +7 |
| 10 | `analitico` | 165 | 158 | +7 |
| 11 | `escolha` | 117 | 111 | +6 |
| 12 | `mapa` | 142 | 136 | +6 |
| 13 | `momento` | 95 | 90 | +5 |
| 14 | `pessoas` | 109 | 104 | +5 |
| 15 | `linguagem` | 144 | 139 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `spira` | 0.5351 |
| 2 | `inscricao` | 0.2324 |
| 3 | `covideiro` | 0.2068 |
| 4 | `cadeia` | 0.1194 |
| 5 | `rede` | 0.1050 |
| 6 | `artigo` | 0.0972 |
| 7 | `objeto` | 0.0937 |
| 8 | `modelo` | 0.0747 |
| 9 | `respiratoria` | 0.0679 |
| 10 | `espectrograma` | 0.0651 |
| 11 | `dado` | 0.0638 |
| 12 | `projeto` | 0.0486 |
| 13 | `coleta` | 0.0329 |
| 14 | `ruido` | 0.0293 |
| 15 | `sinal` | 0.0282 |
| 16 | `marcelo` | 0.0262 |
| 17 | `insuficiencia` | 0.0239 |
| 18 | `pratica` | 0.0237 |
| 19 | `torna` | 0.0234 |
| 20 | `instituicao` | 0.0215 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `respiratoria` | `insuficiencia` | 0.844 | 308 |
| 2 | `imutavel` | `movel` | 0.842 | 81 |
| 3 | `calculo` | `centro` | 0.772 | 85 |
| 4 | `escuta` | `clinica` | 0.641 | 42 |
| 5 | `neural` | `rede` | 0.590 | 127 |
| 6 | `acao` | `programa` | 0.567 | 38 |
| 7 | `sinal` | `acustico` | 0.548 | 61 |
| 8 | `tornou` | `possivel` | 0.535 | 34 |
| 9 | `mapa` | `analitico` | 0.529 | 25 |
| 10 | `linguagem` | `processamento` | 0.526 | 27 |
| 11 | `entrevista` | `marcelo` | 0.505 | 100 |
| 12 | `acesso` | `disponivel` | 0.497 | 24 |
| 13 | `publico` | `repositorio` | 0.497 | 24 |
| 14 | `enfermaria` | `ruido` | 0.488 | 57 |
| 15 | `torna` | `visivel` | 0.483 | 45 |
| 16 | `covideiro` | `pandemico` | 0.477 | 97 |
| 17 | `condicoes` | `producao` | 0.470 | 51 |
| 18 | `publico` | `saude` | 0.467 | 18 |
| 19 | `ciencia` | `construcao` | 0.462 | 19 |
| 20 | `modelo` | `treinado` | 0.459 | 49 |
| 21 | `fonoaudiologos` | `medicos` | 0.457 | 28 |
| 22 | `tornar` | `visivel` | 0.454 | 20 |
| 23 | `cadeia` | `translacoes` | 0.437 | 51 |
| 24 | `textual` | `analise` | 0.435 | 27 |
| 25 | `controles` | `enfermaria` | 0.425 | 27 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (43 termos): dado, modelo, espectrograma, audio, sinal, paciente
- **Tópico 2** (40 termos): inscricao, cadeia, secao, dispositivo, torna, ponto
- **Tópico 3** (31 termos): spira, artigo, projeto, marcelo, artigos, cientifico
- **Tópico 4** (22 termos): respiratoria, insuficiencia, coleta, condicoes, covid, pacientes
- **Tópico 5** (20 termos): covideiro, actante, pandemico, virus, humano, configuracao
- **Tópico 6** (12 termos): rede, partir, analise, neural, textual, associacao
- **Tópico 7** (12 termos): objeto, pratica, condicao, distintas, distintos, diferentes

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 2** [inscricao, cadeia, secao] e **Tópico 4** [respiratoria, insuficiencia, coleta] — densidade ponderada de ligação = 0.6568
- Lacuna entre **Tópico 1** [dado, modelo, espectrograma] e **Tópico 2** [inscricao, cadeia, secao] — densidade ponderada de ligação = 0.7023
- Lacuna entre **Tópico 1** [dado, modelo, espectrograma] e **Tópico 3** [spira, artigo, projeto] — densidade ponderada de ligação = 0.8875
- Lacuna entre **Tópico 2** [inscricao, cadeia, secao] e **Tópico 5** [covideiro, actante, pandemico] — densidade ponderada de ligação = 0.9313
- Lacuna entre **Tópico 1** [dado, modelo, espectrograma] e **Tópico 4** [respiratoria, insuficiencia, coleta] — densidade ponderada de ligação = 0.9450
- Lacuna entre **Tópico 1** [dado, modelo, espectrograma] e **Tópico 5** [covideiro, actante, pandemico] — densidade ponderada de ligação = 0.9860

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
