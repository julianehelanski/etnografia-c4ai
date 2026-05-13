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
- Tokens significativos: **33,678**
- Grafo bruto: **6706** nós · **79241** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **4103** arestas
- Tópicos detectados (Louvain): **6**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `spira` | 2095 |
| 2 | `covideiro` | 1132 |
| 3 | `cadeia` | 1034 |
| 4 | `inscricao` | 1029 |
| 5 | `artigo` | 894 |
| 6 | `rede` | 834 |
| 7 | `respiratoria` | 815 |
| 8 | `objeto` | 814 |
| 9 | `insuficiencia` | 782 |
| 10 | `projeto` | 725 |
| 11 | `modelo` | 706 |
| 12 | `dado` | 704 |
| 13 | `marcelo` | 676 |
| 14 | `espectrograma` | 545 |
| 15 | `artigos` | 532 |
| 16 | `coleta` | 529 |
| 17 | `audio` | 486 |
| 18 | `actante` | 476 |
| 19 | `cientifico` | 435 |
| 20 | `covid` | 432 |
| 21 | `ruido` | 428 |
| 22 | `sinal` | 421 |
| 23 | `condicoes` | 410 |
| 24 | `pacientes` | 407 |
| 25 | `torna` | 403 |
| 26 | `pratica` | 401 |
| 27 | `analise` | 395 |
| 28 | `partir` | 394 |
| 29 | `dispositivo` | 383 |
| 30 | `condicao` | 370 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `spira` | 0.0397 |
| 2 | `covideiro` | 0.0219 |
| 3 | `cadeia` | 0.0204 |
| 4 | `inscricao` | 0.0202 |
| 5 | `artigo` | 0.0176 |
| 6 | `rede` | 0.0166 |
| 7 | `objeto` | 0.0160 |
| 8 | `respiratoria` | 0.0148 |
| 9 | `modelo` | 0.0143 |
| 10 | `projeto` | 0.0142 |
| 11 | `insuficiencia` | 0.0142 |
| 12 | `dado` | 0.0138 |
| 13 | `marcelo` | 0.0136 |
| 14 | `espectrograma` | 0.0112 |
| 15 | `coleta` | 0.0108 |
| 16 | `artigos` | 0.0104 |
| 17 | `audio` | 0.0099 |
| 18 | `actante` | 0.0097 |
| 19 | `ruido` | 0.0090 |
| 20 | `sinal` | 0.0088 |
| 21 | `covid` | 0.0087 |
| 22 | `cientifico` | 0.0086 |
| 23 | `torna` | 0.0085 |
| 24 | `pratica` | 0.0084 |
| 25 | `pacientes` | 0.0084 |
| 26 | `condicoes` | 0.0083 |
| 27 | `partir` | 0.0082 |
| 28 | `analise` | 0.0080 |
| 29 | `dispositivo` | 0.0079 |
| 30 | `condicao` | 0.0077 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `escala` | 90 | 73 | +17 |
| 2 | `caixa` | 87 | 72 | +15 |
| 3 | `preta` | 81 | 67 | +14 |
| 4 | `parametros` | 107 | 95 | +12 |
| 5 | `grade` | 146 | 135 | +11 |
| 6 | `linguagem` | 139 | 129 | +10 |
| 7 | `conceito` | 150 | 140 | +10 |
| 8 | `processamento` | 74 | 68 | +6 |
| 9 | `coeficientes` | 84 | 78 | +6 |
| 10 | `audioset` | 105 | 99 | +6 |
| 11 | `processo` | 117 | 111 | +6 |
| 12 | `ciencia` | 152 | 146 | +6 |
| 13 | `leitor` | 123 | 118 | +5 |
| 14 | `tecnica` | 136 | 131 | +5 |
| 15 | `youtube` | 143 | 138 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `spira` | 0.6527 |
| 2 | `inscricao` | 0.2405 |
| 3 | `covideiro` | 0.1571 |
| 4 | `cadeia` | 0.1294 |
| 5 | `artigo` | 0.1154 |
| 6 | `objeto` | 0.0968 |
| 7 | `modelo` | 0.0656 |
| 8 | `espectrograma` | 0.0630 |
| 9 | `projeto` | 0.0534 |
| 10 | `rede` | 0.0531 |
| 11 | `audio` | 0.0513 |
| 12 | `respiratoria` | 0.0505 |
| 13 | `dado` | 0.0388 |
| 14 | `coleta` | 0.0318 |
| 15 | `ruido` | 0.0301 |
| 16 | `marcelo` | 0.0278 |
| 17 | `sinal` | 0.0272 |
| 18 | `torna` | 0.0272 |
| 19 | `insuficiencia` | 0.0226 |
| 20 | `programa` | 0.0215 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `caixa` | `preta` | 0.897 | 96 |
| 2 | `respiratoria` | `insuficiencia` | 0.841 | 335 |
| 3 | `centro` | `calculo` | 0.769 | 88 |
| 4 | `neural` | `rede` | 0.605 | 131 |
| 5 | `programa` | `acao` | 0.569 | 38 |
| 6 | `possivel` | `tornou` | 0.552 | 37 |
| 7 | `acustico` | `sinal` | 0.550 | 64 |
| 8 | `disponivel` | `acesso` | 0.534 | 27 |
| 9 | `publico` | `saude` | 0.518 | 25 |
| 10 | `processamento` | `linguagem` | 0.517 | 27 |
| 11 | `torna` | `visivel` | 0.514 | 60 |
| 12 | `entrevista` | `marcelo` | 0.507 | 105 |
| 13 | `ciencia` | `acao` | 0.492 | 24 |
| 14 | `repositorio` | `publico` | 0.485 | 21 |
| 15 | `ciencia` | `construcao` | 0.483 | 22 |
| 16 | `pesquisa` | `saude` | 0.477 | 24 |
| 17 | `pandemico` | `covideiro` | 0.474 | 100 |
| 18 | `producao` | `condicoes` | 0.472 | 51 |
| 19 | `youtube` | `audioset` | 0.470 | 18 |
| 20 | `enfermaria` | `ruido` | 0.464 | 58 |
| 21 | `cadeia` | `translacoes` | 0.457 | 57 |
| 22 | `medicos` | `fonoaudiologos` | 0.456 | 28 |
| 23 | `modelo` | `treinado` | 0.436 | 46 |
| 24 | `referencia` | `conceito` | 0.428 | 16 |
| 25 | `precisa` | `forca` | 0.421 | 12 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (50 termos): modelo, espectrograma, audio, sinal, torna, paciente
- **Tópico 2** (39 termos): cadeia, inscricao, objeto, pratica, analise, dispositivo
- **Tópico 3** (34 termos): covideiro, dado, coleta, actante, ruido, condicoes
- **Tópico 4** (25 termos): artigo, rede, marcelo, cientifico, laboratorio, entrevista
- **Tópico 5** (22 termos): spira, projeto, artigos, partir, dataset, centro
- **Tópico 6** (10 termos): respiratoria, insuficiencia, covid, condicao, deteccao, versao

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [modelo, espectrograma, audio] e **Tópico 4** [artigo, rede, marcelo] — densidade ponderada de ligação = 0.6504
- Lacuna entre **Tópico 1** [modelo, espectrograma, audio] e **Tópico 3** [covideiro, dado, coleta] — densidade ponderada de ligação = 0.8318
- Lacuna entre **Tópico 1** [modelo, espectrograma, audio] e **Tópico 2** [cadeia, inscricao, objeto] — densidade ponderada de ligação = 0.8590
- Lacuna entre **Tópico 2** [cadeia, inscricao, objeto] e **Tópico 3** [covideiro, dado, coleta] — densidade ponderada de ligação = 0.8831
- Lacuna entre **Tópico 3** [covideiro, dado, coleta] e **Tópico 4** [artigo, rede, marcelo] — densidade ponderada de ligação = 1.0035
- Lacuna entre **Tópico 1** [modelo, espectrograma, audio] e **Tópico 5** [spira, projeto, artigos] — densidade ponderada de ligação = 1.0118

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
