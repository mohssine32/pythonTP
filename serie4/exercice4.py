def lire_fichier_securise(nom_fichier):
    try:
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            return fichier.read()
    except FileNotFoundError:
        print("Erreur : fichier introuvable.")
        return None


# Bloc principal
nom = input("Entrez le nom du fichier à lire : ")

contenu = lire_fichier_securise(nom)

if contenu is not None:
    print("\n--- Contenu du fichier ---")
    print(contenu)
else:
    print("Lecture impossible.")
