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
  + autres gammes ajoutées au fil du temps (cf section [Modes pris en charge](#modes-pris-en-charge))
- Support de l'équivalence enharmonique (Db = C#, etc.)
- Deux formats d'entrée : fichier CSV ou chaîne de caractères
- Base de données : 63 transpositions au total
- **Correspondances approximatives** : si une note d'entrée n'est dans
  aucun mode, propose les modes les plus proches avec la note de
  substitution la plus proche en demi-tons (et qui complète idéalement
  le mode plutôt qu'une note déjà jouée).

## Modes pris en charge

| Mode | Transpositions | Pattern (demi-tons) |
|---|---|---|
| Mode 1 (Whole Tone) | 2 | 2-2-2-2-2-2 |
| Mode 2 (Octatonic) | 3 | 1-2-1-2-1-2-1-2 |
| Mode 3 | 4 | 2-1-1-2-1-1-2-1-1 |
| Mode 4 | 6 | 1-1-3-1-1-1-3-1 |
| Mode 5 | 6 | 1-4-1-1-4-1 |
| Mode 6 | 6 | 2-2-1-1-2-2-1-1 |
| Mode 7 | 6 | 1-1-1-2-1-1-1-1-2-1 |
| **Maj (add b6)** | **12** | **2-2-1-2-1-1-2-1** — gamme majeure + sixte mineure ajoutée |
| **Slonimsky 194** | **12** | **1-2-1-1-1-1-1-4** — issue du *Thesaurus of Scales and Melodic Patterns* (1947) |
| **Slonimsky 1** | **6** | **1-5-1-5** — tetraton symétrique par tritone (C, Db, F#, G + transpositions) |

Pour ajouter un mode : éditer `messiaen_modes.csv` (1 ligne) +
`messiaen_modes_all_transpositions.csv` (N lignes selon le nombre de
transpositions distinctes), et optionnellement le `mode_patterns`
dans `fmessiaen` pour un affichage plus clair des toniques.

### Convention de nommage

- **Modes de Messiaen** : `Mode 1 (Whole Tone)`, `Mode 2 (Octatonic)`, …, `Mode 7`
- **Modes tonals étendus** : `Maj (add b6)`, etc. (nom musical descriptif)
- **Slonimsky Thesaurus** : `Slonimsky <numéro>` (référence directe au numéro
  d'entrée dans le livre, ex : `Slonimsky 194`)

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
