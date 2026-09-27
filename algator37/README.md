# ALGATOR37 — THE GAME

Un jeu d'aventure et d'exploration jouable dans le navigateur, entièrement consacré à l'univers
d'Algator37. On y retrouve ses vidéos, ses jeux, ses musiques, ses maps, ses amis… et beaucoup de chats.

> Le nom provisoire *ALGATOR37 — THE GAME* reste le titre par défaut dans le code. Dans le jeu,
> **Paramètres → Titre du jeu** permet d'en choisir un autre (par exemple « Algator37 : L'Odyssée du
> Multivers ») ou d'écrire le sien.

## Lancer le jeu

Ouvre `index.html` dans un navigateur récent (Chrome, Edge, Firefox ou Safari), sur ordinateur, tablette
ou téléphone. Tout tient dans ce fichier unique (HTML + CSS + JavaScript natif) :

- aucun serveur, aucune installation, aucune bibliothèque ;
- aucun appel réseau : les graphismes sont dessinés en code, les 20 musiques sont générées en direct
  par un petit synthétiseur WebAudio ;
- la progression est sauvegardée dans le navigateur (`localStorage`).

### Le mettre en ligne

Le fichier est autonome : il suffit de l'héberger n'importe où.

- **GitHub Pages** : dans le dépôt, *Settings → Pages → Deploy from a branch*, choisir la branche et le
  dossier racine. Le jeu est alors disponible à l'adresse `https://<compte>.github.io/<dépôt>/algator37/`.
- N'importe quel hébergement statique (Netlify, un serveur perso…) fonctionne aussi. On peut aussi
  simplement envoyer le fichier `index.html`.

## Contrôles

| Action | Clavier | Tactile | Souris | Manette |
|---|---|---|---|---|
| Se déplacer | ZQSD / WASD / flèches | joystick (moitié gauche de l'écran) | clic sur le sol | stick gauche ou croix |
| Courir | Maj | bouton 🏃 (ou joystick poussé à fond) | — | gâchettes (LB, RB, LT, RT) |
| Sauter | Espace | bouton ⤒ | — | A |
| Interagir / parler | E ou Entrée | bouton E | clic sur l'objet | X ou B |
| Danser | X | bouton 💃 | — | Y |
| Mode photo | P | menu pause | menu pause | clic du stick gauche |
| Menu pause | Échap | bouton ⏸️ | bouton ⏸️ | Start |
| Carte / Journal / Sac / Collection | M / J / I / C | boutons du haut | boutons du haut | Select (carte) |

Dans les menus, la manette navigue avec la croix ou le stick : A valide, B revient en arrière, et LB/RB
changent d'onglet. Chaque mini-jeu affiche ses propres contrôles avant de commencer, avec des boutons
tactiles adaptés. Le jeu se met en pause tout seul quand on change d'onglet ou d'application.

## Le concept

Un fichier mystérieux, `PROJET_37_FINAL_final_v2.exe`, a fait buguer l'univers d'Algator37. Les
créations se sont éparpillées dans plusieurs mondes et 7 Fragments d'Algator ont disparu. Depuis son
studio, Algator37 part les retrouver. Il traverse le Hub, les mondes des Vidéos, des Jeux, de Fortnite
et de la Musique, puis le Multivers. Là, ALGATOR.EXE l'attend : une version chaotique de lui-même,
faite de tous les brouillons abandonnés.

## Contenu

| | |
|---|---|
| Zones | 10 : Studio (personnalisable, sert aussi de menu), Hub (avec un cycle jour/nuit), Monde des Vidéos, Coulisses du Tournage, Monde des Jeux, Monde Fortnite, Monde Musical, Multivers, Cloud d'Algator (après le boss), Salle des Trophées |
| Personnages | 27, dont les 13 principaux (Sharkz_29, Alexandrefvx, Isaac Desulme, YooGos, Antoff, Footastique, Peter Beatbox, Mabiche4990, Oligator, Alessia Lo Cicero, Sola_Joe, LiamSi, Yanis Skafeh), plus des personnages inventés pour le jeu, des personnages cachés et des versions alternatives dans le Multivers. Plus de 260 répliques. |
| Mini-jeux | 18 : Algator Run, Algator Flappy, Algator Battle, Algator Rhythm, Griffophone, Peadle × Oligator, Parkour (3 parcours + les tiens), Memory, Clicker (Studio Tycoon + Sprint), Boss Multivers, Algator League, Tirs au but, Départ F1, Build Battle, Quiz de l'Univers, Blind Test, Alibito, Caméraman |
| Quêtes | 101 : 18 principales, 52 secondaires, 15 missions générales, 5 défis chronométrés, 11 quêtes secrètes, plus 3 quêtes quotidiennes et un Défi du jour |
| Collection | 11 catégories : personnages, 20 chats, 23 badges, 45 trophées, 20 chansons, 11 affiches, 16 captures, objets, 19 références, 21 costumes, 45 easter eggs |
| Inventaire | 174 objets classés en quête, cosmétiques, rares, musique, badges, nourriture (avec effets), inutiles, secrets et déco |
| Progression | 25 niveaux (de « Débutant » à « Algator37 × ∞ »), XP, pièces, likes, vues, abonnés, réputation, tickets, 7 Fragments d'Algator, améliorations (vitesse, saut, radars, aimant…) |
| Fins | 5 : Multivers, Explorateur, Créateur, Collectionneur, et une Fin Secrète qui demande presque tout. L'écran titre prend les couleurs de la dernière fin obtenue. |

Après la première victoire contre le boss, le Cloud d'Algator et le **mode libre** se débloquent :
toutes les zones deviennent accessibles et le Trône du Multivers permet de rejouer le combat final pour
découvrir les autres fins.

## Nouveautés de la version 1.1

- **Vraies références** : les 7 codes de maps du Monde Fortnite sont maintenant les vraies maps
  d'Algator37 (voir plus bas), et la vidéo « Cobra Kai » remplace l'ancien héros inventé.
- **Cycle jour/nuit dans le Hub** : une journée dure 8 minutes. La nuit, les lampadaires s'allument et le
  Veilleur de Nuit apparaît avec son piano, un télescope et son échoppe. Le Chat de Minuit vient alors au
  bord de l'étang. Le lit du studio permet de dormir jusqu'à la nuit ou jusqu'au matin.
- **Mode photo** (touche P) : caméra libre, 7 poses, 8 filtres (VHS, néon, pixel, noir et blanc, sépia,
  cinéma, rêve), zoom et cadre. L'image est téléchargée en PNG, une miniature va dans l'album
  (*Galerie → Mes photos*), et 5 nouvelles captures se débloquent en photo.
- **Coulisses du Tournage** : nouvelle zone derrière le cinéma du Monde des Vidéos, avec un fond vert, une
  fosse de cascade, deux personnages (Claquette et Casse-Cou), un chat, un bêtisier à retrouver et le
  mini-jeu **Caméraman** : garde l'acteur dans le cadre, change de plan et évite la perche micro.
- **Nouveau Jeu+** : après la victoire contre le boss, l'histoire recommence. On garde son niveau et toute
  sa collection, les chats changent de cachette, et ALGATOR.EXE devient plus coriace. Le costume exclusif
  « Algator Chromé » récompense la victoire.
- **Atelier Parkour** (YooGos, ordinateur du studio ou menu principal) : on dessine son parcours et on le
  termine pour le valider. On obtient alors un code texte (`A37P-…`) que les amis collent dans *Importer
  un code*.
- **Défi du jour** : chaque jour, un mini-jeu et des réglages imposés, les mêmes pour tout le monde, avec
  une série de jours. Le score donne un code (`A37D-…`) à comparer avec ses amis. Ce code a une clé de
  contrôle qui repère les fautes de frappe, mais il n'empêche pas la triche.
- **Accessibilité** : option « Réduire les flashs » (activée d'office si le système demande moins
  d'animations), taille du texte réglable et mode daltonien, qui ajoute des couleurs adaptées et un
  symbole par rareté.
- **Manette** : Xbox, PlayStation ou toute manette standard, dans le jeu, les mini-jeux et les menus.
- **Titre au choix** et **écran titre qui change selon la fin obtenue**.

## Références à l'univers d'Algator37

Ces références sont réelles et publiques :

- **Griffophone** et **Alibito**, les jeux d'Algator37 sur itch.io ;
- **la série H**, **Nelson Mandela (En anglais)** et **Cobra Kai**, des vidéos de la chaîne YouTube ;
- les lives TikTok de **@algator37live**, dont la vidéo « Rejoin mon clan stp » ;
- la **Gymnopédie n°1** d'Erik Satie (1888, domaine public), utilisée dans une vidéo TikTok
  d'Algator37. Le Veilleur de Nuit la joue au piano, note pour note, grâce au synthé du jeu ;
- les **7 maps Fortnite** publiées par le créateur « algator » :

| Map | Code |
|---|---|
| Boxe Sharkz 🥊 | 3191-2964-0724 |
| Slime Climb Fall Guys | 6399-3233-4731 |
| Raphael VS Leonardo | 0729-4017-8959 |
| Green Vs Black Version Lilou.81 | 0400-2414-1735 |
| Squeezie Michou Inoxtag Cyprien Natmor | 5892-0333-8073 |
| Algator00 vs Sharkz_29 Bêta | 0563-2234-4615 |
| Build fight LdL ancienneté | 0028-6012-3116 |

Deux mini-jeux rendent hommage aux jeux d'Algator37. Le Griffophone est un vol dont la trajectoire
devient un dessin que les autres joueurs doivent deviner, avec des modes inspirés du vrai jeu : miroir,
séisme, nuit, VHS, disco, trou noir, pixel art. Alibito consiste à démasquer le menteur parmi trois alibis.

D'autres éléments ont été **inventés pour le jeu** :

- Algator36 et son fantôme ;
- les personnages secondaires (Croco-Marchand, Madame Tickette, Professeur Upgrade, Veilleur de Nuit,
  Claquette, Casse-Cou…) ;
- les dialogues ;
- les statistiques « fictives » du tableau de bord.

Tous se modifient facilement (voir plus bas). Les personnages apparaissent sous forme d'avatars stylisés
au même teint « jouet », sans chercher à reproduire l'apparence de vraies personnes.

## Sauvegarde

- Sauvegarde automatique toutes les 30 secondes, à chaque changement de zone et en quittant la page.
- Sauvegarde manuelle : lit du studio, ordinateur, menu pause ou Paramètres.
- **Paramètres → Sauvegarde** : exporter (texte JSON, fichier `.json`, presse-papiers), importer
  (coller le JSON ou choisir un fichier) et réinitialiser.
- Clés `localStorage` :
  - `algator37_thegame_save_v1` pour la partie. Une ancienne sauvegarde ou une sauvegarde importée est
    complétée automatiquement avec les champs manquants ;
  - `algator37_prefs_v1` pour les réglages d'affichage et d'accessibilité, gardés même sans partie ;
  - `algator37_photos_v1` pour les 12 dernières miniatures du mode photo.

## Organisation du code

Tout le jeu est dans `index.html`, découpé en sections clairement commentées :

`UTILS` · `DATA` (raretés, niveaux, costumes, déco, objets, chats, musiques, trophées, fins, personnages,
dialogues, quêtes, épisodes, quiz, enquêtes Alibito, cartes des zones, parcours de parkour) ·
`GAME STATE` · `SAVE SYSTEM` · `AUDIO` · `INPUT` · `DRAW` · `WORLD` · `JOUR / NUIT` · `PLAYER` · `NPC` ·
`SECRETS` · `QUESTS` · `INVENTORY` · `UI` · `MAP` · `PRÉFÉRENCES` · `ACCESSIBILITÉ` · `MODE PHOTO` ·
`NOUVEAU JEU+` · `DÉFI DU JOUR` · `ATELIER PARKOUR` · `MANETTE` · `MINIGAMES` · `SCENES` · `ENDINGS` ·
`MAIN`

### Modifier le contenu

- **Dialogues d'un personnage** : objet `NPCS` (`intro`, `talk`, `party`).
- **Quêtes** : tableau `QUESTS`. L'objectif (`goal`) utilise des types prêts à l'emploi : `met`,
  `posters`, `win`, `rec`, `eggs`, `cats`, `songs`, `item`, `visit`…
- **Cartes** : objet `ZONES`. Chaque zone est un dessin ASCII (`#` mur, `.` sol, `~` vide, `=` barrière
  sautable, `%` faux mur, `$` fond vert…) et sa légende associe les autres caractères aux entités.
- **Musiques** : tableau `SONGS`. Tempo, gamme, accords et style de batterie suffisent à créer un
  nouveau morceau. Un morceau peut aussi être écrit note par note avec `score`, comme la Gymnopédie.
- **Références et affiches** : objets `REFS` et `POSTERS`. Les codes des maps sont dans `REFS`.
- **Défi du jour** : tableau `DAILY_CH_POOL` (mini-jeu, réglages, objectif).

## Avertissement

Jeu hommage non officiel, créé pour l'univers d'Algator37. Les dialogues sont humoristiques et
bienveillants, les statistiques affichées dans le jeu sont fictives.
