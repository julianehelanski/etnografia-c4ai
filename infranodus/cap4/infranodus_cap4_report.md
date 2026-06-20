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
- Tokens significativos: **33,162**
- Grafo bruto: **6699** nós · **78360** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **4116** arestas
- Tópicos detectados (Louvain): **6**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `spira` | 2071 |
| 2 | `covideiro` | 1181 |
| 3 | `inscricao` | 1061 |
| 4 | `cadeia` | 1050 |
| 5 | `artigo` | 906 |
| 6 | `objeto` | 841 |
| 7 | `rede` | 823 |
| 8 | `respiratoria` | 807 |
| 9 | `insuficiencia` | 768 |
| 10 | `projeto` | 717 |
| 11 | `dado` | 706 |
| 12 | `modelo` | 700 |
| 13 | `marcelo` | 655 |
| 14 | `espectrograma` | 560 |
| 15 | `coleta` | 533 |
| 16 | `artigos` | 521 |
| 17 | `actante` | 458 |
| 18 | `audio` | 453 |
| 19 | `ruido` | 435 |
| 20 | `covid` | 426 |
| 21 | `cientifico` | 424 |
| 22 | `condicoes` | 422 |
| 23 | `pacientes` | 418 |
| 24 | `sinal` | 416 |
| 25 | `pratica` | 414 |
| 26 | `torna` | 396 |
| 27 | `analise` | 390 |
| 28 | `partir` | 388 |
| 29 | `dispositivo` | 384 |
| 30 | `dataset` | 364 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `spira` | 0.0394 |
| 2 | `covideiro` | 0.0227 |
| 3 | `inscricao` | 0.0208 |
| 4 | `cadeia` | 0.0205 |
| 5 | `artigo` | 0.0177 |
| 6 | `objeto` | 0.0166 |
| 7 | `rede` | 0.0164 |
| 8 | `respiratoria` | 0.0147 |
| 9 | `modelo` | 0.0142 |
| 10 | `projeto` | 0.0141 |
| 11 | `insuficiencia` | 0.0139 |
| 12 | `dado` | 0.0139 |
| 13 | `marcelo` | 0.0129 |
| 14 | `espectrograma` | 0.0114 |
| 15 | `coleta` | 0.0108 |
| 16 | `artigos` | 0.0102 |
| 17 | `actante` | 0.0094 |
| 18 | `audio` | 0.0093 |
| 19 | `ruido` | 0.0092 |
| 20 | `sinal` | 0.0087 |
| 21 | `pratica` | 0.0087 |
| 22 | `covid` | 0.0086 |
| 23 | `pacientes` | 0.0086 |
| 24 | `condicoes` | 0.0085 |
| 25 | `cientifico` | 0.0084 |
| 26 | `torna` | 0.0084 |
| 27 | `partir` | 0.0081 |
| 28 | `dispositivo` | 0.0080 |
| 29 | `analise` | 0.0079 |
| 30 | `condicao` | 0.0076 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `preta` | 104 | 81 | +23 |
| 2 | `caixa` | 110 | 90 | +20 |
| 3 | `parametros` | 131 | 116 | +15 |
| 4 | `escala` | 81 | 68 | +13 |
| 5 | `controle` | 126 | 117 | +9 |
| 6 | `algoritmo` | 83 | 75 | +8 |
| 7 | `coeficientes` | 93 | 86 | +7 |
| 8 | `disponivel` | 102 | 95 | +7 |
| 9 | `tecnica` | 140 | 133 | +7 |
| 10 | `microfone` | 158 | 151 | +7 |
| 11 | `processamento` | 75 | 69 | +6 |
| 12 | `momento` | 100 | 94 | +6 |
| 13 | `escolha` | 106 | 100 | +6 |
| 14 | `acesso` | 108 | 102 | +6 |
| 15 | `leitor` | 128 | 122 | +6 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `spira` | 0.6226 |
| 2 | `inscricao` | 0.2554 |
| 3 | `covideiro` | 0.1659 |
| 4 | `cadeia` | 0.1203 |
| 5 | `objeto` | 0.0998 |
| 6 | `artigo` | 0.0884 |
| 7 | `modelo` | 0.0729 |
| 8 | `espectrograma` | 0.0628 |
| 9 | `rede` | 0.0580 |
| 10 | `respiratoria` | 0.0520 |
| 11 | `dado` | 0.0468 |
| 12 | `audio` | 0.0461 |
| 13 | `projeto` | 0.0420 |
| 14 | `ruido` | 0.0334 |
| 15 | `sinal` | 0.0273 |
| 16 | `coleta` | 0.0272 |
| 17 | `torna` | 0.0269 |
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
| 2 | `respiratoria` | `insuficiencia` | 0.842 | 332 |
| 3 | `imutavel` | `movel` | 0.842 | 81 |
| 4 | `calculo` | `centro` | 0.763 | 88 |
| 5 | `grupo` | `controle` | 0.649 | 40 |
| 6 | `neural` | `rede` | 0.610 | 136 |
| 7 | `acao` | `programa` | 0.563 | 38 |
| 8 | `tornou` | `possivel` | 0.551 | 37 |
| 9 | `sinal` | `acustico` | 0.549 | 64 |
| 10 | `acesso` | `disponivel` | 0.532 | 27 |
| 11 | `linguagem` | `processamento` | 0.530 | 27 |
| 12 | `torna` | `visivel` | 0.509 | 57 |
| 13 | `entrevista` | `marcelo` | 0.506 | 105 |
| 14 | `publico` | `saude` | 0.503 | 22 |
| 15 | `publico` | `repositorio` | 0.488 | 21 |
| 16 | `ciencia` | `construcao` | 0.486 | 22 |
| 17 | `covideiro` | `pandemico` | 0.477 | 103 |
| 18 | `condicoes` | `producao` | 0.476 | 51 |
| 19 | `enfermaria` | `ruido` | 0.464 | 58 |
| 20 | `ciencia` | `acao` | 0.461 | 21 |
| 21 | `fonoaudiologos` | `medicos` | 0.458 | 28 |
| 22 | `cadeia` | `translacoes` | 0.453 | 57 |
| 23 | `modelo` | `treinado` | 0.449 | 49 |
| 24 | `saude` | `pesquisa` | 0.434 | 18 |
| 25 | `cadeia` | `translacao` | 0.428 | 83 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (51 termos): dado, modelo, espectrograma, audio, sinal, paciente
- **Tópico 2** (37 termos): spira, artigo, projeto, marcelo, artigos, cientifico
- **Tópico 3** (35 termos): inscricao, cadeia, torna, dispositivo, secao, ponto
- **Tópico 4** (22 termos): respiratoria, insuficiencia, coleta, ruido, covid, pacientes
- **Tópico 5** (19 termos): covideiro, actante, condicoes, pandemico, humano, configuracao
- **Tópico 6** (16 termos): objeto, rede, pratica, partir, neural, distintos

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 3** [inscricao, cadeia, torna] e **Tópico 4** [respiratoria, insuficiencia, coleta] — densidade ponderada de ligação = 0.6390
- Lacuna entre **Tópico 1** [dado, modelo, espectrograma] e **Tópico 3** [inscricao, cadeia, torna] — densidade ponderada de ligação = 0.7804
- Lacuna entre **Tópico 1** [dado, modelo, espectrograma] e **Tópico 2** [spira, artigo, projeto] — densidade ponderada de ligação = 0.8532
- Lacuna entre **Tópico 1** [dado, modelo, espectrograma] e **Tópico 5** [covideiro, actante, condicoes] — densidade ponderada de ligação = 0.8844
- Lacuna entre **Tópico 1** [dado, modelo, espectrograma] e **Tópico 4** [respiratoria, insuficiencia, coleta] — densidade ponderada de ligação = 0.9733
- Lacuna entre **Tópico 3** [inscricao, cadeia, torna] e **Tópico 5** [covideiro, actante, condicoes] — densidade ponderada de ligação = 1.1699

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
