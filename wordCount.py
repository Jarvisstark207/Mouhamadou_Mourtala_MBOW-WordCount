def count_mots_fichier(chemin_fichier):
    # Dictionnaire pour stocker les mots et leur fréquence
    compte_mots = {}
    
    # Ouvrir le fichier et lire son contenu
    with open(chemin_fichier, 'r') as fichier:
        # Parcourir chaque ligne du fichier
        for ligne in fichier:
            # Diviser la ligne en mots en utilisant l'espace comme séparateur
            mots = ligne.split()
            
            # Parcourir chaque mot dans la ligne
            for mot in mots:
                # Supprimer la ponctuation des mots (ex: ., !, ?, etc.)
                mot = mot.strip('.,!?";:()')
                
                # Convertir le mot en minuscule pour éviter les doublons (par exemple, "Senegal" et "senegal")
                mot = mot.lower()
                
                # Si le mot est déjà dans le dictionnaire, augmenter son compteur
                if mot in compte_mots:
                    compte_mots[mot] += 1
                # Si le mot n'est pas encore dans le dictionnaire, l'ajouter avec une fréquence de 1
                else:
                    compte_mots[mot] = 1
    
    # Retourner le dictionnaire contenant les mots et leurs fréquences
    return compte_mots

# Chemin du fichier
# NB: notre fichier Senegal.txt doit se trouver dans le meme repertoire que ce code wordCount.py
chemin_fichier = 'Senegal.txt'

# Appeler la fonction et obtenir le comptage des mots
compte_mots = count_mots_fichier(chemin_fichier)

# Afficher le résultat (le mot et le nombre de fois qu'il apparaît)
for mot, compte in compte_mots.items():
    print(f"{mot}: {compte}")
