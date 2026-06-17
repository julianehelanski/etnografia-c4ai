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
- Tokens significativos: **17,511**
- Grafo bruto: **5255** nós · **45081** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **2388** arestas
- Tópicos detectados (Louvain): **8**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `pesquisa` | 690 |
| 2 | `claudio` | 634 |
| 3 | `centro` | 510 |
| 4 | `publico` | 438 |
| 5 | `corporacao` | 436 |
| 6 | `rede` | 421 |
| 7 | `fabio` | 393 |
| 8 | `instituicao` | 326 |
| 9 | `inteligencia` | 317 |
| 10 | `arranjo` | 317 |
| 11 | `seguir` | 315 |
| 12 | `artificial` | 309 |
| 13 | `tecnologia` | 305 |
| 14 | `infraestrutura` | 282 |
| 15 | `modelo` | 277 |
| 16 | `hollerith` | 274 |
| 17 | `laboratorio` | 273 |
| 18 | `ator` | 265 |
| 19 | `brasil` | 257 |
| 20 | `universidade` | 250 |
| 21 | `trajetoria` | 238 |
| 22 | `cientifico` | 237 |
| 23 | `fapesp` | 232 |
| 24 | `encerramento` | 199 |
| 25 | `maquina` | 193 |
| 26 | `informacao` | 191 |
| 27 | `ecossistema` | 187 |
| 28 | `dado` | 185 |
| 29 | `tabulacao` | 184 |
| 30 | `porta` | 183 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `pesquisa` | 0.0269 |
| 2 | `claudio` | 0.0238 |
| 3 | `centro` | 0.0199 |
| 4 | `corporacao` | 0.0176 |
| 5 | `publico` | 0.0170 |
| 6 | `rede` | 0.0168 |
| 7 | `fabio` | 0.0147 |
| 8 | `instituicao` | 0.0130 |
| 9 | `tecnologia` | 0.0128 |
| 10 | `seguir` | 0.0125 |
| 11 | `arranjo` | 0.0123 |
| 12 | `inteligencia` | 0.0119 |
| 13 | `modelo` | 0.0118 |
| 14 | `infraestrutura` | 0.0118 |
| 15 | `artificial` | 0.0117 |
| 16 | `hollerith` | 0.0116 |
| 17 | `laboratorio` | 0.0111 |
| 18 | `ator` | 0.0108 |
| 19 | `brasil` | 0.0105 |
| 20 | `universidade` | 0.0102 |
| 21 | `trajetoria` | 0.0101 |
| 22 | `cientifico` | 0.0097 |
| 23 | `fapesp` | 0.0095 |
| 24 | `maquina` | 0.0084 |
| 25 | `dado` | 0.0082 |
| 26 | `encerramento` | 0.0081 |
| 27 | `tabulacao` | 0.0080 |
| 28 | `parte` | 0.0078 |
| 29 | `ecossistema` | 0.0078 |
| 30 | `ponto` | 0.0076 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `estados` | 86 | 71 | +15 |
| 2 | `estatistica` | 129 | 116 | +13 |
| 3 | `censo` | 134 | 121 | +13 |
| 4 | `cadeia` | 102 | 90 | +12 |
| 5 | `unidos` | 111 | 99 | +12 |
| 6 | `pratica` | 119 | 108 | +11 |
| 7 | `lado` | 135 | 124 | +11 |
| 8 | `dinheiro` | 123 | 113 | +10 |
| 9 | `escala` | 95 | 86 | +9 |
| 10 | `deixa` | 106 | 97 | +9 |
| 11 | `translacao` | 109 | 101 | +8 |
| 12 | `secao` | 122 | 115 | +7 |
| 13 | `conta` | 141 | 134 | +7 |
| 14 | `humano` | 71 | 65 | +6 |
| 15 | `tecnociencia` | 94 | 88 | +6 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `pesquisa` | 0.2494 |
| 2 | `centro` | 0.2087 |
| 3 | `rede` | 0.1616 |
| 4 | `claudio` | 0.1514 |
| 5 | `corporacao` | 0.1507 |
| 6 | `publico` | 0.1237 |
| 7 | `tecnologia` | 0.0874 |
| 8 | `fabio` | 0.0871 |
| 9 | `ator` | 0.0657 |
| 10 | `hollerith` | 0.0651 |
| 11 | `seguir` | 0.0607 |
| 12 | `trajetoria` | 0.0555 |
| 13 | `infraestrutura` | 0.0507 |
| 14 | `instituicao` | 0.0491 |
| 15 | `cientifico` | 0.0431 |
| 16 | `universidade` | 0.0408 |
| 17 | `arranjo` | 0.0378 |
| 18 | `laboratorio` | 0.0362 |
| 19 | `inteligencia` | 0.0346 |
| 20 | `fapesp` | 0.0313 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `porta` | `voz` | 0.881 | 68 |
| 2 | `inteligencia` | `artificial` | 0.870 | 147 |
| 3 | `informacao` | `verbal` | 0.861 | 72 |
| 4 | `unidos` | `estados` | 0.857 | 51 |
| 5 | `relatorios` | `anuais` | 0.800 | 41 |
| 6 | `aberto` | `codigo` | 0.745 | 48 |
| 7 | `informacao` | `pinhanez` | 0.737 | 51 |
| 8 | `verbal` | `pinhanez` | 0.670 | 36 |
| 9 | `elaboracao` | `base` | 0.660 | 21 |
| 10 | `claudio` | `fabio` | 0.623 | 147 |
| 11 | `historica` | `investigacao` | 0.621 | 24 |
| 12 | `relatorios` | `elaboracao` | 0.601 | 20 |
| 13 | `passagem` | `ponto` | 0.599 | 33 |
| 14 | `relatorios` | `base` | 0.585 | 18 |
| 15 | `cientifico` | `producao` | 0.572 | 43 |
| 16 | `research` | `brasil` | 0.553 | 33 |
| 17 | `acesso` | `disponivel` | 0.549 | 21 |
| 18 | `anuais` | `base` | 0.540 | 12 |
| 19 | `novembro` | `dezembro` | 0.517 | 18 |
| 20 | `dezembro` | `encerramento` | 0.517 | 34 |
| 21 | `comercial` | `tecnica` | 0.514 | 16 |
| 22 | `translacao` | `cadeias` | 0.507 | 15 |
| 23 | `instituicao` | `multiplicacao` | 0.506 | 30 |
| 24 | `funcionamento` | `condicao` | 0.502 | 15 |
| 25 | `hollerith` | `tabulacao` | 0.501 | 39 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (43 termos): claudio, rede, fabio, seguir, ator, porta
- **Tópico 2** (41 termos): publico, corporacao, instituicao, tecnologia, infraestrutura, universidade
- **Tópico 3** (25 termos): hollerith, trajetoria, maquina, tabulacao, empresa, tecnica
- **Tópico 4** (21 termos): pesquisa, centro, cientifico, relatorios, pesquisador, partir
- **Tópico 5** (18 termos): arranjo, laboratorio, brasil, encerramento, parte, dezembro
- **Tópico 6** (15 termos): modelo, dado, codigo, publicacoes, analise, aberto
- **Tópico 7** (11 termos): inteligencia, artificial, ecossistema, inovacao, brasileiro, valor
- **Tópico 8** (6 termos): informacao, verbal, pinhanez, estados, unidos, projeto

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 3** [hollerith, trajetoria, maquina] e **Tópico 5** [arranjo, laboratorio, brasil] — densidade ponderada de ligação = 0.2778
- Lacuna entre **Tópico 3** [hollerith, trajetoria, maquina] e **Tópico 4** [pesquisa, centro, cientifico] — densidade ponderada de ligação = 0.3371
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 2** [publico, corporacao, instituicao] — densidade ponderada de ligação = 0.3426
- Lacuna entre **Tópico 2** [publico, corporacao, instituicao] e **Tópico 3** [hollerith, trajetoria, maquina] — densidade ponderada de ligação = 0.3795
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 3** [hollerith, trajetoria, maquina] — densidade ponderada de ligação = 0.4074
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 5** [arranjo, laboratorio, brasil] — densidade ponderada de ligação = 0.4264

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
