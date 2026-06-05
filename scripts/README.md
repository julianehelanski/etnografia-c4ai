# scripts/

Utilitários para manter o site sincronizado com a tese.

## `atualizar_keywords.py`

Recalcula, a partir do código-fonte LaTeX da tese, as duas listas de
palavras-chave de cada capítulo — **mais frequentes** e **mais distintivas
(TF-IDF)** — e reescreve os blocos `<div class="kw-block">` dentro de
`index.html`.

```bash
# usa /tmp/tese (clona/atualiza automaticamente se preciso)
python3 scripts/atualizar_keywords.py

# ou aponte para uma cópia local da tese
python3 scripts/atualizar_keywords.py /caminho/para/a/tese
```

### O que é automático e o que não é

- **Automático:** as *contagens* dos termos já escolhidos. Toda vez que a
  tese mudar, rode o script e os números são atualizados (contagem feita só
  sobre o texto corrido — comandos LaTeX, chaves e chaves de citação são
  removidos).
- **Curado à mão:** *quais* termos entram em cada lista. Ficam fixados no
  dicionário `CURADAS` no topo do script (com regex que funde
  singular/plural). Isso preserva a curadoria — p.ex. excluir
  "inteligência artificial" (presente em todos os capítulos) e filtrar
  artefatos de citação em inglês.

### Re-curadoria

Ao final, o script imprime um **relatório** com o novo top de frequência e
de TF-IDF por capítulo. Se a tese mudar muito e um termo novo passar a ser
relevante, edite a lista `CURADAS` e rode de novo.

> O resto do site (nós, links entre capítulos, textos dos nós, seções) é
> editorial e não é gerado por script — peça ao Claude para atualizar
> quando a estrutura da tese mudar.
