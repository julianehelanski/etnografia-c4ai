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
- Tokens significativos: **32,668**
- Grafo bruto: **6745** nós · **77924** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **4012** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `spira` | 1886 |
| 2 | `covideiro` | 1177 |
| 3 | `inscricao` | 1094 |
| 4 | `cadeia` | 1020 |
| 5 | `rede` | 935 |
| 6 | `artigo` | 884 |
| 7 | `objeto` | 882 |
| 8 | `respiratoria` | 760 |
| 9 | `insuficiencia` | 724 |
| 10 | `dado` | 718 |
| 11 | `modelo` | 657 |
| 12 | `projeto` | 655 |
| 13 | `marcelo` | 610 |
| 14 | `espectrograma` | 527 |
| 15 | `artigos` | 527 |
| 16 | `coleta` | 505 |
| 17 | `actante` | 465 |
| 18 | `condicoes` | 435 |
| 19 | `cientifico` | 430 |
| 20 | `pratica` | 418 |
| 21 | `covid` | 418 |
| 22 | `audio` | 414 |
| 23 | `partir` | 391 |
| 24 | `pacientes` | 387 |
| 25 | `sinal` | 386 |
| 26 | `ruido` | 374 |
| 27 | `analise` | 371 |
| 28 | `secao` | 369 |
| 29 | `torna` | 353 |
| 30 | `dispositivo` | 350 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `spira` | 0.0372 |
| 2 | `covideiro` | 0.0234 |
| 3 | `inscricao` | 0.0221 |
| 4 | `cadeia` | 0.0206 |
| 5 | `rede` | 0.0189 |
| 6 | `objeto` | 0.0179 |
| 7 | `artigo` | 0.0178 |
| 8 | `dado` | 0.0146 |
| 9 | `respiratoria` | 0.0145 |
| 10 | `modelo` | 0.0138 |
| 11 | `insuficiencia` | 0.0138 |
| 12 | `projeto` | 0.0133 |
| 13 | `marcelo` | 0.0125 |
| 14 | `espectrograma` | 0.0111 |
| 15 | `artigos` | 0.0106 |
| 16 | `coleta` | 0.0106 |
| 17 | `actante` | 0.0098 |
| 18 | `condicoes` | 0.0091 |
| 19 | `pratica` | 0.0091 |
| 20 | `audio` | 0.0089 |
| 21 | `covid` | 0.0088 |
| 22 | `cientifico` | 0.0088 |
| 23 | `sinal` | 0.0084 |
| 24 | `ruido` | 0.0083 |
| 25 | `partir` | 0.0083 |
| 26 | `pacientes` | 0.0082 |
| 27 | `secao` | 0.0080 |
| 28 | `torna` | 0.0079 |
| 29 | `analise` | 0.0077 |
| 30 | `laboratorio` | 0.0076 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `escala` | 80 | 65 | +15 |
| 2 | `coeficientes` | 96 | 86 | +10 |
| 3 | `processo` | 118 | 109 | +9 |
| 4 | `pesquisa` | 74 | 66 | +8 |
| 5 | `processamento` | 76 | 68 | +8 |
| 6 | `momento` | 93 | 85 | +8 |
| 7 | `leitor` | 125 | 117 | +8 |
| 8 | `clinica` | 94 | 87 | +7 |
| 9 | `disponivel` | 106 | 99 | +7 |
| 10 | `grupo` | 113 | 106 | +7 |
| 11 | `acesso` | 126 | 119 | +7 |
| 12 | `microfone` | 152 | 146 | +6 |
| 13 | `parametros` | 155 | 149 | +6 |
| 14 | `analitico` | 160 | 154 | +6 |
| 15 | `resultado` | 82 | 77 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `spira` | 0.5461 |
| 2 | `inscricao` | 0.2301 |
| 3 | `covideiro` | 0.2011 |
| 4 | `cadeia` | 0.1276 |
| 5 | `objeto` | 0.0945 |
| 6 | `rede` | 0.0938 |
| 7 | `artigo` | 0.0875 |
| 8 | `respiratoria` | 0.0759 |
| 9 | `modelo` | 0.0744 |
| 10 | `dado` | 0.0642 |
| 11 | `espectrograma` | 0.0555 |
| 12 | `projeto` | 0.0549 |
| 13 | `coleta` | 0.0326 |
| 14 | `insuficiencia` | 0.0325 |
| 15 | `ruido` | 0.0297 |
| 16 | `sinal` | 0.0284 |
| 17 | `marcelo` | 0.0245 |
| 18 | `torna` | 0.0237 |
| 19 | `instituicao` | 0.0213 |
| 20 | `covid` | 0.0202 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `respiratoria` | `insuficiencia` | 0.844 | 305 |
| 2 | `imutavel` | `movel` | 0.842 | 81 |
| 3 | `calculo` | `centro` | 0.771 | 85 |
| 4 | `escuta` | `clinica` | 0.636 | 39 |
| 5 | `neural` | `rede` | 0.593 | 127 |
| 6 | `acao` | `programa` | 0.566 | 38 |
| 7 | `sinal` | `acustico` | 0.548 | 61 |
| 8 | `tornou` | `possivel` | 0.538 | 34 |
| 9 | `mapa` | `analitico` | 0.529 | 25 |
| 10 | `linguagem` | `processamento` | 0.525 | 27 |
| 11 | `entrevista` | `marcelo` | 0.505 | 100 |
| 12 | `publico` | `repositorio` | 0.500 | 24 |
| 13 | `acesso` | `disponivel` | 0.500 | 24 |
| 14 | `enfermaria` | `ruido` | 0.488 | 57 |
| 15 | `torna` | `visivel` | 0.480 | 45 |
| 16 | `covideiro` | `pandemico` | 0.478 | 97 |
| 17 | `condicoes` | `producao` | 0.475 | 51 |
| 18 | `publico` | `saude` | 0.470 | 18 |
| 19 | `ciencia` | `construcao` | 0.467 | 19 |
| 20 | `modelo` | `treinado` | 0.460 | 49 |
| 21 | `fonoaudiologos` | `medicos` | 0.457 | 28 |
| 22 | `tornar` | `visivel` | 0.453 | 20 |
| 23 | `cadeia` | `translacoes` | 0.437 | 51 |
| 24 | `conceito` | `referencia` | 0.435 | 16 |
| 25 | `controles` | `enfermaria` | 0.424 | 27 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (39 termos): inscricao, cadeia, analise, secao, torna, dispositivo
- **Tópico 2** (36 termos): dado, modelo, audio, sinal, ruido, enfermaria
- **Tópico 3** (30 termos): spira, artigo, projeto, marcelo, artigos, cientifico
- **Tópico 4** (24 termos): covideiro, coleta, actante, condicoes, pandemico, humano
- **Tópico 5** (21 termos): espectrograma, condicao, paciente, arquivo, virus, imagem
- **Tópico 6** (12 termos): respiratoria, insuficiencia, covid, pacientes, deteccao, acustica
- **Tópico 7** (9 termos): rede, partir, neural, associacao, topologia, arquitetura
- **Tópico 8** (9 termos): objeto, pratica, distintos, distintas, diferentes, existir

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [inscricao, cadeia, analise] e **Tópico 2** [dado, modelo, audio] — densidade ponderada de ligação = 0.5926
- Lacuna entre **Tópico 2** [dado, modelo, audio] e **Tópico 3** [spira, artigo, projeto] — densidade ponderada de ligação = 0.8426
- Lacuna entre **Tópico 2** [dado, modelo, audio] e **Tópico 5** [espectrograma, condicao, paciente] — densidade ponderada de ligação = 0.8519
- Lacuna entre **Tópico 1** [inscricao, cadeia, analise] e **Tópico 5** [espectrograma, condicao, paciente] — densidade ponderada de ligação = 0.8962
- Lacuna entre **Tópico 3** [spira, artigo, projeto] e **Tópico 5** [espectrograma, condicao, paciente] — densidade ponderada de ligação = 0.9206
- Lacuna entre **Tópico 2** [dado, modelo, audio] e **Tópico 4** [covideiro, coleta, actante] — densidade ponderada de ligação = 0.9248

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
