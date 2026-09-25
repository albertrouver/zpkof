# Ticket de Caisse Casino

Un jeu-quiz qui fait reconstituer, rayon par rayon, la **fiche d'identité du Groupe Casino**.
Chaque bonne réponse s'imprime sur un ticket de caisse ; à la fin, le ticket est édité
et la fiche complète s'affiche, prête à être recopiée dans un dossier d'entreprise.

Page unique, sans dépendance ni build : ouvrez `index.html` dans un navigateur.

## Les six rayons

| # | Rayon | Mécanique | Points |
|---|-------|-----------|--------|
| 1 | Secteur & positionnement | cases à cocher (vrai / faux) | 15 |
| 2 | Le portefeuille d'enseignes | tri « avant 2024 » / « depuis 2025-26 » | 24 |
| 3 | Le chiffre d'affaires | deux curseurs à placer, tolérance ± 0,5 Md€ | 16 |
| 4 | Les valeurs de l'enseigne | 4 étiquettes à retrouver parmi 8 | 16 |
| 5 | La politique RSE | 4 piliers à retrouver parmi 8 | 16 |
| 6 | La restructuration de 2024 | chronologie à remettre dans l'ordre | 13 |

Total : 100 points, convertis en mention (de « stagiaire, à revoir » à « direction générale »).

Un **mode révision**, accessible depuis l'accueil, affiche la fiche complète sans jeu ni score.

## Contenu pédagogique

Les réponses attendues suivent les données du cours :

- **Secteur** — grande distribution alimentaire, recentrage *exclusif* sur le commerce de proximité.
- **Enseignes** — Géant, Monoprix, Casino, Franprix, Spar avant 2024 ; Cdiscount, Vival, Naturalia depuis 2025-2026.
- **Chiffre d'affaires** — environ 9,4 Md€ en 2022-2023, 1,4 Md€ en 2025, soit une baisse d'environ 85 %.
- **Valeurs** — intégrité, équité, honnêteté, qualité de service.
- **RSE** — proximité, climat, nutrition, solidarités.
- **Actualité** — crise de 2023, restructuration financière concrétisée en mars 2024 par le passage sous
  le contrôle de nouveaux repreneurs, transformation stratégique depuis.

Chaque correction ajoute un « repère pour votre dossier » : la nuance d'analyse qu'un correcteur attend
(le changement de périmètre derrière la chute du chiffre d'affaires, la séquence d'une restructuration,
la symétrie entre positionnement commercial et premier pilier RSE).

## Structure du dépôt

```
index.html          le jeu, autonome (HTML + CSS + JS en un seul fichier)
outils/fragment.py  extrait de index.html la version publiable comme Artifact
algator37/          ALGATOR37 — THE GAME, un autre jeu autonome (voir algator37/README.md)
```

Les marqueurs `<!-- A1 -->` … `<!-- A4 -->` dans `index.html` délimitent ce que le script extrait :
l'hôte des Artifacts fournit lui-même le squelette `<html>`/`<head>`/`<body>`.

## Avertissement

Exercice pédagogique construit à partir de données de cours. Ce dépôt n'est ni édité ni approuvé par
le Groupe Casino et ne reproduit aucun de ses éléments de marque. Les chiffres sont des ordres de
grandeur, à vérifier dans les documents financiers de l'entreprise avant tout usage en dossier noté.
