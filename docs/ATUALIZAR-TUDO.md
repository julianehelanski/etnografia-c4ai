# Atualizar todas as análises (esquema por pasta)

Colinha para entrar em **cada repositório** e regerar suas análises. Cada
projeto é independente: rode sempre **dentro da pasta dele** (os caminhos
são relativos) e publique por repositório (`git add -A ; git commit ; git push`).

> Caminhos assumem as pastas no Desktop (Windows/PowerShell). Ajuste se as
> suas estiverem em outro lugar. Em macOS/Linux, troque `\` por `/` e
> `$env:VAR = "x"` por `export VAR=x`.

---

## 1) SITE — rede textual (lexicométrica)
📁 `tecno-etnografia-tese-site`

```powershell
cd C:\Users\julia\Desktop\tecno-etnografia-tese-site
$env:PYTHONHASHSEED = "0"
$tese = "..\tecno-etnografia-centro-ia"

python infranodus\run_all.py --source-root $tese            # PNGs por capítulo
python infranodus\tese_network.py --source-root $tese --inject index.html  # mapa
python scripts\atualizar_keywords.py $tese                  # palavras-chave

git add -A ; git commit -m "Atualiza análise textual" ; git push   # publica o site
```
➡️ Atualiza o site (mapa + figuras). O `push` republica online via GitHub Pages.
Detalhes: [`COMO-RODAR.md`](COMO-RODAR.md) · parâmetros: [`PARAMETROS.md`](PARAMETROS.md).

---

## 2) BIBLIOMETRIA C4AI — co-palavras das publicações
📁 `bibliometria-publicacoes-c4ai`

```powershell
cd C:\Users\julia\Desktop\bibliometria-publicacoes-c4ai
python scrape_c4ai.py        # (opcional) recoleta do site do C4AI — precisa internet
python preparar_base.py      # c4ai_publicacoes_manual.xlsx -> c4ai_publicacoes.xlsx
python enrich_metadata.py    # enriquece metadados
python coword_analysis.py    # análise de co-palavras (gráficos)
```
⚠️ Ordem **provável** — confirmar nos cabeçalhos de `enrich_metadata.py` e
`coword_analysis.py`. Se os dados (`c4ai_publicacoes_manual.xlsx`) já
estiverem na pasta, dá para pular o `scrape_c4ai.py`.

---

## 3) BIBLIOMETRIA IA-HUMANAS — CAPES / SciELO / OpenAlex
📁 `bibliometria-ia-humanas`

```powershell
cd C:\Users\julia\Desktop\bibliometria-ia-humanas
pip install -r requirements.txt          # só na primeira vez

# CAPES (precisa dos 4 XLSX em dados_capes/ — se for Git LFS: git lfs pull)
python analise_capes_2021_2024.py
python figuras_capes_2021_2024.py
python analise_capes_humanas.py

# SciELO (precisa de internet)
python analise_scielo_articlemeta.py
python figuras_scielo_articlemeta.py

# OpenAlex (internet + seu e-mail)
python analise_openalex.py --modo agregado --mailto SEU_EMAIL@exemplo.com
python figuras_openalex.py

# comparativo final (depois de CAPES + SciELO)
python analise_comparativa_2026.py
```
➡️ Gera tudo em `figuras/`. Regra: `analise_*` **antes** do `figuras_*`;
comparativo **por último**. Versões antigas (`analise_scielo.py`,
`analise_capes.py`, `analise_comparativa.py`) são o recorte histórico.

---

## 4) FIGURAÇÕES — Latour × Haraway (Cap. 2)
📁 `analise_figuracoes`  ·  scripts numerados em `scripts/`

```powershell
cd C:\Users\julia\Desktop\analise_figuracoes
pip install -r requirements.txt          # só na primeira vez
$env:PYTHONHASHSEED = "0"

python scripts\01_extract_text.py    # SÓ se for re-extrair dos PDFs (precisa dos PDFs + .env)
python scripts\02_kwic.py            # concordâncias (keyword-in-context)
python scripts\03_frequencies.py     # tabelas de frequência
python scripts\04_visualizations.py  # gráficos
python scripts\05_cooccurrence.py    # redes de co-ocorrência
python scripts\06_sampling.py        # amostragem de passagens
```
➡️ Saídas em `outputs/` (`csv/`, `figuras/`, `relatorios/`, `latex/`).
💡 Como o texto já está em `corpus/txt/` (commitado), normalmente **pula-se o
`01`** e começa no `02`. A ordem é a dos números (01→06).

---

## 🔑 Regras de ouro (valem para as 4)

1. **Rode dentro da pasta do próprio repositório** (os caminhos são relativos).
2. **`analise_*` / `0X` vêm antes** dos passos que desenham (figuras/visualizações).
3. **Publicar é por repositório:** `git add -A ; git commit -m "..." ; git push`.
4. **1ª vez em cada repo:** `pip install -r requirements.txt` (se houver).
5. **Determinismo:** `$env:PYTHONHASHSEED = "0"` antes de rodar (importa
   sobretudo no site, por causa do Louvain).

---

## Mundos separados (importante)

- O botão **"Run workflow" do GitHub Actions** atualiza **apenas o site**
  (análise lexicométrica). Os três repositórios de bibliometria/figurações
  são independentes e **não** têm essa automação — cada um se roda por si.
- As figuras geradas nos repositórios de bibliometria/figurações entram na
  tese/site por um passo **manual** de cópia (não automático).
