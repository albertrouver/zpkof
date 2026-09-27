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
- aucun appel réseau : les graphismes sont dessinés en code, les 24 musiques sont générées en direct
  par un petit synthétiseur WebAudio ;
- la progression est sauvegardée dans le navigateur (`localStorage`).

### Le mettre en ligne

Le fichier est autonome : il suffit de l'héberger n'importe où.

- **GitHub Pages** : dans le dépôt, *Settings → Pages → Deploy from a branch*, choisir la branche et le
  dossier racine. Le jeu est alors disponible à l'adresse `https://<compte>.github.io/<dépôt>/algator37/`.
- N'importe quel hébergement statique (Netlify, un serveur perso…) fonctionne aussi. On peut aussi
  simplement envoyer le fichier `index.html`.

### L'édition connectée (claude.ai)

Publié comme page claude.ai avec les capacités `db` et `user`, le même fichier active deux fonctions
de plus. Partout ailleurs, elles restent cachées et le jeu marche normalement.

- **Sauvegarde synchronisée** : la partie est envoyée dans l'espace privé du joueur (lisible par lui
  seul) à chaque sauvegarde manuelle et toutes les 4 minutes de jeu. Sur un autre appareil connecté au
  même compte, le menu propose de récupérer la sauvegarde si elle est plus récente.
- **Classement partagé** : Défi du jour, speedrun, Algator Run, Flappy, deux parcours de parkour,
  Modération et les deux boss. Chaque joueur n'a qu'une ligne, avec son pseudo du jeu.

Limite à connaître : une page claude.ai qui utilise cette base de données n'est visible que par les
membres de l'organisation du propriétaire, et seuls ceux qui ont au moins l'accès « Contributeur »
peuvent y écrire. Elle ne peut pas être partagée par un lien public. Pour jouer avec des amis
extérieurs, on utilise la version sans base de données (lien public ou GitHub Pages) et les codes de
score du Défi du jour.

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
changent d'onglet.

**À deux** (Algator Battle et Algator League, bouton *2 JOUEURS* du menu) :

| | Joueur 1 | Joueur 2 |
|---|---|---|
| Se déplacer | ZQSD / WASD | flèches |
| Battle : sauter / bloquer | Z (W) / S | ↑ / ↓ |
| Battle : frapper / spécial | F / G | K / L (ou 1 / 2 du pavé numérique) |
| League : boost | Maj gauche ou Espace | Maj droite, K ou 0 du pavé numérique |
| Manette | manette 1 | manette 2 |
| Tactile | boutons à gauche (League : moitié gauche de l'écran) | boutons à droite (League : moitié droite) |
 Chaque mini-jeu affiche ses propres contrôles avant de commencer, avec des boutons
tactiles adaptés. Le jeu se met en pause tout seul quand on change d'onglet ou d'application.

## Le concept

Un fichier mystérieux, `PROJET_37_FINAL_final_v2.exe`, a fait buguer l'univers d'Algator37. Les
créations se sont éparpillées dans plusieurs mondes et 7 Fragments d'Algator ont disparu. Depuis son
studio, Algator37 part les retrouver. Il traverse le Hub, les mondes des Vidéos, des Jeux, de Fortnite
et de la Musique, puis le Multivers. Là, ALGATOR.EXE l'attend : une version chaotique de lui-même,
faite de tous les brouillons abandonnés.

**Chapitre 2 — Le Signal.** Après la rencontre avec l'Algator Primordial, tout en haut du Cloud, les
lives de l'univers se mettent à ramer. LAGATOR, le monstre du lag, fige tout. Un portail s'ouvre dans le
parc du Hub vers le Monde du Live, où il faut réunir 5 Éclats de Signal pour l'affronter.

## Contenu

| | |
|---|---|
| Zones | 11 : Studio (personnalisable, sert aussi de menu), Hub (avec un cycle jour/nuit et des événements de saison), Monde des Vidéos, Coulisses du Tournage, Monde des Jeux, Monde Fortnite, Monde Musical, Multivers, Cloud d'Algator (après le boss), Monde du Live (Chapitre 2), Salle des Trophées |
| Personnages | 32, dont les 13 principaux (Sharkz_29, Alexandrefvx, Isaac Desulme, YooGos, Antoff, Footastique, Peter Beatbox, Mabiche4990, Oligator, Alessia Lo Cicero, Sola_Joe, LiamSi, Yanis Skafeh), plus des personnages inventés pour le jeu, des personnages cachés, des versions alternatives dans le Multivers et deux visiteurs de saison. Près de 300 répliques. |
| Mini-jeux | 20 : Algator Run, Algator Flappy, Algator Battle (seul ou à deux), Algator Rhythm, Griffophone, Peadle × Oligator, Parkour (3 parcours + les tiens, avec fantôme), Memory, Clicker (Studio Tycoon + Sprint), Boss Multivers, Algator League (seul ou à deux), Tirs au but, Départ F1, Build Battle, Quiz de l'Univers, Blind Test, Alibito, Caméraman, Modération du chat, Boss du Live (LAGATOR) |
| Quêtes | 112 : 18 principales, 5 du Chapitre 2, 58 secondaires, 15 missions générales, 5 défis chronométrés, 11 quêtes secrètes, plus 3 quêtes quotidiennes et un Défi du jour |
| Collection | 11 catégories : personnages, 23 chats, 25 badges, 51 trophées, 24 chansons, 11 affiches, 17 captures, objets, 19 références, 24 costumes, 50 easter eggs |
| Inventaire | 194 objets classés en quête, cosmétiques, rares, musique, badges, nourriture (avec effets), inutiles, secrets et déco |
| Progression | 25 niveaux (de « Débutant » à « Algator37 × ∞ »), XP, pièces, likes, vues, abonnés, réputation, tickets, 7 Fragments d'Algator, améliorations (vitesse, saut, radars, aimant…) |
| Fins | 5 : Multivers, Explorateur, Créateur, Collectionneur, et une Fin Secrète qui demande presque tout. L'écran titre prend les couleurs de la dernière fin obtenue. |

Après la première victoire contre le boss, le Cloud d'Algator et le **mode libre** se débloquent :
toutes les zones deviennent accessibles et le Trône du Multivers permet de rejouer le combat final pour
découvrir les autres fins.

## Nouveautés de la version 1.2

- **Chapitre 2 — Le Signal** : le Monde du Live, trois nouveaux personnages (la Régie, Modo 37 et
  LAGATOR), 5 quêtes, 5 Éclats de Signal (un derrière un faux mur, un sur un îlot, un chez les
  serveurs…), 4 prises à rebrancher et le Chat Buffering, qui n'apparaît que si l'on reste immobile près
  de lui. Deux mini-jeux : **Modération du chat** (bannir le spam, laisser passer les gentils messages) et
  le **Boss du Live**, en trois phases : mise en mémoire tampon, pics de lag qui figent tout, puis
  déconnexion dans le noir. Récompenses : la Tenue de Streamer, le Routeur Doré et deux musiques.
- **Événements de saison**, selon la vraie date (modifiable dans *Paramètres → Événements de saison*) :
  - **Halloween**, du 1er octobre au 2 novembre : le Hub se couvre de citrouilles et de chauves-souris,
    Citrouillator propose un « bonbon ou un sort » par jour, 13 Bonbons Hantés sont cachés dans
    l'univers, et on peut trouver le Chat-Citrouille et le costume Citrouille ;
  - **Noël**, du 1er décembre au 6 janvier : il neige sur le Hub, le Père Gator a perdu 7 cadeaux, et on
    peut trouver le Chat Flocon, un calendrier de l'Avent de 24 cases (une par jour) et la tenue du Père
    Gator.

  Les bonbons, les cadeaux et les chats changent de cachette chaque année. Les chats de saison ne sont
  pas nécessaires pour le Chat Secret Ultime.
- **Mode 2 joueurs** sur le même écran pour Algator Battle et Algator League : clavier partagé, deux
  manettes ou tablette (voir les contrôles plus haut). Les matchs entre amis ne comptent pas pour les
  records, et le score de la soirée s'affiche.
- **Speedrun** : au lancement d'une nouvelle partie, choisir « Speedrun ». Le chrono s'affiche en haut et
  un temps intermédiaire s'inscrit à chaque quête principale. Le chrono s'arrête pendant la pause. Le
  record (Any% : jusqu'à ALGATOR.EXE), la somme des meilleurs segments et les 10 derniers runs sont
  dans *Statistiques*.
- **Fantôme du parkour** : ton meilleur passage de chaque parcours, y compris ceux que tu as créés, est
  rejoué à côté de toi en transparence. On peut le masquer dans les options du mini-jeu.
- **Lecture des dialogues à voix haute** (*Paramètres → Accessibilité*) : utilise la synthèse vocale de
  l'appareil, avec une voix française si elle est installée. Chaque personnage a sa hauteur de voix, et
  la vitesse se règle.
- **Édition connectée** sur claude.ai : sauvegarde synchronisée entre téléphone et ordinateur, et
  classement partagé (voir « L'édition connectée » plus haut).

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
- pour Noël, le refrain de **Jingle Bells** (James Lord Pierpont, 1857, domaine public), joué au synthé
  sans paroles ;
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
  Claquette, Casse-Cou, Citrouillator, le Père Gator, la Régie, Modo 37…) ;
- LAGATOR et tout le Chapitre 2 ;
- les dialogues ;
- les statistiques « fictives » du tableau de bord.

Tous se modifient facilement (voir plus bas). Les personnages apparaissent sous forme d'avatars stylisés
au même teint « jouet », sans chercher à reproduire l'apparence de vraies personnes.

## Sauvegarde

- Sauvegarde automatique toutes les 30 secondes, à chaque changement de zone et en quittant la page.
- Sauvegarde manuelle : lit du studio, ordinateur, menu pause ou Paramètres.
- Dans l'édition connectée, la partie est aussi envoyée en ligne (*Paramètres → En ligne*).
- **Paramètres → Sauvegarde** : exporter (texte JSON, fichier `.json`, presse-papiers), importer
  (coller le JSON ou choisir un fichier) et réinitialiser.
- Clés `localStorage` :
  - `algator37_thegame_save_v1` pour la partie. Une ancienne sauvegarde ou une sauvegarde importée est
    complétée automatiquement avec les champs manquants ;
  - `algator37_prefs_v1` pour les réglages d'affichage et d'accessibilité, gardés même sans partie ;
  - `algator37_photos_v1` pour les 12 dernières miniatures du mode photo ;
  - `algator37_speedrun_v1` pour le record de speedrun et les 10 derniers runs ;
  - `algator37_ghosts_v1` pour les fantômes du parkour (40 parcours au plus).

## Organisation du code

Tout le jeu est dans `index.html`, découpé en sections clairement commentées :

`UTILS` · `DATA` (raretés, niveaux, costumes, déco, objets, chats, musiques, trophées, fins, personnages,
dialogues, quêtes, épisodes, quiz, enquêtes Alibito, cartes des zones, parcours de parkour) ·
`GAME STATE` · `SAVE SYSTEM` · `AUDIO` · `INPUT` · `DRAW` · `WORLD` · `JOUR / NUIT` · `SAISONS` ·
`PLAYER` · `NPC` · `SECRETS` · `QUESTS` · `INVENTORY` · `UI` · `MAP` · `PRÉFÉRENCES` · `ACCESSIBILITÉ` ·
`MODE PHOTO` · `NOUVEAU JEU+` · `DÉFI DU JOUR` · `ATELIER PARKOUR` · `MANETTE` · `SPEEDRUN` · `FANTÔME` ·
`VOIX` · `EN LIGNE` · `MINIGAMES` · `MODE 2 JOUEURS` · `CHAPITRE 2` · `SCENES` · `ENDINGS` · `MAIN`

### Modifier le contenu

- **Dialogues d'un personnage** : objet `NPCS` (`intro`, `talk`, `party`).
- **Quêtes** : tableau `QUESTS`. L'objectif (`goal`) utilise des types prêts à l'emploi : `met`,
  `posters`, `win`, `rec`, `eggs`, `cats`, `songs`, `item`, `visit`, `flags`… Les quêtes du Chapitre 2
  ont le type `chap2` et s'enchaînent dans l'ordre.
- **Cartes** : objet `ZONES`. Chaque zone est un dessin ASCII (`#` mur, `.` sol, `~` vide, `=` barrière
  sautable, `%` faux mur, `$` fond vert…) et sa légende associe les autres caractères aux entités.
- **Musiques** : tableau `SONGS`. Tempo, gamme, accords et style de batterie suffisent à créer un
  nouveau morceau. Un morceau peut aussi être écrit note par note avec `score`, comme la Gymnopédie.
- **Références et affiches** : objets `REFS` et `POSTERS`. Les codes des maps sont dans `REFS`.
- **Défi du jour** : tableau `DAILY_CH_POOL` (mini-jeu, réglages, objectif).
- **Saisons** : `SEASONS` (dates, nombre d'objets par zone), `SEASON_HUB` (décor et personnage du Hub),
  `SEASON_THEME` (couleurs), `ADVENT` (les 24 cases du calendrier).
- **Modération du chat** : listes `MODO_GOOD` et `MODO_BAD`. **Boss du Live** : `LAG_PHASES`.

## Avertissement

Jeu hommage non officiel, créé pour l'univers d'Algator37. Les dialogues sont humoristiques et
bienveillants, les statistiques affichées dans le jeu sont fictives.
