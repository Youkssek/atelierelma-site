#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur du site atelierelma.com (site statique, sans dépendance).
Usage : python3 outils/generer.py   (depuis le dossier SITE-WORKSPACE)
Tout le contenu éditable est dans les dictionnaires ci-dessous.
"""
import os, html

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ------------------------------------------------------------------ CONTENU
AGENCE = {
    "nom": "Atelier ELMA",
    "email": "contact@atelierelma.com",
    "siret": "980 273 403 00017",
    "ape": "7410Z",
    "personnes": [
        {"nom": "Clara Marquet", "titre": "Architecte HMONP, cofondatrice", "tel": "06 83 80 44 77"},
        {"nom": "Youssef El Kholfi", "titre": "Architecte HMONP, cofondateur", "tel": "06 60 70 33 54"},
    ],
}

HERO = {
    "titre": "L’espace comme une œuvre à habiter",
    "sous": "Atelier d’architecture et d’architecture d’intérieur, entre Paris et Rabat. "
            "Appartements, maisons, boutiques et restaurants : nous dessinons des lieux justes et lumineux pour ceux qui les habitent.",
}

MANIFESTE = ("Nous croyons que la lumière fait l’espace, que le sur-mesure fait le caractère "
             "et que les matières vraies font la durée. Chaque projet commence par une écoute : "
             "votre lieu, vos usages, votre budget. Puis nous dessinons, jusqu’au dernier détail.")

MARQUEE = ["Rénovation d’appartement", "Autorisations administratives", "Étude de faisabilité", "Extension",
           "Locaux commerciaux", "Mobilier sur mesure", "Images 3D"]

MONDES = [
    {
        "id": "particuliers", "eyebrow": "Particuliers & commerçants", "titre": "Habiter, exercer",
        "intro": "Vous avez un appartement à repenser, un local à ouvrir, une maison à agrandir ou un bien à évaluer avant d’acheter. Nous prenons le projet du premier croquis au dossier déposé en mairie.",
        "image": ("appartement-trousseau", "01-salon"),
        "items": [
            ("Rénovation d’appartement",
             "Réorganiser le plan, faire entrer la lumière, dessiner la cuisine et les rangements : nous concevons l’appartement dans son ensemble, avec des plans précis et des images pour décider.",
             ["Plans", "Images 3D", "Mobilier sur mesure", "Matériaux"], ("appartement-trousseau", "02-salle-a-manger")),
            ("Autorisations administratives",
             "Déclaration préalable, permis de construire, changement de destination, devanture de local commercial, extension ou surélévation de maison : nous constituons le dossier, le déposons et dialoguons avec la mairie jusqu’à l’accord.",
             ["Déclaration préalable", "Permis de construire", "Locaux commerciaux", "Copropriété"], ("maison-salengro", "02-sejour")),
            ("Étude de faisabilité",
             "Avant d’acheter ou de vous engager : ce que les règles d’urbanisme autorisent, ce que la structure permet, ce que le projet coûtera. Une réponse claire, chiffrée, en quelques semaines.",
             ["Urbanisme", "Potentiel", "Budget", "Avant achat"], ("appartement-dormoy", "01-plan")),
            ("Extension, maison & locaux",
             "Agrandir une maison, surélever, transformer un garage, aménager une boutique ou un restaurant : nous dessinons le projet et gérons son autorisation.",
             ["Extension", "Surélévation", "Boutique", "Restaurant"], ("maison-el-guettar", "01-sejour")),
        ],
    },
    {
        "id": "agences", "eyebrow": "Agences d’architecture", "titre": "En renfort des agences",
        "intro": "Concours, phases études, dossiers de permis : nous mettons nos outils et notre production au service des agences, sur site ou à distance, dans vos délais.",
        "image": ("appartement-dormoy", "01-plan"),
        "items": [
            ("Modélisation 3D & BIM",
             "Maquette numérique sur Archicad, gabarits et bibliothèques d’objets, mise en cohérence des modèles : une maquette propre, exploitable par toute l’équipe.",
             ["Archicad", "Maquette numérique", "Gabarits", "Bibliothèques"], ("maison-el-guettar", "02-chambre")),
            ("Images de synthèse",
             "Perspectives de concours, insertions dans le site, vues intérieures et planches matières : des images qui racontent le projet, produites dans vos délais.",
             ["Perspectives", "Insertions", "Vues intérieures", "Planches"], ("maison-salengro", "01-cuisine")),
            ("Phase études",
             "Esquisse, APS, APD, PC, PRO : nous renforçons votre équipe en production graphique, dessin de détails et montage de dossiers.",
             ["ESQ à PRO", "Plans, coupes, façades", "Détails", "Dossiers PC"], ("appartement-cauvin", "03-cuisine")),
            ("Concours & dossiers",
             "Panneaux, notices, maquettes physiques, préparation des auditions : nous prenons en charge la production d’un rendu complet.",
             ["Panneaux", "Notices", "Maquettes", "Auditions"], ("maison-el-guettar", "03-materiaux")),
        ],
    },
]

ETAPES = [
    ("Rencontre", "Une première visite du lieu pour comprendre vos envies, vos usages et votre budget."),
    ("Esquisse", "Deux ou trois pistes dessinées en plan et en volume. On choisit ensemble la bonne direction."),
    ("Projet", "Plans, perspectives 3D, matériaux et mobilier sur mesure : le projet prend forme dans le détail."),
    ("Dossier", "Autorisations administratives, plans détaillés et estimation : tout est prêt pour passer à la suite."),
]

VALEURS = [
    ("La lumière d’abord", "Orientation, ouvertures, plafonds, reflets : nous travaillons la lumière avant le mobilier. C’est elle qui fait l’espace."),
    ("Le sur-mesure", "Une bibliothèque qui épouse un mur en biais, une tête de lit qui range : le mobilier dessiné donne à chaque lieu son caractère."),
    ("Des matières vraies", "Bois massif, terrazzo, pierre, cannage, peintures minérales : des matériaux qui vieillissent bien et se touchent avec plaisir."),
]

PROJETS = [
    {
        "slug": "appartement-trousseau",
        "nom": "Appartement Trousseau", "lieu": "Paris 11e",
        "type": "Rénovation d’un appartement haussmannien", "surface": "115 m²",
        "mission": "Architecture d’intérieur, mobilier, images 3D",
        "accroche": "Un haussmannien révélé",
        "resume": "Boiseries teintées d’un bleu profond, parquet à chevrons restauré, mobilier aux lignes simples : l’appartement retrouve son caractère, sans nostalgie.",
        "texte": [
            "Les moulures, la cheminée et le parquet étaient là. Nous les avons gardés et mis en tension avec une teinte profonde sur les boiseries du salon, qui donne de la présence aux volumes et fait ressortir la blancheur des plafonds.",
            "Dans les pièces de réception, le mobilier reste discret : lignes droites, bois blond, textiles clairs. Quelques touches d’ocre réchauffent l’ensemble. La cuisine reprend la teinte des boiseries pour ne faire qu’un avec le séjour.",
            "La chambre suit une autre logique : palette neutre, matières naturelles, lumière filtrée. Un espace de repos, simplement.",
        ],
        "hero": "01-salon",
        "figures": [
            ("02-salle-a-manger", "La salle à manger, entre boiseries sombres et parquet clair"),
            ("03-chambre", "La chambre, palette neutre et lumière filtrée"),
            ("04-cuisine", "La cuisine, dans la teinte des boiseries du salon"),
        ],
    },
    {
        "slug": "maison-el-guettar",
        "nom": "Maison Mori", "lieu": "El Guettar, Tunisie",
        "type": "Construction d’une maison familiale", "surface": "135 m²",
        "mission": "Conception, plans, images 3D, planches matières",
        "accroche": "Une maison ouverte sur les montagnes",
        "resume": "Des terrasses à chaque pièce de vie, une verrière courbe entre cuisine et séjour, et des matières chaudes : bois, pierre, marbre, cannage.",
        "texte": [
            "La maison s’installe dans un quartier résidentiel récent d’El Guettar. Chaque pièce de vie et chaque chambre ouvre sur une terrasse, pour suivre le soleil au fil de la journée et garder la vue sur les montagnes.",
            "À l’intérieur, la cheminée est le point fixe autour duquel le séjour s’organise. Une verrière courbe sépare la cuisine sans la fermer. L’entrée et la buanderie forment un seul meuble menuisé, qui range et accueille la bibliothèque.",
            "Les matières font le reste : bois, pierre, marbre et cannage, choisis sur planche avec la famille, pour une maison contemporaine et chaleureuse.",
        ],
        "hero": "01-sejour",
        "figures": [
            ("02-chambre", "La suite parentale, avec salle de bain et dressing"),
            ("03-materiaux", "Planche matières : couleurs, matériaux et équipements"),
        ],
    },
    {
        "slug": "maison-salengro",
        "nom": "Maison Salengro", "lieu": "Le Mans",
        "type": "Transformation d’un garage en maison", "surface": "85 m²",
        "mission": "Conception, plans, autorisations, mobilier sur mesure",
        "accroche": "Un garage devenu maison",
        "resume": "Une véranda vers le jardin, une verrière au cœur du plan et une cuisine en bois et terrazzo : le garage et sa dépendance deviennent une maison familiale.",
        "texte": [
            "Le point de départ : un garage et sa dépendance, tout en longueur. Nous avons ouvert la pièce principale sur le jardin par une véranda et percé une verrière au centre du plan pour faire entrer la lumière là où elle manquait.",
            "La cuisine est compacte et dessinée au millimètre : façades en bois, plan de travail et table en terrazzo. La partie nuit, à l’écart, reste calme.",
            "Dans la chambre des enfants, un meuble-lit en hauteur libère le sol pour le jeu et range en dessous. Une petite maison pensée pour grandir.",
        ],
        "hero": "01-cuisine",
        "figures": [
            ("02-sejour", "Le séjour, tout en longueur, tourné vers la véranda et le jardin"),
            ("03-chambre-enfants", "La chambre des enfants et son meuble-lit sur mesure"),
            ("04-chambre-parents", "La chambre parentale et son rangement intégré"),
        ],
    },
    {
        "slug": "appartement-cauvin",
        "nom": "Appartement Cauvin", "lieu": "Le Mans",
        "type": "Rénovation d’un appartement sous les toits", "surface": "75 m²",
        "mission": "Architecture d’intérieur, mobilier sur mesure",
        "accroche": "Deux orientations, deux ambiances",
        "resume": "Un salon cocon au nord, une chambre fraîche au sud : les couleurs suivent la lumière, et les rangements épousent les pentes du toit.",
        "texte": [
            "Le plan est simple : un salon exposé au nord, une chambre plein sud. Nous avons laissé la lumière décider des couleurs.",
            "Côté salon, une grande bibliothèque terracotta enveloppe le mur, accueille la télévision et les livres, et donne à la pièce une atmosphère de cocon.",
            "Côté chambre, une palette plus fraîche. Les murs en biais et les recoins sous la pente sont transformés en placards sur mesure, intégrés à une tête de lit.",
        ],
        "hero": "01-salon",
        "figures": [
            ("02-chambre", "La chambre : les recoins sous pente deviennent des placards, intégrés à la tête de lit"),
            ("03-cuisine", "La cuisine, dans la continuité chromatique du salon"),
        ],
    },
    {
        "slug": "appartement-dormoy",
        "nom": "Appartement Dormoy", "lieu": "Fontenay-aux-Roses",
        "type": "Aménagement d’un appartement", "surface": "80 m²",
        "mission": "Architecture d’intérieur, plans d’aménagement",
        "accroche": "Le bois et la lumière",
        "resume": "Des faux plafonds rétro-éclairés et un claustra en tasseaux redessinent un appartement familial, plus lumineux et plus chaleureux.",
        "texte": [
            "L’appartement manquait de relief. Nous avons redessiné les plafonds : des faux plafonds équipés d’éclairages intégrés diffusent une lumière douce et uniforme, et donnent une nouvelle lecture des pièces.",
            "Un claustra en tasseaux de bois sépare le séjour de la cuisine sans les fermer. Le même bois habille le mur du salon et unifie l’ensemble.",
            "Le plan d’aménagement, avec l’implantation électrique, a servi de base à toutes les entreprises.",
        ],
        "hero": "02-sejour",
        "figures": [
            ("01-plan", "Plan d’aménagement, avec la nouvelle implantation électrique"),
        ],
    },
]

NAV = [("projets.html", "Projets"), ("expertises.html", "Expertises"),
       ("atelier.html", "L’atelier"), ("contact.html", "Contact")]

# ------------------------------------------------------------------ GABARIT
def e(s): return html.escape(s, quote=True)

def page(titre, corps, base="", courant="", description="", over=False, loader=False, nav_items=None, body_class=""):
    nav = "".join(
        f'<li><a href="{base}{href}"{" aria-current=\"page\"" if href == courant else ""}>{e(lbl)}</a></li>'
        for href, lbl in (nav_items or NAV))
    desc = e(description or HERO["sous"])
    tel = "".join(f'<p>{e(p["nom"])}<br><span>{e(p["titre"])}</span></p>' for p in AGENCE["personnes"])
    ld = f'<div id="loader" aria-hidden="true"><div class="in"><img src="{base}assets/img/logo/logo-atelier-elma-blanc.png" alt=""><i></i></div></div>' if loader else ""
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(titre)}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{base}assets/img/logo/logo-monogramme.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jost:wght@300;400;500&family=Instrument+Serif:ital@1&display=swap">
<link rel="stylesheet" href="{base}assets/css/fonts.css">
<link rel="stylesheet" href="{base}assets/css/style.css">
</head>
<body class="{body_class}">
{ld}
<div id="veil" aria-hidden="true"></div>
<header class="site-header{' over' if over else ''}">
  <div class="wrap">
    <a class="brand" href="{base}index.html" aria-label="Atelier ELMA, accueil">
      <img class="on-light" src="{base}assets/img/logo/logo-atelier-elma.png" alt="atelier elma">
      <img class="on-dark" src="{base}assets/img/logo/logo-atelier-elma-blanc.png" alt="">
    </a>
    <button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
    <ul class="nav" id="nav">{nav}</ul>
  </div>
</header>
<main>
{corps}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div><img src="{base}assets/img/logo/logo-elma-blanc.png" alt="elma"></div>
    <div>{tel}</div>
    <div><p><a href="mailto:{AGENCE["email"]}">{AGENCE["email"]}</a></p><p><a href="{base}contact.html">Nous écrire</a></p></div>
    <div><p><a href="{base}projets.html">Projets</a></p><p><a href="{base}expertises.html">Expertises</a></p><p><a href="{base}atelier.html">L’atelier</a></p><p style="margin-top:.8em"><a href="{base}agences.html" class="muted">Vous êtes une agence d’architecture ?</a></p></div>
    <div class="legal"><span>© 2026 {e(AGENCE["nom"])}</span><span>SIRET {AGENCE["siret"]}</span><span>APE {AGENCE["ape"]}</span><a href="{base}mentions-legales.html">Mentions légales</a></div>
  </div>
</footer>
<script src="{base}assets/js/main.js"></script>
</body>
</html>
"""

def img(p, nom, base="", thumb=False):
    return f'{base}assets/img/projets/{p["slug"]}/{nom}{"-thumb" if thumb else ""}.jpg'

def cta(base=""):
    return f"""<section class="cta"><div class="wrap">
  <h2 class="h-l reveal">Un lieu à transformer&nbsp;? <em class="serif">Parlons-en.</em></h2>
  <a class="btn light reveal" style="--i:2" href="{base}contact.html">Nous écrire <span aria-hidden="true">→</span></a>
</div></section>"""

def feat(p, cls, base="", i=0):
    return f"""<article class="feat {cls}">
  <a class="media-box img-reveal tilt" href="{base}projets/{p["slug"]}.html" data-parallax data-cursor="Voir"><img src="{img(p, p["hero"], base)}" alt="{e(p["nom"])}, {e(p["lieu"])}" loading="lazy"></a>
  <div class="cap reveal"><p class="eyebrow">{e(p["lieu"])}</p><h3>{e(p["nom"])}</h3><p>{e(p["type"])} · {e(p["surface"])}</p><a class="link" href="{base}projets/{p["slug"]}.html">Voir le projet</a></div>
</article>"""

# ------------------------------------------------------------------ PAGES
def accueil():
    v = PROJETS[0]
    marq = "".join(f"<span>{e(m)}</span>" for m in MARQUEE) * 2
    feats = feat(PROJETS[1], "wide") + feat(PROJETS[3], "narrow") + feat(PROJETS[2], "mid")
    steps = "".join(f'<div class="step reveal" style="--i:{i}"><div class="n">0{i+1}</div><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i, (t, d) in enumerate(ETAPES))
    items = MONDES[0]["items"]
    xp_rows = "".join(f'<li class="reveal" style="--i:{i}" data-media="{i}"><a href="expertises.html#particuliers"><span class="num">0{i+1}</span><span class="t"><h3>{e(t)}</h3><p>{e(tags[0])} · {e(tags[1])} · {e(tags[2])}</p></span><span class="arrow" aria-hidden="true">→</span></a></li>' for i, (t, d, tags, im) in enumerate(items))
    xp_media = "".join(f'<img src="{img({"slug": im[0]}, im[1])}" alt="" data-i="{i}" class="{"on" if i == 0 else ""}" loading="lazy">' for i, (t, d, tags, im) in enumerate(items))
    corps = f"""
<section class="hero" data-src="{img(v, v["hero"])}" data-alt="{e(v["nom"])}, {e(v["lieu"])}">
  <div class="frame"></div>
  <div class="wrap">
    <p class="eyebrow" style="color:rgba(250,249,246,.8)">Atelier d’architecture</p>
    <h1 class="h-xl" data-words>{e(HERO["titre"])}</h1>
    <div class="sub">
      <p class="lead">{e(HERO["sous"])}</p>
      <div class="scroll-hint"><i></i>Défiler</div>
    </div>
  </div>
</section>

<section class="manifesto"><div class="wrap grid-12">
  <p class="eyebrow">L’atelier</p>
  <p class="h-l words">{e(MANIFESTE)}</p>
</div></section>

<div class="marquee" aria-hidden="true"><div class="marquee__track">{marq}</div></div>

<section class="section selection"><div class="wrap">
  <div class="head"><h2 class="h-l reveal">Projets <em class="serif">choisis</em></h2><a class="link reveal" href="projets.html">Tous les projets</a></div>
  {feats}
</div></section>

<section class="section xp" style="background:var(--bg-2)"><div class="wrap grid-12">
  <div class="side"><div class="sticky"><p class="eyebrow reveal">Expertises</p><h2 class="h-l reveal">De l’idée au dossier <em class="serif">déposé</em></h2><p class="muted reveal" style="margin-top:1.2rem;max-width:36ch">Rénovation, autorisations, faisabilité, extension : une seule équipe, du premier croquis au dossier en mairie.</p><p class="reveal" style="margin-top:1.6rem"><a class="link" href="expertises.html">Toutes les expertises</a></p></div></div>
  <div class="list">
    <ul class="xp-list line-grow">{xp_rows}</ul>
  </div>
  <div class="xp-media reveal"><div class="media-box">{xp_media}</div></div>
</div></section>

<section class="section"><div class="wrap">
  <p class="eyebrow reveal">Comment nous travaillons</p>
  <h2 class="h-l reveal" style="max-width:18ch;margin-bottom:clamp(32px,4vw,56px)">Quatre étapes, un seul interlocuteur</h2>
  <div class="steps line-grow">{steps}</div>
</div></section>

<section class="section atelier-teaser" style="padding-top:0"><div class="wrap grid-12">
  <div class="media-box img-reveal" data-parallax><img src="{img(PROJETS[4], "02-sejour")}" alt="{e(PROJETS[4]["nom"])}" loading="lazy"></div>
  <div class="txt reveal"><p class="eyebrow">Qui sommes-nous</p><h2 class="h-m">Deux architectes, <em class="serif">un atelier</em></h2><p class="lead" style="margin-top:1.2rem">Clara Marquet et Youssef El Kholfi, architectes diplômés HMONP, ont fondé l’atelier entre Paris et Rabat pour dessiner des espaces à hauteur d’habitant : précis, chaleureux, faits pour durer.</p><p style="margin-top:1.6rem"><a class="btn" href="atelier.html">Découvrir l’atelier</a></p></div>
</div></section>
{cta()}
"""
    return page("Atelier ELMA", corps, courant="index.html", over=True, loader=True)

def projets():
    rows = "".join(
        f'<li><a href="projets/{p["slug"]}.html" data-img="{img(p, p["hero"], thumb=True)}"><span class="name">{e(p["nom"])}</span><span class="meta">{e(p["lieu"])}</span><span class="meta">{e(p["type"])}</span><span class="arrow" aria-hidden="true">→</span></a></li>'
        for p in PROJETS)
    grid = "".join(
        f'<a href="projets/{p["slug"]}.html" class="reveal"><div class="media-box"><img src="{img(p, p["hero"], thumb=True)}" alt="" loading="lazy"></div><h3>{e(p["nom"])}</h3><p class="muted small">{e(p["lieu"])} · {e(p["type"])}</p></a>'
        for p in PROJETS)
    corps = f"""
<section class="a-head section"><div class="wrap">
  <p class="eyebrow">Projets</p>
  <h1 class="h-xl" data-words>Lieux transformés</h1>
  <p class="lead reveal" style="margin-top:1.5rem">Appartements et maisons conçus par l’atelier, entre Paris, Rabat et le Mans. Survolez pour voir, cliquez pour entrer.</p>
</div></section>
<section class="wrap" style="padding-bottom:clamp(64px,9vw,140px)">
  <ul class="index reveal">{rows}</ul>
  <div class="index-grid">{grid}</div>
</section>
<div class="float-img" aria-hidden="true"><img src="" alt=""></div>
{cta()}
"""
    return page("Projets — Atelier ELMA", corps, courant="projets.html",
                description="Projets d’architecture d’intérieur et de rénovation conçus par Atelier ELMA.")

def fiche(i):
    p = PROJETS[i]; b = "../"; suiv = PROJETS[(i + 1) % len(PROJETS)]
    texte = "".join(f"<p>{e(t)}</p>" for t in p["texte"])
    figs = "".join(
        f'<figure class="reveal"><div class="media-box img-reveal" data-parallax><img src="{img(p, f, b)}" alt="{e(c)}" loading="lazy"></div><figcaption>{e(c)}</figcaption></figure>'
        for f, c in p["figures"])
    corps = f"""
<section class="p-head"><div class="wrap">
  <p class="eyebrow">{e(p["type"])}</p>
  <h1 class="h-xl" data-words>{e(p["accroche"])}</h1>
  <div class="p-facts reveal line-grow">
    <div><span class="k">Projet</span>{e(p["nom"])}</div>
    <div><span class="k">Lieu</span>{e(p["lieu"])}</div>
    <div><span class="k">Surface</span>{e(p["surface"])}</div>
    <div><span class="k">Mission</span>{e(p["mission"])}</div>
  </div>
</div></section>
<div class="wrap p-hero"><div class="media-box img-reveal tilt" data-parallax><img src="{img(p, p["hero"], b)}" alt="{e(p["nom"])}, {e(p["lieu"])}" fetchpriority="high"></div></div>
<section class="p-body"><div class="wrap grid-12">
  <div class="intro reveal"><h2>{e(p["resume"])}</h2></div>
  <div class="txt prose reveal" style="--i:2">{texte}</div>
</div></section>
<section class="wrap" style="padding-bottom:clamp(64px,9vw,140px)"><div class="gallery">{figs}</div></section>
<a class="next-project" href="{suiv["slug"]}.html">
  <div class="media" data-parallax><img src="{img(suiv, suiv["hero"], b)}" alt="" loading="lazy"></div>
  <div class="wrap"><p class="eyebrow">Projet suivant</p><h2 class="h-xl">{e(suiv["nom"])}</h2><p class="lead" style="color:rgba(250,249,246,.8);margin-top:.8rem">{e(suiv["lieu"])} · {e(suiv["type"])}</p></div>
</a>
"""
    return page(f'{p["nom"]} — Atelier ELMA', corps, base=b, courant="projets.html", description=p["resume"])

def expertises():
    m1, m2 = MONDES
    cards = "".join(
        f'<article class="stack-card" style="--k:{i}"><div class="txt"><div><div class="num">0{i+1}</div><h3>{e(t)}</h3><p style="margin-top:1rem">{e(d)}</p></div><div class="tags">{"".join(f"<span>{e(x)}</span>" for x in tags)}</div></div>'
        f'<div class="media-box"><img src="{img({"slug": im[0]}, im[1])}" alt="" loading="lazy"></div></article>'
        for i, (t, d, tags, im) in enumerate(m1["items"]))
    steps = "".join(f'<div class="step reveal" style="--i:{i}"><div class="n">0{i+1}</div><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i, (t, d) in enumerate(ETAPES))
    corps = f"""
<section class="x-head section" id="particuliers"><div class="wrap">
  <p class="eyebrow">Expertises</p>
  <h1 class="h-xl" data-words>{e(m1["titre"])}</h1>
  <p class="lead reveal" style="margin-top:1.5rem">{e(m1["intro"])}</p>
  <div class="stack">{cards}</div>
</div></section>
<section class="section" style="background:var(--bg-2)"><div class="wrap">
  <p class="eyebrow reveal">Comment nous travaillons</p>
  <h2 class="h-l reveal" style="max-width:18ch;margin-bottom:clamp(32px,4vw,56px)">Quatre étapes, un seul interlocuteur</h2>
  <div class="steps line-grow">{steps}</div>
</div></section>
{cta()}
<div class="wrap"><p class="small muted" style="padding-block:20px"><a href="agences.html">Vous êtes une agence d’architecture ? Notre offre dédiée →</a></p></div>
"""
    return page("Expertises — Atelier ELMA", corps, courant="expertises.html",
                description="Rénovation d’appartement, autorisations administratives, étude de faisabilité, extension, maison et locaux commerciaux.")

def agences():
    m2 = MONDES[1]
    panels = f'<div class="hs-panel intro"><p class="eyebrow">{e(m2["eyebrow"])}</p><h2 class="h-l">Ce que nous apportons</h2><p class="lead" style="margin-top:1rem;color:var(--ink-2)">Quatre façons de renforcer votre équipe, ponctuellement ou dans la durée.</p></div>' + "".join(
        f'<div class="hs-panel"><div class="num">0{i+1}</div><h3>{e(t)}</h3><p>{e(d)}</p><div class="media-box"><img src="{img({"slug": im[0]}, im[1])}" alt="" loading="lazy"></div><p class="small muted">{" · ".join(e(x) for x in tags)}</p></div>'
        for i, (t, d, tags, im) in enumerate(m2["items"]))
    nav = [("agences.html#offre", "L’offre"), ("agences.html#contact", "Nous solliciter"), ("index.html", "Le site de l’atelier")]
    corps = f"""
<section class="x-head section" style="padding-bottom:clamp(40px,5vw,72px)"><div class="wrap">
  <p class="eyebrow">{e(m2["eyebrow"])}</p>
  <h1 class="h-xl" data-words>{e(m2["titre"])}</h1>
  <div class="grid-12" style="margin-top:clamp(32px,4vw,56px)">
    <p class="lead reveal" style="grid-column:1/8">{e(m2["intro"])}</p>
    <div class="reveal" style="grid-column:9/13;--i:2"><p class="muted">Deux architectes HMONP formés en agence sur des équipements publics, des logements collectifs et des concours. Archicad, BIM, images, dossiers : nous parlons votre langue et tenons vos délais.</p></div>
  </div>
</div></section>
<section id="offre" class="hs">
  <div class="hs-sticky">
    <div class="hs-track">{panels}</div>
    <div class="hs-progress"><i></i></div>
  </div>
</section>
<section id="contact" class="section" style="border-top:1px solid var(--line)"><div class="wrap">
  <div class="grid-12">
    <div style="grid-column:1/7"><p class="eyebrow reveal">Nous solliciter</p><h2 class="h-l reveal">Envoyez-nous <em class="serif">votre brief</em></h2></div>
    <div class="reveal" style="grid-column:8/13;--i:2"><p class="muted">Un concours à rendre, une phase à absorber, une maquette à monter : décrivez le besoin, le délai et le format attendu. Nous répondons sous 48 heures avec une proposition.</p><p style="margin-top:1.6rem"><a class="btn light" href="mailto:{AGENCE["email"]}?subject=Brief%20agence">Écrire à l’atelier <span aria-hidden="true">→</span></a></p><p class="small muted" style="margin-top:1rem">{AGENCE["email"]}</p></div>
  </div>
</div></section>
"""
    return page("Pour les agences — Atelier ELMA", corps, courant="agences.html", nav_items=nav, body_class="page-dark",
                description="Atelier ELMA en renfort des agences d’architecture : modélisation 3D et BIM sur Archicad, images de synthèse, phase études, concours et dossiers.")

def atelier():
    gens = "".join(
        f'<div class="person reveal" style="--i:{i}"><div class="initials">{"".join(w[0] for w in x["nom"].split())}</div><h3>{e(x["nom"])}</h3><p>{e(x["titre"])}</p></div>'
        for i, x in enumerate(AGENCE["personnes"]))
    imgs = [("maison-el-guettar", "01-sejour"), ("appartement-cauvin", "02-chambre"), ("maison-salengro", "01-cuisine")]
    blocks = "".join(f'<div class="story-block" data-i="{i}"><div class="num">0{i+1}</div><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i, (t, d) in enumerate(VALEURS))
    media = "".join(f'<img src="{img({"slug": a}, b_)}" alt="" data-i="{i}" class="{"on" if i == 0 else ""}" loading="lazy">' for i, (a, b_) in enumerate(imgs))
    corps = f"""
<section class="a-head section"><div class="wrap">
  <p class="eyebrow">L’atelier</p>
  <h1 class="h-xl" data-words>Dessiner pour ceux qui habitent</h1>
  <div class="grid-12" style="margin-top:clamp(40px,5vw,72px)">
    <div class="prose reveal" style="grid-column:1/7">
      <p class="lead">Atelier ELMA est né de la rencontre de deux architectes diplômés HMONP, Clara Marquet et Youssef El Kholfi, et d’une conviction : l’architecture est un art qui se vit tous les jours, à hauteur d’habitant.</p>
      <p>Formés en agence sur des équipements publics et des logements collectifs, nous avons voulu retrouver le détail, le dialogue direct et le plaisir du projet mené de bout en bout. L’atelier travaille entre Paris et Rabat.</p>
      <p>Chaque lieu a déjà une histoire. Notre travail consiste à la lire, puis à la prolonger avec justesse.</p>
      <p class="small muted">Nous mettons aussi nos outils au service des agences d’architecture : <a href="agences.html" style="text-decoration:underline">voir l’offre dédiée</a>.</p>
    </div>
    <div class="media-box img-reveal" data-parallax style="grid-column:8/13;aspect-ratio:4/5"><img src="assets/img/projets/appartement-trousseau/03-chambre.jpg" alt="Appartement Trousseau, la chambre" loading="lazy"></div>
  </div>
  <div class="cities line-grow"><div><small>Atelier</small>Paris</div><div><small>Atelier</small>Rabat</div><div><small>Projets</small>France &amp; Maroc</div></div>
</div></section>

<section class="section" style="padding-top:0"><div class="wrap">
  <p class="eyebrow reveal">Ce qui guide chaque projet</p>
  <div class="story">
    <div class="story-blocks">{blocks}</div>
    <div class="story-media">{media}</div>
  </div>
</div></section>

<section class="section" style="padding-top:0"><div class="wrap">
  <p class="eyebrow reveal">Les fondateurs</p>
  <h2 class="h-l reveal">Deux architectes, <em class="serif">un atelier</em></h2>
  <div class="people">{gens}</div>
</div></section>
{cta()}
"""
    return page("L’atelier — Atelier ELMA", corps, courant="atelier.html",
                description="Atelier ELMA, atelier d’architecture fondé par Clara Marquet et Youssef El Kholfi, architectes HMONP, entre Paris et Rabat.")

def contact():
    tels = "".join(
        f'<li class="reveal" style="--i:{i+1}"><span class="label">{e(x["nom"])}</span><a href="tel:+33{x["tel"].replace(" ", "")[1:]}">{e(x["tel"])}</a></li>'
        for i, x in enumerate(AGENCE["personnes"]))
    corps = f"""
<section class="c-head section"><div class="wrap">
  <p class="eyebrow">Contact</p>
  <h1 class="h-xl" data-words>Parlons de votre lieu</h1>
  <div class="contact-grid">
    <div>
      <p class="lead reveal" style="margin-bottom:2rem">Décrivez-nous l’endroit, vos envies et votre calendrier. Nous vous répondons rapidement pour convenir d’une première visite.</p>
      <ul class="contact-list">
        <li class="reveal"><span class="label">E-mail</span><a href="mailto:{AGENCE["email"]}">{AGENCE["email"]}</a></li>
        {tels}
      </ul>
    </div>
    <form class="form reveal" style="--i:2" action="mailto:{AGENCE["email"]}" method="post" enctype="text/plain">
      <div class="field"><label for="nom">Nom</label><input id="nom" name="nom" type="text" autocomplete="name" required></div>
      <div class="field"><label for="email">E-mail</label><input id="email" name="email" type="email" autocomplete="email" required></div>
      <div class="field"><label for="type">Type de projet</label>
        <select id="type" name="type"><option>Rénovation d’appartement</option><option>Rénovation de maison</option><option>Extension ou surélévation</option><option>Construction neuve</option><option>Local commercial</option><option>Autorisation administrative</option><option>Étude de faisabilité</option><option>Autre</option></select></div>
      <div class="field"><label for="lieu">Lieu du projet</label><input id="lieu" name="lieu" type="text"></div>
      <div class="field"><label for="message">Votre projet</label><textarea id="message" name="message" required></textarea></div>
      <div><button class="btn" type="submit">Envoyer <span aria-hidden="true">→</span></button></div>
      <p class="form-note">Le formulaire ouvre votre messagerie. Un envoi direct sera mis en place avec l’hébergement.</p>
    </form>
  </div>
</div></section>
"""
    return page("Contact — Atelier ELMA", corps, courant="contact.html",
                description="Contacter Atelier ELMA pour un projet de rénovation, d’aménagement ou d’extension.")

def mentions():
    corps = f"""
<section class="section legal-page"><div class="wrap prose">
  <p class="eyebrow">Informations légales</p>
  <h1 class="h-l">Mentions légales</h1>
  <h2>Éditeur du site</h2>
  <p>{e(AGENCE["nom"])} — SIRET {AGENCE["siret"]} — Code APE {AGENCE["ape"]}<br>Contact : <a href="mailto:{AGENCE["email"]}">{AGENCE["email"]}</a></p>
  <p>Architectes inscrits à l’Ordre des architectes : <em>numéros d’inscription et assurance professionnelle à compléter</em>.</p>
  <h2>Hébergement</h2><p><em>À compléter selon l’hébergeur retenu.</em></p>
  <h2>Propriété intellectuelle</h2>
  <p>Textes, plans, images de synthèse et photographies présentés sur ce site sont la propriété d’{e(AGENCE["nom"])} ou de leurs auteurs. Toute reproduction est soumise à autorisation.</p>
  <h2>Données personnelles</h2>
  <p>Les informations transmises via le formulaire de contact servent uniquement à répondre à votre demande. Aucun outil de suivi ni cookie publicitaire n’est utilisé.</p>
</div></section>
"""
    return page("Mentions légales — Atelier ELMA", corps)

# ------------------------------------------------------------------ ÉCRITURE
def ecrire(chemin, contenu):
    chemin = os.path.join(RACINE, chemin)
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(contenu)
    print("écrit", os.path.relpath(chemin, RACINE))

if __name__ == "__main__":
    ecrire("index.html", accueil())
    ecrire("projets.html", projets())
    for i in range(len(PROJETS)):
        ecrire(f"projets/{PROJETS[i]['slug']}.html", fiche(i))
    ecrire("expertises.html", expertises())
    ecrire("agences.html", agences())
    ecrire("atelier.html", atelier())
    ecrire("contact.html", contact())
    ecrire("mentions-legales.html", mentions())
