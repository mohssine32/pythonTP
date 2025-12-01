produits = ["PC", "Clavier", "Souris", "Écran", "Imprimante"]


try: 
 indice = int(input("Entrez l’indice du produit (0 à 4) : "))
 print(f"Produit sélectionné : {produits[indice]}")
except ValueError:
 print("Erreur : veuillez entrer un nombre entier valide.")
except IndexError:
    print("Erreur : indice hors limites. Veuillez entrer un indice entre 0 et 4.")