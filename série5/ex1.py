utilisateur = {
    "nom": "Alice",
    "email": "alice@example.com",
    "age": 30
}
def get_age_lbyl(utilisateur):
    """Version LBYL : vérifier avant d'accéder."""
    if "age" in utilisateur:
        return utilisateur["age"]
    else:
        print("La clé 'age' est manquante (LBYL).")
        return None


def get_age_eafp(utilisateur):
    """Version EAFP : tenter, puis gérer l'erreur."""
    try:
        return utilisateur["age"]
    except KeyError:
        print("La clé 'age' est manquante (EAFP).")
        return None


# ----- Bloc principal -----

if __name__ == "__main__":

    user_with_age = {"nom": "Ali", "age": 25}
    user_without_age = {"nom": "Sara"}

    print("=== Test LBYL ===")
    print(get_age_lbyl(user_with_age))       # devrait afficher 25
    print(get_age_lbyl(user_without_age))    # devrait afficher None + message

    print("\n=== Test EAFP ===")
    print(get_age_eafp(user_with_age))       # devrait afficher 25
    print(get_age_eafp(user_without_age))    # devrait afficher None + message
