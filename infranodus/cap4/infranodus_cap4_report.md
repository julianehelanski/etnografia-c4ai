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
- Tokens significativos: **33,378**
- Grafo bruto: **6704** nós · **78811** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **4112** arestas
- Tópicos detectados (Louvain): **7**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `spira` | 2086 |
| 2 | `covideiro` | 1165 |
| 3 | `inscricao` | 1133 |
| 4 | `cadeia` | 1064 |
| 5 | `artigo` | 937 |
| 6 | `objeto` | 878 |
| 7 | `rede` | 869 |
| 8 | `respiratoria` | 808 |
| 9 | `insuficiencia` | 767 |
| 10 | `projeto` | 719 |
| 11 | `modelo` | 709 |
| 12 | `dado` | 701 |
| 13 | `marcelo` | 664 |
| 14 | `espectrograma` | 572 |
| 15 | `artigos` | 528 |
| 16 | `coleta` | 523 |
| 17 | `actante` | 471 |
| 18 | `audio` | 453 |
| 19 | `pratica` | 435 |
| 20 | `ruido` | 435 |
| 21 | `covid` | 429 |
| 22 | `condicoes` | 425 |
| 23 | `pacientes` | 418 |
| 24 | `sinal` | 416 |
| 25 | `partir` | 408 |
| 26 | `cientifico` | 407 |
| 27 | `torna` | 403 |
| 28 | `analise` | 401 |
| 29 | `secao` | 380 |
| 30 | `dispositivo` | 376 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `spira` | 0.0395 |
| 2 | `covideiro` | 0.0222 |
| 3 | `inscricao` | 0.0221 |
| 4 | `cadeia` | 0.0207 |
| 5 | `artigo` | 0.0182 |
| 6 | `objeto` | 0.0172 |
| 7 | `rede` | 0.0171 |
| 8 | `respiratoria` | 0.0146 |
| 9 | `modelo` | 0.0143 |
| 10 | `projeto` | 0.0141 |
| 11 | `insuficiencia` | 0.0138 |
| 12 | `dado` | 0.0137 |
| 13 | `marcelo` | 0.0129 |
| 14 | `espectrograma` | 0.0116 |
| 15 | `coleta` | 0.0106 |
| 16 | `artigos` | 0.0103 |
| 17 | `actante` | 0.0096 |
| 18 | `audio` | 0.0092 |
| 19 | `ruido` | 0.0092 |
| 20 | `pratica` | 0.0090 |
| 21 | `sinal` | 0.0087 |
| 22 | `covid` | 0.0086 |
| 23 | `condicoes` | 0.0086 |
| 24 | `pacientes` | 0.0085 |
| 25 | `torna` | 0.0085 |
| 26 | `partir` | 0.0084 |
| 27 | `analise` | 0.0081 |
| 28 | `cientifico` | 0.0081 |
| 29 | `secao` | 0.0080 |
| 30 | `dispositivo` | 0.0078 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `caixa` | 110 | 88 | +22 |
| 2 | `preta` | 103 | 83 | +20 |
| 3 | `escala` | 78 | 65 | +13 |
| 4 | `parametros` | 131 | 119 | +12 |
| 5 | `coeficientes` | 102 | 93 | +9 |
| 6 | `operacao` | 112 | 103 | +9 |
| 7 | `tecnica` | 140 | 131 | +9 |
| 8 | `processamento` | 77 | 69 | +8 |
| 9 | `leitor` | 123 | 115 | +8 |
| 10 | `algoritmo` | 83 | 77 | +6 |
| 11 | `grade` | 149 | 143 | +6 |
| 12 | `visivel` | 43 | 38 | +5 |
| 13 | `momento` | 91 | 86 | +5 |
| 14 | `acao` | 96 | 91 | +5 |
| 15 | `escolha` | 111 | 106 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `spira` | 0.6226 |
| 2 | `inscricao` | 0.2677 |
| 3 | `covideiro` | 0.1678 |
| 4 | `cadeia` | 0.1340 |
| 5 | `objeto` | 0.1018 |
| 6 | `artigo` | 0.1012 |
| 7 | `modelo` | 0.0729 |
| 8 | `rede` | 0.0628 |
| 9 | `espectrograma` | 0.0618 |
| 10 | `respiratoria` | 0.0532 |
| 11 | `audio` | 0.0446 |
| 12 | `projeto` | 0.0395 |
| 13 | `dado` | 0.0355 |
| 14 | `ruido` | 0.0328 |
| 15 | `sinal` | 0.0272 |
| 16 | `torna` | 0.0267 |
| 17 | `coleta` | 0.0266 |
| 18 | `marcelo` | 0.0234 |
| 19 | `insuficiencia` | 0.0232 |
| 20 | `programa` | 0.0211 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `caixa` | `preta` | 0.898 | 84 |
| 2 | `imutavel` | `movel` | 0.846 | 82 |
| 3 | `respiratoria` | `insuficiencia` | 0.842 | 332 |
| 4 | `grupo` | `controle` | 0.645 | 40 |
| 5 | `neural` | `rede` | 0.603 | 136 |
| 6 | `acao` | `programa` | 0.561 | 38 |
| 7 | `sinal` | `acustico` | 0.549 | 64 |
| 8 | `tornou` | `possivel` | 0.548 | 37 |
| 9 | `linguagem` | `processamento` | 0.531 | 27 |
| 10 | `torna` | `visivel` | 0.511 | 60 |
| 11 | `acesso` | `disponivel` | 0.511 | 24 |
| 12 | `publico` | `saude` | 0.504 | 22 |
| 13 | `entrevista` | `marcelo` | 0.501 | 107 |
| 14 | `publico` | `repositorio` | 0.488 | 21 |
| 15 | `ciencia` | `construcao` | 0.486 | 22 |
| 16 | `covideiro` | `pandemico` | 0.481 | 103 |
| 17 | `condicoes` | `producao` | 0.477 | 51 |
| 18 | `enfermaria` | `ruido` | 0.462 | 58 |
| 19 | `ciencia` | `acao` | 0.461 | 21 |
| 20 | `cadeia` | `translacoes` | 0.460 | 60 |
| 21 | `fonoaudiologos` | `medicos` | 0.459 | 28 |
| 22 | `modelo` | `treinado` | 0.448 | 49 |
| 23 | `conceito` | `referencia` | 0.445 | 16 |
| 24 | `saude` | `pesquisa` | 0.434 | 18 |
| 25 | `forca` | `precisa` | 0.432 | 12 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (52 termos): rede, modelo, espectrograma, audio, sinal, partir
- **Tópico 2** (42 termos): spira, artigo, projeto, marcelo, artigos, cientifico
- **Tópico 3** (26 termos): inscricao, cadeia, torna, dispositivo, ponto, translacao
- **Tópico 4** (23 termos): covideiro, dado, coleta, ruido, condicoes, pacientes
- **Tópico 5** (17 termos): actante, latour, virus, humano, descreve, configuracao
- **Tópico 6** (12 termos): objeto, pratica, distintos, distintas, diferentes, computacional
- **Tópico 7** (8 termos): respiratoria, insuficiencia, covid, deteccao, versao, acustica

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [rede, modelo, espectrograma] e **Tópico 5** [actante, latour, virus] — densidade ponderada de ligação = 0.6075
- Lacuna entre **Tópico 1** [rede, modelo, espectrograma] e **Tópico 3** [inscricao, cadeia, torna] — densidade ponderada de ligação = 0.8210
- Lacuna entre **Tópico 1** [rede, modelo, espectrograma] e **Tópico 2** [spira, artigo, projeto] — densidade ponderada de ligação = 0.9116
- Lacuna entre **Tópico 1** [rede, modelo, espectrograma] e **Tópico 4** [covideiro, dado, coleta] — densidade ponderada de ligação = 0.9281
- Lacuna entre **Tópico 2** [spira, artigo, projeto] e **Tópico 5** [actante, latour, virus] — densidade ponderada de ligação = 0.9678
- Lacuna entre **Tópico 3** [inscricao, cadeia, torna] e **Tópico 5** [actante, latour, virus] — densidade ponderada de ligação = 1.0407

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
