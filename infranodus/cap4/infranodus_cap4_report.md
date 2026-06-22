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
- Tokens significativos: **33,706**
- Grafo bruto: **6786** nós · **79639** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **4117** arestas
- Tópicos detectados (Louvain): **7**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `spira` | 2093 |
| 2 | `covideiro` | 1169 |
| 3 | `inscricao` | 1135 |
| 4 | `cadeia` | 1057 |
| 5 | `artigo` | 939 |
| 6 | `rede` | 898 |
| 7 | `objeto` | 876 |
| 8 | `respiratoria` | 809 |
| 9 | `insuficiencia` | 768 |
| 10 | `modelo` | 717 |
| 11 | `projeto` | 714 |
| 12 | `dado` | 703 |
| 13 | `marcelo` | 643 |
| 14 | `espectrograma` | 572 |
| 15 | `artigos` | 525 |
| 16 | `coleta` | 522 |
| 17 | `actante` | 473 |
| 18 | `audio` | 449 |
| 19 | `analise` | 434 |
| 20 | `pratica` | 433 |
| 21 | `ruido` | 432 |
| 22 | `covid` | 429 |
| 23 | `condicoes` | 425 |
| 24 | `partir` | 420 |
| 25 | `cientifico` | 419 |
| 26 | `pacientes` | 415 |
| 27 | `sinal` | 414 |
| 28 | `torna` | 389 |
| 29 | `secao` | 376 |
| 30 | `dataset` | 375 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `spira` | 0.0396 |
| 2 | `covideiro` | 0.0223 |
| 3 | `inscricao` | 0.0221 |
| 4 | `cadeia` | 0.0205 |
| 5 | `artigo` | 0.0182 |
| 6 | `rede` | 0.0176 |
| 7 | `objeto` | 0.0171 |
| 8 | `respiratoria` | 0.0146 |
| 9 | `modelo` | 0.0144 |
| 10 | `projeto` | 0.0140 |
| 11 | `insuficiencia` | 0.0138 |
| 12 | `dado` | 0.0137 |
| 13 | `marcelo` | 0.0125 |
| 14 | `espectrograma` | 0.0115 |
| 15 | `coleta` | 0.0105 |
| 16 | `artigos` | 0.0102 |
| 17 | `actante` | 0.0096 |
| 18 | `audio` | 0.0092 |
| 19 | `ruido` | 0.0091 |
| 20 | `pratica` | 0.0089 |
| 21 | `sinal` | 0.0086 |
| 22 | `analise` | 0.0086 |
| 23 | `covid` | 0.0086 |
| 24 | `partir` | 0.0086 |
| 25 | `condicoes` | 0.0086 |
| 26 | `pacientes` | 0.0084 |
| 27 | `cientifico` | 0.0083 |
| 28 | `torna` | 0.0082 |
| 29 | `secao` | 0.0079 |
| 30 | `dataset` | 0.0077 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `caixa` | 110 | 87 | +23 |
| 2 | `preta` | 104 | 84 | +20 |
| 3 | `escala` | 81 | 68 | +13 |
| 4 | `parametros` | 131 | 120 | +11 |
| 5 | `coeficientes` | 103 | 93 | +10 |
| 6 | `disponivel` | 113 | 104 | +9 |
| 7 | `linguagem` | 146 | 137 | +9 |
| 8 | `algoritmo` | 84 | 76 | +8 |
| 9 | `momento` | 96 | 88 | +8 |
| 10 | `leitor` | 124 | 116 | +8 |
| 11 | `processamento` | 76 | 69 | +7 |
| 12 | `sinal` | 27 | 21 | +6 |
| 13 | `tecnica` | 136 | 130 | +6 |
| 14 | `grade` | 151 | 145 | +6 |
| 15 | `acustico` | 59 | 54 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `spira` | 0.6313 |
| 2 | `inscricao` | 0.2612 |
| 3 | `covideiro` | 0.1673 |
| 4 | `cadeia` | 0.1287 |
| 5 | `objeto` | 0.0963 |
| 6 | `artigo` | 0.0944 |
| 7 | `modelo` | 0.0730 |
| 8 | `espectrograma` | 0.0625 |
| 9 | `rede` | 0.0618 |
| 10 | `respiratoria` | 0.0537 |
| 11 | `dado` | 0.0417 |
| 12 | `projeto` | 0.0407 |
| 13 | `audio` | 0.0404 |
| 14 | `ruido` | 0.0321 |
| 15 | `coleta` | 0.0272 |
| 16 | `sinal` | 0.0267 |
| 17 | `torna` | 0.0250 |
| 18 | `insuficiencia` | 0.0234 |
| 19 | `marcelo` | 0.0213 |
| 20 | `programa` | 0.0209 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `caixa` | `preta` | 0.898 | 84 |
| 2 | `imutavel` | `movel` | 0.846 | 82 |
| 3 | `respiratoria` | `insuficiencia` | 0.843 | 332 |
| 4 | `grupo` | `controle` | 0.646 | 40 |
| 5 | `neural` | `rede` | 0.592 | 136 |
| 6 | `acao` | `programa` | 0.561 | 38 |
| 7 | `sinal` | `acustico` | 0.550 | 64 |
| 8 | `tornou` | `possivel` | 0.536 | 34 |
| 9 | `linguagem` | `processamento` | 0.531 | 27 |
| 10 | `entrevista` | `marcelo` | 0.508 | 107 |
| 11 | `torna` | `visivel` | 0.507 | 57 |
| 12 | `publico` | `saude` | 0.504 | 22 |
| 13 | `acesso` | `disponivel` | 0.498 | 24 |
| 14 | `ciencia` | `construcao` | 0.487 | 22 |
| 15 | `covideiro` | `pandemico` | 0.482 | 103 |
| 16 | `condicoes` | `producao` | 0.478 | 51 |
| 17 | `publico` | `repositorio` | 0.476 | 21 |
| 18 | `enfermaria` | `ruido` | 0.463 | 58 |
| 19 | `ciencia` | `acao` | 0.462 | 21 |
| 20 | `cadeia` | `translacoes` | 0.461 | 60 |
| 21 | `fonoaudiologos` | `medicos` | 0.459 | 28 |
| 22 | `modelo` | `treinado` | 0.448 | 49 |
| 23 | `conceito` | `referencia` | 0.437 | 16 |
| 24 | `saude` | `pesquisa` | 0.435 | 18 |
| 25 | `forca` | `precisa` | 0.433 | 12 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (39 termos): spira, artigo, projeto, marcelo, artigos, analise
- **Tópico 2** (38 termos): inscricao, cadeia, torna, secao, dispositivo, ponto
- **Tópico 3** (31 termos): covideiro, modelo, dado, coleta, actante, condicoes
- **Tópico 4** (25 termos): rede, espectrograma, partir, imagem, produz, neural
- **Tópico 5** (25 termos): audio, ruido, sinal, paciente, arquivo, virus
- **Tópico 6** (14 termos): respiratoria, insuficiencia, covid, pacientes, condicao, deteccao
- **Tópico 7** (8 termos): objeto, pratica, distintos, distintas, diferentes, produzido

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 2** [inscricao, cadeia, torna] e **Tópico 5** [audio, ruido, sinal] — densidade ponderada de ligação = 0.7053
- Lacuna entre **Tópico 1** [spira, artigo, projeto] e **Tópico 5** [audio, ruido, sinal] — densidade ponderada de ligação = 0.7754
- Lacuna entre **Tópico 3** [covideiro, modelo, dado] e **Tópico 4** [rede, espectrograma, partir] — densidade ponderada de ligação = 0.7897
- Lacuna entre **Tópico 4** [rede, espectrograma, partir] e **Tópico 5** [audio, ruido, sinal] — densidade ponderada de ligação = 0.8352
- Lacuna entre **Tópico 2** [inscricao, cadeia, torna] e **Tópico 4** [rede, espectrograma, partir] — densidade ponderada de ligação = 0.8474
- Lacuna entre **Tópico 1** [spira, artigo, projeto] e **Tópico 4** [rede, espectrograma, partir] — densidade ponderada de ligação = 0.9272

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
