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
- Tokens significativos: **33,195**
- Grafo bruto: **6686** nós · **78385** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **4110** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `spira` | 2069 |
| 2 | `covideiro` | 1198 |
| 3 | `inscricao` | 1079 |
| 4 | `cadeia` | 1074 |
| 5 | `artigo` | 900 |
| 6 | `objeto` | 857 |
| 7 | `rede` | 832 |
| 8 | `respiratoria` | 806 |
| 9 | `insuficiencia` | 763 |
| 10 | `projeto` | 717 |
| 11 | `modelo` | 706 |
| 12 | `dado` | 706 |
| 13 | `marcelo` | 655 |
| 14 | `espectrograma` | 551 |
| 15 | `coleta` | 528 |
| 16 | `artigos` | 522 |
| 17 | `actante` | 458 |
| 18 | `audio` | 453 |
| 19 | `ruido` | 435 |
| 20 | `covid` | 429 |
| 21 | `condicoes` | 426 |
| 22 | `pratica` | 424 |
| 23 | `cientifico` | 420 |
| 24 | `pacientes` | 415 |
| 25 | `sinal` | 413 |
| 26 | `torna` | 397 |
| 27 | `analise` | 390 |
| 28 | `partir` | 385 |
| 29 | `dispositivo` | 380 |
| 30 | `dataset` | 369 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `spira` | 0.0392 |
| 2 | `covideiro` | 0.0230 |
| 3 | `inscricao` | 0.0211 |
| 4 | `cadeia` | 0.0209 |
| 5 | `artigo` | 0.0176 |
| 6 | `objeto` | 0.0168 |
| 7 | `rede` | 0.0165 |
| 8 | `respiratoria` | 0.0146 |
| 9 | `modelo` | 0.0143 |
| 10 | `projeto` | 0.0141 |
| 11 | `dado` | 0.0138 |
| 12 | `insuficiencia` | 0.0138 |
| 13 | `marcelo` | 0.0129 |
| 14 | `espectrograma` | 0.0112 |
| 15 | `coleta` | 0.0107 |
| 16 | `artigos` | 0.0102 |
| 17 | `actante` | 0.0094 |
| 18 | `audio` | 0.0093 |
| 19 | `ruido` | 0.0092 |
| 20 | `pratica` | 0.0088 |
| 21 | `sinal` | 0.0087 |
| 22 | `covid` | 0.0086 |
| 23 | `condicoes` | 0.0086 |
| 24 | `pacientes` | 0.0085 |
| 25 | `torna` | 0.0084 |
| 26 | `cientifico` | 0.0083 |
| 27 | `partir` | 0.0080 |
| 28 | `analise` | 0.0079 |
| 29 | `dispositivo` | 0.0079 |
| 30 | `secao` | 0.0078 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `preta` | 103 | 80 | +23 |
| 2 | `caixa` | 110 | 89 | +21 |
| 3 | `escala` | 79 | 66 | +13 |
| 4 | `parametros` | 134 | 122 | +12 |
| 5 | `tecnica` | 136 | 126 | +10 |
| 6 | `leitor` | 122 | 113 | +9 |
| 7 | `algoritmo` | 84 | 76 | +8 |
| 8 | `coeficientes` | 99 | 91 | +8 |
| 9 | `processo` | 116 | 109 | +7 |
| 10 | `ciencia` | 154 | 147 | +7 |
| 11 | `processamento` | 75 | 69 | +6 |
| 12 | `disponivel` | 101 | 95 | +6 |
| 13 | `acesso` | 105 | 100 | +5 |
| 14 | `controle` | 128 | 123 | +5 |
| 15 | `grade` | 144 | 139 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `spira` | 0.6184 |
| 2 | `inscricao` | 0.2631 |
| 3 | `covideiro` | 0.1768 |
| 4 | `cadeia` | 0.1240 |
| 5 | `objeto` | 0.1001 |
| 6 | `artigo` | 0.0996 |
| 7 | `modelo` | 0.0730 |
| 8 | `rede` | 0.0612 |
| 9 | `respiratoria` | 0.0534 |
| 10 | `espectrograma` | 0.0529 |
| 11 | `audio` | 0.0458 |
| 12 | `projeto` | 0.0415 |
| 13 | `dado` | 0.0361 |
| 14 | `ruido` | 0.0337 |
| 15 | `sinal` | 0.0272 |
| 16 | `coleta` | 0.0271 |
| 17 | `torna` | 0.0268 |
| 18 | `insuficiencia` | 0.0235 |
| 19 | `programa` | 0.0210 |
| 20 | `covid` | 0.0173 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `caixa` | `preta` | 0.898 | 84 |
| 2 | `imutavel` | `movel` | 0.845 | 79 |
| 3 | `respiratoria` | `insuficiencia` | 0.842 | 332 |
| 4 | `calculo` | `centro` | 0.766 | 85 |
| 5 | `grupo` | `controle` | 0.649 | 40 |
| 6 | `neural` | `rede` | 0.606 | 136 |
| 7 | `acao` | `programa` | 0.563 | 38 |
| 8 | `sinal` | `acustico` | 0.549 | 64 |
| 9 | `tornou` | `possivel` | 0.547 | 37 |
| 10 | `acesso` | `disponivel` | 0.532 | 27 |
| 11 | `linguagem` | `processamento` | 0.530 | 27 |
| 12 | `torna` | `visivel` | 0.514 | 60 |
| 13 | `entrevista` | `marcelo` | 0.506 | 105 |
| 14 | `publico` | `saude` | 0.503 | 22 |
| 15 | `publico` | `repositorio` | 0.488 | 21 |
| 16 | `ciencia` | `construcao` | 0.486 | 22 |
| 17 | `condicoes` | `producao` | 0.476 | 51 |
| 18 | `covideiro` | `pandemico` | 0.476 | 103 |
| 19 | `enfermaria` | `ruido` | 0.464 | 58 |
| 20 | `ciencia` | `acao` | 0.461 | 21 |
| 21 | `fonoaudiologos` | `medicos` | 0.458 | 28 |
| 22 | `cadeia` | `translacoes` | 0.456 | 60 |
| 23 | `modelo` | `treinado` | 0.448 | 49 |
| 24 | `saude` | `pesquisa` | 0.434 | 18 |
| 25 | `forca` | `precisa` | 0.432 | 12 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (43 termos): spira, artigo, projeto, marcelo, artigos, cientifico
- **Tópico 2** (35 termos): modelo, dado, audio, sinal, treinamento, acustico
- **Tópico 3** (34 termos): inscricao, cadeia, torna, dispositivo, secao, ponto
- **Tópico 4** (27 termos): rede, espectrograma, actante, partir, paciente, imagem
- **Tópico 5** (25 termos): covideiro, respiratoria, insuficiencia, coleta, ruido, covid
- **Tópico 6** (9 termos): objeto, pratica, distintos, distintas, diferentes, produzido
- **Tópico 7** (5 termos): programa, acao, inscrito, ciencia, construcao
- **Tópico 8** (2 termos): movel, imutavel

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 2** [modelo, dado, audio] e **Tópico 3** [inscricao, cadeia, torna] — densidade ponderada de ligação = 0.6697
- Lacuna entre **Tópico 1** [spira, artigo, projeto] e **Tópico 2** [modelo, dado, audio] — densidade ponderada de ligação = 0.7748
- Lacuna entre **Tópico 2** [modelo, dado, audio] e **Tópico 4** [rede, espectrograma, actante] — densidade ponderada de ligação = 0.9090
- Lacuna entre **Tópico 3** [inscricao, cadeia, torna] e **Tópico 5** [covideiro, respiratoria, insuficiencia] — densidade ponderada de ligação = 0.9153
- Lacuna entre **Tópico 1** [spira, artigo, projeto] e **Tópico 4** [rede, espectrograma, actante] — densidade ponderada de ligação = 0.9828
- Lacuna entre **Tópico 4** [rede, espectrograma, actante] e **Tópico 5** [covideiro, respiratoria, insuficiencia] — densidade ponderada de ligação = 1.1170

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
