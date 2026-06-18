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
- Tokens significativos: **33,061**
- Grafo bruto: **6695** nós · **78103** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **4086** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `spira` | 2069 |
| 2 | `covideiro` | 1139 |
| 3 | `inscricao` | 1104 |
| 4 | `cadeia` | 1075 |
| 5 | `artigo` | 879 |
| 6 | `objeto` | 820 |
| 7 | `respiratoria` | 801 |
| 8 | `rede` | 768 |
| 9 | `insuficiencia` | 763 |
| 10 | `projeto` | 717 |
| 11 | `dado` | 709 |
| 12 | `modelo` | 702 |
| 13 | `marcelo` | 661 |
| 14 | `espectrograma` | 560 |
| 15 | `coleta` | 530 |
| 16 | `artigos` | 517 |
| 17 | `actante` | 456 |
| 18 | `audio` | 452 |
| 19 | `ruido` | 445 |
| 20 | `sinal` | 424 |
| 21 | `covid` | 422 |
| 22 | `cientifico` | 417 |
| 23 | `pacientes` | 413 |
| 24 | `condicoes` | 404 |
| 25 | `analise` | 401 |
| 26 | `partir` | 387 |
| 27 | `torna` | 386 |
| 28 | `pratica` | 383 |
| 29 | `dispositivo` | 380 |
| 30 | `condicao` | 372 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `spira` | 0.0396 |
| 2 | `covideiro` | 0.0221 |
| 3 | `inscricao` | 0.0220 |
| 4 | `cadeia` | 0.0212 |
| 5 | `artigo` | 0.0174 |
| 6 | `objeto` | 0.0163 |
| 7 | `rede` | 0.0154 |
| 8 | `respiratoria` | 0.0147 |
| 9 | `modelo` | 0.0144 |
| 10 | `projeto` | 0.0142 |
| 11 | `dado` | 0.0140 |
| 12 | `insuficiencia` | 0.0139 |
| 13 | `marcelo` | 0.0131 |
| 14 | `espectrograma` | 0.0115 |
| 15 | `coleta` | 0.0108 |
| 16 | `artigos` | 0.0102 |
| 17 | `ruido` | 0.0095 |
| 18 | `actante` | 0.0094 |
| 19 | `audio` | 0.0093 |
| 20 | `sinal` | 0.0090 |
| 21 | `covid` | 0.0086 |
| 22 | `pacientes` | 0.0085 |
| 23 | `cientifico` | 0.0083 |
| 24 | `condicoes` | 0.0083 |
| 25 | `torna` | 0.0082 |
| 26 | `analise` | 0.0082 |
| 27 | `partir` | 0.0081 |
| 28 | `pratica` | 0.0081 |
| 29 | `dispositivo` | 0.0080 |
| 30 | `condicao` | 0.0078 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `preta` | 100 | 77 | +23 |
| 2 | `caixa` | 107 | 87 | +20 |
| 3 | `escala` | 84 | 69 | +15 |
| 4 | `parametros` | 134 | 124 | +10 |
| 5 | `processo` | 111 | 102 | +9 |
| 6 | `algoritmo` | 83 | 76 | +7 |
| 7 | `disponivel` | 102 | 95 | +7 |
| 8 | `linguagem` | 137 | 130 | +7 |
| 9 | `frequencias` | 146 | 139 | +7 |
| 10 | `processamento` | 76 | 70 | +6 |
| 11 | `coeficientes` | 89 | 83 | +6 |
| 12 | `controle` | 124 | 118 | +6 |
| 13 | `grade` | 142 | 136 | +6 |
| 14 | `microfone` | 156 | 150 | +6 |
| 15 | `pesquisa` | 71 | 66 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `spira` | 0.6132 |
| 2 | `inscricao` | 0.2767 |
| 3 | `cadeia` | 0.1399 |
| 4 | `covideiro` | 0.1363 |
| 5 | `objeto` | 0.0953 |
| 6 | `artigo` | 0.0928 |
| 7 | `modelo` | 0.0688 |
| 8 | `espectrograma` | 0.0534 |
| 9 | `respiratoria` | 0.0529 |
| 10 | `rede` | 0.0524 |
| 11 | `dado` | 0.0497 |
| 12 | `audio` | 0.0448 |
| 13 | `projeto` | 0.0418 |
| 14 | `coleta` | 0.0379 |
| 15 | `ruido` | 0.0326 |
| 16 | `sinal` | 0.0283 |
| 17 | `torna` | 0.0266 |
| 18 | `insuficiencia` | 0.0230 |
| 19 | `programa` | 0.0212 |
| 20 | `covid` | 0.0175 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `caixa` | `preta` | 0.898 | 84 |
| 2 | `respiratoria` | `insuficiencia` | 0.840 | 329 |
| 3 | `calculo` | `centro` | 0.768 | 88 |
| 4 | `grupo` | `controle` | 0.658 | 40 |
| 5 | `neural` | `rede` | 0.615 | 133 |
| 6 | `escuta` | `clinica` | 0.585 | 30 |
| 7 | `acao` | `programa` | 0.575 | 38 |
| 8 | `tornou` | `possivel` | 0.551 | 37 |
| 9 | `sinal` | `acustico` | 0.549 | 64 |
| 10 | `acesso` | `disponivel` | 0.532 | 27 |
| 11 | `linguagem` | `processamento` | 0.519 | 27 |
| 12 | `entrevista` | `marcelo` | 0.506 | 105 |
| 13 | `publico` | `saude` | 0.503 | 22 |
| 14 | `torna` | `visivel` | 0.501 | 54 |
| 15 | `publico` | `repositorio` | 0.487 | 21 |
| 16 | `ciencia` | `construcao` | 0.485 | 22 |
| 17 | `covideiro` | `pandemico` | 0.476 | 100 |
| 18 | `condicoes` | `producao` | 0.475 | 51 |
| 19 | `ciencia` | `acao` | 0.471 | 21 |
| 20 | `enfermaria` | `ruido` | 0.464 | 58 |
| 21 | `medicos` | `fonoaudiologos` | 0.458 | 28 |
| 22 | `cadeia` | `translacoes` | 0.451 | 57 |
| 23 | `conceito` | `referencia` | 0.440 | 16 |
| 24 | `modelo` | `treinado` | 0.436 | 46 |
| 25 | `forca` | `precisa` | 0.436 | 12 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (42 termos): inscricao, cadeia, objeto, torna, pratica, dispositivo
- **Tópico 2** (36 termos): spira, artigo, projeto, marcelo, artigos, cientifico
- **Tópico 3** (30 termos): dado, modelo, audio, treinamento, campo, processamento
- **Tópico 4** (21 termos): espectrograma, condicao, paciente, imagem, arquivo, virus
- **Tópico 5** (21 termos): covideiro, coleta, actante, condicoes, pandemico, humano
- **Tópico 6** (14 termos): respiratoria, insuficiencia, covid, pacientes, deteccao, versao
- **Tópico 7** (10 termos): ruido, sinal, enfermaria, acustico, fonoaudiologos, controles
- **Tópico 8** (6 termos): rede, partir, neural, entrada, associacao, ator

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [inscricao, cadeia, objeto] e **Tópico 3** [dado, modelo, audio] — densidade ponderada de ligação = 0.6270
- Lacuna entre **Tópico 3** [dado, modelo, audio] e **Tópico 4** [espectrograma, condicao, paciente] — densidade ponderada de ligação = 0.7048
- Lacuna entre **Tópico 3** [dado, modelo, audio] e **Tópico 5** [covideiro, coleta, actante] — densidade ponderada de ligação = 0.8524
- Lacuna entre **Tópico 2** [spira, artigo, projeto] e **Tópico 4** [espectrograma, condicao, paciente] — densidade ponderada de ligação = 0.9048
- Lacuna entre **Tópico 2** [spira, artigo, projeto] e **Tópico 3** [dado, modelo, audio] — densidade ponderada de ligação = 0.9306
- Lacuna entre **Tópico 1** [inscricao, cadeia, objeto] e **Tópico 4** [espectrograma, condicao, paciente] — densidade ponderada de ligação = 1.0295

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
