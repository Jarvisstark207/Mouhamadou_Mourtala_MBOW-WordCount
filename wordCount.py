def compter_mots(fichier):

    # Dictionnaire pour stocker le nombre d'occurrences de chaque mot
    dictionnaire_mots = {}

    # Ouvrir le fichier en mode lecture
    with open(fichier, 'r', encoding='utf-8') as f:
        for ligne in f:  # Lire le fichier ligne par ligne
            ligne = ligne.strip()  # Supprimer les espaces en début et fin de ligne
            mots = ligne.split()  # Découper la ligne en mots en gardant la ponctuation
            
            for mot in mots:  # Parcourir chaque mot dans la ligne
                if mot in dictionnaire_mots:
                    dictionnaire_mots[mot] += 1  # Augmenter le compteur du mot s'il existe déjà
                else:
                    dictionnaire_mots[mot] = 1  # Ajouter le mot avec une fréquence de 1

    return dictionnaire_mots  # Retourner le dictionnaire avec les comptages

# 📂 Nom du fichier à analyser (doit être dans le même dossier que ce script)
nom_fichier = 'Senegal.txt'

# 🖩 Appeler la fonction et récupérer le résultat
resultats = compter_mots(nom_fichier)

# 📜 Afficher chaque mot suivi de son nombre d'apparitions
for mot, nombre in resultats.items():
    print(f"{mot}\t{nombre}")  # Utilisation de "\t" pour bien aligner les résultats
