#!/usr/bin/env python3
import sys

# Lire les lignes depuis l'entrée standard
for ligne in sys.stdin:
    # Supprimer les espaces au début et à la fin
    ligne = ligne.strip()
    
    # Découper la ligne en mots
    mots = ligne.split()
    
    # Émettre chaque mot avec un compte de 1
    for mot in mots:
        print(f"{mot}\t1")
