# Site atelierelma.com — maquette

Site statique (HTML + CSS, sans framework ni CMS). Aucune dépendance à installer pour l'héberger.

## Structure
- `index.html`, `projets.html`, `atelier.html`, `expertises.html`, `contact.html`, `mentions-legales.html` : pages
- `projets/*.html` : une fiche par projet
- `agences.html` : univers séparé pour les agences d'architecture (lien en pied de page)
- `assets/css/style.css` : mise en page ; `assets/css/fonts.css` : polices
- `assets/fonts/` : HarmonyOS Sans (sous-ensemble latin, woff2)
- `assets/img/projets/<projet>/` : images optimisées (1800 px max) + vignettes `-thumb`
- `assets/img/logo/` : logos détourés (noir et blanc)
- `outils/generer.py` : générateur des pages HTML

## Modifier le contenu
Tout le texte (projets, missions, coordonnées) est dans `outils/generer.py`, en tête de fichier.
Après modification :
```
cd SITE-WORKSPACE
python3 outils/generer.py
```
Ne pas éditer les `.html` à la main : ils sont régénérés.

## Voir le site en local
```
cd SITE-WORKSPACE
python3 -m http.server 8000
```
puis ouvrir http://localhost:8000

## Ajouter un projet
1. Déposer les images dans `assets/img/projets/<slug>/` (une image `-thumb.jpg` 900×675 pour la grille)
2. Ajouter une entrée dans `PROJETS` de `outils/generer.py`
3. Régénérer

## Mise en ligne (à venir)
Hébergement statique gratuit (Cloudflare Pages ou GitHub Pages), DNS pointés depuis Gandi.
