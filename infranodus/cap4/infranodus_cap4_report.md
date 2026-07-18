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
- Tokens significativos: **32,048**
- Grafo bruto: **6680** nós · **77064** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **3983** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `spira` | 1857 |
| 2 | `covideiro` | 1175 |
| 3 | `inscricao` | 1056 |
| 4 | `rede` | 1028 |
| 5 | `cadeia` | 899 |
| 6 | `artigo` | 848 |
| 7 | `objeto` | 813 |
| 8 | `dado` | 747 |
| 9 | `respiratoria` | 733 |
| 10 | `insuficiencia` | 703 |
| 11 | `modelo` | 657 |
| 12 | `marcelo` | 647 |
| 13 | `projeto` | 646 |
| 14 | `espectrograma` | 550 |
| 15 | `artigos` | 491 |
| 16 | `coleta` | 487 |
| 17 | `pratica` | 419 |
| 18 | `partir` | 412 |
| 19 | `actante` | 412 |
| 20 | `sinal` | 401 |
| 21 | `covid` | 401 |
| 22 | `audio` | 394 |
| 23 | `condicoes` | 372 |
| 24 | `pacientes` | 372 |
| 25 | `ruido` | 371 |
| 26 | `dataset` | 354 |
| 27 | `secao` | 341 |
| 28 | `laboratorio` | 340 |
| 29 | `cientifico` | 337 |
| 30 | `condicao` | 334 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `spira` | 0.0376 |
| 2 | `covideiro` | 0.0241 |
| 3 | `inscricao` | 0.0221 |
| 4 | `rede` | 0.0210 |
| 5 | `cadeia` | 0.0187 |
| 6 | `artigo` | 0.0176 |
| 7 | `objeto` | 0.0170 |
| 8 | `dado` | 0.0156 |
| 9 | `respiratoria` | 0.0143 |
| 10 | `modelo` | 0.0141 |
| 11 | `insuficiencia` | 0.0137 |
| 12 | `marcelo` | 0.0136 |
| 13 | `projeto` | 0.0135 |
| 14 | `espectrograma` | 0.0117 |
| 15 | `coleta` | 0.0106 |
| 16 | `artigos` | 0.0102 |
| 17 | `pratica` | 0.0093 |
| 18 | `actante` | 0.0090 |
| 19 | `partir` | 0.0089 |
| 20 | `sinal` | 0.0089 |
| 21 | `covid` | 0.0087 |
| 22 | `audio` | 0.0087 |
| 23 | `ruido` | 0.0085 |
| 24 | `pacientes` | 0.0082 |
| 25 | `condicoes` | 0.0081 |
| 26 | `dataset` | 0.0078 |
| 27 | `secao` | 0.0077 |
| 28 | `laboratorio` | 0.0076 |
| 29 | `condicao` | 0.0075 |
| 30 | `ponto` | 0.0075 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `microfone` | 106 | 90 | +16 |
| 2 | `frequencia` | 123 | 108 | +15 |
| 3 | `escala` | 99 | 88 | +11 |
| 4 | `diante` | 148 | 138 | +10 |
| 5 | `disponivel` | 98 | 89 | +9 |
| 6 | `coeficientes` | 102 | 93 | +9 |
| 7 | `pesquisa` | 85 | 77 | +8 |
| 8 | `leitor` | 121 | 113 | +8 |
| 9 | `parametros` | 131 | 123 | +8 |
| 10 | `carrega` | 112 | 105 | +7 |
| 11 | `ciencia` | 165 | 158 | +7 |
| 12 | `linguagem` | 140 | 134 | +6 |
| 13 | `processamento` | 69 | 64 | +5 |
| 14 | `nenhum` | 117 | 112 | +5 |
| 15 | `grade` | 133 | 128 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `spira` | 0.5268 |
| 2 | `covideiro` | 0.1909 |
| 3 | `inscricao` | 0.1539 |
| 4 | `rede` | 0.1213 |
| 5 | `artigo` | 0.1172 |
| 6 | `objeto` | 0.0983 |
| 7 | `cadeia` | 0.0954 |
| 8 | `respiratoria` | 0.0758 |
| 9 | `modelo` | 0.0661 |
| 10 | `dado` | 0.0654 |
| 11 | `espectrograma` | 0.0573 |
| 12 | `projeto` | 0.0484 |
| 13 | `sinal` | 0.0371 |
| 14 | `pratica` | 0.0348 |
| 15 | `insuficiencia` | 0.0290 |
| 16 | `torna` | 0.0283 |
| 17 | `ruido` | 0.0249 |
| 18 | `marcelo` | 0.0248 |
| 19 | `coleta` | 0.0232 |
| 20 | `covid` | 0.0195 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `imutavel` | `movel` | 0.846 | 78 |
| 2 | `respiratoria` | `insuficiencia` | 0.840 | 303 |
| 3 | `grupo` | `controle` | 0.673 | 49 |
| 4 | `escuta` | `clinica` | 0.613 | 39 |
| 5 | `neural` | `rede` | 0.587 | 141 |
| 6 | `acao` | `programa` | 0.576 | 35 |
| 7 | `diante` | `microfone` | 0.573 | 30 |
| 8 | `linguagem` | `processamento` | 0.558 | 33 |
| 9 | `sinal` | `acustico` | 0.542 | 61 |
| 10 | `tornou` | `possivel` | 0.531 | 34 |
| 11 | `entrevista` | `marcelo` | 0.496 | 94 |
| 12 | `enfermaria` | `ruido` | 0.494 | 65 |
| 13 | `torna` | `visivel` | 0.490 | 42 |
| 14 | `acesso` | `disponivel` | 0.489 | 25 |
| 15 | `publico` | `repositorio` | 0.485 | 24 |
| 16 | `modelo` | `treinado` | 0.479 | 52 |
| 17 | `covideiro` | `pandemico` | 0.473 | 94 |
| 18 | `ciencia` | `construcao` | 0.469 | 19 |
| 19 | `fonoaudiologos` | `medicos` | 0.464 | 22 |
| 20 | `tornar` | `visivel` | 0.463 | 20 |
| 21 | `pessoas` | `voz` | 0.448 | 26 |
| 22 | `controles` | `pacientes` | 0.444 | 40 |
| 23 | `publico` | `saude` | 0.443 | 18 |
| 24 | `tornou` | `visivel` | 0.436 | 21 |
| 25 | `saude` | `pesquisa` | 0.432 | 20 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (37 termos): spira, artigo, marcelo, projeto, artigos, dataset
- **Tópico 2** (35 termos): inscricao, cadeia, actante, secao, ponto, analise
- **Tópico 3** (30 termos): espectrograma, sinal, paciente, torna, arquivo, imagem
- **Tópico 4** (22 termos): dado, modelo, audio, treinamento, repositorio, computacional
- **Tópico 5** (18 termos): respiratoria, insuficiencia, covid, pacientes, ruido, enfermaria
- **Tópico 6** (18 termos): covideiro, coleta, condicoes, pandemico, celular, possivel
- **Tópico 7** (10 termos): rede, partir, neural, associacao, topologia, ator
- **Tópico 8** (10 termos): objeto, pratica, condicao, distintas, clinica, existir

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 2** [inscricao, cadeia, actante] e **Tópico 5** [respiratoria, insuficiencia, covid] — densidade ponderada de ligação = 0.5873
- Lacuna entre **Tópico 2** [inscricao, cadeia, actante] e **Tópico 4** [dado, modelo, audio] — densidade ponderada de ligação = 0.6182
- Lacuna entre **Tópico 1** [spira, artigo, marcelo] e **Tópico 3** [espectrograma, sinal, paciente] — densidade ponderada de ligação = 0.6604
- Lacuna entre **Tópico 2** [inscricao, cadeia, actante] e **Tópico 3** [espectrograma, sinal, paciente] — densidade ponderada de ligação = 0.8457
- Lacuna entre **Tópico 3** [espectrograma, sinal, paciente] e **Tópico 5** [respiratoria, insuficiencia, covid] — densidade ponderada de ligação = 0.8611
- Lacuna entre **Tópico 3** [espectrograma, sinal, paciente] e **Tópico 4** [dado, modelo, audio] — densidade ponderada de ligação = 0.9288

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
