while True:
    try:
        age = int(input("Entrez votre âge : "))
        break   # On sort de la boucle si aucun problème
    except ValueError:
        print("Erreur : veuillez entrer un nombre entier valide.")
print(f"Vous avez {age} ans.")
