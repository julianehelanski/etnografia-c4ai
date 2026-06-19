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
- Tokens significativos: **16,729**
- Grafo bruto: **5142** nós · **43387** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **2435** arestas
- Tópicos detectados (Louvain): **7**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `claudio` | 775 |
| 2 | `pesquisa` | 662 |
| 3 | `centro` | 496 |
| 4 | `fabio` | 470 |
| 5 | `rede` | 463 |
| 6 | `publico` | 425 |
| 7 | `corporacao` | 418 |
| 8 | `seguir` | 376 |
| 9 | `inteligencia` | 314 |
| 10 | `arranjo` | 312 |
| 11 | `tecnologia` | 306 |
| 12 | `artificial` | 304 |
| 13 | `brasil` | 299 |
| 14 | `hollerith` | 293 |
| 15 | `laboratorio` | 277 |
| 16 | `ator` | 269 |
| 17 | `cientifico` | 249 |
| 18 | `infraestrutura` | 246 |
| 19 | `instituicao` | 243 |
| 20 | `universidade` | 240 |
| 21 | `modelo` | 233 |
| 22 | `trajetoria` | 226 |
| 23 | `fapesp` | 219 |
| 24 | `encerramento` | 219 |
| 25 | `maquina` | 216 |
| 26 | `ecossistema` | 213 |
| 27 | `empresa` | 203 |
| 28 | `informacao` | 200 |
| 29 | `campo` | 191 |
| 30 | `associacao` | 181 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `claudio` | 0.0282 |
| 2 | `pesquisa` | 0.0256 |
| 3 | `centro` | 0.0193 |
| 4 | `rede` | 0.0184 |
| 5 | `fabio` | 0.0170 |
| 6 | `corporacao` | 0.0169 |
| 7 | `publico` | 0.0168 |
| 8 | `seguir` | 0.0147 |
| 9 | `tecnologia` | 0.0129 |
| 10 | `arranjo` | 0.0123 |
| 11 | `hollerith` | 0.0121 |
| 12 | `brasil` | 0.0120 |
| 13 | `inteligencia` | 0.0117 |
| 14 | `artificial` | 0.0114 |
| 15 | `laboratorio` | 0.0111 |
| 16 | `ator` | 0.0109 |
| 17 | `infraestrutura` | 0.0104 |
| 18 | `cientifico` | 0.0103 |
| 19 | `modelo` | 0.0099 |
| 20 | `universidade` | 0.0099 |
| 21 | `instituicao` | 0.0098 |
| 22 | `trajetoria` | 0.0094 |
| 23 | `maquina` | 0.0090 |
| 24 | `fapesp` | 0.0090 |
| 25 | `encerramento` | 0.0088 |
| 26 | `empresa` | 0.0086 |
| 27 | `ecossistema` | 0.0086 |
| 28 | `campo` | 0.0081 |
| 29 | `dado` | 0.0080 |
| 30 | `associacao` | 0.0077 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `conta` | 126 | 103 | +23 |
| 2 | `estatistica` | 98 | 85 | +13 |
| 3 | `lado` | 131 | 121 | +10 |
| 4 | `condicao` | 142 | 132 | +10 |
| 5 | `estados` | 66 | 57 | +9 |
| 6 | `censo` | 104 | 95 | +9 |
| 7 | `descreve` | 59 | 52 | +7 |
| 8 | `humano` | 87 | 80 | +7 |
| 9 | `conhecimento` | 97 | 90 | +7 |
| 10 | `latour` | 105 | 98 | +7 |
| 11 | `cadeia` | 108 | 101 | +7 |
| 12 | `computacional` | 134 | 127 | +7 |
| 13 | `expertise` | 172 | 165 | +7 |
| 14 | `deixa` | 76 | 70 | +6 |
| 15 | `cartoes` | 102 | 96 | +6 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `pesquisa` | 0.2212 |
| 2 | `centro` | 0.2170 |
| 3 | `rede` | 0.1758 |
| 4 | `claudio` | 0.1665 |
| 5 | `publico` | 0.1209 |
| 6 | `corporacao` | 0.1167 |
| 7 | `tecnologia` | 0.0926 |
| 8 | `fabio` | 0.0909 |
| 9 | `seguir` | 0.0896 |
| 10 | `ator` | 0.0692 |
| 11 | `hollerith` | 0.0688 |
| 12 | `cientifico` | 0.0623 |
| 13 | `brasil` | 0.0484 |
| 14 | `universidade` | 0.0402 |
| 15 | `trajetoria` | 0.0358 |
| 16 | `laboratorio` | 0.0336 |
| 17 | `inteligencia` | 0.0317 |
| 18 | `ecossistema` | 0.0313 |
| 19 | `infraestrutura` | 0.0277 |
| 20 | `arranjo` | 0.0277 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `informacao` | `verbal` | 0.870 | 77 |
| 2 | `inteligencia` | `artificial` | 0.869 | 144 |
| 3 | `porta` | `voz` | 0.864 | 50 |
| 4 | `unidos` | `estados` | 0.858 | 57 |
| 5 | `relatorios` | `anuais` | 0.780 | 38 |
| 6 | `aberto` | `codigo` | 0.745 | 45 |
| 7 | `elaboracao` | `base` | 0.650 | 21 |
| 8 | `acesso` | `disponivel` | 0.635 | 30 |
| 9 | `historica` | `investigacao` | 0.619 | 24 |
| 10 | `passagem` | `ponto` | 0.597 | 30 |
| 11 | `claudio` | `fabio` | 0.582 | 161 |
| 12 | `cientifico` | `producao` | 0.581 | 43 |
| 13 | `relatorios` | `elaboracao` | 0.558 | 16 |
| 14 | `relatorios` | `base` | 0.551 | 18 |
| 15 | `research` | `brasil` | 0.545 | 38 |
| 16 | `novembro` | `dezembro` | 0.542 | 21 |
| 17 | `translacao` | `cadeias` | 0.539 | 15 |
| 18 | `anuais` | `base` | 0.523 | 12 |
| 19 | `estatistica` | `foucault` | 0.509 | 14 |
| 20 | `comercial` | `tecnica` | 0.508 | 13 |
| 21 | `gente` | `dinheiro` | 0.499 | 15 |
| 22 | `hollerith` | `maquina` | 0.493 | 54 |
| 23 | `inteligencia` | `brasileiro` | 0.491 | 24 |
| 24 | `research` | `fechamento` | 0.490 | 12 |
| 25 | `inovacao` | `ecossistema` | 0.483 | 38 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (55 termos): claudio, fabio, rede, seguir, ator, informacao
- **Tópico 2** (49 termos): corporacao, tecnologia, hollerith, infraestrutura, modelo, trajetoria
- **Tópico 3** (30 termos): publico, arranjo, brasil, laboratorio, instituicao, universidade
- **Tópico 4** (21 termos): pesquisa, centro, cientifico, relatorios, parte, grupo
- **Tópico 5** (13 termos): inteligencia, artificial, ecossistema, inovacao, brasileiro, obia
- **Tópico 6** (9 termos): ponto, financiamento, deixa, passagem, gente, dinheiro
- **Tópico 7** (3 termos): estados, unidos, decisao

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 1** [claudio, fabio, rede] e **Tópico 5** [inteligencia, artificial, ecossistema] — densidade ponderada de ligação = 0.2965
- Lacuna entre **Tópico 1** [claudio, fabio, rede] e **Tópico 2** [corporacao, tecnologia, hollerith] — densidade ponderada de ligação = 0.3306
- Lacuna entre **Tópico 1** [claudio, fabio, rede] e **Tópico 3** [publico, arranjo, brasil] — densidade ponderada de ligação = 0.3715
- Lacuna entre **Tópico 2** [corporacao, tecnologia, hollerith] e **Tópico 5** [inteligencia, artificial, ecossistema] — densidade ponderada de ligação = 0.4301
- Lacuna entre **Tópico 1** [claudio, fabio, rede] e **Tópico 4** [pesquisa, centro, cientifico] — densidade ponderada de ligação = 0.4545
- Lacuna entre **Tópico 2** [corporacao, tecnologia, hollerith] e **Tópico 3** [publico, arranjo, brasil] — densidade ponderada de ligação = 0.4585

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
