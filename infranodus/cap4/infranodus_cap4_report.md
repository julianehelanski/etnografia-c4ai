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
- Tokens significativos: **32,942**
- Grafo bruto: **6736** nós · **78109** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **4071** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `spira` | 1977 |
| 2 | `covideiro` | 1171 |
| 3 | `inscricao` | 1126 |
| 4 | `cadeia` | 1056 |
| 5 | `artigo` | 910 |
| 6 | `objeto` | 886 |
| 7 | `rede` | 869 |
| 8 | `respiratoria` | 752 |
| 9 | `insuficiencia` | 719 |
| 10 | `dado` | 686 |
| 11 | `projeto` | 686 |
| 12 | `modelo` | 655 |
| 13 | `marcelo` | 647 |
| 14 | `artigos` | 524 |
| 15 | `espectrograma` | 512 |
| 16 | `coleta` | 509 |
| 17 | `actante` | 470 |
| 18 | `pratica` | 458 |
| 19 | `cientifico` | 421 |
| 20 | `condicoes` | 421 |
| 21 | `analise` | 419 |
| 22 | `covid` | 411 |
| 23 | `audio` | 403 |
| 24 | `partir` | 397 |
| 25 | `pacientes` | 388 |
| 26 | `sinal` | 386 |
| 27 | `secao` | 378 |
| 28 | `dispositivo` | 369 |
| 29 | `ruido` | 368 |
| 30 | `torna` | 367 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `spira` | 0.0386 |
| 2 | `covideiro` | 0.0230 |
| 3 | `inscricao` | 0.0226 |
| 4 | `cadeia` | 0.0211 |
| 5 | `artigo` | 0.0182 |
| 6 | `objeto` | 0.0178 |
| 7 | `rede` | 0.0176 |
| 8 | `respiratoria` | 0.0141 |
| 9 | `projeto` | 0.0138 |
| 10 | `dado` | 0.0138 |
| 11 | `modelo` | 0.0137 |
| 12 | `insuficiencia` | 0.0134 |
| 13 | `marcelo` | 0.0130 |
| 14 | `espectrograma` | 0.0107 |
| 15 | `coleta` | 0.0106 |
| 16 | `artigos` | 0.0105 |
| 17 | `actante` | 0.0098 |
| 18 | `pratica` | 0.0097 |
| 19 | `condicoes` | 0.0087 |
| 20 | `audio` | 0.0086 |
| 21 | `analise` | 0.0086 |
| 22 | `covid` | 0.0086 |
| 23 | `cientifico` | 0.0086 |
| 24 | `partir` | 0.0084 |
| 25 | `sinal` | 0.0083 |
| 26 | `pacientes` | 0.0081 |
| 27 | `secao` | 0.0081 |
| 28 | `ruido` | 0.0081 |
| 29 | `torna` | 0.0080 |
| 30 | `dispositivo` | 0.0078 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `preta` | 107 | 83 | +24 |
| 2 | `caixa` | 113 | 93 | +20 |
| 3 | `escala` | 78 | 61 | +17 |
| 4 | `parametros` | 140 | 128 | +12 |
| 5 | `algoritmo` | 80 | 70 | +10 |
| 6 | `operacao` | 110 | 101 | +9 |
| 7 | `linguagem` | 141 | 132 | +9 |
| 8 | `grade` | 143 | 134 | +9 |
| 9 | `processamento` | 75 | 67 | +8 |
| 10 | `tecnica` | 134 | 126 | +8 |
| 11 | `pesquisa` | 72 | 65 | +7 |
| 12 | `disponivel` | 103 | 96 | +7 |
| 13 | `processo` | 118 | 111 | +7 |
| 14 | `repositorio` | 77 | 71 | +6 |
| 15 | `resultado` | 83 | 77 | +6 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `spira` | 0.6076 |
| 2 | `inscricao` | 0.2592 |
| 3 | `covideiro` | 0.1863 |
| 4 | `cadeia` | 0.1379 |
| 5 | `objeto` | 0.0993 |
| 6 | `rede` | 0.0806 |
| 7 | `artigo` | 0.0760 |
| 8 | `modelo` | 0.0746 |
| 9 | `respiratoria` | 0.0694 |
| 10 | `espectrograma` | 0.0547 |
| 11 | `projeto` | 0.0466 |
| 12 | `dado` | 0.0464 |
| 13 | `ruido` | 0.0298 |
| 14 | `coleta` | 0.0269 |
| 15 | `sinal` | 0.0265 |
| 16 | `torna` | 0.0233 |
| 17 | `insuficiencia` | 0.0232 |
| 18 | `programa` | 0.0209 |
| 19 | `audio` | 0.0196 |
| 20 | `analise` | 0.0193 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `caixa` | `preta` | 0.898 | 81 |
| 2 | `imutavel` | `movel` | 0.846 | 82 |
| 3 | `respiratoria` | `insuficiencia` | 0.844 | 308 |
| 4 | `neural` | `rede` | 0.588 | 121 |
| 5 | `acao` | `programa` | 0.563 | 38 |
| 6 | `sinal` | `acustico` | 0.549 | 61 |
| 7 | `tornou` | `possivel` | 0.532 | 34 |
| 8 | `linguagem` | `processamento` | 0.530 | 27 |
| 9 | `publico` | `saude` | 0.506 | 22 |
| 10 | `entrevista` | `marcelo` | 0.497 | 103 |
| 11 | `acesso` | `disponivel` | 0.497 | 24 |
| 12 | `ciencia` | `construcao` | 0.490 | 22 |
| 13 | `torna` | `visivel` | 0.479 | 48 |
| 14 | `condicoes` | `producao` | 0.478 | 51 |
| 15 | `publico` | `repositorio` | 0.477 | 21 |
| 16 | `enfermaria` | `ruido` | 0.477 | 55 |
| 17 | `covideiro` | `pandemico` | 0.474 | 97 |
| 18 | `modelo` | `treinado` | 0.460 | 49 |
| 19 | `ciencia` | `acao` | 0.460 | 21 |
| 20 | `cadeia` | `translacoes` | 0.459 | 60 |
| 21 | `fonoaudiologos` | `medicos` | 0.458 | 28 |
| 22 | `conceito` | `referencia` | 0.435 | 16 |
| 23 | `saude` | `pesquisa` | 0.433 | 18 |
| 24 | `forca` | `precisa` | 0.431 | 12 |
| 25 | `controles` | `enfermaria` | 0.423 | 27 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (33 termos): inscricao, cadeia, secao, dispositivo, torna, latour
- **Tópico 2** (31 termos): dado, modelo, audio, campo, treinamento, pesquisador
- **Tópico 3** (31 termos): spira, artigo, projeto, marcelo, artigos, cientifico
- **Tópico 4** (29 termos): covideiro, coleta, actante, condicoes, condicao, laboratorio
- **Tópico 5** (21 termos): espectrograma, sinal, paciente, arquivo, virus, imagem
- **Tópico 6** (17 termos): respiratoria, insuficiencia, covid, pacientes, ruido, enfermaria
- **Tópico 7** (9 termos): rede, partir, neural, ator, associacao, arquitetura
- **Tópico 8** (9 termos): objeto, pratica, distintos, distintas, diferentes, produzido

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [inscricao, cadeia, secao] e **Tópico 2** [dado, modelo, audio] — densidade ponderada de ligação = 0.6217
- Lacuna entre **Tópico 2** [dado, modelo, audio] e **Tópico 4** [covideiro, coleta, actante] — densidade ponderada de ligação = 0.7341
- Lacuna entre **Tópico 2** [dado, modelo, audio] e **Tópico 5** [espectrograma, sinal, paciente] — densidade ponderada de ligação = 0.7880
- Lacuna entre **Tópico 3** [spira, artigo, projeto] e **Tópico 5** [espectrograma, sinal, paciente] — densidade ponderada de ligação = 0.8495
- Lacuna entre **Tópico 2** [dado, modelo, audio] e **Tópico 3** [spira, artigo, projeto] — densidade ponderada de ligação = 0.9594
- Lacuna entre **Tópico 4** [covideiro, coleta, actante] e **Tópico 5** [espectrograma, sinal, paciente] — densidade ponderada de ligação = 0.9606

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
