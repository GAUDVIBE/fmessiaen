#!/usr/bin/env python3
"""
Script pour identifier les modes de Messiaen à partir d'une liste de notes.
"""

import csv
import sys

# Table d'équivalence enharmonique (toutes les notes en dièses)
ENHARMONIC_MAP = {
    'C': 'C',
    'B#': 'C',
    'C#': 'C#',
    'Db': 'C#',
    'D': 'D',
    'D#': 'D#',
    'Eb': 'D#',
    'E': 'E',
    'Fb': 'E',
    'E#': 'F',
    'F': 'F',
    'F#': 'F#',
    'Gb': 'F#',
    'G': 'G',
    'G#': 'G#',
    'Ab': 'G#',
    'A': 'A',
    'A#': 'A#',
    'Bb': 'A#',
    'B': 'B',
    'Cb': 'B',
}

def normalize_note(note):
    """Convertit une note en sa forme normalisée (enharmonie en dièses)."""
    note = note.strip()
    if note in ENHARMONIC_MAP:
        return ENHARMONIC_MAP[note]
    else:
        print(f"⚠️  Note inconnue : {note}")
        return note

def load_modes(csv_file):
    """Charge les modes de Messiaen depuis le fichier CSV."""
    modes = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            mode_name = row['Mode']
            transposition = row['Transposition_Number']
            starting_note = row['Starting_Note']
            notes_str = row['Notes']
            
            # Extraire et normaliser les notes
            notes = [normalize_note(n.strip()) for n in notes_str.split(',')]
            notes_set = set(notes)
            
            modes.append({
                'mode': mode_name,
                'transposition': transposition,
                'starting_note': starting_note,
                'notes': notes,
                'notes_set': notes_set
            })
    
    return modes

def load_input_notes(csv_file):
    """Charge les notes à analyser depuis un fichier CSV."""
    with open(csv_file, 'r', encoding='utf-8') as f:
        content = f.read().strip()
        # Supporter plusieurs formats : une ligne, plusieurs lignes, avec ou sans header
        notes_raw = content.replace('\n', ',').split(',')
        notes = [normalize_note(n) for n in notes_raw if n.strip() and n.strip() != 'Notes']
        return notes

def find_matching_modes(input_notes, modes):
    """
    Trouve tous les modes qui contiennent toutes les notes en entrée.
    Retourne un dictionnaire {mode_name: [starting_notes]}.
    """
    input_set = set(input_notes)
    matches = {}
    
    for mode_data in modes:
        # Vérifier si toutes les notes d'entrée sont dans ce mode
        if input_set.issubset(mode_data['notes_set']):
            mode_name = mode_data['mode']
            starting_note = mode_data['starting_note']
            
            if mode_name not in matches:
                matches[mode_name] = []
            
            matches[mode_name].append(starting_note)
    
    return matches

def main():
    if len(sys.argv) < 2:
        print("Usage: python find_messiaen_mode.py <input_notes.csv>")
        print("Exemple: python find_messiaen_mode.py notes_input.csv")
        sys.exit(1)
    
    input_csv = sys.argv[1]
    modes_csv = 'messiaen_modes_all_transpositions.csv'
    
    print("🎵 Analyse des modes de Messiaen\n")
    print("=" * 60)
    
    # Charger les modes
    print(f"📂 Chargement des modes depuis {modes_csv}...")
    modes = load_modes(modes_csv)
    print(f"✅ {len(modes)} transpositions chargées\n")
    
    # Charger les notes en entrée
    print(f"📂 Chargement des notes depuis {input_csv}...")
    input_notes = load_input_notes(input_csv)
    print(f"✅ Notes en entrée : {', '.join(input_notes)}\n")
    
    # Trouver les correspondances
    print("🔍 Recherche des modes correspondants...\n")
    matches = find_matching_modes(input_notes, modes)
    
    # Afficher les résultats
    print("=" * 60)
    print("📊 RÉSULTATS\n")
    
    if not matches:
        print("❌ Aucun mode de Messiaen ne correspond à ces notes.")
    else:
        for mode_name, starting_notes in sorted(matches.items()):
            starting_notes_str = '/'.join(starting_notes)
            print(f"✅ {starting_notes_str} {mode_name}")
    
    print("\n" + "=" * 60)

if __name__ == '__main__':
    main()
