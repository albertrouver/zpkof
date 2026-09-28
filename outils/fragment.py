#!/usr/bin/env python3
"""Extrait d'une page du dépôt le fragment publiable comme Artifact.

L'hôte des Artifacts fournit lui-meme <!doctype>, <html>, <head> et <body> :
on ne lui transmet que le <title>, les polices, le <style> et le contenu du
<body>, delimites dans la page par les marqueurs A1..A2 et A3..A4.

    python3 outils/fragment.py                          # index.html (Ticket de Caisse Casino)
    python3 outils/fragment.py --jeu banger-party       # banger-party/index.html
    python3 outils/fragment.py --jeu banger-party /tmp/sortie.html

Sans chemin de sortie, le fragment est ecrit a cote de la page, sous le nom
fragment-artifact.html (ignore par git).
"""
import argparse
import pathlib

racine = pathlib.Path(__file__).resolve().parent.parent

arguments = argparse.ArgumentParser(description=__doc__.splitlines()[0])
arguments.add_argument("sortie", nargs="?", help="fichier a ecrire")
arguments.add_argument("--jeu", default=".", help="dossier du jeu, relatif a la racine du depot")
options = arguments.parse_args()

page = racine / options.jeu / "index.html"
source = page.read_text(encoding="utf-8")


def entre(debut, fin):
    i = source.index(debut) + len(debut)
    return source[i:source.index(fin, i)]


tete = entre("<!-- A1 -->", "<!-- A2 -->")
for balise in ("</head>", "<body>"):
    tete = tete.replace(balise, "")

fragment = tete.strip() + "\n\n" + entre("<!-- A3 -->", "<!-- A4 -->").strip() + "\n"

sortie = pathlib.Path(options.sortie) if options.sortie else page.parent / "fragment-artifact.html"
sortie.write_text(fragment, encoding="utf-8")
print(f"{sortie} — {len(fragment)} octets")
