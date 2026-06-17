# Restaurar o site no modelo antigo (mapa curado)

O site foi trocado: a página principal (`index.html`) passou a ser a
**cartografia textual da tese** (rede de co-ocorrência gerada do `.tex`).

O **modelo antigo** — o mapa curado de conceitos, com painéis de
capítulo/seção, figuras, tour guiado e os modos capítulo/natureza/rede —
**não foi apagado**. Ele está guardado de duas formas:

1. **Arquivo no repositório:** `index-curado.html`
   É a página antiga completa e autossuficiente. Para ver, é só abrir
   esse arquivo no navegador (ou acessar `…/index-curado.html` no site
   publicado).

2. **Histórico do git:** qualquer commit anterior a
   *"Torna a cartografia textual a página principal"* tem o site antigo
   como `index.html`.

## Como voltar ao modelo antigo (definitivamente)

Basta tornar o arquivo curado a página principal:

```bash
# faz um backup da rede nova e restaura o curado como index
git mv index.html index-rede.html
git mv index-curado.html index.html
git commit -m "Volta ao modelo curado como página principal"
git push
```

Para **desfazer** e voltar à rede textual, é só inverter os dois `git mv`.

## Como manter os dois (sem escolher)

Os dois arquivos podem coexistir: `index.html` (rede) e
`index-curado.html` (mapa curado). Você pode, por exemplo, colocar um
link discreto de um para o outro. Peça ao Claude se quiser esse botão de
alternância.

## Regenerar a rede textual quando a tese mudar

**Automático:** o workflow `.github/workflows/analyze.yml` regenera a rede
e reinjeta o JSON no `index.html` a cada atualização da tese. Ele dispara:

- por *repository_dispatch* (`thesis-updated`) vindo do repo da tese —
  **requer** que o workflow de `docs/dispatch-from-tex.yml.example` esteja
  instalado no repo `tecno-etnografia-centro-ia` (com o secret PAT);
- pelo botão **Run workflow** em Actions (manual, a qualquer momento);
- ao alterar `infranodus/tese_network.py` ou os scripts de análise.

**Manual** (rodar localmente):

```bash
git clone --depth 1 https://github.com/julianehelanski/tecno-etnografia-centro-ia.git /tmp/tese
python3 infranodus/tese_network.py --source-root /tmp/tese --inject index.html
```
