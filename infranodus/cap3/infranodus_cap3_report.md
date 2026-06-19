# Análise de rede textual — Capítulo 3

> Análise de rede textual (*text network analysis*, Paranyushkin 2019)
> aplicada ao arquivo `ex_cap3.tex`. O texto foi limpo de comandos LaTeX,
> citações e notas de rodapé foram reincorporadas; janela deslizante de
> 4 *tokens* com pesos decrescentes pela distância (3-2-1). Comunidades
> detectadas por Louvain ponderado. Esta versão acrescenta duas métricas
> *informativas* que não dependem da frequência bruta: **PageRank** dos
> nós e **NPMI** das arestas. As métricas baseadas em frequência são
> mantidas em paralelo, para comparação.

## 1. Resumo quantitativo
- Tokens significativos: **16,786**
- Grafo bruto: **5158** nós · **43479** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **2402** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `claudio` | 752 |
| 2 | `pesquisa` | 682 |
| 3 | `centro` | 495 |
| 4 | `rede` | 449 |
| 5 | `fabio` | 436 |
| 6 | `publico` | 414 |
| 7 | `corporacao` | 397 |
| 8 | `seguir` | 355 |
| 9 | `inteligencia` | 312 |
| 10 | `brasil` | 301 |
| 11 | `artificial` | 301 |
| 12 | `tecnologia` | 294 |
| 13 | `hollerith` | 293 |
| 14 | `arranjo` | 290 |
| 15 | `laboratorio` | 279 |
| 16 | `ator` | 274 |
| 17 | `cientifico` | 261 |
| 18 | `infraestrutura` | 243 |
| 19 | `modelo` | 240 |
| 20 | `instituicao` | 238 |
| 21 | `trajetoria` | 231 |
| 22 | `universidade` | 230 |
| 23 | `ecossistema` | 223 |
| 24 | `maquina` | 215 |
| 25 | `encerramento` | 208 |
| 26 | `fapesp` | 206 |
| 27 | `informacao` | 200 |
| 28 | `empresa` | 199 |
| 29 | `verbal` | 179 |
| 30 | `dado` | 178 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `claudio` | 0.0276 |
| 2 | `pesquisa` | 0.0264 |
| 3 | `centro` | 0.0193 |
| 4 | `rede` | 0.0179 |
| 5 | `publico` | 0.0164 |
| 6 | `corporacao` | 0.0161 |
| 7 | `fabio` | 0.0159 |
| 8 | `seguir` | 0.0139 |
| 9 | `tecnologia` | 0.0124 |
| 10 | `hollerith` | 0.0122 |
| 11 | `brasil` | 0.0121 |
| 12 | `inteligencia` | 0.0117 |
| 13 | `arranjo` | 0.0115 |
| 14 | `artificial` | 0.0114 |
| 15 | `laboratorio` | 0.0113 |
| 16 | `ator` | 0.0112 |
| 17 | `cientifico` | 0.0108 |
| 18 | `infraestrutura` | 0.0103 |
| 19 | `modelo` | 0.0103 |
| 20 | `trajetoria` | 0.0097 |
| 21 | `instituicao` | 0.0096 |
| 22 | `universidade` | 0.0094 |
| 23 | `ecossistema` | 0.0091 |
| 24 | `maquina` | 0.0090 |
| 25 | `empresa` | 0.0084 |
| 26 | `fapesp` | 0.0084 |
| 27 | `encerramento` | 0.0084 |
| 28 | `dado` | 0.0080 |
| 29 | `tabulacao` | 0.0075 |
| 30 | `campo` | 0.0075 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `estatistica` | 104 | 85 | +19 |
| 2 | `conta` | 127 | 108 | +19 |
| 3 | `source` | 105 | 92 | +13 |
| 4 | `open` | 110 | 98 | +12 |
| 5 | `humano` | 76 | 65 | +11 |
| 6 | `deixa` | 86 | 75 | +11 |
| 7 | `expertise` | 164 | 153 | +11 |
| 8 | `computacional` | 140 | 130 | +10 |
| 9 | `condicao` | 136 | 127 | +9 |
| 10 | `estados` | 65 | 57 | +8 |
| 11 | `censo` | 108 | 100 | +8 |
| 12 | `objeto` | 141 | 133 | +8 |
| 13 | `unidos` | 87 | 80 | +7 |
| 14 | `cadeia` | 102 | 95 | +7 |
| 15 | `lado` | 132 | 125 | +7 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `pesquisa` | 0.2553 |
| 2 | `centro` | 0.2226 |
| 3 | `rede` | 0.1652 |
| 4 | `claudio` | 0.1522 |
| 5 | `publico` | 0.1133 |
| 6 | `corporacao` | 0.1009 |
| 7 | `seguir` | 0.0871 |
| 8 | `tecnologia` | 0.0837 |
| 9 | `fabio` | 0.0812 |
| 10 | `ator` | 0.0728 |
| 11 | `hollerith` | 0.0687 |
| 12 | `cientifico` | 0.0660 |
| 13 | `brasil` | 0.0620 |
| 14 | `laboratorio` | 0.0343 |
| 15 | `inteligencia` | 0.0324 |
| 16 | `ecossistema` | 0.0314 |
| 17 | `universidade` | 0.0304 |
| 18 | `ciencia` | 0.0294 |
| 19 | `fapesp` | 0.0286 |
| 20 | `infraestrutura` | 0.0271 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `open` | `source` | 0.904 | 42 |
| 2 | `informacao` | `verbal` | 0.870 | 77 |
| 3 | `inteligencia` | `artificial` | 0.869 | 144 |
| 4 | `unidos` | `estados` | 0.858 | 57 |
| 5 | `porta` | `voz` | 0.855 | 47 |
| 6 | `relatorios` | `anuais` | 0.780 | 38 |
| 7 | `aberto` | `codigo` | 0.745 | 45 |
| 8 | `elaboracao` | `fonte` | 0.696 | 21 |
| 9 | `elaboracao` | `base` | 0.643 | 21 |
| 10 | `acesso` | `disponivel` | 0.635 | 30 |
| 11 | `historica` | `investigacao` | 0.612 | 24 |
| 12 | `passagem` | `ponto` | 0.585 | 30 |
| 13 | `claudio` | `fabio` | 0.575 | 152 |
| 14 | `cientifico` | `producao` | 0.575 | 43 |
| 15 | `base` | `fonte` | 0.559 | 14 |
| 16 | `relatorios` | `elaboracao` | 0.558 | 16 |
| 17 | `translacao` | `cadeias` | 0.546 | 15 |
| 18 | `relatorios` | `base` | 0.543 | 18 |
| 19 | `research` | `brasil` | 0.542 | 38 |
| 20 | `novembro` | `dezembro` | 0.542 | 21 |
| 21 | `anuais` | `base` | 0.516 | 12 |
| 22 | `estatistica` | `foucault` | 0.513 | 14 |
| 23 | `comercial` | `tecnica` | 0.509 | 13 |
| 24 | `gente` | `dinheiro` | 0.499 | 15 |
| 25 | `inteligencia` | `brasileiro` | 0.499 | 24 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (36 termos): tecnologia, hollerith, infraestrutura, trajetoria, maquina, empresa
- **Tópico 2** (36 termos): rede, seguir, ator, associacao, campo, etnografia
- **Tópico 3** (29 termos): pesquisa, centro, cientifico, fapesp, relatorios, grupo
- **Tópico 4** (28 termos): publico, corporacao, brasil, arranjo, laboratorio, instituicao
- **Tópico 5** (18 termos): modelo, dado, codigo, aberto, negocio, torna
- **Tópico 6** (12 termos): inteligencia, artificial, ecossistema, inovacao, brasileiro, obia
- **Tópico 7** (11 termos): claudio, fabio, informacao, verbal, pergunta, bluetalks
- **Tópico 8** (10 termos): ponto, historica, estados, deixa, unidos, passagem

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 2** [rede, seguir, ator] e **Tópico 5** [modelo, dado, codigo] — densidade ponderada de ligação = 0.2485
- Lacuna entre **Tópico 2** [rede, seguir, ator] e **Tópico 3** [pesquisa, centro, cientifico] — densidade ponderada de ligação = 0.3333
- Lacuna entre **Tópico 3** [pesquisa, centro, cientifico] e **Tópico 5** [modelo, dado, codigo] — densidade ponderada de ligação = 0.3467
- Lacuna entre **Tópico 1** [tecnologia, hollerith, infraestrutura] e **Tópico 2** [rede, seguir, ator] — densidade ponderada de ligação = 0.3549
- Lacuna entre **Tópico 1** [tecnologia, hollerith, infraestrutura] e **Tópico 3** [pesquisa, centro, cientifico] — densidade ponderada de ligação = 0.3659
- Lacuna entre **Tópico 1** [tecnologia, hollerith, infraestrutura] e **Tópico 5** [modelo, dado, codigo] — densidade ponderada de ligação = 0.3873

## 9. Leitura interpretativa
_Leitura interpretativa ainda não escrita para este capítulo. Crie `interpretation_cap3.md` ao lado dos outputs para que o conteúdo seja embutido aqui automaticamente._

## 10. Arquivos gerados
**Visões frequentistas**
- `infranodus_cap3_network.png` — rede completa, tamanho por degree.
- `infranodus_cap3_focus.png` — núcleo (top-100, peso ≥ 3).

**Visões informativas**
- `infranodus_cap3_pmi.png` — rede completa, tamanho por **PageRank**,
  arestas filtradas por **NPMI ≥ 0,20**.
- `infranodus_cap3_focus_pmi.png` — núcleo, NPMI ≥ 0,25.

**Dados**
- `infranodus_cap3_metrics.json` — métricas brutas (degree, betweenness,
  PageRank, NPMI, comunidades, lacunas).
- `infranodus_cap3.gexf` / `infranodus_cap3_focus.gexf` — grafos para Gephi
  já com `community`, `frequency`, `degree_weighted`, `betweenness`,
  `pagerank` (nós) e `weight`, `npmi` (arestas).
- `infranodus_cap3_nodes.csv` / `infranodus_cap3_edges.csv` (e `_focus_*`)
  — fallback em planilha; CSVs trazem todas as colunas acima.

## 11. Como abrir no Gephi
1. Instale Gephi (≥ 0.10): https://gephi.org/users/download/
2. `File → Open…` → selecione `infranodus_cap3.gexf` (ou `_focus.gexf`).
3. No painel **Appearance**: já vem com cor por `community` e tamanho por
   `degree_weighted` (embutidos via atributos `viz`). Ajuste se quiser.
4. Em **Layout**: aplique *ForceAtlas 2* (ative *Prevent Overlap* e
   *Dissuade Hubs*) por ~30 s; ou *Fruchterman-Reingold* para algo mais rápido.
5. Em **Statistics**: rode *Modularity* e *Average Path Length* se quiser
   recalcular comunidades dentro do Gephi (resultados serão semelhantes).
6. Em **Preview**: ative *Node Labels*, escolha fonte e exporte para PDF/SVG.
