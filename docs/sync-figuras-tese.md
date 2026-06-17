# Sincronização automática das figuras da tese → site

Quando você adiciona ou atualiza uma figura no repositório da tese
(`tecno-etnografia-centro-ia`), o site pode ressincronizar a imagem
correspondente automaticamente. Funciona assim:

1. **Gatilho** — o workflow `notify-c4ai.yml` na tese avisa o site a cada push
   que toque `figuras/**` ou `ex_cap*.tex` (veja `docs/dispatch-from-tex.yml.example`).
2. **Sync** — o site roda `scripts/sync_tese_figuras.py`, que lê o mapa
   `infranodus/figuras_tese_map.tsv` e copia, para cada destino do site, a
   versão **mais recente** da origem na tese.
3. **Cache-busting** — `scripts/cache_busting_figuras.py` atualiza o `?v=` das
   imagens, para o navegador baixar as novas.
4. O GitHub Pages republica o site.

## O mapa (`infranodus/figuras_tese_map.tsv`)

Cada linha liga `destino-no-site` ⟶ `origem-na-tese` (um *glob*; `*` cobre os
timestamps de data que mudam a cada re-exportação). Exemplo:

```
figuras/cadeia-translacao-spira-2026-03-11-130346.png	figuras/cap.4/diagramas-mermaid/cadeia-translacao-spira-capitulo4-*.png
```

As **24 entradas iniciais** foram detectadas automaticamente por hash de
conteúdo (bytes idênticos entre site e tese) — são seguras.

## Como adicionar uma figura nova

1. Coloque/atualize o arquivo na tese (em `figuras/...`).
2. Adicione uma linha no mapa: `caminho/no/site.png` ⟨TAB⟩ `figuras/.../arquivo*.png`.
3. Referencie a figura no `index.html` (`<img src="figuras/no/site.png">`).
4. Pronto — a partir daí ela se atualiza sozinha.

## Figuras exibidas no site que ainda NÃO estão no mapa

Estas usam nomes curados no site, diferentes (e com conteúdo diferente) dos da
tese, então não dá para casá-las automaticamente sem risco de erro. O palpite
ao lado é por similaridade de nome — **confirme antes de adicionar ao mapa**
(em especial o capítulo, que o palpite às vezes erra):

| destino no site | possível origem na tese (CONFERIR) |
|---|---|
| `figuras/cap1/cap1-caderno-campo.jpg` | `figuras/cap.1/caderno_quadro.jpg` |
| `figuras/cap1/cap1-grade-tres-planos.png` | `figuras/cap.1/grade_tres_planos.png` |
| `figuras/cap1/cap1-urdidura.png` | `figuras/cap.1/urdidura-capitulo1-*.pdf` |
| `figuras/cap2/cap2-bib-capes-grande-area.png` | `figuras/cap.2/bibliometria/capes_11_grande_area_share.png` |
| `figuras/cap2/cap2-bib-capes-heatmap-kw.png` | `figuras/cap.2/bibliometria/capes_13_heatmap_area_keyword.png` |
| `figuras/cap2/cap2-bib-capes-heatmap-sub.png` | `figuras/cap.2/bibliometria/capes_22_heatmap_subcampo_grande_area.png` |
| `figuras/cap2/cap2-bib-capes-humanas-temporal.png` | `figuras/cap.2/bibliometria/capes_h02_temporal_humanas.png` |
| `figuras/cap2/cap2-bib-capes-humanas.png` | `figuras/cap.2/bibliometria/capes_h01_areas_humanas.png` |
| `figuras/cap2/cap2-bib-capes-subcampos.png` | `figuras/cap.2/bibliometria/capes_21_subcampos_distribuicao.png` |
| `figuras/cap2/cap2-bib-comparativo.png` | `figuras/cap.2/bibliometria/comparativo_scielo_capes_2026.png` |
| `figuras/cap2/cap2-bib-scielo-area.png` | `figuras/cap.2/bibliometria/scielo_11_subject_area_share.png` |
| `figuras/cap2/cap2-bib-scielo-subcampos.png` | `figuras/cap.2/bibliometria/scielo_21_subcampos_distribuicao.png` |
| `figuras/cap2/cap2-lex-aime.png` | `figuras/cap.2/lexicometria/etapa3_aime_freq_e_densidade.png` |
| `figuras/cap2/cap2-lex-clarifications.png` | `figuras/cap.2/lexicometria/etapa2_clarifications_freq_e_densidade.png` |
| `figuras/cap2/cap2-lex-comparacao.png` | `figuras/cap.2/lexicometria/etapa1_passo4_comparacao_frequencias_tres_obras.png` |
| `figuras/cap2/cap2-lex-lab-life.png` | `figuras/cap.2/lexicometria/etapa1_lab_life_freq_e_densidade.png` |
| `figuras/cap2/cap2-lex-pandora.png` | `figuras/cap.2/lexicometria/etapa1_pandora_freq_e_densidade.png` |
| `figuras/cap2/cap2-lex-recalling.png` | `figuras/cap.2/lexicometria/etapa2bis_recalling_integral_freq_e_densidade.png` |
| `figuras/cap2/cap2-lex-science-in-action.png` | `figuras/cap.2/lexicometria/etapa1_sia_freq_e_densidade.png` |
| `figuras/cap2/cap2-mediacao-diferencial.png` | `figuras/cap.2/diagramas/mediacaodiferencial_ia_mediacao.png` |
| `figuras/cap2/cap2-urdidura.png` | `figuras/cap.2/urdidura-capitulo2-*.png` (conferir; pode não existir) |
| `figuras/cap3/cap3-arranjo-publico-privado.png` | (conferir na tese) |
| `figuras/cap3/cap3-biblio-1-ranking.png` | `figuras/cap.3/biblimetria-c4ai/1_ranking_grupos.png` |
| `figuras/cap3/cap3-biblio-3-evolucao.png` | `figuras/cap.3/biblimetria-c4ai/3_evolucao_temporal_geral.png` |
| `figuras/cap3/cap3-biblio-4-heatmap.png` | `figuras/cap.3/biblimetria-c4ai/4_heatmap_grupo_ano.png` |
| `figuras/cap3/cap3-biblio-6-produtividade.png` | `figuras/cap.3/biblimetria-c4ai/6_produtividade_grupos.png` |
| `figuras/cap3/cap3-biblio-8-composicao.png` | `figuras/cap.3/biblimetria-c4ai/8_*.png` (conferir) |
| `figuras/cap3/cap3-biblio-9-concentracao.png` | `figuras/cap.3/biblimetria-c4ai/9_analise_concentracao.png` |
| `figuras/cap3/cap3-cadeia-translacao-ibm.png` | `figuras/cap.3/diagramas/cadeia-translacao-ibm-capitulo3-*.png` |
| `figuras/cap3/cap3-dobra-etnografica.png` | `figuras/cap.3/dobra-etnografica-capitulo3-*.png` |
| `figuras/cap3/cap3-hollerith-rede-sociotecnica.png` | `figuras/cap.3/hollerith-rede-sociotecnica-capitulo3-*.png` |
| `figuras/cap3/cap3-panorama-c4ai.png` | `figuras/cap.3/panorama-c4ai-capitulo3-*.png` |
| `figuras/cap3/cap3-quadro-analitico.png` | `figuras/cap.3/quadro-analitico-capitulo3-*.png` |
| `figuras/cap3/cap3-roadmap-ciclo.png` | `figuras/cap.3/roadmap-ciclo-capitulo3-*.png` |
| `figuras/cap3/cap3-seguindo-atores.png` | `figuras/cap.3/seguindo-atores-metodologia-capitulo3-*.png` |
| `figuras/cap4-argumento.png` | `figuras/cap.4/argumento-capitulo4-*.png` |
| `figuras/cronologia-spira-*.png` | `figuras/cap.4/...cronologia...` (conferir) |
| `figuras/roadmap-genealogia-ibm.png` | `figuras/cap.4/roadmap-genealogia-ibm-capitulo3-*.png` |
| `figuras/spira-roadmap-english-*.png` | `figuras/cap.4/roadmap-spira-*.png` (conferir) |
| `figuras/translacao-spira-antes-depois-*.png` | (conferir na tese) |

> Quer que eu confirme e preencha essas entradas? Posso comparar cada par
> visualmente / por similaridade e completar o mapa — é só pedir.
