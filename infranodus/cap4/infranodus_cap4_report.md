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
- Tokens significativos: **33,614**
- Grafo bruto: **6733** nós · **79255** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **4114** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `spira` | 2091 |
| 2 | `covideiro` | 1138 |
| 3 | `inscricao` | 1066 |
| 4 | `cadeia` | 1028 |
| 5 | `artigo` | 880 |
| 6 | `rede` | 837 |
| 7 | `respiratoria` | 815 |
| 8 | `objeto` | 794 |
| 9 | `insuficiencia` | 782 |
| 10 | `projeto` | 730 |
| 11 | `modelo` | 707 |
| 12 | `dado` | 706 |
| 13 | `marcelo` | 679 |
| 14 | `espectrograma` | 564 |
| 15 | `artigos` | 531 |
| 16 | `coleta` | 531 |
| 17 | `actante` | 478 |
| 18 | `audio` | 466 |
| 19 | `covid` | 434 |
| 20 | `ruido` | 433 |
| 21 | `torna` | 420 |
| 22 | `cientifico` | 417 |
| 23 | `sinal` | 414 |
| 24 | `analise` | 410 |
| 25 | `condicoes` | 409 |
| 26 | `pacientes` | 407 |
| 27 | `partir` | 402 |
| 28 | `pratica` | 396 |
| 29 | `dispositivo` | 378 |
| 30 | `condicao` | 372 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `spira` | 0.0397 |
| 2 | `covideiro` | 0.0221 |
| 3 | `inscricao` | 0.0210 |
| 4 | `cadeia` | 0.0203 |
| 5 | `artigo` | 0.0173 |
| 6 | `rede` | 0.0167 |
| 7 | `objeto` | 0.0157 |
| 8 | `respiratoria` | 0.0148 |
| 9 | `projeto` | 0.0144 |
| 10 | `modelo` | 0.0143 |
| 11 | `insuficiencia` | 0.0142 |
| 12 | `dado` | 0.0139 |
| 13 | `marcelo` | 0.0136 |
| 14 | `espectrograma` | 0.0115 |
| 15 | `coleta` | 0.0108 |
| 16 | `artigos` | 0.0104 |
| 17 | `actante` | 0.0098 |
| 18 | `audio` | 0.0096 |
| 19 | `ruido` | 0.0091 |
| 20 | `torna` | 0.0088 |
| 21 | `covid` | 0.0088 |
| 22 | `sinal` | 0.0087 |
| 23 | `pacientes` | 0.0084 |
| 24 | `partir` | 0.0084 |
| 25 | `condicoes` | 0.0083 |
| 26 | `analise` | 0.0083 |
| 27 | `pratica` | 0.0083 |
| 28 | `cientifico` | 0.0083 |
| 29 | `dispositivo` | 0.0078 |
| 30 | `condicao` | 0.0078 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `preta` | 93 | 74 | +19 |
| 2 | `escala` | 86 | 69 | +17 |
| 3 | `caixa` | 102 | 86 | +16 |
| 4 | `parametros` | 112 | 98 | +14 |
| 5 | `processo` | 105 | 96 | +9 |
| 6 | `linguagem` | 139 | 130 | +9 |
| 7 | `grade` | 144 | 135 | +9 |
| 8 | `processamento` | 78 | 70 | +8 |
| 9 | `disponivel` | 107 | 101 | +6 |
| 10 | `carrega` | 116 | 110 | +6 |
| 11 | `tecnica` | 135 | 129 | +6 |
| 12 | `publico` | 72 | 67 | +5 |
| 13 | `leitor` | 126 | 121 | +5 |
| 14 | `designa` | 137 | 132 | +5 |
| 15 | `ciencia` | 149 | 144 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `spira` | 0.6532 |
| 2 | `inscricao` | 0.2546 |
| 3 | `covideiro` | 0.1565 |
| 4 | `cadeia` | 0.1395 |
| 5 | `artigo` | 0.0895 |
| 6 | `objeto` | 0.0883 |
| 7 | `modelo` | 0.0664 |
| 8 | `espectrograma` | 0.0633 |
| 9 | `audio` | 0.0567 |
| 10 | `projeto` | 0.0532 |
| 11 | `rede` | 0.0530 |
| 12 | `respiratoria` | 0.0497 |
| 13 | `dado` | 0.0389 |
| 14 | `coleta` | 0.0321 |
| 15 | `ruido` | 0.0300 |
| 16 | `marcelo` | 0.0277 |
| 17 | `sinal` | 0.0273 |
| 18 | `torna` | 0.0272 |
| 19 | `analise` | 0.0248 |
| 20 | `insuficiencia` | 0.0224 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `caixa` | `preta` | 0.898 | 87 |
| 2 | `insuficiencia` | `respiratoria` | 0.841 | 335 |
| 3 | `centro` | `calculo` | 0.769 | 88 |
| 4 | `neural` | `rede` | 0.601 | 130 |
| 5 | `acao` | `programa` | 0.569 | 38 |
| 6 | `sinal` | `acustico` | 0.550 | 64 |
| 7 | `possivel` | `tornou` | 0.549 | 37 |
| 8 | `acesso` | `disponivel` | 0.533 | 27 |
| 9 | `linguagem` | `processamento` | 0.520 | 27 |
| 10 | `publico` | `saude` | 0.518 | 25 |
| 11 | `visivel` | `torna` | 0.512 | 60 |
| 12 | `marcelo` | `entrevista` | 0.507 | 105 |
| 13 | `ciencia` | `acao` | 0.492 | 24 |
| 14 | `publico` | `repositorio` | 0.485 | 21 |
| 15 | `ciencia` | `construcao` | 0.483 | 22 |
| 16 | `saude` | `pesquisa` | 0.477 | 24 |
| 17 | `condicoes` | `producao` | 0.473 | 51 |
| 18 | `covideiro` | `pandemico` | 0.473 | 100 |
| 19 | `youtube` | `audioset` | 0.466 | 17 |
| 20 | `enfermaria` | `ruido` | 0.464 | 58 |
| 21 | `translacoes` | `cadeia` | 0.456 | 57 |
| 22 | `medicos` | `fonoaudiologos` | 0.456 | 28 |
| 23 | `conceito` | `referencia` | 0.436 | 16 |
| 24 | `treinado` | `modelo` | 0.436 | 46 |
| 25 | `forca` | `precisa` | 0.424 | 12 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (35 termos): inscricao, cadeia, torna, analise, dispositivo, secao
- **Tópico 2** (34 termos): spira, projeto, marcelo, artigos, partir, condicao
- **Tópico 3** (31 termos): rede, objeto, espectrograma, pratica, imagem, produz
- **Tópico 4** (27 termos): covideiro, modelo, dado, actante, pandemico, humano
- **Tópico 5** (19 termos): artigo, coleta, cientifico, condicoes, laboratorio, producao
- **Tópico 6** (19 termos): audio, ruido, sinal, paciente, arquivo, virus
- **Tópico 7** (9 termos): respiratoria, insuficiencia, covid, pacientes, deteccao, versao
- **Tópico 8** (6 termos): preta, caixa, audioset, parametros, youtube, corpus

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 3** [rede, objeto, espectrograma] e **Tópico 5** [artigo, coleta, cientifico] — densidade ponderada de ligação = 0.7165
- Lacuna entre **Tópico 3** [rede, objeto, espectrograma] e **Tópico 4** [covideiro, modelo, dado] — densidade ponderada de ligação = 0.8375
- Lacuna entre **Tópico 2** [spira, projeto, marcelo] e **Tópico 3** [rede, objeto, espectrograma] — densidade ponderada de ligação = 0.8861
- Lacuna entre **Tópico 1** [inscricao, cadeia, torna] e **Tópico 4** [covideiro, modelo, dado] — densidade ponderada de ligação = 0.9217
- Lacuna entre **Tópico 1** [inscricao, cadeia, torna] e **Tópico 3** [rede, objeto, espectrograma] — densidade ponderada de ligação = 1.0461
- Lacuna entre **Tópico 1** [inscricao, cadeia, torna] e **Tópico 5** [artigo, coleta, cientifico] — densidade ponderada de ligação = 1.1519

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
