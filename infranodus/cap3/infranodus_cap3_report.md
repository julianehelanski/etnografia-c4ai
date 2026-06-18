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
- Tokens significativos: **17,531**
- Grafo bruto: **5265** nós · **45260** arestas
- Grafo analítico (top 180 nós, peso ≥ 2, maior componente): **180** nós · **2382** arestas
- Tópicos detectados (Louvain): **7**

## 2. Conceitos mais influentes (degree ponderado · *baseline* frequentista)
| # | termo | grau ponderado |
|---|-------|----------------|
| 1 | `pesquisa` | 690 |
| 2 | `claudio` | 618 |
| 3 | `centro` | 509 |
| 4 | `publico` | 440 |
| 5 | `rede` | 431 |
| 6 | `corporacao` | 431 |
| 7 | `fabio` | 403 |
| 8 | `instituicao` | 326 |
| 9 | `seguir` | 317 |
| 10 | `inteligencia` | 311 |
| 11 | `arranjo` | 307 |
| 12 | `tecnologia` | 305 |
| 13 | `artificial` | 303 |
| 14 | `infraestrutura` | 279 |
| 15 | `hollerith` | 274 |
| 16 | `laboratorio` | 273 |
| 17 | `ator` | 271 |
| 18 | `modelo` | 255 |
| 19 | `brasil` | 249 |
| 20 | `universidade` | 247 |
| 21 | `trajetoria` | 243 |
| 22 | `cientifico` | 236 |
| 23 | `fapesp` | 230 |
| 24 | `encerramento` | 202 |
| 25 | `maquina` | 193 |
| 26 | `ponto` | 188 |
| 27 | `ecossistema` | 187 |
| 28 | `dado` | 185 |
| 29 | `tabulacao` | 184 |
| 30 | `parte` | 181 |

## 3. Conceitos mais influentes (PageRank · centralidade na rede)
PageRank pondera a importância de um nó pela importância dos seus
vizinhos. Termos pouco frequentes mas bem posicionados na rede sobem;
termos frequentes mas perifericamente conectados descem.

| # | termo | PageRank |
|---|-------|----------|
| 1 | `pesquisa` | 0.0269 |
| 2 | `claudio` | 0.0235 |
| 3 | `centro` | 0.0199 |
| 4 | `corporacao` | 0.0175 |
| 5 | `rede` | 0.0172 |
| 6 | `publico` | 0.0172 |
| 7 | `fabio` | 0.0152 |
| 8 | `instituicao` | 0.0131 |
| 9 | `tecnologia` | 0.0128 |
| 10 | `seguir` | 0.0126 |
| 11 | `arranjo` | 0.0120 |
| 12 | `inteligencia` | 0.0118 |
| 13 | `infraestrutura` | 0.0117 |
| 14 | `hollerith` | 0.0116 |
| 15 | `artificial` | 0.0116 |
| 16 | `laboratorio` | 0.0111 |
| 17 | `ator` | 0.0111 |
| 18 | `modelo` | 0.0109 |
| 19 | `trajetoria` | 0.0103 |
| 20 | `brasil` | 0.0103 |
| 21 | `universidade` | 0.0101 |
| 22 | `cientifico` | 0.0097 |
| 23 | `fapesp` | 0.0094 |
| 24 | `maquina` | 0.0084 |
| 25 | `encerramento` | 0.0083 |
| 26 | `dado` | 0.0082 |
| 27 | `ponto` | 0.0082 |
| 28 | `tabulacao` | 0.0081 |
| 29 | `ecossistema` | 0.0078 |
| 30 | `parte` | 0.0078 |

## 4. Termos mais subvalorizados pela frequência (degree → PageRank)
Diferença de posição (rank por degree) − (rank por PageRank). Valor
positivo = o termo é *mais central na rede* do que sugere sua frequência.

| # | termo | degree-rank | pagerank-rank | salto |
|---|-------|-------------|----------------|-------|
| 1 | `estados` | 85 | 70 | +15 |
| 2 | `escala` | 96 | 84 | +12 |
| 3 | `censo` | 130 | 119 | +11 |
| 4 | `conta` | 141 | 130 | +11 |
| 5 | `cadeia` | 97 | 87 | +10 |
| 6 | `estatistica` | 127 | 117 | +10 |
| 7 | `unidos` | 110 | 101 | +9 |
| 8 | `lado` | 131 | 122 | +9 |
| 9 | `dinheiro` | 121 | 113 | +8 |
| 10 | `humano` | 75 | 68 | +7 |
| 11 | `translacao` | 105 | 98 | +7 |
| 12 | `conjunto` | 161 | 154 | +7 |
| 13 | `sigo` | 126 | 120 | +6 |
| 14 | `sistemas` | 129 | 123 | +6 |
| 15 | `objeto` | 135 | 129 | +6 |

## 5. Pontes conceituais (betweenness — termos que costuram tópicos)
| # | termo | betweenness |
|---|-------|-------------|
| 1 | `pesquisa` | 0.2371 |
| 2 | `centro` | 0.1998 |
| 3 | `rede` | 0.1681 |
| 4 | `claudio` | 0.1541 |
| 5 | `corporacao` | 0.1487 |
| 6 | `publico` | 0.1395 |
| 7 | `fabio` | 0.0934 |
| 8 | `tecnologia` | 0.0800 |
| 9 | `seguir` | 0.0704 |
| 10 | `ator` | 0.0676 |
| 11 | `hollerith` | 0.0668 |
| 12 | `instituicao` | 0.0547 |
| 13 | `infraestrutura` | 0.0505 |
| 14 | `trajetoria` | 0.0472 |
| 15 | `universidade` | 0.0394 |
| 16 | `arranjo` | 0.0386 |
| 17 | `laboratorio` | 0.0384 |
| 18 | `cientifico` | 0.0353 |
| 19 | `inteligencia` | 0.0341 |
| 20 | `fapesp` | 0.0316 |

## 6. Pares de termos com associação mais surpreendente (NPMI)
NPMI mede *quão surpreendente* é a co-ocorrência de duas palavras dadas
suas frequências individuais. Diferente do peso bruto, ele faz aparecer
pares semanticamente fortes mesmo quando os termos co-ocorrem poucas
vezes.

| # | termo A | termo B | NPMI | co-ocorr. (peso) |
|---|---------|---------|------|------------------|
| 1 | `porta` | `voz` | 0.881 | 65 |
| 2 | `inteligencia` | `artificial` | 0.871 | 144 |
| 3 | `informacao` | `verbal` | 0.864 | 77 |
| 4 | `unidos` | `estados` | 0.857 | 51 |
| 5 | `relatorios` | `anuais` | 0.789 | 39 |
| 6 | `aberto` | `codigo` | 0.752 | 48 |
| 7 | `informacao` | `pinhanez` | 0.736 | 48 |
| 8 | `elaboracao` | `fonte` | 0.669 | 21 |
| 9 | `elaboracao` | `base` | 0.660 | 21 |
| 10 | `verbal` | `pinhanez` | 0.653 | 32 |
| 11 | `claudio` | `fabio` | 0.626 | 150 |
| 12 | `historica` | `investigacao` | 0.621 | 24 |
| 13 | `relatorios` | `elaboracao` | 0.594 | 20 |
| 14 | `passagem` | `ponto` | 0.592 | 33 |
| 15 | `base` | `fonte` | 0.583 | 14 |
| 16 | `relatorios` | `base` | 0.579 | 18 |
| 17 | `cientifico` | `producao` | 0.572 | 43 |
| 18 | `acesso` | `disponivel` | 0.567 | 21 |
| 19 | `anuais` | `base` | 0.549 | 12 |
| 20 | `research` | `brasil` | 0.527 | 27 |
| 21 | `novembro` | `dezembro` | 0.517 | 18 |
| 22 | `comercial` | `tecnica` | 0.514 | 16 |
| 23 | `dezembro` | `encerramento` | 0.513 | 34 |
| 24 | `translacao` | `cadeias` | 0.507 | 15 |
| 25 | `hollerith` | `tabulacao` | 0.501 | 39 |

## 7. Tópicos latentes (comunidades Louvain)
- **Tópico 1** (49 termos): claudio, rede, fabio, seguir, ator, ponto
- **Tópico 2** (42 termos): tecnologia, hollerith, modelo, trajetoria, maquina, dado
- **Tópico 3** (34 termos): publico, corporacao, instituicao, infraestrutura, universidade, fapesp
- **Tópico 4** (19 termos): arranjo, laboratorio, brasil, encerramento, pesquisador, dezembro
- **Tópico 5** (19 termos): pesquisa, centro, cientifico, relatorios, partir, grupo
- **Tópico 6** (11 termos): inteligencia, artificial, ecossistema, inovacao, brasileiro, valor
- **Tópico 7** (6 termos): informacao, verbal, pinhanez, estados, unidos, projeto

## 8. Lacunas estruturais (pares de tópicos fracamente conectados)
Lacunas estruturais sinalizam *espaços de ideia* pouco articulados no
texto — candidatos a aprofundamento argumentativo.

- Lacuna entre **Tópico 2** [tecnologia, hollerith, modelo] e **Tópico 4** [arranjo, laboratorio, brasil] — densidade ponderada de ligação = 0.3083
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 2** [tecnologia, hollerith, modelo] — densidade ponderada de ligação = 0.3163
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 3** [publico, corporacao, instituicao] — densidade ponderada de ligação = 0.3715
- Lacuna entre **Tópico 2** [tecnologia, hollerith, modelo] e **Tópico 5** [pesquisa, centro, cientifico] — densidade ponderada de ligação = 0.3835
- Lacuna entre **Tópico 1** [claudio, rede, fabio] e **Tópico 4** [arranjo, laboratorio, brasil] — densidade ponderada de ligação = 0.3867
- Lacuna entre **Tópico 2** [tecnologia, hollerith, modelo] e **Tópico 3** [publico, corporacao, instituicao] — densidade ponderada de ligação = 0.4489

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
