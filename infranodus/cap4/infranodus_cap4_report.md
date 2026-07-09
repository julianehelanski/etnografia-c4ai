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
- Tokens significativos: **32,793**
- Grafo bruto: **6762** nós · **78208** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **4022** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `spira` | 1908 |
| 2 | `covideiro` | 1185 |
| 3 | `inscricao` | 1107 |
| 4 | `cadeia` | 1041 |
| 5 | `rede` | 950 |
| 6 | `artigo` | 890 |
| 7 | `objeto` | 888 |
| 8 | `respiratoria` | 765 |
| 9 | `insuficiencia` | 730 |
| 10 | `dado` | 730 |
| 11 | `modelo` | 664 |
| 12 | `projeto` | 655 |
| 13 | `marcelo` | 620 |
| 14 | `espectrograma` | 538 |
| 15 | `artigos` | 527 |
| 16 | `coleta` | 503 |
| 17 | `actante` | 461 |
| 18 | `condicoes` | 436 |
| 19 | `cientifico` | 430 |
| 20 | `pratica` | 422 |
| 21 | `covid` | 420 |
| 22 | `audio` | 417 |
| 23 | `partir` | 403 |
| 24 | `pacientes` | 385 |
| 25 | `sinal` | 384 |
| 26 | `ruido` | 376 |
| 27 | `secao` | 360 |
| 28 | `analise` | 357 |
| 29 | `laboratorio` | 350 |
| 30 | `dispositivo` | 349 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `spira` | 0.0374 |
| 2 | `covideiro` | 0.0234 |
| 3 | `inscricao` | 0.0223 |
| 4 | `cadeia` | 0.0209 |
| 5 | `rede` | 0.0191 |
| 6 | `objeto` | 0.0179 |
| 7 | `artigo` | 0.0178 |
| 8 | `dado` | 0.0148 |
| 9 | `respiratoria` | 0.0145 |
| 10 | `modelo` | 0.0139 |
| 11 | `insuficiencia` | 0.0138 |
| 12 | `projeto` | 0.0132 |
| 13 | `marcelo` | 0.0126 |
| 14 | `espectrograma` | 0.0113 |
| 15 | `artigos` | 0.0106 |
| 16 | `coleta` | 0.0105 |
| 17 | `actante` | 0.0097 |
| 18 | `pratica` | 0.0091 |
| 19 | `condicoes` | 0.0091 |
| 20 | `audio` | 0.0089 |
| 21 | `covid` | 0.0088 |
| 22 | `cientifico` | 0.0088 |
| 23 | `partir` | 0.0085 |
| 24 | `sinal` | 0.0083 |
| 25 | `ruido` | 0.0083 |
| 26 | `pacientes` | 0.0081 |
| 27 | `secao` | 0.0077 |
| 28 | `torna` | 0.0076 |
| 29 | `laboratorio` | 0.0076 |
| 30 | `ponto` | 0.0076 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `escala` | 82 | 66 | +16 |
| 2 | `clinica` | 89 | 79 | +10 |
| 3 | `grade` | 137 | 127 | +10 |
| 4 | `leitor` | 126 | 117 | +9 |
| 5 | `coeficientes` | 95 | 87 | +8 |
| 6 | `pesquisa` | 74 | 67 | +7 |
| 7 | `resultado` | 88 | 81 | +7 |
| 8 | `processamento` | 79 | 73 | +6 |
| 9 | `momento` | 94 | 88 | +6 |
| 10 | `onda` | 115 | 109 | +6 |
| 11 | `acesso` | 127 | 121 | +6 |
| 12 | `linguagem` | 141 | 135 | +6 |
| 13 | `frequencia` | 150 | 144 | +6 |
| 14 | `microfone` | 154 | 148 | +6 |
| 15 | `torna` | 33 | 28 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `spira` | 0.5434 |
| 2 | `inscricao` | 0.2277 |
| 3 | `covideiro` | 0.2075 |
| 4 | `cadeia` | 0.1273 |
| 5 | `artigo` | 0.0970 |
| 6 | `rede` | 0.0969 |
| 7 | `objeto` | 0.0936 |
| 8 | `respiratoria` | 0.0749 |
| 9 | `modelo` | 0.0746 |
| 10 | `espectrograma` | 0.0647 |
| 11 | `dado` | 0.0638 |
| 12 | `projeto` | 0.0485 |
| 13 | `insuficiencia` | 0.0329 |
| 14 | `coleta` | 0.0327 |
| 15 | `ruido` | 0.0293 |
| 16 | `sinal` | 0.0282 |
| 17 | `marcelo` | 0.0260 |
| 18 | `pratica` | 0.0237 |
| 19 | `torna` | 0.0232 |
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
| 4 | `escuta` | `clinica` | 0.640 | 42 |
| 5 | `neural` | `rede` | 0.591 | 127 |
| 6 | `acao` | `programa` | 0.567 | 38 |
| 7 | `sinal` | `acustico` | 0.548 | 61 |
| 8 | `tornou` | `possivel` | 0.535 | 34 |
| 9 | `mapa` | `analitico` | 0.529 | 25 |
| 10 | `linguagem` | `processamento` | 0.525 | 27 |
| 11 | `entrevista` | `marcelo` | 0.504 | 100 |
| 12 | `publico` | `repositorio` | 0.497 | 24 |
| 13 | `acesso` | `disponivel` | 0.493 | 24 |
| 14 | `enfermaria` | `ruido` | 0.488 | 57 |
| 15 | `torna` | `visivel` | 0.482 | 45 |
| 16 | `covideiro` | `pandemico` | 0.477 | 97 |
| 17 | `condicoes` | `producao` | 0.470 | 51 |
| 18 | `publico` | `saude` | 0.467 | 18 |
| 19 | `ciencia` | `construcao` | 0.462 | 19 |
| 20 | `modelo` | `treinado` | 0.459 | 49 |
| 21 | `fonoaudiologos` | `medicos` | 0.457 | 28 |
| 22 | `tornar` | `visivel` | 0.454 | 20 |
| 23 | `cadeia` | `translacoes` | 0.436 | 51 |
| 24 | `conceito` | `referencia` | 0.431 | 16 |
| 25 | `controles` | `enfermaria` | 0.425 | 27 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (35 termos): inscricao, cadeia, secao, dispositivo, ponto, torna
- **Tópico 2** (34 termos): dado, modelo, audio, sinal, ruido, enfermaria
- **Tópico 3** (29 termos): covideiro, coleta, actante, condicoes, laboratorio, pandemico
- **Tópico 4** (25 termos): espectrograma, paciente, arquivo, virus, produz, imagem
- **Tópico 5** (24 termos): spira, artigo, projeto, marcelo, artigos, cientifico
- **Tópico 6** (12 termos): objeto, pratica, condicao, distintas, distintos, diferentes
- **Tópico 7** (11 termos): respiratoria, insuficiencia, covid, pacientes, acustica, deteccao
- **Tópico 8** (10 termos): rede, partir, neural, associacao, topologia, arquitetura

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [inscricao, cadeia, secao] e **Tópico 2** [dado, modelo, audio] — densidade ponderada de ligação = 0.5908
- Lacuna entre **Tópico 3** [covideiro, coleta, actante] e **Tópico 4** [espectrograma, paciente, arquivo] — densidade ponderada de ligação = 0.7572
- Lacuna entre **Tópico 2** [dado, modelo, audio] e **Tópico 4** [espectrograma, paciente, arquivo] — densidade ponderada de ligação = 0.8071
- Lacuna entre **Tópico 2** [dado, modelo, audio] e **Tópico 3** [covideiro, coleta, actante] — densidade ponderada de ligação = 0.8611
- Lacuna entre **Tópico 1** [inscricao, cadeia, secao] e **Tópico 4** [espectrograma, paciente, arquivo] — densidade ponderada de ligação = 0.8617
- Lacuna entre **Tópico 4** [espectrograma, paciente, arquivo] e **Tópico 5** [spira, artigo, projeto] — densidade ponderada de ligação = 0.9383

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
