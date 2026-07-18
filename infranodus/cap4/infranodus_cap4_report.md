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
- Tokens significativos: **31,888**
- Grafo bruto: **6688** nós · **76776** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **3975** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `spira` | 1829 |
| 2 | `covideiro` | 1148 |
| 3 | `inscricao` | 1034 |
| 4 | `rede` | 1019 |
| 5 | `cadeia` | 875 |
| 6 | `artigo` | 851 |
| 7 | `objeto` | 796 |
| 8 | `respiratoria` | 729 |
| 9 | `dado` | 729 |
| 10 | `insuficiencia` | 696 |
| 11 | `modelo` | 683 |
| 12 | `projeto` | 646 |
| 13 | `marcelo` | 631 |
| 14 | `espectrograma` | 567 |
| 15 | `coleta` | 500 |
| 16 | `artigos` | 493 |
| 17 | `sinal` | 420 |
| 18 | `pratica` | 420 |
| 19 | `actante` | 408 |
| 20 | `partir` | 402 |
| 21 | `covid` | 399 |
| 22 | `audio` | 395 |
| 23 | `pacientes` | 375 |
| 24 | `ruido` | 374 |
| 25 | `condicoes` | 363 |
| 26 | `dataset` | 349 |
| 27 | `torna` | 349 |
| 28 | `cientifico` | 338 |
| 29 | `secao` | 337 |
| 30 | `paciente` | 335 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `spira` | 0.0372 |
| 2 | `covideiro` | 0.0237 |
| 3 | `inscricao` | 0.0218 |
| 4 | `rede` | 0.0209 |
| 5 | `cadeia` | 0.0183 |
| 6 | `artigo` | 0.0177 |
| 7 | `objeto` | 0.0167 |
| 8 | `dado` | 0.0153 |
| 9 | `modelo` | 0.0147 |
| 10 | `respiratoria` | 0.0142 |
| 11 | `insuficiencia` | 0.0136 |
| 12 | `projeto` | 0.0135 |
| 13 | `marcelo` | 0.0134 |
| 14 | `espectrograma` | 0.0121 |
| 15 | `coleta` | 0.0109 |
| 16 | `artigos` | 0.0103 |
| 17 | `pratica` | 0.0093 |
| 18 | `sinal` | 0.0093 |
| 19 | `actante` | 0.0091 |
| 20 | `partir` | 0.0088 |
| 21 | `audio` | 0.0087 |
| 22 | `covid` | 0.0087 |
| 23 | `ruido` | 0.0085 |
| 24 | `pacientes` | 0.0083 |
| 25 | `torna` | 0.0080 |
| 26 | `condicoes` | 0.0079 |
| 27 | `dataset` | 0.0077 |
| 28 | `secao` | 0.0076 |
| 29 | `ponto` | 0.0075 |
| 30 | `paciente` | 0.0075 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `frequencia` | 123 | 111 | +12 |
| 2 | `microfone` | 93 | 82 | +11 |
| 3 | `carrega` | 115 | 104 | +11 |
| 4 | `escala` | 101 | 91 | +10 |
| 5 | `diante` | 147 | 137 | +10 |
| 6 | `processo` | 114 | 106 | +8 |
| 7 | `leitor` | 120 | 112 | +8 |
| 8 | `coeficientes` | 92 | 85 | +7 |
| 9 | `parametros` | 132 | 125 | +7 |
| 10 | `pesquisa` | 83 | 77 | +6 |
| 11 | `disponivel` | 94 | 88 | +6 |
| 12 | `diferenca` | 125 | 119 | +6 |
| 13 | `argumento` | 129 | 123 | +6 |
| 14 | `linguagem` | 140 | 134 | +6 |
| 15 | `saude` | 162 | 157 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `spira` | 0.5411 |
| 2 | `covideiro` | 0.1988 |
| 3 | `inscricao` | 0.1390 |
| 4 | `rede` | 0.1247 |
| 5 | `artigo` | 0.1185 |
| 6 | `cadeia` | 0.1045 |
| 7 | `objeto` | 0.0915 |
| 8 | `modelo` | 0.0843 |
| 9 | `espectrograma` | 0.0790 |
| 10 | `respiratoria` | 0.0755 |
| 11 | `dado` | 0.0648 |
| 12 | `sinal` | 0.0484 |
| 13 | `projeto` | 0.0457 |
| 14 | `pratica` | 0.0345 |
| 15 | `insuficiencia` | 0.0288 |
| 16 | `coleta` | 0.0266 |
| 17 | `ruido` | 0.0252 |
| 18 | `marcelo` | 0.0233 |
| 19 | `torna` | 0.0228 |
| 20 | `actante` | 0.0196 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `imutavel` | `movel` | 0.844 | 75 |
| 2 | `respiratoria` | `insuficiencia` | 0.840 | 300 |
| 3 | `grupo` | `controle` | 0.676 | 49 |
| 4 | `escuta` | `clinica` | 0.612 | 39 |
| 5 | `neural` | `rede` | 0.588 | 141 |
| 6 | `diante` | `microfone` | 0.566 | 30 |
| 7 | `acao` | `programa` | 0.558 | 29 |
| 8 | `linguagem` | `processamento` | 0.557 | 33 |
| 9 | `tornou` | `possivel` | 0.541 | 34 |
| 10 | `sinal` | `acustico` | 0.539 | 61 |
| 11 | `entrevista` | `marcelo` | 0.491 | 90 |
| 12 | `modelo` | `treinado` | 0.491 | 58 |
| 13 | `enfermaria` | `ruido` | 0.489 | 65 |
| 14 | `acesso` | `disponivel` | 0.485 | 25 |
| 15 | `publico` | `repositorio` | 0.485 | 24 |
| 16 | `covideiro` | `pandemico` | 0.472 | 91 |
| 17 | `torna` | `visivel` | 0.466 | 39 |
| 18 | `fonoaudiologos` | `medicos` | 0.456 | 22 |
| 19 | `tornou` | `visivel` | 0.452 | 21 |
| 20 | `pessoas` | `voz` | 0.451 | 26 |
| 21 | `tornar` | `visivel` | 0.445 | 17 |
| 22 | `publico` | `saude` | 0.443 | 18 |
| 23 | `controles` | `pacientes` | 0.440 | 40 |
| 24 | `saude` | `pesquisa` | 0.435 | 20 |
| 25 | `cadeia` | `translacao` | 0.427 | 71 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (37 termos): espectrograma, sinal, actante, audio, torna, paciente
- **Tópico 2** (36 termos): inscricao, cadeia, secao, ponto, dispositivo, latour
- **Tópico 3** (35 termos): covideiro, dado, coleta, covid, pacientes, ruido
- **Tópico 4** (28 termos): spira, projeto, marcelo, artigos, dataset, analise
- **Tópico 5** (18 termos): artigo, modelo, cientifico, laboratorio, treinado, repositorio
- **Tópico 6** (9 termos): rede, partir, neural, associacao, topologia, ator
- **Tópico 7** (9 termos): objeto, pratica, condicao, distintas, clinica, existir
- **Tópico 8** (8 termos): respiratoria, insuficiencia, sistema, versao, acustica, deteccao

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [espectrograma, sinal, actante] e **Tópico 2** [inscricao, cadeia, secao] — densidade ponderada de ligação = 0.7132
- Lacuna entre **Tópico 1** [espectrograma, sinal, actante] e **Tópico 5** [artigo, modelo, cientifico] — densidade ponderada de ligação = 0.7492
- Lacuna entre **Tópico 2** [inscricao, cadeia, secao] e **Tópico 3** [covideiro, dado, coleta] — densidade ponderada de ligação = 0.7556
- Lacuna entre **Tópico 1** [espectrograma, sinal, actante] e **Tópico 4** [spira, projeto, marcelo] — densidade ponderada de ligação = 0.8050
- Lacuna entre **Tópico 1** [espectrograma, sinal, actante] e **Tópico 3** [covideiro, dado, coleta] — densidade ponderada de ligação = 0.8255
- Lacuna entre **Tópico 2** [inscricao, cadeia, secao] e **Tópico 5** [artigo, modelo, cientifico] — densidade ponderada de ligação = 0.8256

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
