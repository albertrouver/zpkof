#!/usr/bin/env python3
"""Extrait de index.html le fragment publiable comme Artifact.

L'hôte des Artifacts fournit lui-meme <!doctype>, <html>, <head> et <body> :
on ne lui transmet que le <title>, les polices, le <style> et le contenu du
<body>, delimites dans index.html par les marqueurs A1..A2 et A3..A4.
"""
import pathlib
import sys

racine = pathlib.Path(__file__).resolve().parent.parent
source = (racine / "index.html").read_text(encoding="utf-8")


def entre(debut, fin):
    i = source.index(debut) + len(debut)
    return source[i:source.index(fin, i)]


tete = entre("<!-- A1 -->", "<!-- A2 -->")
for balise in ("</head>", "<body>"):
    tete = tete.replace(balise, "")

fragment = tete.strip() + "\n\n" + entre("<!-- A3 -->", "<!-- A4 -->").strip() + "\n"

sortie = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else racine / "fragment-artifact.html"
sortie.write_text(fragment, encoding="utf-8")
print(f"{sortie} — {len(fragment)} octets")
