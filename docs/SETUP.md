# Como conectar este repo ao `julianehelanski/etnografia` (.tex)

Este repositório roda a análise de rede textual (InfraNodus-style) sobre os
capítulos da tese, que vivem no repo irmão `julianehelanski/etnografia`. A
cada atualização lá, este repo regenera automaticamente PNG/GEXF/relatório.

## Passos manuais (uma vez só)

### 1. No repo `etnografia-c4ai` (este)

- Vá em **Settings → Secrets and variables → Actions** e crie:
  - `ETNOGRAFIA_PAT` *(opcional, só se o repo etnografia for privado)*:
    Personal Access Token fine-grained com `Contents: read` no repo
    `julianehelanski/etnografia`. Se o repo for público, pode pular.

### 2. No repo `etnografia` (.tex)

- Crie o secret **Settings → Secrets and variables → Actions**:
  - `C4AI_DISPATCH_PAT`: PAT fine-grained com `Contents: read & write` no
    repo `julianehelanski/etnografia-c4ai`.
- Copie o conteúdo de `docs/dispatch-from-tex.yml.example` (deste repo)
  para `.github/workflows/notify-c4ai.yml` no repo etnografia e commite.

### 3. No `infranodus/chapters.yml` (deste repo)

- Mude `enabled: false` para `enabled: true` em cada capítulo cujo `.tex`
  já exista no repo etnografia. O nome em `source:` precisa bater com o
  caminho relativo no repo etnografia (ex.: `capitulo2.tex`).
- *(Opcional)* Crie `infranodus/interpretation_capN.md` com sua leitura
  interpretativa — o conteúdo é embutido na seção 9 do relatório.

## Fluxo automático que isso habilita

1. Você commita uma mudança em `capitulo3.tex` no repo `etnografia`.
2. O workflow `notify-c4ai.yml` no repo etnografia dispara um
   `repository_dispatch` (tipo `thesis-updated`) para este repo.
3. O workflow `analyze.yml` aqui:
   - faz checkout deste repo + checkout do repo etnografia em `_tex/`;
   - roda `python infranodus/run_all.py --source-root _tex`;
   - commita os PNG/GEXF/CSV/JSON/`.md` atualizados em `main`.

## Rodar localmente

```bash
# clonar o repo .tex ao lado para que _tex/ aponte para ele
git clone https://github.com/julianehelanski/etnografia.git _tex
pip install -r requirements.txt

# todos os capítulos habilitados
python infranodus/run_all.py --source-root _tex

# só alguns
python infranodus/run_all.py --source-root _tex --only cap1,cap2

# ou um único, manualmente, sem o manifesto
python infranodus/infranodus_cap1.py \
  --chapter _tex/capitulo2.tex --slug cap2 --title "Capítulo 2"
```

Outputs:
- `cap1` (legado): `infranodus/infranodus_cap1_*` direto na pasta `infranodus/`.
- `cap2`, `cap3`, …: subpasta `infranodus/<slug>/` (mantém a história
  intocada e separa cada capítulo).

## Trigger manual

Em **Actions → "Analisa capítulos da tese" → Run workflow** você pode
forçar uma rerun (e opcionalmente passar `only=cap2` para limitar).
