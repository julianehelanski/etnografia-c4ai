#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tese_documento.py
=================
Extrai do `.tex` da tese os "paratextos" para apresentar na defesa:
resumo (PT), palavras-chave, sumário (capítulos · seções · subseções,
com um breve resumo por capítulo e uma nota por seção), lista de
ilustrações e lista de tabelas. Exporta JSON e, opcionalmente, reinjeta
num HTML (<script id="docdata">).

Uso:
    python3 infranodus/tese_documento.py --source-root /tmp/tese --inject index.html
"""
import argparse
import json
import re
import sys
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(THIS_DIR.parent / "scripts"))
from relatorio_divergencia_tese import clean_title, _match_brace_arg  # noqa: E402

# Síntese para a banca, ancorada no Resumo e nas Considerações Finais (cap.5).
# Curada (não gerada): revise/ajuste se quiser outra ênfase.
TESE = {
    "tema": "A pesquisa em inteligência artificial como prática tecnocientífica "
            "situada — tecnografias do C4AI, o Centro de Inteligência "
            "Artificial da USP, seguindo cientistas e engenheiros universidade "
            "afora.",
    "objeto": "Cada capítulo corta um objeto etnográfico próprio: a própria "
              "pesquisa enquanto prática composta, humana e além de humana "
              "(cap. 1); a obra de Latour e o campo brasileiro de estudos de IA "
              "nas ciências humanas (cap. 2); a rede longa do arranjo "
              "USP · FAPESP · IBM que sustentou o C4AI, da fundação (2020) à "
              "dissolução da parceria (2025) (cap. 3); e a rede curta que se "
              "ata em torno do SPIRA, da voz de pacientes hospitalizados com "
              "Covid-19 à detecção de insuficiência respiratória pela rede "
              "neural (cap. 4).",
    "pergunta": "Onde está o laboratório de IA e onde estão os seus cientistas? "
                "O que cientistas e engenheiros fazem quando desenvolvem "
                "inteligência artificial?",
    "objetivo": "Descrever o arranjo das práticas tecnocientíficas da rede "
                "sociotécnica do C4AI e analisar como o plano "
                "institucional-corporativo e o plano técnico-situado se "
                "articulam na produção de conhecimento em IA e na produção de "
                "conhecimento sobre IA pelas ciências sociais.",
    "questoes": [
        "Como se faz IA, na prática, num centro de pesquisa?",
        "Como um arranjo público-privado nasce, funciona e se dissolve?",
        "Como a voz de um paciente se converte em dado e em classificação pela "
        "rede neural — e o que se perde nessa cadeia de inscrições?",
        "Que vocabulário (figurações) descreve a tecnociência sem denunciá-la "
        "nem celebrá-la?",
    ],
    "conclusao": "Fazer IA é fazer tecnociência: construir fatos e, ao mesmo "
                 "tempo, sustentar as redes que os tornam possíveis. O "
                 "computador é o próprio laboratório — a tecnociência da IA se "
                 "faz distribuída, sobre infraestrutura computacional que poucos "
                 "atores no mundo detêm — e as redes que pareciam estáveis "
                 "revelaram-se composições precárias: a falha de generalização "
                 "do SPIRA e a dissolução da parceria IBM-C4AI (dez. 2025) "
                 "tornaram visível essa fragilidade.",
    "contribuicoes": [
        "Empírica — o registro etnográfico do ciclo completo de uma parceria "
        "público-privada em IA no Brasil, do nascimento à dissolução (inclui "
        "relatórios não-públicos e entrevistas que preservam a ciência em "
        "construção).",
        "Metodológica — as quatro lições do Capítulo 1, a proposta da "
        "tecnografia (conceito que nasceu como tecnoetnografia e foi renomeado "
        "no encontro com a antropologia da técnica) e o uso das notas de rodapé "
        "como dispositivo teórico-metodológico.",
        "Analítica — o conceito de inscrição tecnográfica, a leitura do SPIRA "
        "como objeto fracional (Mol/Law), a descrição da IA generativa como "
        "mediador não determinista, cuja resposta se enacta a cada uso situado, "
        "e o tecnopoder (termo tomado de Brennan e deslocado para o material do "
        "Capítulo 3).",
    ],
    "desdobramentos": [
        "A reconfiguração da rede após o encerramento da parceria C4AI-IBM "
        "(dez. 2025): como se redistribuem recursos, competências e vínculos "
        "quando um arranjo desse porte se desfaz.",
        "O lugar da universidade pública na pesquisa em IA quando o "
        "conhecimento de ponta migra para as corporações: sob quais arranjos, "
        "com quais salvaguardas e em direção a quais finalidades se firmam os "
        "vínculos com quem detém a infraestrutura computacional (do Arandu ao "
        "JAIRU, inaugurado em fev. 2026) — pergunta que um retorno ao campo, "
        "com a continuação do SPIRA-BM, talvez deixe seguir.",
        "O vocabulário crítico que as ciências humanas e sociais brasileiras "
        "ainda constroem para descrever a IA — o campo em formação que o "
        "mapeamento bibliométrico registrou.",
        "O que o não determinismo da IA generativa significa para a pesquisa e "
        "o ensino: regimes de declaração e auditabilidade, letramento técnico "
        "nas ciências sociais e a desigualdade epistêmica entre acessos.",
    ],
}

# capítulo: (arquivo, número, título, resumo [o que faz], conclusão [a que chega])
CHAPTERS = [
    ("ex_cap0.tex", "", "Apresentação",
     "A entrada em campo: a pergunta que move a tese e o primeiro encontro com "
     "um sistema de IA (o SPIRA), que abre o percurso etnográfico.",
     ""),
    ("ex_cap1.tex", "1", "Onde está o laboratório e os seus cientistas?",
     "Documenta o percurso da etnógrafa pelo campo e constrói o método a partir "
     "da experiência: o patchwork como figuração, as existências parciais "
     "(incluindo o fazer-com IA generativa) e a compostagem.",
     "Chega a quatro lições metodológicas e à proposta da tecnografia — "
     "modo de pesquisa que habita a tensão entre a circulabilidade técnica das "
     "inscrições e a realidade sensível dos corpos."),
    ("ex_cap2.tex", "2", "Metáforas, figurações e alianças: revisão da literatura",
     "Reconstrói as alianças teóricas da tese em duas tramas: a análise "
     "lexicométrica das figurações em seis obras de Latour e o mapeamento "
     "bibliométrico do campo brasileiro de IA nas ciências humanas.",
     "Mostra que a figuração militar-industrial é situada e que o vocabulário "
     "têxtil-topológico organiza os textos metateóricos de Latour; documenta um "
     "campo brasileiro em formação, onde a pesquisa se insere."),
    ("ex_cap3.tex", "3", "A rede que Fábio e Cláudio construíram",
     "Segue Fábio e Cláudio pela rede longa que sustentou o C4AI por cinco "
     "anos, dos cartões de Hollerith (1890) à genealogia da IBM e à "
     "racionalidade do ecossistema de inovação.",
     "Documenta o ciclo completo da parceria (2020–2025) e descreve o padrão "
     "de reprodução de dependências técnica e comercial sedimentado pela IBM "
     "ao longo de 135 anos, lido na figura do tecnopoder (termo tomado de "
     "Brennan); encerra com a dissolução IBM-C4AI (dez. 2025)."),
    ("ex_cap4.tex", "4", "A rede que Marcelo construiu",
     "Segue Marcelo Finger pela rede curta do SPIRA: a cadeia de translações "
     "que converte a voz de pacientes com Covid-19 em espectrogramas "
     "processados por redes neurais — da fala ao dado à detecção de "
     "insuficiência respiratória.",
     "Mostra que o modelo (96,5% de precisão) aprendeu uma insuficiência "
     "respiratória específica ao covideiro pandêmico: sua falha de "
     "generalização é evidência empírica da tensão ontológica (Mol). Propõe a "
     "inscrição tecnográfica."),
    ("ex_cap5.tex", "", "Considerações finais: arrematando os fios",
     "Retoma os três movimentos do método — o corte, os atores e actantes, a "
     "compostagem —, relê o C4AI (rede longa) e o SPIRA (rede curta) como a "
     "mesma rede sob cortes distintos e reúne as contribuições e as questões "
     "que ficam em aberto.",
     "O computador é o próprio laboratório de uma tecnociência distribuída, e "
     "as redes que pareciam estáveis revelaram-se composições precárias; a "
     "própria tese — repartida entre Overleaf, GitHub e o site — partilha essa "
     "condição: existe enquanto as suas conexões forem mantidas."),
]

# título real do capítulo: primeiro \chapter{...} ou \chapter*{...} do .tex
CHAP_RE = re.compile(r'\\chapter\*?\s*(?:\[[^\]]*\])?\s*\{')


def parse_chapter_title(tex: str, fallback: str) -> str:
    """Extrai o título real do \\chapter{...} (ou \\chapter*{...}) do .tex,
    para casar com o nome oficial no documento. Cai no fallback curado se
    o comando não for encontrado."""
    m = CHAP_RE.search(tex)
    if not m:
        return fallback
    arg, _ = _match_brace_arg(tex, m.end() - 1)
    return clean_title(arg) or fallback

ENV_RE = re.compile(
    r'\\begin\{(figure|table|longtable)\*?\}'
    r'|\\end\{(figure|table|longtable)\*?\}'
    r'|\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}'
    r'|\\caption(?:\[([^\]]*)\])?\{')

SEC_RE = re.compile(r'\\(section|subsection)\*?\s*\{')

# Diagrama interativo (MermaidChart) embutido na legenda via \href{...}.
MERMAID_RE = re.compile(r'https://mermaid\.ai/d/[0-9a-fA-F-]+')

# Pasta de figuras que o SITE de fato exibe (figuras/<slug>/...).
SITE_FIGURAS = THIS_DIR.parent / "figuras"


def _site_image(texpath: str | None) -> str | None:
    r"""Mapeia o \includegraphics da tese para a figura que o site exibe.

    Hoje só as inscrições de rede textual (InfraNodus) e as trajetórias
    narrativas têm cópia em figuras/<slug>/ com o nome do site. Retorna o
    caminho relativo ao repositório do site se o arquivo existir; senão None
    — mesmo princípio de sync_site_figuras.py: só mostra o que o site tem.
    """
    if not texpath:
        return None
    base = texpath.strip().replace("\\", "/").rsplit("/", 1)[-1].lower()
    # Rede textual da tese inteira (Considerações finais): cópia na raiz de figuras/.
    if base == "rede_tese_inteira.png":
        return "figuras/rede_tese_inteira.png" if (SITE_FIGURAS / base).exists() else None
    mname = re.search(r"infranodus_cap(\d+)_", base)
    mdir = re.search(r"cap\.?(\d+)", texpath)
    m = mname or mdir
    if not m:
        return None
    slug = f"cap{m.group(1)}"
    name_map = {
        f"infranodus_cap{m.group(1)}_network.png":   f"{slug}-infranodus-network.png",
        f"infranodus_cap{m.group(1)}_focus.png":     f"{slug}-infranodus-focus.png",
        f"infranodus_cap{m.group(1)}_pmi.png":       f"{slug}-infranodus-pmi.png",
        f"infranodus_cap{m.group(1)}_focus_pmi.png": f"{slug}-infranodus-pmi.png",
        "trajectory_gantt.png":                      f"{slug}-trajectory-gantt.png",
        "trajectory_alluvial.png":                   f"{slug}-trajectory-alluvial.png",
        "trajectory_semantic.png":                   f"{slug}-trajectory-semantic.png",
    }
    mapped = name_map.get(base)
    if not mapped:
        return None
    rel = f"figuras/{slug}/{mapped}"
    return rel if (SITE_FIGURAS / slug / mapped).exists() else None


def _is_continuation(s: str) -> bool:
    """Rótulo de continuação (parte seguinte de uma figura/longtable),
    que compartilha o número e não entra na lista de ilustrações."""
    return re.sub(r"[()\.\s]", "", s).lower() in (
        "continua", "continuacao", "continuação")


def _trunc(s: str, n: int = 170) -> str:
    s = s.strip()
    return s if len(s) <= n else s[:n - 1].rstrip() + "…"


def _refs_cap(s: str) -> str:
    """\\ref{capituloN} → N, como no PDF compilado (para exibição)."""
    return re.sub(r"~?\\(?:ref|cref|Cref|autoref|nameref)\{capitulo(\d+)\}", r" \1", s)


def _polish(s: str) -> str:
    """Acabamento tipográfico do texto extraído: travessões TeX, \\_ e espaços."""
    s = s.replace("---", "—").replace("--", "–").replace(r"\_", "_")
    s = re.sub(r"\s+([.,;:!?])", r"\1", s)
    return re.sub(r"\s+", " ", s).strip()


def _pre(s: str) -> str:
    """Remove ruído de LaTeX preservando caixa, acentos e hífens (para exibição)."""
    s = _refs_cap(s)
    s = re.sub(r"(?<!\\)%.*", "", s)                                   # comentários
    s = re.sub(r"\\(begin|end)\{[^}]*\}", " ", s)                      # ambientes
    s = re.sub(r"\\label\{[^}]*\}", " ", s)
    s = re.sub(r"\\(ref|cref|Cref|autoref|eqref|pageref|nameref)\{[^}]*\}", " ", s)
    s = re.sub(r"\\(parencite|textcite|cite[a-zA-Z]*)\*?(?:\[[^\]]*\])*\{[^}]*\}", " ", s)
    s = re.sub(r"\\includegraphics(?:\[[^\]]*\])?\{[^}]*\}", " ", s)
    s = re.sub(r"\\footnote\{[^{}]*\}", " ", s)
    s = re.sub(r"\\(selectlanguage|setstretch|setlength)\{[^}]*\}", " ", s)
    s = re.sub(r"\\(begingroup|endgroup|noindent|large|Large|centering|small|par)\b", " ", s)
    return s


def first_sentence(tex_segment: str) -> str:
    """Primeira frase de prosa de um trecho .tex (para nota de seção)."""
    txt = _polish(clean_title(_pre(tex_segment)))
    m = re.search(r"(.+?[.!?])(\s|$)", txt)
    sent = (m.group(1) if m else txt)
    return _trunc(sent, 180)


def parse_outline(tex: str) -> list[dict]:
    """Seções (com subseções e nota de 1ª frase), na ordem do documento."""
    secs: list[dict] = []
    seen = False
    matches = list(SEC_RE.finditer(tex))
    for idx, m in enumerate(matches):
        kind = m.group(1)
        arg, nxt = _match_brace_arg(tex, m.end() - 1)
        title = clean_title(arg)
        if not title:
            continue
        # trecho até o próximo section/subsection → nota (1ª frase)
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(tex)
        body = tex[nxt:end]
        # corta no primeiro ambiente para evitar legendas como "nota"
        cut = re.search(r"\\begin\{(figure|table|longtable|itemize|enumerate)", body)
        if cut:
            body = body[:cut.start()]
        nota = first_sentence(body)
        if kind == "section" or not seen:
            seen = seen or kind == "section"
            secs.append({"t": title, "nota": nota, "subs": []})
        else:
            if secs:
                secs[-1]["subs"].append(title)
    return secs


def parse_captions(tex: str):
    """(figuras, tabelas): legendas na ordem do documento, por ambiente."""
    figs, tabs = [], []
    stack = []
    last_img = None   # último \includegraphics do ambiente figure corrente
    for m in ENV_RE.finditer(tex):
        g = m.group(0)
        if g.startswith(r"\begin"):
            stack.append(m.group(1))
            last_img = None
        elif g.startswith(r"\end"):
            if stack:
                stack.pop()
            last_img = None
        elif g.startswith(r"\includegraphics"):
            last_img = m.group(3)
        else:  # \caption
            short = m.group(4)
            if short is not None and short.strip() == "":
                # \caption[]{...}: entrada vazia na lista de ilustrações
                # (típico de continuação de longtable) — não listar.
                continue
            arg, _ = _match_brace_arg(tex, m.end() - 1)
            cap = (_polish(clean_title(_refs_cap(short))) if short
                   else _trunc(_polish(clean_title(_refs_cap(arg)))))
            if not cap or _is_continuation(cap):
                continue
            link_m = MERMAID_RE.search(arg)
            link = link_m.group(0) if link_m else None
            env = stack[-1] if stack else "figure"
            img = None if env in ("table", "longtable") else _site_image(last_img)
            (tabs if env in ("table", "longtable") else figs).append((cap, link, img))
    return figs, tabs


def parse_resumo(src: Path):
    raw = src.read_text(encoding="utf-8")
    clean = _polish(clean_title(_pre(raw)))
    parts = re.split(r"Palavras[\s-]*chave\s*:?\s*", clean, maxsplit=1)
    resumo = re.sub(r"^Resumo\s+", "", parts[0].strip())
    palavras = []
    if len(parts) > 1:
        kw = parts[1].split(".")[0]   # só a frase das palavras-chave
        palavras = [k.strip() for k in re.split(r"[,;]", kw) if k.strip()]
    return resumo, palavras


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-root", type=Path, default=Path("/tmp/tese"))
    ap.add_argument("--out", type=Path, default=THIS_DIR / "tese_documento.json")
    ap.add_argument("--inject", type=Path, default=None)
    args = ap.parse_args()

    resumo, palavras = parse_resumo(args.source_root / "resumo.tex")

    sumario, figuras, tabelas = [], [], []
    fign = tabn = 0
    for fname, num, title, resumo_cap, conclusao_cap in CHAPTERS:
        src = args.source_root / fname
        if not src.exists():
            print(f"[doc] aviso: {fname} ausente, pulando.")
            continue
        tex = src.read_text(encoding="utf-8")
        sumario.append({
            "id": fname.replace("ex_", "").replace(".tex", ""),
            "num": num, "title": parse_chapter_title(tex, title),
            "resumo": resumo_cap,
            "conclusao": conclusao_cap,
            "sections": parse_outline(tex),
        })
        f, t = parse_captions(tex)
        for c, link, img in f:
            fign += 1
            entry = {"n": fign, "cap": num or title, "t": c}
            if link:
                entry["link"] = link
            if img:
                entry["img"] = img
            figuras.append(entry)
        for c, _link, _img in t:
            tabn += 1
            tabelas.append({"n": tabn, "cap": num or title, "t": c})

    payload = {
        "tese": TESE,
        "resumo": resumo,
        "palavras_chave": palavras,
        "sumario": sumario,
        "figuras": figuras,
        "tabelas": tabelas,
    }
    data_str = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    args.out.write_text(data_str, encoding="utf-8")
    print(f"[doc] JSON: {args.out} ({args.out.stat().st_size/1024:.0f} KB) | "
          f"resumo={len(resumo)}c · {len(palavras)} palavras-chave · "
          f"{len(sumario)} capítulos · {len(figuras)} figuras · {len(tabelas)} tabelas")

    if args.inject is not None:
        assert "</script" not in data_str.lower()
        html = args.inject.read_text(encoding="utf-8")
        pat = re.compile(r'(<script type="application/json" id="docdata">).*?(</script>)', re.DOTALL)
        new, n = pat.subn(lambda m: m.group(1) + data_str + m.group(2), html, count=1)
        if n != 1:
            print(f"[doc] ERRO: <script id=docdata> não encontrado em {args.inject}")
            return 1
        args.inject.write_text(new, encoding="utf-8")
        print(f"[doc] reinjetado em {args.inject}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
