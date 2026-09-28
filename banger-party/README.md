# Banger Party

Un jeu de micro-jeux façon WarioWare qui fond trois jeux d'Algator37 en un seul :

- **L'Empire Banger V3** (le clicker) : les clics, les likes dorés et noirs, les parents, les lives TikTok,
  les codes secrets, la barre BlockStarPlanet vers la Renaissance, la Team et Douza ;
- **Sharkz_29 Arcade v2** : le sprite de Sharkz et ses ennemis en pixel art, et le synthé maison ;
- **le Griffophone** : les dessins du carnet, et ses modes (miroir, séisme, nocturne…) qui viennent
  dérégler les micro-jeux après chaque boss.

Page unique, sans dépendance ni build : ouvrez `index.html` dans un navigateur. Tout est dessiné en code
(canvas), aucune image ni aucun son n'est chargé. Seules les polices Bangers et Nunito viennent de Google
Fonts, avec un repli si le réseau les bloque.

## Déroulement d'une partie

Chaque micro-jeu dure environ cinq secondes : un verbe s'affiche (« CLIQUE ! », « SAUTE ! »…), la batterie
se vide, on réussit ou on perd une vie (4 en Normale). Tous les cinq micro-jeux, la vitesse monte de ×0,1.
Tous les dix, **Douza** débarque : il faut le frapper quand il brille, pas quand son bouclier est levé
(le bouclier le soigne). Le battre rend une vie. Après chaque boss, un mode du Griffophone rejoint la
roulette et peut tomber sur n'importe quel micro-jeu.

Chaque réussite rapporte des likes : 1 000 × vitesse × (1 + 10 % par point de combo), ×5 contre Douza.

## Les 13 micro-jeux

| Jeu d'origine | Micro-jeu | Ce qu'il faut faire | Commandes |
|---|---|---|---|
| L'Empire Banger | CLIQUE ! | faire cliquer Algator N fois | tap · Espace |
| | LE LIKE DORÉ ! | toucher le like doré, jamais les noirs | tap |
| | CACHE LE TÉLÉPHONE ! | glisser le téléphone dans la cachette avant que la porte s'ouvre | glisser · flèches |
| | SUR LE BEAT ! | taper trois fois quand le cercle touche le disque | tap · Espace |
| | LE LIVE ! | attraper les cadeaux (🌹 🦁 🌌) en évitant les haters | tap sur une ligne · ↑ ↓ |
| | LE CODE SECRET ! | taper un code de la Team, lettre par lettre | lettres |
| | RENAISSANCE ! | maintenir puis lâcher pile sur le Niv. 81 | maintenir · Espace |
| Sharkz Arcade | SAUTE ! | sauter les crabes et les requins, pas les drones | tap · Espace · ↑ |
| | COGNE ! | frapper à gauche ou à droite avant d'être touché | tap gauche/droite · ← → |
| | ESQUIVE ! | éviter les carapaces qui tombent | glisser · ← → |
| Le Griffophone | DESSINE UN ROND ! | un rond d'un seul trait, bien fermé | dessin |
| | REPASSE ! | suivre les pointillés (étoile, éclair, cœur…) | dessin |
| | DEVINE LE DESSIN ! | reconnaître un perso qui se précise pixel par pixel | tap · 1 2 3 |

Au clavier seul, les trois micro-jeux qui se jouent au doigt (le like doré et les deux dessins) sont retirés
de la roulette. DEVINE LE DESSIN est retiré si l'appareil n'affiche pas les emoji en couleur.

## La Team

21 potes, repris de la Team du clicker, chacun avec un bonus adapté aux micro-jeux. On en équipe un
avant la partie. 16 se débloquent en jouant (atteindre 15, battre Douza, cacher le téléphone 5 fois…) ;
les 5 autres seulement avec un code secret, à taper dans le menu.

<details>
<summary>Les codes secrets (spoilers)</summary>

| Code | Effet |
|---|---|
| `gerard` | Gérard : rater ne casse plus le combo |
| `woulgator` | Woulgator37 : la partie commence avec un combo de 5 |
| `sixsept` ou `67` | 67 : +6,7 % de likes |
| `canard` | Le Canard de bain : les jeux de l'Empire vont 20 % moins vite |
| `le truc` | Le Truc : un mode du Griffophone dès le début, likes ×2 |
| `griffophone` ou le code Konami | débloque le Mode Chaos |

Taper le nom d'un pote qui se débloque en jouant rappelle comment l'obtenir.
</details>

Le **Mode Chaos** (Réglages) met un mode du Griffophone sur presque chaque micro-jeu dès le premier,
avec des likes ×1,5 et un record à part. Il se débloque aussi en atteignant 30 dans une partie.

## Ce qui vient des fichiers d'origine

- `00-donnees.js` : les répliques des parents et de Douza, les commentaires et les cadeaux des lives,
  les lettres de fan, la Team (noms, titres, codes), les couleurs des thèmes des codes secrets ;
- `style.css` : la palette néon (`#07000d`, `#b026ff`, `#ff2e9a`, `#ffd700`) et les polices ;
- `sharkzv3.html` : le moteur pixel-art (`drawArt`, la palette, le sprite découpé de Sharkz, les ennemis),
  le synthé et la musique, le rangement prudent de `localStorage`, le code Konami ;
- `05-lobby.js` : les modes du Griffophone et leurs effets, transposés sur le canvas.

La sauvegarde (records, Team, réglages) reste dans le `localStorage` du navigateur, sous la clé
`banger_party_v1`.

## Pour bricoler

`index.html#debug` expose une petite console dans le navigateur :

```js
BP.liste()                 // les identifiants des micro-jeux
BP.jouer('saute')          // lance un micro-jeu tout de suite
BP.jouer('dore', ['miroir', 'nocturne'])   // … avec des modes du Griffophone
BP.aller(9)                // saute au micro-jeu 10 (Douza)
BP.etat()                  // phase, vies, score…
```

Pour publier la page comme Artifact : `python3 outils/fragment.py --jeu banger-party`.
