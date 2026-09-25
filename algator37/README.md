# ALGATOR37 — THE GAME

Un jeu d'aventure et d'exploration jouable dans le navigateur, entièrement consacré à l'univers
d'Algator37. On y retrouve ses vidéos, ses jeux, ses musiques, ses maps, ses amis… et beaucoup de chats.

> Titre proposé : **« Algator37 : L'Odyssée du Multivers »**. Le nom provisoire
> *ALGATOR37 — THE GAME* est conservé dans le code tant qu'aucun autre titre n'est choisi.

## Lancer le jeu

Ouvre `index.html` dans un navigateur récent (Chrome, Edge, Firefox ou Safari), sur ordinateur, tablette
ou téléphone. Tout tient dans ce fichier unique (HTML + CSS + JavaScript natif) :

- aucun serveur, aucune installation, aucune bibliothèque ;
- aucun appel réseau : les graphismes sont dessinés en code, les 17 musiques sont générées en direct
  par un petit synthétiseur WebAudio ;
- la progression est sauvegardée dans le navigateur (`localStorage`).

Pour y jouer sur téléphone, il suffit d'y copier le fichier `index.html` ou de l'héberger sur
n'importe quel hébergement statique (GitHub Pages, par exemple).

## Contrôles

| Action | Clavier | Tactile | Souris |
|---|---|---|---|
| Se déplacer | ZQSD / WASD / flèches | joystick (moitié gauche de l'écran) | clic sur le sol |
| Courir | Maj | bouton 🏃 (ou joystick poussé à fond) | — |
| Sauter | Espace | bouton ⤒ | — |
| Interagir / parler | E ou Entrée | bouton E | clic sur l'objet |
| Danser | X | bouton 💃 | — |
| Menu pause | Échap | bouton ⏸️ | bouton ⏸️ |
| Carte / Journal / Sac / Collection | M / J / I / C | boutons du haut | boutons du haut |

Chaque mini-jeu affiche ses propres contrôles avant de commencer, avec des boutons tactiles adaptés.
Le jeu se met en pause tout seul quand on change d'onglet ou d'application.

## Le concept

Un fichier mystérieux, `PROJET_37_FINAL_final_v2.exe`, a fait buguer l'univers d'Algator37. Les
créations se sont éparpillées dans plusieurs mondes et 7 Fragments d'Algator ont disparu. Depuis son
studio, Algator37 part les retrouver. Il traverse le Hub, les mondes des Vidéos, des Jeux, de Fortnite
et de la Musique, puis le Multivers. Là, ALGATOR.EXE l'attend : une version chaotique de lui-même,
faite de tous les brouillons abandonnés.

## Contenu

| | |
|---|---|
| Zones | 9 : Studio (personnalisable, sert aussi de menu), Hub, Monde des Vidéos, Monde des Jeux, Monde Fortnite, Monde Musical, Multivers, Cloud d'Algator (après le boss), Salle des Trophées |
| Personnages | 24, dont les 13 principaux (Sharkz_29, Alexandrefvx, Isaac Desulme, YooGos, Antoff, Footastique, Peter Beatbox, Mabiche4990, Oligator, Alessia Lo Cicero, Sola_Joe, LiamSi, Yanis Skafeh), plus des personnages cachés et des versions alternatives dans le Multivers. Plus de 230 répliques. |
| Mini-jeux | 17 : Algator Run, Algator Flappy, Algator Battle, Algator Rhythm, Griffophone, Peadle × Oligator, Parkour (3 parcours), Memory, Clicker (Studio Tycoon + Sprint), Boss Multivers, Algator League, Tirs au but, Départ F1, Build Battle, Quiz de l'Univers, Blind Test, Alibito |
| Quêtes | 86 : 18 principales, 43 secondaires, 11 missions générales, 5 défis chronométrés, 9 quêtes secrètes, plus 3 quêtes quotidiennes tirées chaque jour |
| Collection | 11 catégories : personnages, 18 chats, 19 badges, 37 trophées, 17 chansons, 10 affiches, 10 captures, objets, 18 références, 18 costumes, 39 easter eggs |
| Inventaire | 155 objets classés en quête, cosmétiques, rares, musique, badges, nourriture (avec effets), inutiles, secrets et déco |
| Progression | 25 niveaux (de « Débutant » à « Algator37 × ∞ »), XP, pièces, likes, vues, abonnés, réputation, tickets, 7 Fragments d'Algator, améliorations (vitesse, saut, radars, aimant…) |
| Fins | 5 : Multivers, Explorateur, Créateur, Collectionneur, et une Fin Secrète qui demande presque tout |

Après la première victoire contre le boss, le Cloud d'Algator et le **mode libre** se débloquent :
toutes les zones deviennent accessibles et le Trône du Multivers permet de rejouer le combat final pour
découvrir les autres fins.

## Références à l'univers d'Algator37

Certaines références sont réelles et publiques :

- **Griffophone** et **Alibito**, les jeux d'Algator37 sur itch.io ;
- **la série H** et **Nelson Mandela (En anglais)**, des vidéos de la chaîne YouTube ;
- les lives TikTok (@algator37live).

Deux mini-jeux leur rendent hommage. Le Griffophone est un vol dont la trajectoire devient un dessin
que les autres joueurs doivent deviner, avec des modes inspirés du vrai jeu : miroir, séisme, nuit, VHS,
disco, trou noir, pixel art. Alibito est un jeu où il faut démasquer le menteur parmi trois alibis.

D'autres éléments ont été **inventés pour le jeu** : Algator36, Algator Kart, Croco-Man, les codes de
maps `ALGA-TOR3-…`, les statistiques « fictives » du tableau de bord… Tous se modifient facilement
(voir plus bas). Les personnages apparaissent sous forme d'avatars stylisés au même teint « jouet », sans
chercher à reproduire l'apparence de vraies personnes.

## Sauvegarde

- Sauvegarde automatique toutes les 30 secondes, à chaque changement de zone et en quittant la page.
- Sauvegarde manuelle : lit du studio, ordinateur, menu pause ou Paramètres.
- **Paramètres → Sauvegarde** : exporter (texte JSON, fichier `.json`, presse-papiers), importer
  (coller le JSON ou choisir un fichier) et réinitialiser.
- Clé `localStorage` : `algator37_thegame_save_v1`. Une ancienne sauvegarde ou une sauvegarde importée
  est complétée automatiquement avec les champs manquants.

## Organisation du code

Tout le jeu est dans `index.html`, découpé en sections clairement commentées :

`UTILS` · `DATA` (raretés, niveaux, costumes, déco, objets, chats, musiques, trophées, fins, personnages,
dialogues, quêtes, épisodes, quiz, enquêtes Alibito, cartes des zones, parcours de parkour) ·
`GAME STATE` · `SAVE SYSTEM` · `AUDIO` · `INPUT` · `DRAW` · `WORLD` · `PLAYER` · `NPC` · `SECRETS` ·
`QUESTS` · `INVENTORY` · `UI` · `MAP` · `MINIGAMES` · `SCENES` · `ENDINGS` · `MAIN`

### Modifier le contenu

- **Dialogues d'un personnage** : objet `NPCS` (`intro`, `talk`, `party`).
- **Quêtes** : tableau `QUESTS`. L'objectif (`goal`) utilise des types prêts à l'emploi : `met`,
  `posters`, `win`, `rec`, `eggs`, `cats`, `songs`, `item`…
- **Cartes** : objet `ZONES`. Chaque zone est un dessin ASCII (`#` mur, `.` sol, `~` vide, `=` barrière
  sautable, `%` faux mur…) et sa légende associe les autres caractères aux entités.
- **Musiques** : tableau `SONGS`. Tempo, gamme, accords et style de batterie suffisent à créer un
  nouveau morceau.
- **Références et affiches** : objets `REFS` et `POSTERS`.

## Avertissement

Jeu hommage non officiel, créé pour l'univers d'Algator37. Les dialogues sont humoristiques et
bienveillants, les statistiques affichées dans le jeu sont fictives.
