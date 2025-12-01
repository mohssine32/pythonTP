import os

def lire_fichier_lbyl(nom_fichier):
    """Version LBYL : vérifier l'existence avant d’essayer d’ouvrir."""
    if os.path.exists(nom_fichier):
        with open(nom_fichier, "r", encoding="utf-8") as f:
            return f.read()
    else:
        print(f"Le fichier '{nom_fichier}' n'existe pas (LBYL).")
        return None


def lire_fichier_eafp(nom_fichier):
    """Version EAFP : essayer d’ouvrir et gérer l’erreur."""
    try:
        with open(nom_fichier, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Le fichier '{nom_fichier}' n'existe pas (EAFP).")
        return None


# ----- Bloc principal -----

if __name__ == "__main__":
    # 1) Fichier existant
    fichier_existant = "exemple.txt"
    with open(fichier_existant, "w", encoding="utf-8") as f:
        f.write("Ceci est un fichier de test.\n")

    # 2) Fichier inexistant
    fichier_inexistant = "inexistant.txt"

    print("=== Test LBYL ===")
    print(lire_fichier_lbyl(fichier_existant))
    print(lire_fichier_lbyl(fichier_inexistant))

    print("\n=== Test EAFP ===")
    print(lire_fichier_eafp(fichier_existant))
    print(lire_fichier_eafp(fichier_inexistant))
