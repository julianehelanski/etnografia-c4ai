# Renomeação das figuras da tese conforme o título curto da legenda

Gerado por `scripts/renomear_figuras_tese.py` a partir do repositório da tese (`tecno-etnografia-centro-ia`).

Cada arquivo de figura passa a se chamar `cap<N>-<slug-do-título-curto>`, onde o título curto é o texto entre colchetes de `\caption[...]`. Os caminhos `\includegraphics{...}` são atualizados junto, e nenhuma referência existente fica quebrada.

## Como aplicar (no repositório da tese)

```bash
# simulação (não altera nada):
python3 scripts/renomear_figuras_tese.py /caminho/para/a/tese

# aplica de fato (git mv + reescreve os .tex):
python3 scripts/renomear_figuras_tese.py /caminho/para/a/tese --apply
```

## 65 renomeações (arquivos existentes)

| antigo | novo |
|---|---|
| `figuras/cap.1/Screenshot_20260430_160250_Chrome.jpg` | `figuras/cap.1/cap1-cafe-apos-a-tech-hour-do-c4ai-realizada-em-23-de-marco-de-2022-no-inovausp-primeiro-ano-do-trabalho-de-campo-desta-pesquisa.jpg` |
| `figuras/cap.1/urdidura-capitulo1-2026-05-12-231748.pdf` | `figuras/cap.1/cap1-urdidura-do-capitulo.pdf` |
| `figuras/cap.1/grade_tres_planos.png` | `figuras/cap.1/cap1-grade-dos-tres-planos.png` |
| `figuras/cap.1/1000015590.pdf` | `figuras/cap.1/cap1-fazer-com-o-claude-durante-a-escrita-do-capitulo.pdf` |
| `figuras/cap.1/1000015599.pdf` | `figuras/cap.1/cap1-fazer-com-o-claude-durante-a-escrita-do-capitulo-2.pdf` |
| `figuras/cap.1/1000015602.pdf` | `figuras/cap.1/cap1-fazer-com-o-claude-durante-a-escrita-do-capitulo-3.pdf` |
| `figuras/cap.1/infranodus_cap1_network.png` | `figuras/cap.1/cap1-rede-textual-completa-do-capitulo.png` |
| `figuras/cap.1/infranodus_cap1_focus.png` | `figuras/cap.1/cap1-nucleo-da-rede-textual-do-capitulo.png` |
| `figuras/cap.1/infranodus_cap1_pmi.png` | `figuras/cap.1/cap1-nucleo-da-rede-textual-do-capitulo-ponderado-por-pagerank-e-npmi.png` |
| `figuras/cap.1/trajectory_gantt.png` | `figuras/cap.1/cap1-gantt-lexical-do-capitulo-entrada-persistencia-e-saida-dos-conceitos.png` |
| `figuras/cap.1/trajectory_alluvial.png` | `figuras/cap.1/cap1-fluxo-aluvial-de-topicos-ao-longo-do-capitulo.png` |
| `figuras/cap.1/trajectory_semantic.png` | `figuras/cap.1/cap1-trajetoria-semantica-do-capitulo.png` |
| `figuras/cap.1/caderno_quadro.jpg` | `figuras/cap.1/cap1-anotacao-de-caderno-de-campo-de-28-de-julho-de-2025.jpg` |
| `figuras/cap.2/latour.jpg` | `figuras/cap.2/cap2-o-autor-cercado-de-aliados-e-o-leitor-sozinho.jpg` |
| `figuras/cap.2/haraway.jpg` | `figuras/cap.2/cap2-cat-s-cradle-string-theory-de-baila-goldenthal.jpg` |
| `figuras/cap.2/diagramas/mapa-capitulo2.png` | `figuras/cap.2/diagramas/cap2-texto-mapa-do-capitulo.png` |
| `figuras/cap.2/lexicometria/etapa1_lab_life_freq_e_densidade.png` | `figuras/cap.2/lexicometria/cap2-frequencia-e-distribuicao-dos-campos-figurativos-em-laboratory-life.png` |
| `figuras/cap.2/lexicometria/etapa1_sia_freq_e_densidade.png` | `figuras/cap.2/lexicometria/cap2-frequencia-e-distribuicao-dos-campos-figurativos-em-science-in-action.png` |
| `figuras/cap.2/lexicometria/etapa1_pandora_freq_e_densidade.png` | `figuras/cap.2/lexicometria/cap2-frequencia-e-distribuicao-dos-campos-figurativos-em-pandora-s-hope.png` |
| `figuras/cap.2/lexicometria/etapa1_passo4_comparacao_frequencias_tres_obras.png` | `figuras/cap.2/lexicometria/cap2-densidade-comparada-dos-campos-figurativos-nas-tres-obras-de-latour.png` |
| `figuras/cap.2/lexicometria/etapa2_clarifications_freq_e_densidade.png` | `figuras/cap.2/lexicometria/cap2-frequencia-e-distribuicao-dos-campos-figurativos-em-clarifications.png` |
| `figuras/cap.2/lexicometria/etapa2bis_recalling_integral_freq_e_densidade.png` | `figuras/cap.2/lexicometria/cap2-frequencia-e-distribuicao-dos-campos-figurativos-em-on-recalling-ant.png` |
| `figuras/cap.2/lexicometria/etapa3_aime_freq_e_densidade.png` | `figuras/cap.2/lexicometria/cap2-frequencia-e-distribuicao-dos-campos-figurativos-em-aime.png` |
| `figuras/cap.2/diagramas/mediacaosignificado_1_traducao.png` | `figuras/cap.2/diagramas/cap2-primeiro-significado-da-mediacao-tecnica-traducao-de-objetivos.png` |
| `figuras/cap.2/diagramas/mediacaosignificado_2_composicao.png` | `figuras/cap.2/diagramas/cap2-segundo-significado-da-mediacao-tecnica-composicao.png` |
| `figuras/cap.2/diagramas/mediacaosignificado_3_obscurecimento.png` | `figuras/cap.2/diagramas/cap2-terceiro-significado-da-mediacao-tecnica-entrelacamento-de-tempo-e-espaco.png` |
| `figuras/cap.2/diagramas/mediacaosignificado_4_delegacao.png` | `figuras/cap.2/diagramas/cap2-quarto-significado-da-mediacao-tecnica-delegacao.png` |
| `figuras/cap.2/diagramas/mediacaodiferencial_ia_mediacao.png` | `figuras/cap.2/diagramas/cap2-o-diferencial-da-ia-generativa-na-mediacao-tecnica.png` |
| `figuras/cap.3/diagramas/mapa-capitulo3.png` | `figuras/cap.3/diagramas/cap3-texto-mapa-do-capitulo.png` |
| `figuras/cap.3/hollerith_1890_product_sheet.png` | `figuras/cap.3/cap3-folha-de-produto-da-maquina-de-tabulacao-de-hollerith.png` |
| `figuras/cap.3/guaman_poma_acllaconas_fiando.png` | `figuras/cap.3/cap3-acllaconas-fiando-em-guaman-poma.png` |
| `figuras/cap.3/khipu_chancay_huando_amnh_b8707.png` | `figuras/cap.3/cap3-khipu-da-regiao-de-chancay-huando.png` |
| `figuras/cap.3/caderno_rodrigues_aula1.pdf` | `figuras/cap.3/cap3-caderno-de-campo-primeira-aula-do-curso-de-probabilidade-e-estatistica.pdf` |
| `figuras/cap.2/Screenshot_20260521_155105_My Files.jpg` | `figuras/cap.2/cap2-multispecies-cat-s-cradle.jpg` |
| `figuras/cap.4/diagramas-mermaid/cadeia-translacao-condensada-capitulo4-2026-04-13-175942.png` | `figuras/cap.4/diagramas-mermaid/cap4-cadeias-de-translacao-do-projeto-spira-do-covideiro-ao-objeto-fracional.png` |
| `figuras/cap.4/diagramas-mermaid/rede-sociotecnica-spira-capitulo4-2026-04-13-175810.png` | `figuras/cap.4/diagramas-mermaid/cap4-a-rede-sociotecnica-do-spira-do-covideiro-a-dissolucao-da-parceria.png` |
| `figuras/artigos-marcelo/ibmed2026_fig1_pipeline_coleta_IR_SpO2.png` | `figuras/artigos-marcelo/cap4-pipeline-do-projeto-spira-da-coleta-hospitalar-as-duas-tarefas-computacionais.png` |
| `figuras/artigos-marcelo/acl2021_tabela2_ruido_paciente_controle_acuracia.png` | `figuras/artigos-marcelo/cap4-experimentos-de-analise-de-ruido-da-primeira-versao-do-spira-casanova2021deeplearning.png` |
| `figuras/artigos-marcelo/acl2021_fig4_analise_ruido_experimentos3x.png` | `figuras/artigos-marcelo/cap4-curvas-de-acuracia-nos-experimentos-de-insercao-de-ruido-casanova2021deeplearning.png` |
| `figuras/artigos-marcelo/ibmed2026_tabela1_revisao_trabalhos_IR.png` | `figuras/artigos-marcelo/cap4-revisao-dos-trabalhos-de-deteccao-de-ir-por-voz-e-audio-gauy2025contrasting.png` |
| `figuras/artigos-marcelo/distribuicao_SpO2_P2.png` | `figuras/artigos-marcelo/cap4-distribuicao-de-spo-2-em-p2-pacientes-com-ir-versus-controles-gauy2024discriminant.png` |
| `figuras/cap.4/diagramas-mermaid/quadro-analitico-capitulo4-2026-04-01-145652.png` | `figuras/cap.4/diagramas-mermaid/cap4-mapa-dos-referenciais.png` |
| `figuras/cap.4/argumento-capitulo4-2026-04-12-191438.png` | `figuras/cap.4/cap4-diagrama-do-procedimento.png` |
| `figuras/cap.4/covid/HIS-77-186-g004.jpg` | `figuras/cap.4/covid/cap4-autopsia-minimamente-invasiva-guiada-por-ultrassom-em-casos-fatais-de-covid-19-duarteneto2020.jpg` |
| `figuras/cap.4/covid/HIS-77-186-g001.jpg` | `figuras/cap.4/covid/cap4-caracteristicas-histologicas-pulmonares-em-casos-fatais-de-covid-19-duarteneto2020.jpg` |
| `figuras/cap.4/covid/HIS-77-186-g002.jpg` | `figuras/cap.4/covid/cap4-marcadores-epiteliais-no-tecido-pulmonar-duarteneto2020.jpg` |
| `figuras/cap.4/covid/HIS-77-186-g003.jpg` | `figuras/cap.4/covid/cap4-caracteristicas-histologicas-extrapulmonares-em-casos-fatais-de-covid-19-duarteneto2020.jpg` |
| `figuras/cap.4/covid/AISelect_20260403_164426_Chrome.jpg` | `figuras/cap.4/covid/cap4-patologia-pulmonar-cerebral-e-esplenica-em-casos-fatais-de-sars-duarteneto2020.jpg` |
| `figuras/artigos-marcelo/stil2021_tabela3_pretraining_com_sem_ruido.png` | `figuras/artigos-marcelo/cap4-efeito-do-pre-treinamento-nao-supervisionado-na-deteccao-de-ir-gauy2021mfcc.png` |
| `figuras/artigos-marcelo/acl2021_fig2_topologia_CNN_quatro_camadas_conv.png` | `figuras/artigos-marcelo/cap4-topologia-da-rede-neural-convolucional-da-primeira-versao-do-spira.png` |
| `figuras/artigos-marcelo/ibmed2026_fig3_arquitetura_classificacao_binaria.png` | `figuras/artigos-marcelo/cap4-arquitetura-da-tarefa-de-classificacao-binaria-adotada-pelo-spira-gauy2025contrasting.png` |
| `figuras/artigos-marcelo/ibmed2026_tabela3_arquiteturas_PANN_CNN6_10_14.png` | `figuras/artigos-marcelo/cap4-arquiteturas-das-redes-pre-treinadas-cnn6-cnn10-e-cnn14-gauy2025contrasting.png` |
| `figuras/artigos-marcelo/ibmed2026_fig4_audioMAE_pretraining.png` | `figuras/artigos-marcelo/cap4-visao-geral-do-audio-mae-e-seu-esquema-de-pre-treinamento-por-mascaramento.png` |
| `figuras/artigos-marcelo/ibmed2026_fig7_curvas_ROC_AudioMAE_CNN6.png` | `figuras/artigos-marcelo/cap4-curvas-roc-dos-modelos-com-melhor-mcc-para-deteccao-de-ir-gauy2025contrasting.png` |
| `figuras/artigos-marcelo/ibmed2026_fig8_matrizes_confusao_AudioMAE_CNN6.png` | `figuras/artigos-marcelo/cap4-matrizes-de-confusao-dos-modelos-vencedores-de-cada-dataset-gauy2025contrasting.png` |
| `figuras/artigos-marcelo/silva2022_tabela1_configuracoes_experimentos.png` | `figuras/artigos-marcelo/cap4-desempenho-dos-modelos-em-p2-apos-treinamento-em-p1-gauy2024discriminant.png` |
| `figuras/cap.4/pipeline-voz-espectograma-2026-04-12-220916.png` | `figuras/cap.4/cap4-da-voz-ao-veredicto-cadeia-de-translacao-entre-o-corpo-que-fala-e-a-rede-neural.png` |
| `figuras/cap.4/covid/novel-coronavirus-sars-cov-2_49645120251_o.jpg` | `figuras/cap.4/covid/cap4-sars-cov-2-visualizado-por-microscopia-eletronica-de-varredura-e-de-transmissao-com-colorizacao-artificial-1.jpg` |
| `figuras/cap.4/covid/novel-coronavirus-sars-cov-2_49534865371_o.jpg` | `figuras/cap.4/covid/cap4-sars-cov-2-visualizado-por-microscopia-eletronica-de-varredura-e-de-transmissao-com-colorizacao-artificial-2.jpg` |
| `figuras/cap.4/younesi2024_fig8_cnn1d.png` | `figuras/cap.4/cap4-componentes-de-uma-rede-neural-convolucional-filtro-mapas-de-ativacao-e-pooling.png` |
| `figuras/cap.4/artigos-spira/cnn14_arquitetura.png` | `figuras/cap.4/artigos-spira/cap4-arquitetura-da-cnn14-utilizada-pelo-projeto-spira-gauy2025contrasting.png` |
| `figuras/cap.4/artigos-spira/AISelect_20260402_155051_Adobe Acrobat.jpg` | `figuras/cap.4/artigos-spira/cap4-fig-2-resultados-do-experimento-1-pelo-metodo-grad-cam.jpg` |
| `figuras/cap.4/artigos-spira/AISelect_20260402_155107_Adobe Acrobat.jpg` | `figuras/cap.4/artigos-spira/cap4-fig-3-resultados-do-experimento-2-pelo-metodo-grad-cam.jpg` |
| `figuras/cap.4/artigos-spira/AISelect_20260402_155118_Adobe Acrobat.jpg` | `figuras/cap.4/artigos-spira/cap4-fig-4-grad-cam-experimento-3-silva2022interpretability-exo-e-idade.jpg` |
| `figuras/cap.1/20260507_154749.png` | `figuras/cap.1/cap1-estrela-da-amizade.png` |

## 40 referências sem arquivo em disco (NÃO alteradas)

Figuras citadas no `.tex` mas ausentes do repositório — provavelmente geradas no build (bibliometria, OpenAlex etc.) ou ainda não versionadas. Quando esses arquivos existirem, rode o script de novo para incluí-las.

- `figuras/cap.1/Nvidia-entrega-openai.jpg`
- `figuras/cap.1/urdidura-capitulo1.png`
- `figuras/cap.2/analise_bibliometrica/capes_21_subcampos_distribuicao.png`
- `figuras/cap.2/analise_bibliometrica/capes_11_grande_area_share.png`
- `figuras/cap.2/analise_bibliometrica/capes_13_heatmap_area_keyword.png`
- `figuras/cap.2/analise_bibliometrica/capes_22_heatmap_subcampo_grande_area.png`
- `figuras/cap.2/analise_bibliometrica/capes_h01_areas_humanas.png`
- `figuras/cap.2/analise_bibliometrica/capes_h02_temporal_humanas.png`
- `figuras/cap.2/analise_bibliometrica/scielo_11_subject_area_share.png`
- `figuras/cap.2/analise_bibliometrica/scielo_21_subcampos_distribuicao.png`
- `figuras/cap.2/analise_bibliometrica/comparativo_scielo_capes_2026.png`
- `figuras/cap.2/openalex_01_ranking_paises.png`
- `figuras/cap.2/openalex_02_taxa_interna_paises.png`
- `figuras/cap.2/openalex_03_brasil_temporal.png`
- `figuras/cap.2/openalex_04_subcampos_3bases.png`
- `figuras/cap.3/quadro-analitico-capitulo3-2026-04-17-222958.png`
- `figuras/cap.3/panorama-c4ai-capitulo3-2026-04-17-222942.png`
- `figuras/cap.3/seguindo-atores-metodologia-capitulo3-2026-04-17-222948.png`
- `figuras/cap.3/dobra-etnografica-capitulo3-2026-04-17-222937.png`
- `figuras/cap.3/roadmap-ciclo-capitulo3-2026-04-17-213930.png`
- `figuras/cap.3/hollerith-rede-sociotecnica-capitulo3-2026-04-17-222952.png`
- `figuras/cap.3/cadeia-translacao-ibm-capitulo3-2026-04-17-213736.png`
- `figuras/cap.3/analise-bibliometrica-c4ai/1_ranking_grupos.png`
- `figuras/cap.3/analise-bibliometrica-c4ai/9_analise_concentracao.png`
- `figuras/cap.3/analise-bibliometrica-c4ai/3_evolucao_temporal_geral.png`
- `figuras/cap.3/analise-bibliometrica-c4ai/8_composicao_temporal.png`
- `figuras/cap.3/analise-bibliometrica-c4ai/4_heatmap_grupo_ano.png`
- `figuras/cap.3/analise-bibliometrica-c4ai/6_produtividade_grupos.png`
- `figuras/cap.3/arranjo-publico-privado-capitulo3-2026-04-17-222955.png`
- `figuras/cap.3/roadmap-ciclo-capitulo3-2026-04-17-213930.png`
- `figuras/cap.4/imagem-voz/Spira_paciente_sem_legenda.png`
- `figuras/cap.4/diagramas-mermaid/roadmap-Spira-capitulo4-2026-04-13-082509.png`
- `figuras/cap.4/imagem-voz/Spira_waveform_controle.png`
- `figuras/cap.4/imagem-voz/Spira_waveform_paciente.png`
- `figuras/cap.4/imagem-voz/Spira_espectrograma_sem_legenda.png`
- `figuras/cap.4/imagem-voz/Spira_espectrograma_com_eixos.png`
- `figuras/cap.4/imagem-voz/Spira_paciente_com_eixos.png`
- `figuras/cap.4/imagem-voz/Spira_paciente_sem_legenda.png`
- `figuras/cap.4/imagem-voz/Spira_cnn_diagrama_real.png`
- `figuras/cap.4/imagem-voz/Spira_comparacao_linear_log.png`
