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
- Tokens significativos: **32,361**
- Grafo bruto: **6703** nós · **77315** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **3995** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `spira` | 1864 |
| 2 | `covideiro` | 1181 |
| 3 | `inscricao` | 1056 |
| 4 | `rede` | 1028 |
| 5 | `cadeia` | 905 |
| 6 | `artigo` | 855 |
| 7 | `objeto` | 816 |
| 8 | `dado` | 750 |
| 9 | `respiratoria` | 733 |
| 10 | `insuficiencia` | 703 |
| 11 | `marcelo` | 660 |
| 12 | `modelo` | 656 |
| 13 | `projeto` | 646 |
| 14 | `espectrograma` | 550 |
| 15 | `artigos` | 504 |
| 16 | `coleta` | 499 |
| 17 | `pratica` | 419 |
| 18 | `actante` | 412 |
| 19 | `partir` | 408 |
| 20 | `sinal` | 401 |
| 21 | `covid` | 401 |
| 22 | `audio` | 394 |
| 23 | `pacientes` | 374 |
| 24 | `condicoes` | 372 |
| 25 | `ruido` | 371 |
| 26 | `dataset` | 354 |
| 27 | `cientifico` | 346 |
| 28 | `analise` | 342 |
| 29 | `secao` | 341 |
| 30 | `laboratorio` | 340 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `spira` | 0.0375 |
| 2 | `covideiro` | 0.0241 |
| 3 | `inscricao` | 0.0219 |
| 4 | `rede` | 0.0209 |
| 5 | `cadeia` | 0.0187 |
| 6 | `artigo` | 0.0176 |
| 7 | `objeto` | 0.0169 |
| 8 | `dado` | 0.0156 |
| 9 | `respiratoria` | 0.0142 |
| 10 | `modelo` | 0.0140 |
| 11 | `marcelo` | 0.0138 |
| 12 | `insuficiencia` | 0.0136 |
| 13 | `projeto` | 0.0134 |
| 14 | `espectrograma` | 0.0117 |
| 15 | `coleta` | 0.0108 |
| 16 | `artigos` | 0.0104 |
| 17 | `pratica` | 0.0092 |
| 18 | `actante` | 0.0090 |
| 19 | `sinal` | 0.0089 |
| 20 | `partir` | 0.0088 |
| 21 | `covid` | 0.0087 |
| 22 | `audio` | 0.0086 |
| 23 | `ruido` | 0.0084 |
| 24 | `pacientes` | 0.0082 |
| 25 | `condicoes` | 0.0081 |
| 26 | `dataset` | 0.0078 |
| 27 | `secao` | 0.0076 |
| 28 | `laboratorio` | 0.0075 |
| 29 | `condicao` | 0.0074 |
| 30 | `paciente` | 0.0074 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `microfone` | 106 | 90 | +16 |
| 2 | `frequencia` | 125 | 110 | +15 |
| 3 | `pesquisa` | 77 | 65 | +12 |
| 4 | `escala` | 99 | 88 | +11 |
| 5 | `processamento` | 74 | 64 | +10 |
| 6 | `disponivel` | 98 | 89 | +9 |
| 7 | `coeficientes` | 102 | 93 | +9 |
| 8 | `carrega` | 114 | 105 | +9 |
| 9 | `diante` | 149 | 140 | +9 |
| 10 | `leitor` | 122 | 114 | +8 |
| 11 | `ciencia` | 164 | 157 | +7 |
| 12 | `argumento` | 123 | 117 | +6 |
| 13 | `parametros` | 133 | 127 | +6 |
| 14 | `grade` | 135 | 129 | +6 |
| 15 | `frequencias` | 138 | 133 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `spira` | 0.5237 |
| 2 | `covideiro` | 0.1929 |
| 3 | `inscricao` | 0.1528 |
| 4 | `rede` | 0.1177 |
| 5 | `artigo` | 0.1165 |
| 6 | `objeto` | 0.0984 |
| 7 | `cadeia` | 0.0953 |
| 8 | `respiratoria` | 0.0778 |
| 9 | `modelo` | 0.0692 |
| 10 | `dado` | 0.0627 |
| 11 | `espectrograma` | 0.0575 |
| 12 | `projeto` | 0.0488 |
| 13 | `sinal` | 0.0373 |
| 14 | `pratica` | 0.0349 |
| 15 | `insuficiencia` | 0.0290 |
| 16 | `marcelo` | 0.0282 |
| 17 | `coleta` | 0.0264 |
| 18 | `torna` | 0.0259 |
| 19 | `ruido` | 0.0251 |
| 20 | `covid` | 0.0195 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `imutavel` | `movel` | 0.846 | 78 |
| 2 | `respiratoria` | `insuficiencia` | 0.841 | 303 |
| 3 | `grupo` | `controle` | 0.673 | 49 |
| 4 | `escuta` | `clinica` | 0.623 | 42 |
| 5 | `neural` | `rede` | 0.587 | 141 |
| 6 | `diante` | `microfone` | 0.573 | 30 |
| 7 | `acao` | `programa` | 0.573 | 35 |
| 8 | `linguagem` | `processamento` | 0.558 | 33 |
| 9 | `sinal` | `acustico` | 0.543 | 61 |
| 10 | `tornou` | `possivel` | 0.528 | 34 |
| 11 | `enfermaria` | `ruido` | 0.494 | 65 |
| 12 | `entrevista` | `marcelo` | 0.494 | 98 |
| 13 | `torna` | `visivel` | 0.491 | 42 |
| 14 | `acesso` | `disponivel` | 0.490 | 25 |
| 15 | `publico` | `repositorio` | 0.486 | 24 |
| 16 | `modelo` | `treinado` | 0.480 | 52 |
| 17 | `covideiro` | `pandemico` | 0.478 | 97 |
| 18 | `ciencia` | `construcao` | 0.470 | 19 |
| 19 | `fonoaudiologos` | `medicos` | 0.464 | 22 |
| 20 | `tornar` | `visivel` | 0.464 | 20 |
| 21 | `publico` | `saude` | 0.448 | 18 |
| 22 | `pessoas` | `voz` | 0.444 | 26 |
| 23 | `controles` | `pacientes` | 0.443 | 40 |
| 24 | `tornou` | `visivel` | 0.434 | 21 |
| 25 | `saude` | `pesquisa` | 0.429 | 20 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (37 termos): spira, artigo, marcelo, projeto, artigos, dataset
- **Tópico 2** (34 termos): inscricao, cadeia, actante, analise, secao, ponto
- **Tópico 3** (29 termos): espectrograma, sinal, paciente, torna, arquivo, imagem
- **Tópico 4** (22 termos): dado, modelo, audio, treinamento, repositorio, computacional
- **Tópico 5** (20 termos): respiratoria, insuficiencia, covid, pacientes, ruido, enfermaria
- **Tópico 6** (18 termos): covideiro, coleta, condicoes, pandemico, celular, possivel
- **Tópico 7** (10 termos): rede, partir, neural, associacao, topologia, ator
- **Tópico 8** (10 termos): objeto, pratica, condicao, clinica, distintas, existir

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 2** [inscricao, cadeia, actante] e **Tópico 5** [respiratoria, insuficiencia, covid] — densidade ponderada de ligação = 0.5779
- Lacuna entre **Tópico 2** [inscricao, cadeia, actante] e **Tópico 4** [dado, modelo, audio] — densidade ponderada de ligação = 0.6484
- Lacuna entre **Tópico 1** [spira, artigo, marcelo] e **Tópico 3** [espectrograma, sinal, paciente] — densidade ponderada de ligação = 0.6747
- Lacuna entre **Tópico 3** [espectrograma, sinal, paciente] e **Tópico 5** [respiratoria, insuficiencia, covid] — densidade ponderada de ligação = 0.8328
- Lacuna entre **Tópico 2** [inscricao, cadeia, actante] e **Tópico 3** [espectrograma, sinal, paciente] — densidade ponderada de ligação = 0.8682
- Lacuna entre **Tópico 1** [spira, artigo, marcelo] e **Tópico 5** [respiratoria, insuficiencia, covid] — densidade ponderada de ligação = 0.9095

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
