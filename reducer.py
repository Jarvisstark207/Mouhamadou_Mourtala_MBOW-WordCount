#!/usr/bin/env python3
import sys

# Dictionnaire pour stocker le comptage des mots
compteur_mots = {}

# Lire l'entrée ligne par ligne
for ligne in sys.stdin:
    # Supprimer les espaces et diviser par tabulation
    mot, compte = ligne.strip().split("\t")
    
    # Convertir la valeur en entier
    compte = int(compte)
    
    # Ajouter au dictionnaire ou incrémenter
    if mot in compteur_mots:
        compteur_mots[mot] += compte
    else:
        compteur_mots[mot] = compte

# Afficher les résultats (mot, total)
for mot, total in compteur_mots.items():
    print(f"{mot}\t{total}")
