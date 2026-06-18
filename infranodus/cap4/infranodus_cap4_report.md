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
- Tokens significativos: **33,300**
- Grafo bruto: **6696** nós · **78491** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **4101** arestas
- Tópicos detectados (Louvain): **9**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `spira` | 2086 |
| 2 | `covideiro` | 1136 |
| 3 | `inscricao` | 1067 |
| 4 | `cadeia` | 1011 |
| 5 | `artigo` | 878 |
| 6 | `rede` | 808 |
| 7 | `respiratoria` | 803 |
| 8 | `objeto` | 787 |
| 9 | `insuficiencia` | 769 |
| 10 | `projeto` | 721 |
| 11 | `dado` | 701 |
| 12 | `modelo` | 700 |
| 13 | `marcelo` | 654 |
| 14 | `espectrograma` | 560 |
| 15 | `artigos` | 531 |
| 16 | `coleta` | 528 |
| 17 | `actante` | 478 |
| 18 | `audio` | 466 |
| 19 | `ruido` | 445 |
| 20 | `covid` | 423 |
| 21 | `cientifico` | 417 |
| 22 | `sinal` | 412 |
| 23 | `pacientes` | 411 |
| 24 | `condicoes` | 406 |
| 25 | `partir` | 406 |
| 26 | `torna` | 402 |
| 27 | `analise` | 399 |
| 28 | `pratica` | 390 |
| 29 | `dispositivo` | 388 |
| 30 | `laboratorio` | 365 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `spira` | 0.0399 |
| 2 | `covideiro` | 0.0221 |
| 3 | `inscricao` | 0.0212 |
| 4 | `cadeia` | 0.0201 |
| 5 | `artigo` | 0.0173 |
| 6 | `rede` | 0.0162 |
| 7 | `objeto` | 0.0156 |
| 8 | `respiratoria` | 0.0147 |
| 9 | `modelo` | 0.0143 |
| 10 | `projeto` | 0.0143 |
| 11 | `insuficiencia` | 0.0141 |
| 12 | `dado` | 0.0139 |
| 13 | `marcelo` | 0.0130 |
| 14 | `espectrograma` | 0.0115 |
| 15 | `coleta` | 0.0108 |
| 16 | `artigos` | 0.0105 |
| 17 | `actante` | 0.0098 |
| 18 | `audio` | 0.0096 |
| 19 | `ruido` | 0.0095 |
| 20 | `sinal` | 0.0087 |
| 21 | `covid` | 0.0086 |
| 22 | `torna` | 0.0085 |
| 23 | `pacientes` | 0.0085 |
| 24 | `partir` | 0.0085 |
| 25 | `cientifico` | 0.0083 |
| 26 | `condicoes` | 0.0083 |
| 27 | `pratica` | 0.0082 |
| 28 | `analise` | 0.0081 |
| 29 | `dispositivo` | 0.0081 |
| 30 | `laboratorio` | 0.0078 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `preta` | 93 | 74 | +19 |
| 2 | `caixa` | 103 | 86 | +17 |
| 3 | `escala` | 84 | 68 | +16 |
| 4 | `processo` | 107 | 97 | +10 |
| 5 | `parametros` | 118 | 108 | +10 |
| 6 | `ciencia` | 151 | 144 | +7 |
| 7 | `processamento` | 75 | 69 | +6 |
| 8 | `grade` | 141 | 135 | +6 |
| 9 | `youtube` | 145 | 139 | +6 |
| 10 | `frequencias` | 146 | 140 | +6 |
| 11 | `conceito` | 166 | 160 | +6 |
| 12 | `grupo` | 80 | 75 | +5 |
| 13 | `escolha` | 101 | 96 | +5 |
| 14 | `audioset` | 106 | 101 | +5 |
| 15 | `leitor` | 127 | 122 | +5 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `spira` | 0.6358 |
| 2 | `inscricao` | 0.2538 |
| 3 | `covideiro` | 0.1561 |
| 4 | `cadeia` | 0.1255 |
| 5 | `objeto` | 0.0890 |
| 6 | `artigo` | 0.0890 |
| 7 | `modelo` | 0.0663 |
| 8 | `espectrograma` | 0.0627 |
| 9 | `audio` | 0.0559 |
| 10 | `respiratoria` | 0.0518 |
| 11 | `rede` | 0.0449 |
| 12 | `projeto` | 0.0447 |
| 13 | `coleta` | 0.0382 |
| 14 | `dado` | 0.0379 |
| 15 | `ruido` | 0.0345 |
| 16 | `sinal` | 0.0281 |
| 17 | `torna` | 0.0269 |
| 18 | `insuficiencia` | 0.0225 |
| 19 | `programa` | 0.0212 |
| 20 | `covid` | 0.0178 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `caixa` | `preta` | 0.898 | 87 |
| 2 | `respiratoria` | `insuficiencia` | 0.841 | 329 |
| 3 | `calculo` | `centro` | 0.769 | 88 |
| 4 | `grupo` | `controle` | 0.659 | 40 |
| 5 | `neural` | `rede` | 0.609 | 130 |
| 6 | `acao` | `programa` | 0.572 | 38 |
| 7 | `tornou` | `possivel` | 0.551 | 37 |
| 8 | `sinal` | `acustico` | 0.549 | 64 |
| 9 | `acesso` | `disponivel` | 0.532 | 27 |
| 10 | `linguagem` | `processamento` | 0.519 | 27 |
| 11 | `torna` | `visivel` | 0.509 | 57 |
| 12 | `entrevista` | `marcelo` | 0.506 | 105 |
| 13 | `publico` | `saude` | 0.499 | 22 |
| 14 | `publico` | `repositorio` | 0.488 | 21 |
| 15 | `ciencia` | `construcao` | 0.486 | 22 |
| 16 | `saude` | `pesquisa` | 0.481 | 24 |
| 17 | `condicoes` | `producao` | 0.474 | 51 |
| 18 | `ciencia` | `acao` | 0.472 | 21 |
| 19 | `covideiro` | `pandemico` | 0.472 | 100 |
| 20 | `audioset` | `youtube` | 0.466 | 17 |
| 21 | `enfermaria` | `ruido` | 0.463 | 58 |
| 22 | `cadeia` | `translacoes` | 0.458 | 57 |
| 23 | `fonoaudiologos` | `medicos` | 0.455 | 28 |
| 24 | `conceito` | `referencia` | 0.444 | 16 |
| 25 | `modelo` | `treinado` | 0.437 | 46 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (35 termos): inscricao, cadeia, objeto, pratica, dispositivo, secao
- **Tópico 2** (31 termos): spira, projeto, marcelo, artigos, analise, dataset
- **Tópico 3** (30 termos): espectrograma, audio, sinal, paciente, arquivo, imagem
- **Tópico 4** (22 termos): dado, modelo, ruido, enfermaria, treinamento, treinado
- **Tópico 5** (20 termos): artigo, coleta, cientifico, condicoes, condicao, termos
- **Tópico 6** (19 termos): covideiro, actante, laboratorio, pandemico, humano, configuracao
- **Tópico 7** (9 termos): respiratoria, insuficiencia, covid, pacientes, deteccao, acustica
- **Tópico 8** (9 termos): rede, partir, ponto, neural, entrada, associacao

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [inscricao, cadeia, objeto] e **Tópico 4** [dado, modelo, ruido] — densidade ponderada de ligação = 0.5584
- Lacuna entre **Tópico 3** [espectrograma, audio, sinal] e **Tópico 5** [artigo, coleta, cientifico] — densidade ponderada de ligação = 0.7417
- Lacuna entre **Tópico 2** [spira, projeto, marcelo] e **Tópico 3** [espectrograma, audio, sinal] — densidade ponderada de ligação = 0.7602
- Lacuna entre **Tópico 4** [dado, modelo, ruido] e **Tópico 5** [artigo, coleta, cientifico] — densidade ponderada de ligação = 0.8000
- Lacuna entre **Tópico 1** [inscricao, cadeia, objeto] e **Tópico 3** [espectrograma, audio, sinal] — densidade ponderada de ligação = 0.8971
- Lacuna entre **Tópico 3** [espectrograma, audio, sinal] e **Tópico 4** [dado, modelo, ruido] — densidade ponderada de ligação = 0.9515

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
