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
- Base de données complète des modes avec 33 transpositions
- **Correspondances approximatives** : si une note d'entrée n'est dans
  aucun mode, propose les modes les plus proches avec la note de
  substitution la plus proche en demi-tons (et qui complète idéalement
  le mode plutôt qu'une note déjà jouée).

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
Analyse des modes de Messiaen

============================================================
33 transpositions chargées

Analyse des notes directes...
Notes en entrée : C, D, E, F#

Recherche des modes correspondants...

============================================================
RÉSULTATS

C Mode 1 (Whole Tone)
  Notes communes   : C, D, E, F#
  Notes manquantes : A#, G#

C/D Mode 3
  Notes communes   : C, D, E, F#
  Notes manquantes : A#, B, D#, G, G#

============================================================
```

## Référence

Basé sur les modes à transpositions limitées d'Olivier Messiaen, décrits dans *Technique de mon langage musical* (1944).
