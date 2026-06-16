#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
atualizar_keywords.py
=====================
Recalcula as palavras-chave de cada capítulo (listas "mais frequentes" e
"mais distintivas / TF-IDF") a partir do código-fonte LaTeX da tese e
reescreve os blocos <div class="kw-block"> dentro de index.html.

A CURADORIA (quais termos aparecem) fica fixada em CURADAS abaixo, para
preservar o trabalho editorial (fusão de singular/plural, remoção de
artefatos de citação em inglês etc.). O script apenas atualiza as
CONTAGENS conforme a tese muda. Ao final, imprime um RELATÓRIO com o novo
top de frequência e de TF-IDF — se o conteúdo mudou muito, use-o para
ajustar a lista CURADAS manualmente.

Uso:
    python3 scripts/atualizar_keywords.py [caminho-da-tese]

Se o caminho não for informado, usa /tmp/tese; se não existir, clona de
THESIS_REPO.
"""
import os, re, sys, math, subprocess
from collections import Counter

THESIS_REPO = "https://github.com/julianehelanski/tecno-etnografia-centro-ia"
HERE = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(HERE, "..", "index.html")

# qual arquivo .tex corresponde a cada capítulo do site
CHAPTER_FILES = {"cap1": "ex_cap1.tex", "cap2": "ex_cap2.tex",
                 "cap3": "ex_cap3.tex", "cap4": "ex_cap4.tex"}

# âncora (badge) de cada nó-capítulo no index.html, p/ localizar o bloco
CHAPTER_ANCHOR = {
    "cap1": 'badge:"\\\\chapter{1} · método",content:`',
    "cap2": 'badge:"\\\\chapter{2}",content:`',
    "cap3": 'badge:"\\\\chapter{3}",content:`',
    "cap4": 'badge:"\\\\chapter{4}",content:`',
}

# ---- CURADORIA: (rótulo exibido, regex de contagem) -------------------------
# 'freq'  = as 5 mais frequentes ; 'dist' = as 5 mais distintivas (TF-IDF)
CURADAS = {
 "cap1": {"freq": [("rede", r"redes?"), ("pesquisa", r"pesquisas?"),
                   ("campo", r"campos?"), ("Latour", r"latour"),
                   ("etnografia", r"etnografias?")],
          "dist": [("fazer-com", r"fazer-com"), ("compostagem", r"compostag(em|ens)"),
                   ("parciais", r"parciais"), ("têxtil", r"t[êse]xt(il|eis)"),
                   ("letramento", r"letramentos?")]},
 "cap2": {"freq": [("campo", r"campos?"), ("Latour", r"latour"),
                   ("figuração", r"figura[çc][õo]es|figura[çc][ãa]o"),
                   ("militar", r"militar(es)?"), ("vocabulário", r"vocabul[áa]rios?")],
          "dist": [("militar", r"militar(es)?"), ("catálogo", r"cat[áa]logos?"),
                   ("figurações", r"figura[çc][õo]es"),
                   ("defesas", r"defesas?"), ("Collins", r"collins")]},
 "cap3": {"freq": [("IBM", r"ibm"), ("C4AI", r"c4ai"),
                   ("Cláudio", r"cl[áa]udio"), ("arranjo", r"arranjos?"),
                   ("ecossistema", r"ecossistemas?")],
          "dist": [("ecossistema", r"ecossistemas?"), ("negócio", r"neg[óo]cios?"),
                   ("serviços", r"servi[çc]os?"),
                   ("multiplicação", r"multiplica[çc][ãa]o"),
                   ("aprisionamento", r"aprisionamentos?")]},
 "cap4": {"freq": [("SPIRA", r"spira"), ("covideiro", r"covideiros?"),
                   ("inscrição", r"inscri[çc][õo]es|inscri[çc][ãa]o"),
                   ("cadeia", r"cadeias?"), ("espectrograma", r"espectrogramas?")],
          "dist": [("mel", r"mel"), ("vírus", r"v[íi]rus"),
                   ("enfermaria", r"enfermarias?"), ("pandêmico", r"pand[êe]mic[oa]s?"),
                   ("fonoaudiólogos", r"fonoaudi[óo]logos?")]},
}

# stopwords p/ o relatório de sugestões (não afeta a contagem das curadas)
STOP = set(('a o e que de do da em um uma os as dos das no na nos nas para por com se ao '
 'à às aos como mais mas ou ser ter seu sua seus suas seja entre sobre quando onde qual '
 'quais sem isso este esta esse essa isto aquilo já não sim também muito muita pouco cada '
 'todo toda todos todas outro outra outros outras mesmo mesma ainda então assim porque pois '
 'até depois antes durante apenas tão tanta tanto tal qualquer algum alguma alguns algumas '
 'nenhum nenhuma quem cujo cuja são foi era está estão estava sendo havia haver tem tinha '
 'tinham fez faz fazer pode podem podia deve devem dois duas três lhe nos vos eu ele ela eles '
 'elas nós você vocês meu minha nossa nosso dela dele deles delas aqui ali lá aquele aquela '
 'num numa pela pelo pelos pelas desde após bem nem ora vez vezes parte forma modo caso ponto '
 'sentido partir além meio através vista lado fim seção capítulo tese trabalho análise objeto '
 'leitura obra figure lugar termos texto relação conceito anos longo descreve ocorrências '
 'science the of and to in aime claude this that fig pode uso via').split())


def clean(path):
    t = open(path, encoding="utf-8").read()
    t = re.sub(r'(?<!\\)%.*', '', t)
    t = re.sub(r'\\(parencite|textcite|cite|footcite|autocite|label|ref|cref|Cref|'
               r'includegraphics|input|index|url|href)\s*(\[[^\]]*\])?\s*(\{[^{}]*\})?', '', t)
    t = re.sub(r'\\[a-zA-Z@]+\*?', '', t)
    t = re.sub(r'[{}\[\]$&~^_\\#]', ' ', t)
    return t.lower()


def count(text, pattern):
    return len(re.findall(r'(?<![\w-])(?:' + pattern + r')(?![\w-])', text))


def inner(items):
    return ", ".join('%s<sup>%d</sup>' % (lbl, c) for lbl, c in items)


def build_block(freq, dist):
    return ('<div class="kw-block">'
            '<div class="kw-line"><span class="kw-cap">% mais frequentes</span>'
            '<span class="kw-cmd">\\keywords{</span><span class="kw">' + inner(freq) +
            '</span><span class="kw-cmd">}</span></div>'
            '<div class="kw-line"><span class="kw-cap">% mais distintivas · tf-idf</span>'
            '<span class="kw-cmd">\\keywords*{</span><span class="kw">' + inner(dist) +
            '</span><span class="kw-cmd">}</span></div></div>')


def suggestions(texts):
    """imprime top frequência e TF-IDF por capítulo (para re-curadoria)."""
    docs = {}
    for c, t in texts.items():
        words = re.findall(r"[a-zà-ÿ0-9][a-zà-ÿ0-9\-]{2,}", t)
        docs[c] = Counter(w for w in words if w not in STOP and len(w) >= 3
                          and not w.isdigit())
    N = len(docs)
    df = Counter()
    for c in docs.values():
        for w in c:
            df[w] += 1
    print("\n================ RELATÓRIO (sugestões de re-curadoria) ================")
    for c in CHAPTER_FILES:
        cc = docs[c]
        tot = sum(cc.values()) or 1
        freq = cc.most_common(12)
        tfidf = sorted(((w, (cc[w] / tot) * math.log(N / df[w]), cc[w])
                        for w in cc if cc[w] >= 8 and df[w] < N),
                       key=lambda x: -x[1])[:12]
        print("\n--- %s ---" % c)
        print("  frequentes:", ", ".join("%s(%d)" % (w, n) for w, n in freq))
        print("  distintivas:", ", ".join("%s(%d)" % (w, ct) for w, _, ct in tfidf))


def main():
    tese = sys.argv[1] if len(sys.argv) > 1 else "/tmp/tese"
    if not os.path.isdir(tese):
        print("Clonando a tese em", tese, "...")
        subprocess.run(["git", "clone", "--depth", "1", THESIS_REPO, tese], check=True)
    else:
        subprocess.run(["git", "-C", tese, "pull", "--ff-only"], check=False)

    texts = {c: clean(os.path.join(tese, f)) for c, f in CHAPTER_FILES.items()}

    html = open(INDEX, encoding="utf-8").read()
    changed = 0
    for c, anchor in CHAPTER_ANCHOR.items():
        freq = [(lbl, count(texts[c], pat)) for lbl, pat in CURADAS[c]["freq"]]
        dist = [(lbl, count(texts[c], pat)) for lbl, pat in CURADAS[c]["dist"]]
        freq.sort(key=lambda x: -x[1])   # exibe sempre em ordem de frequência
        dist.sort(key=lambda x: -x[1])
        block = build_block(freq, dist)
        pat = re.escape(anchor) + r'<div class="kw-block">.*?</div></div>'
        new, n = re.subn(pat, lambda m: anchor + block, html, count=1, flags=re.DOTALL)
        if n != 1:
            print("AVISO: bloco de %s não encontrado (anchor mudou?)" % c)
        else:
            html = new
            changed += 1
            print("%s  freq=%s | dist=%s" % (
                c, [x[1] for x in freq], [x[1] for x in dist]))

    open(INDEX, "w", encoding="utf-8").write(html)
    print("\n%d/4 blocos atualizados em index.html" % changed)
    suggestions(texts)


if __name__ == "__main__":
    main()
