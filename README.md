# Site atelierelma.com

Site de l'Atelier ELMA. Site statique (HTML, CSS, JavaScript), sans framework ni CMS : rien à installer pour l'héberger.

- **Prévisualisation en ligne** (mise à jour automatiquement à chaque modification fusionnée) : https://youkssek.github.io/atelierelma-site/
- **Dépôt** : https://github.com/Youkssek/atelierelma-site

## Où est quoi

| Vous voulez… | Fichier |
|---|---|
| Modifier un texte (projets, expertises, atelier, contact) | `outils/generer.py`, tout en haut du fichier |
| Ajouter ou remplacer une photo de projet | `assets/img/projets/<nom-du-projet>/` |
| Changer les couleurs, les polices, la mise en page | `assets/css/style.css` |
| Modifier une animation | `assets/js/main.js` |

Les fichiers `.html` sont **générés** : ne pas les modifier à la main, ils sont écrasés à chaque génération.

## Modifier le site en 4 étapes

1. Ouvrir le dossier du dépôt sur son ordinateur (voir « Installer » ci-dessous).
2. Modifier `outils/generer.py` ou les images.
3. Régénérer les pages, dans un terminal ouvert à la racine du dossier :
   ```
   python3 outils/generer.py
   ```
4. Vérifier en local, puis envoyer :
   ```
   python3 -m http.server 8000      # puis ouvrir http://localhost:8000
   git add -A
   git commit -m "Ce que j'ai changé"
   git push
   ```
   Une à deux minutes plus tard, la prévisualisation en ligne est à jour.

Avec Claude Code, les étapes 2 à 4 se font en le demandant en français.

## Installer (une seule fois)

1. Créer un compte sur github.com et demander à être ajouté au dépôt.
2. Installer Git : sur Mac, ouvrir le Terminal et taper `git`, macOS propose l'installation.
3. Récupérer le site :
   ```
   git clone https://github.com/Youkssek/atelierelma-site.git
   cd atelierelma-site
   ```
4. Python 3 est déjà présent sur Mac. Aucune autre installation.

## Ajouter un projet

1. Créer `assets/img/projets/<slug>/` avec les images (JPEG, 1800 px de large maximum) et une vignette `NN-nom-thumb.jpg` en 900×675 pour la grille.
2. Ajouter une entrée dans la liste `PROJETS` de `outils/generer.py` en copiant un projet existant.
3. Régénérer, vérifier, envoyer.

## Structure

- `index.html`, `projets.html`, `expertises.html`, `atelier.html`, `contact.html`, `mentions-legales.html` : pages du site
- `projets/*.html` : une fiche par projet
- `agences.html` : offre dédiée aux agences d'architecture, univers séparé, lien discret en pied de page
- `assets/fonts/` : HarmonyOS Sans (sous-ensemble latin, woff2)
- `assets/img/logo/` : logos détourés, noir et blanc
- `outils/generer.py` : générateur des pages

## Mise en ligne sur atelierelma.com (plus tard)

Le domaine est chez Gandi. Quand le site sera prêt : ajouter le fichier `CNAME` contenant `atelierelma.com`, puis chez Gandi pointer `www` en CNAME vers `youkssek.github.io` et l'apex `@` vers les adresses IP de GitHub Pages. HTTPS est automatique.
