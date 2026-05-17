# fmessiaen

Outil CLI pour identifier les modes à transpositions limitées d'Olivier Messiaen à partir d'une liste de notes.

## Installation

Aucune dépendance externe requise. Python 3 uniquement (bibliothèque standard).

## Utilisation

```bash
# Depuis un fichier CSV
fmessiaen notes_input.csv

# Notes directes en argument
fmessiaen 'A,Db,Bb,C,E,G,Eb,F#'
fmessiaen 'C,D,E,F#'
```

## Fonctionnalités

- Analyse des 7 modes de Messiaen avec toutes leurs transpositions
- Support de l'équivalence enharmonique (Db = C#, etc.)
- Deux formats d'entrée : fichier CSV ou chaîne de caractères
- Base de données complète des modes avec 84 transpositions

## Fichiers inclus

- `fmessiaen` : Script principal (exécutable)
- `find_messiaen_mode.py` : Version alternative du script
- `messiaen_modes_all_transpositions.csv` : Base de données des modes
- `messiaen_modes.csv` : Modes de base (sans transpositions)
- `notes_input.csv` : Exemple de fichier d'entrée
- `Messiaen's Modes of Limited Transposition.pdf` : Référence théorique

## Exemple

```bash
$ fmessiaen 'C,D,E,F#'
🎵 Analyse des modes de Messiaen

============================================================
✅ 84 transpositions chargées

📝 Analyse des notes directes...
✅ Notes en entrée : C, D, E, F#

🔍 Recherche des modes correspondants...

============================================================
📊 RÉSULTATS

✅ C/F# Mode 1 (Whole Tone)

============================================================
```

## Référence

Basé sur les modes à transpositions limitées d'Olivier Messiaen, décrits dans *Technique de mon langage musical* (1944).
