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
- Tokens significativos: **33,478**
- Grafo bruto: **6836** nós · **79776** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **4079** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `spira` | 1969 |
| 2 | `covideiro` | 1182 |
| 3 | `inscricao` | 1143 |
| 4 | `cadeia` | 1051 |
| 5 | `rede` | 1048 |
| 6 | `artigo` | 903 |
| 7 | `objeto` | 873 |
| 8 | `respiratoria` | 786 |
| 9 | `insuficiencia` | 748 |
| 10 | `dado` | 742 |
| 11 | `projeto` | 723 |
| 12 | `modelo` | 687 |
| 13 | `marcelo` | 639 |
| 14 | `espectrograma` | 543 |
| 15 | `artigos` | 542 |
| 16 | `coleta` | 516 |
| 17 | `actante` | 468 |
| 18 | `covid` | 451 |
| 19 | `condicoes` | 445 |
| 20 | `cientifico` | 431 |
| 21 | `partir` | 426 |
| 22 | `pratica` | 423 |
| 23 | `audio` | 420 |
| 24 | `pacientes` | 408 |
| 25 | `analise` | 396 |
| 26 | `sinal` | 387 |
| 27 | `ruido` | 374 |
| 28 | `secao` | 361 |
| 29 | `torna` | 353 |
| 30 | `dispositivo` | 351 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `spira` | 0.0379 |
| 2 | `covideiro` | 0.0229 |
| 3 | `inscricao` | 0.0225 |
| 4 | `cadeia` | 0.0206 |
| 5 | `rede` | 0.0206 |
| 6 | `artigo` | 0.0177 |
| 7 | `objeto` | 0.0173 |
| 8 | `dado` | 0.0147 |
| 9 | `respiratoria` | 0.0144 |
| 10 | `projeto` | 0.0143 |
| 11 | `modelo` | 0.0140 |
| 12 | `insuficiencia` | 0.0137 |
| 13 | `marcelo` | 0.0127 |
| 14 | `espectrograma` | 0.0111 |
| 15 | `artigos` | 0.0106 |
| 16 | `coleta` | 0.0106 |
| 17 | `actante` | 0.0097 |
| 18 | `covid` | 0.0091 |
| 19 | `condicoes` | 0.0091 |
| 20 | `pratica` | 0.0089 |
| 21 | `partir` | 0.0088 |
| 22 | `audio` | 0.0087 |
| 23 | `cientifico` | 0.0086 |
| 24 | `pacientes` | 0.0084 |
| 25 | `sinal` | 0.0082 |
| 26 | `ruido` | 0.0081 |
| 27 | `analise` | 0.0080 |
| 28 | `torna` | 0.0077 |
| 29 | `secao` | 0.0076 |
| 30 | `dispositivo` | 0.0074 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `escala` | 78 | 64 | +14 |
| 2 | `pesquisa` | 77 | 67 | +10 |
| 3 | `clinica` | 87 | 77 | +10 |
| 4 | `disponivel` | 114 | 104 | +10 |
| 5 | `parametros` | 138 | 128 | +10 |
| 6 | `resultado` | 93 | 84 | +9 |
| 7 | `argumento` | 97 | 89 | +8 |
| 8 | `mapa` | 146 | 138 | +8 |
| 9 | `processamento` | 73 | 66 | +7 |
| 10 | `analitico` | 157 | 150 | +7 |
| 11 | `movimento` | 86 | 80 | +6 |
| 12 | `processo` | 112 | 106 | +6 |
| 13 | `carrega` | 120 | 114 | +6 |
| 14 | `frequencia` | 131 | 125 | +6 |
| 15 | `codigo` | 91 | 86 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `spira` | 0.5530 |
| 2 | `inscricao` | 0.2208 |
| 3 | `covideiro` | 0.2015 |
| 4 | `rede` | 0.1087 |
| 5 | `cadeia` | 0.1006 |
| 6 | `objeto` | 0.0804 |
| 7 | `artigo` | 0.0795 |
| 8 | `respiratoria` | 0.0778 |
| 9 | `modelo` | 0.0740 |
| 10 | `projeto` | 0.0709 |
| 11 | `dado` | 0.0653 |
| 12 | `espectrograma` | 0.0541 |
| 13 | `coleta` | 0.0326 |
| 14 | `marcelo` | 0.0325 |
| 15 | `sinal` | 0.0305 |
| 16 | `insuficiencia` | 0.0274 |
| 17 | `ruido` | 0.0265 |
| 18 | `pratica` | 0.0235 |
| 19 | `torna` | 0.0230 |
| 20 | `audio` | 0.0206 |

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
| 6 | `linguagem` | `processamento` | 0.556 | 33 |
| 7 | `sinal` | `acustico` | 0.545 | 61 |
| 8 | `tornou` | `possivel` | 0.533 | 34 |
| 9 | `mapa` | `analitico` | 0.530 | 25 |
| 10 | `entrevista` | `marcelo` | 0.502 | 100 |
| 11 | `acesso` | `disponivel` | 0.493 | 25 |
| 12 | `publico` | `repositorio` | 0.488 | 24 |
| 13 | `enfermaria` | `ruido` | 0.486 | 57 |
| 14 | `torna` | `visivel` | 0.482 | 45 |
| 15 | `modelo` | `treinado` | 0.480 | 58 |
| 16 | `covideiro` | `pandemico` | 0.474 | 97 |
| 17 | `ciencia` | `construcao` | 0.464 | 19 |
| 18 | `fonoaudiologos` | `medicos` | 0.459 | 28 |
| 19 | `condicoes` | `producao` | 0.456 | 54 |
| 20 | `tornar` | `visivel` | 0.455 | 20 |
| 21 | `textual` | `analise` | 0.438 | 27 |
| 22 | `publico` | `saude` | 0.437 | 18 |
| 23 | `cadeia` | `translacoes` | 0.435 | 51 |
| 24 | `controles` | `enfermaria` | 0.426 | 27 |
| 25 | `conceito` | `referencia` | 0.424 | 16 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (39 termos): covideiro, dado, coleta, actante, covid, condicoes
- **Tópico 2** (38 termos): inscricao, cadeia, secao, torna, dispositivo, ponto
- **Tópico 3** (35 termos): spira, artigo, projeto, marcelo, artigos, cientifico
- **Tópico 4** (32 termos): modelo, espectrograma, audio, sinal, arquivo, paciente
- **Tópico 5** (13 termos): objeto, pratica, condicao, computacional, distintos, distintas
- **Tópico 6** (11 termos): rede, analise, neural, textual, associacao, arquitetura
- **Tópico 7** (10 termos): respiratoria, insuficiencia, sistema, deteccao, acustica, versao
- **Tópico 8** (2 termos): movel, imutavel

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 2** [inscricao, cadeia, secao] e **Tópico 4** [modelo, espectrograma, audio] — densidade ponderada de ligação = 0.7541
- Lacuna entre **Tópico 4** [modelo, espectrograma, audio] e **Tópico 5** [objeto, pratica, condicao] — densidade ponderada de ligação = 0.7957
- Lacuna entre **Tópico 1** [covideiro, dado, coleta] e **Tópico 2** [inscricao, cadeia, secao] — densidade ponderada de ligação = 0.8306
- Lacuna entre **Tópico 3** [spira, artigo, projeto] e **Tópico 4** [modelo, espectrograma, audio] — densidade ponderada de ligação = 0.9000
- Lacuna entre **Tópico 1** [covideiro, dado, coleta] e **Tópico 5** [objeto, pratica, condicao] — densidade ponderada de ligação = 0.9566
- Lacuna entre **Tópico 1** [covideiro, dado, coleta] e **Tópico 4** [modelo, espectrograma, audio] — densidade ponderada de ligação = 0.9607

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
