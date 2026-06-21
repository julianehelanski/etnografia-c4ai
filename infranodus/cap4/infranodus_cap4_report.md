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
- Tokens significativos: **33,313**
- Grafo bruto: **6697** nós · **78691** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **4108** arestas
- Tópicos detectados (Louvain): **9**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `spira` | 2084 |
| 2 | `covideiro` | 1169 |
| 3 | `inscricao` | 1134 |
| 4 | `cadeia` | 1055 |
| 5 | `artigo` | 939 |
| 6 | `objeto` | 876 |
| 7 | `rede` | 869 |
| 8 | `respiratoria` | 805 |
| 9 | `insuficiencia` | 765 |
| 10 | `modelo` | 713 |
| 11 | `projeto` | 712 |
| 12 | `dado` | 703 |
| 13 | `marcelo` | 646 |
| 14 | `espectrograma` | 572 |
| 15 | `coleta` | 522 |
| 16 | `artigos` | 522 |
| 17 | `actante` | 471 |
| 18 | `audio` | 446 |
| 19 | `pratica` | 435 |
| 20 | `ruido` | 432 |
| 21 | `covid` | 429 |
| 22 | `condicoes` | 425 |
| 23 | `partir` | 417 |
| 24 | `pacientes` | 415 |
| 25 | `sinal` | 414 |
| 26 | `cientifico` | 413 |
| 27 | `analise` | 411 |
| 28 | `torna` | 405 |
| 29 | `dataset` | 375 |
| 30 | `secao` | 374 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `spira` | 0.0393 |
| 2 | `covideiro` | 0.0223 |
| 3 | `inscricao` | 0.0221 |
| 4 | `cadeia` | 0.0205 |
| 5 | `artigo` | 0.0182 |
| 6 | `rede` | 0.0171 |
| 7 | `objeto` | 0.0171 |
| 8 | `respiratoria` | 0.0145 |
| 9 | `modelo` | 0.0143 |
| 10 | `projeto` | 0.0139 |
| 11 | `insuficiencia` | 0.0137 |
| 12 | `dado` | 0.0137 |
| 13 | `marcelo` | 0.0126 |
| 14 | `espectrograma` | 0.0115 |
| 15 | `coleta` | 0.0105 |
| 16 | `artigos` | 0.0101 |
| 17 | `actante` | 0.0095 |
| 18 | `audio` | 0.0091 |
| 19 | `ruido` | 0.0091 |
| 20 | `pratica` | 0.0090 |
| 21 | `sinal` | 0.0086 |
| 22 | `covid` | 0.0086 |
| 23 | `condicoes` | 0.0086 |
| 24 | `partir` | 0.0085 |
| 25 | `torna` | 0.0085 |
| 26 | `pacientes` | 0.0084 |
| 27 | `analise` | 0.0082 |
| 28 | `cientifico` | 0.0081 |
| 29 | `secao` | 0.0078 |
| 30 | `dataset` | 0.0077 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `caixa` | 111 | 87 | +24 |
| 2 | `preta` | 104 | 84 | +20 |
| 3 | `escala` | 81 | 66 | +15 |
| 4 | `coeficientes` | 102 | 90 | +12 |
| 5 | `parametros` | 132 | 120 | +12 |
| 6 | `tecnica` | 141 | 131 | +10 |
| 7 | `operacao` | 113 | 104 | +9 |
| 8 | `linguagem` | 147 | 138 | +9 |
| 9 | `leitor` | 125 | 117 | +8 |
| 10 | `processamento` | 76 | 69 | +7 |
| 11 | `algoritmo` | 83 | 76 | +7 |
| 12 | `momento` | 99 | 92 | +7 |
| 13 | `grade` | 149 | 142 | +7 |
| 14 | `acustico` | 60 | 54 | +6 |
| 15 | `visivel` | 45 | 40 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `spira` | 0.6359 |
| 2 | `inscricao` | 0.2618 |
| 3 | `covideiro` | 0.1678 |
| 4 | `cadeia` | 0.1291 |
| 5 | `objeto` | 0.0968 |
| 6 | `artigo` | 0.0943 |
| 7 | `modelo` | 0.0730 |
| 8 | `espectrograma` | 0.0622 |
| 9 | `rede` | 0.0614 |
| 10 | `respiratoria` | 0.0538 |
| 11 | `dado` | 0.0416 |
| 12 | `projeto` | 0.0407 |
| 13 | `audio` | 0.0404 |
| 14 | `ruido` | 0.0321 |
| 15 | `coleta` | 0.0272 |
| 16 | `torna` | 0.0266 |
| 17 | `sinal` | 0.0262 |
| 18 | `insuficiencia` | 0.0234 |
| 19 | `marcelo` | 0.0213 |
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
| 4 | `calculo` | `centro` | 0.766 | 85 |
| 5 | `grupo` | `controle` | 0.645 | 40 |
| 6 | `neural` | `rede` | 0.602 | 136 |
| 7 | `acao` | `programa` | 0.560 | 38 |
| 8 | `sinal` | `acustico` | 0.549 | 64 |
| 9 | `tornou` | `possivel` | 0.535 | 34 |
| 10 | `linguagem` | `processamento` | 0.531 | 27 |
| 11 | `torna` | `visivel` | 0.514 | 60 |
| 12 | `acesso` | `disponivel` | 0.511 | 24 |
| 13 | `entrevista` | `marcelo` | 0.507 | 107 |
| 14 | `publico` | `saude` | 0.503 | 22 |
| 15 | `publico` | `repositorio` | 0.488 | 21 |
| 16 | `ciencia` | `construcao` | 0.486 | 22 |
| 17 | `covideiro` | `pandemico` | 0.481 | 103 |
| 18 | `condicoes` | `producao` | 0.477 | 51 |
| 19 | `enfermaria` | `ruido` | 0.462 | 58 |
| 20 | `ciencia` | `acao` | 0.461 | 21 |
| 21 | `cadeia` | `translacoes` | 0.461 | 60 |
| 22 | `fonoaudiologos` | `medicos` | 0.458 | 28 |
| 23 | `modelo` | `treinado` | 0.448 | 49 |
| 24 | `conceito` | `referencia` | 0.445 | 16 |
| 25 | `saude` | `pesquisa` | 0.434 | 18 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (43 termos): modelo, dado, audio, ruido, pacientes, sinal
- **Tópico 2** (43 termos): spira, artigo, projeto, marcelo, artigos, cientifico
- **Tópico 3** (30 termos): inscricao, cadeia, torna, dispositivo, ponto, translacao
- **Tópico 4** (27 termos): covideiro, coleta, actante, condicoes, condicao, pandemico
- **Tópico 5** (16 termos): rede, espectrograma, partir, imagem, produz, neural
- **Tópico 6** (9 termos): objeto, pratica, distintos, distintas, diferentes, computacional
- **Tópico 7** (8 termos): respiratoria, insuficiencia, covid, deteccao, versao, acustica
- **Tópico 8** (2 termos): movel, imutavel

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [modelo, dado, audio] e **Tópico 3** [inscricao, cadeia, torna] — densidade ponderada de ligação = 0.7016
- Lacuna entre **Tópico 1** [modelo, dado, audio] e **Tópico 2** [spira, artigo, projeto] — densidade ponderada de ligação = 0.8183
- Lacuna entre **Tópico 4** [covideiro, coleta, actante] e **Tópico 5** [rede, espectrograma, partir] — densidade ponderada de ligação = 0.8704
- Lacuna entre **Tópico 1** [modelo, dado, audio] e **Tópico 4** [covideiro, coleta, actante] — densidade ponderada de ligação = 0.9690
- Lacuna entre **Tópico 1** [modelo, dado, audio] e **Tópico 5** [rede, espectrograma, partir] — densidade ponderada de ligação = 1.0087
- Lacuna entre **Tópico 3** [inscricao, cadeia, torna] e **Tópico 5** [rede, espectrograma, partir] — densidade ponderada de ligação = 1.0312

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
