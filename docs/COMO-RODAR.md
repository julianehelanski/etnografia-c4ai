# Como rodar as análises e atualizar o site (manual)

Guia para regenerar **lexicometria, bibliometria, figuras e o site** sem
depender de ajuda externa. Todo o pipeline está definido em
[`.github/workflows/analyze.yml`](../.github/workflows/analyze.yml); este
documento espelha aquele fluxo.

Há **dois caminhos**: o fácil (botão no GitHub) e o completo (local).

---

## Caminho 1 — sem instalar nada (recomendado)

No GitHub: **Actions → "Analisa capítulos da tese" → Run workflow**.

Isso roda **todo** o pipeline, faz commit dos resultados e o
[`pages.yml`](../.github/workflows/pages.yml) **republica o site** sozinho.

- Campo opcional `only`: limita a capítulos (ex.: `cap1,cap2`).
- Também roda **automaticamente** todo dia às 6h17 UTC e quando a tese é
  atualizada (evento `repository_dispatch: thesis-updated`).
- A regeneração é **determinística** (`PYTHONHASHSEED=0`): se a tese não
  mudou, não há commit.

---

## Caminho 2 — rodar local, manualmente

### Pré-requisitos

- Python 3.11 e git.
- A análise lê o código-fonte `.tex` da tese, que mora em **outro
  repositório**: `julianehelanski/tecno-etnografia-centro-ia`.

### Preparação

```bash
# 1) clonar o site e a tese lado a lado (a tese vai em _tex/)
git clone https://github.com/julianehelanski/tecno-etnografia-tese-site.git
cd tecno-etnografia-tese-site
git clone https://github.com/julianehelanski/tecno-etnografia-centro-ia.git _tex

# 2) ambiente Python
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 3) mesma saída determinística do CI (IMPORTANTE)
export PYTHONHASHSEED=0
```

### Pipeline (na mesma ordem do CI)

```bash
# (A) LEXICOMETRIA por capítulo: infranodus (co-ocorrência · NPMI · Louvain
#     · PageRank) + trajetória narrativa. Saídas em infranodus/<cap>/
python infranodus/run_all.py --source-root _tex            # ou: --only cap1,cap2

# (B) REDE TEXTUAL principal e injeção no mapa (index.html)
python infranodus/tese_network.py --source-root _tex --inject index.html

# (C) Imagens da análise -> figuras/
python infranodus/sync_site_figuras.py

# (D) Figuras de conteúdo da tese -> figuras/
python scripts/sync_tese_figuras.py --source-root _tex

# (E) Página curada (index-curado.html): palavras-chave, cache-busting, sumário
SITE_INDEX=index-curado.html python scripts/atualizar_keywords.py _tex
SITE_INDEX=index-curado.html python scripts/cache_busting_figuras.py
SITE_INDEX=index-curado.html python scripts/sumario_auto.py --source-root _tex

# (F) Relatório de divergência tese <-> site
python scripts/relatorio_divergencia_tese.py --source-root _tex

# (G) Documento da tese (resumo · sumário · ilustrações · tabelas) -> index.html
python infranodus/tese_documento.py --source-root _tex --inject index.html
```

### Publicar (atualizar o site)

```bash
git add infranodus/ figuras/ index.html index-curado.html \
        docs/divergencia-tese.md scripts/tex_structure_snapshot.json
git commit -m "Regenera redes + figuras/keywords a partir da tese"
git push        # o push na main dispara o pages.yml e republica o site
```

---

## Onde fica cada "análise"

| Análise | Script | Observação |
|---|---|---|
| **Lexicométrica** (rede de termos) | `infranodus/tese_network.py` (mapa) e `infranodus/run_all.py` → `infranodus_cap*.py` (por capítulo) | núcleo do site |
| **Palavras-chave** (frequência + TF‑IDF) | `scripts/atualizar_keywords.py` | só recalcula contagens; *quais* termos entram é curado à mão no dicionário `CURADAS` no topo do script |
| **Bibliométrica** (CAPES/SciELO) | as figuras (`figuras/cap2/cap2-bib-*`) são geradas no **repositório da tese** e só **sincronizadas** aqui por `scripts/sync_tese_figuras.py`; o agrupamento "Bibliometria · panorama do campo" é curado em `tese_network.py` (`carve_bibliometric_territory`) | a geração dos gráficos bibliométricos está no repo `.tex`, não aqui |
| **Trajetória narrativa** | `infranodus/narrative_trajectory.py` (via `run_all.py`) | alluvial / gantt / semântico |
| **Atualização do site** | injeção via `--inject` + `git push` → `pages.yml` | deploy automático |

---

## Dois pontos importantes

- **Determinismo:** use sempre `PYTHONHASHSEED=0` (como o CI). Sem isso, a
  saída pode variar e gerar diffs espúrios.
- **O que NÃO é gerado por script:** textos dos nós, ligações editoriais
  entre capítulos, seções escritas à mão — e os ajustes visuais do site
  (cores, capa, fontes, responsividade, QR). Isso é edição direta nos
  arquivos `index.html` / `index-curado.html`. O pipeline acima regenera
  **dados e figuras**, preservando o restante.

> Veja também [`scripts/README.md`](../scripts/README.md) e
> [`infranodus/README.md`](../infranodus/README.md) para detalhes de cada
> utilitário.
