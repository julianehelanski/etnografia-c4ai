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
- Tokens significativos: **32,885**
- Grafo bruto: **6730** nós · **77973** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **4069** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `spira` | 1967 |
| 2 | `covideiro` | 1179 |
| 3 | `inscricao` | 1126 |
| 4 | `cadeia` | 1056 |
| 5 | `artigo` | 918 |
| 6 | `objeto` | 886 |
| 7 | `rede` | 857 |
| 8 | `respiratoria` | 758 |
| 9 | `insuficiencia` | 722 |
| 10 | `dado` | 686 |
| 11 | `projeto` | 673 |
| 12 | `modelo` | 655 |
| 13 | `marcelo` | 649 |
| 14 | `espectrograma` | 519 |
| 15 | `artigos` | 514 |
| 16 | `coleta` | 509 |
| 17 | `actante` | 471 |
| 18 | `pratica` | 454 |
| 19 | `condicoes` | 423 |
| 20 | `analise` | 419 |
| 21 | `covid` | 415 |
| 22 | `cientifico` | 412 |
| 23 | `audio` | 403 |
| 24 | `partir` | 396 |
| 25 | `sinal` | 388 |
| 26 | `pacientes` | 388 |
| 27 | `secao` | 373 |
| 28 | `ruido` | 372 |
| 29 | `dispositivo` | 371 |
| 30 | `torna` | 368 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `spira` | 0.0383 |
| 2 | `covideiro` | 0.0233 |
| 3 | `inscricao` | 0.0226 |
| 4 | `cadeia` | 0.0212 |
| 5 | `artigo` | 0.0183 |
| 6 | `objeto` | 0.0178 |
| 7 | `rede` | 0.0173 |
| 8 | `respiratoria` | 0.0142 |
| 9 | `dado` | 0.0138 |
| 10 | `modelo` | 0.0137 |
| 11 | `projeto` | 0.0136 |
| 12 | `insuficiencia` | 0.0135 |
| 13 | `marcelo` | 0.0130 |
| 14 | `espectrograma` | 0.0108 |
| 15 | `coleta` | 0.0106 |
| 16 | `artigos` | 0.0103 |
| 17 | `actante` | 0.0098 |
| 18 | `pratica` | 0.0096 |
| 19 | `condicoes` | 0.0088 |
| 20 | `covid` | 0.0087 |
| 21 | `audio` | 0.0086 |
| 22 | `analise` | 0.0086 |
| 23 | `sinal` | 0.0084 |
| 24 | `partir` | 0.0084 |
| 25 | `cientifico` | 0.0083 |
| 26 | `ruido` | 0.0082 |
| 27 | `pacientes` | 0.0082 |
| 28 | `torna` | 0.0080 |
| 29 | `secao` | 0.0080 |
| 30 | `dispositivo` | 0.0079 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `preta` | 106 | 83 | +23 |
| 2 | `caixa` | 114 | 93 | +21 |
| 3 | `escala` | 79 | 62 | +17 |
| 4 | `algoritmo` | 81 | 70 | +11 |
| 5 | `disponivel` | 110 | 99 | +11 |
| 6 | `parametros` | 129 | 119 | +10 |
| 7 | `grade` | 143 | 133 | +10 |
| 8 | `operacao` | 109 | 100 | +9 |
| 9 | `linguagem` | 140 | 131 | +9 |
| 10 | `pesquisa` | 75 | 67 | +8 |
| 11 | `resultado` | 76 | 68 | +8 |
| 12 | `processo` | 118 | 111 | +7 |
| 13 | `processamento` | 71 | 65 | +6 |
| 14 | `repositorio` | 78 | 72 | +6 |
| 15 | `acao` | 92 | 87 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `spira` | 0.5935 |
| 2 | `inscricao` | 0.2571 |
| 3 | `covideiro` | 0.1966 |
| 4 | `cadeia` | 0.1367 |
| 5 | `objeto` | 0.0992 |
| 6 | `artigo` | 0.0864 |
| 7 | `rede` | 0.0808 |
| 8 | `modelo` | 0.0747 |
| 9 | `respiratoria` | 0.0695 |
| 10 | `espectrograma` | 0.0550 |
| 11 | `dado` | 0.0470 |
| 12 | `projeto` | 0.0465 |
| 13 | `ruido` | 0.0303 |
| 14 | `coleta` | 0.0266 |
| 15 | `sinal` | 0.0264 |
| 16 | `marcelo` | 0.0258 |
| 17 | `torna` | 0.0229 |
| 18 | `insuficiencia` | 0.0225 |
| 19 | `programa` | 0.0209 |
| 20 | `audio` | 0.0193 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `caixa` | `preta` | 0.898 | 81 |
| 2 | `imutavel` | `movel` | 0.846 | 82 |
| 3 | `respiratoria` | `insuficiencia` | 0.844 | 311 |
| 4 | `neural` | `rede` | 0.593 | 124 |
| 5 | `acao` | `programa` | 0.563 | 38 |
| 6 | `sinal` | `acustico` | 0.549 | 61 |
| 7 | `tornou` | `possivel` | 0.531 | 34 |
| 8 | `linguagem` | `processamento` | 0.530 | 27 |
| 9 | `publico` | `saude` | 0.506 | 22 |
| 10 | `entrevista` | `marcelo` | 0.504 | 105 |
| 11 | `acesso` | `disponivel` | 0.497 | 24 |
| 12 | `ciencia` | `construcao` | 0.490 | 22 |
| 13 | `torna` | `visivel` | 0.481 | 48 |
| 14 | `condicoes` | `producao` | 0.478 | 51 |
| 15 | `publico` | `repositorio` | 0.477 | 21 |
| 16 | `enfermaria` | `ruido` | 0.477 | 55 |
| 17 | `covideiro` | `pandemico` | 0.474 | 97 |
| 18 | `ciencia` | `acao` | 0.460 | 21 |
| 19 | `modelo` | `treinado` | 0.460 | 49 |
| 20 | `cadeia` | `translacoes` | 0.459 | 60 |
| 21 | `fonoaudiologos` | `medicos` | 0.457 | 28 |
| 22 | `conceito` | `referencia` | 0.435 | 16 |
| 23 | `saude` | `pesquisa` | 0.433 | 18 |
| 24 | `forca` | `precisa` | 0.431 | 12 |
| 25 | `controles` | `enfermaria` | 0.423 | 27 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (38 termos): inscricao, cadeia, secao, dispositivo, torna, latour
- **Tópico 2** (36 termos): spira, artigo, projeto, marcelo, artigos, condicoes
- **Tópico 3** (32 termos): dado, modelo, audio, campo, treinamento, treinado
- **Tópico 4** (20 termos): espectrograma, sinal, paciente, arquivo, virus, imagem
- **Tópico 5** (20 termos): respiratoria, insuficiencia, coleta, covid, pacientes, ruido
- **Tópico 6** (15 termos): covideiro, actante, pandemico, humano, configuracao, programa
- **Tópico 7** (10 termos): objeto, pratica, distintos, distintas, diferentes, produzido
- **Tópico 8** (9 termos): rede, partir, neural, ator, associacao, arquitetura

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [inscricao, cadeia, secao] e **Tópico 3** [dado, modelo, audio] — densidade ponderada de ligação = 0.5674
- Lacuna entre **Tópico 1** [inscricao, cadeia, secao] e **Tópico 5** [respiratoria, insuficiencia, coleta] — densidade ponderada de ligação = 0.6368
- Lacuna entre **Tópico 3** [dado, modelo, audio] e **Tópico 5** [respiratoria, insuficiencia, coleta] — densidade ponderada de ligação = 0.8234
- Lacuna entre **Tópico 3** [dado, modelo, audio] e **Tópico 4** [espectrograma, sinal, paciente] — densidade ponderada de ligação = 0.8266
- Lacuna entre **Tópico 2** [spira, artigo, projeto] e **Tópico 4** [espectrograma, sinal, paciente] — densidade ponderada de ligação = 0.8306
- Lacuna entre **Tópico 2** [spira, artigo, projeto] e **Tópico 3** [dado, modelo, audio] — densidade ponderada de ligação = 0.8576

## 9. Leitura interpretativa
_Leitura interpretativa ainda não escrita para este capítulo. Crie `interpretation_cap4.md` ao lado dos outputs para que o conteúdo seja embutido aqui automaticamente._

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
