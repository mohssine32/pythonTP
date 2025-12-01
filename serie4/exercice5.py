# Définition de l'exception personnalisée
class CommandeInvalideError(Exception):
    pass

# Fonction pour valider le montant de la commande
def valider_commande(montant):
    if montant <= 0:
        raise CommandeInvalideError("Le montant doit être supérieur à 0.")
    if montant > 10_000:
        raise CommandeInvalideError("Le montant est trop élevé et suspect.")
    return True

# Bloc principal
try:
    montant_str = input("Entrez le montant de la commande : ")
    montant = float(montant_str)  # Conversion en nombre flottant
    if valider_commande(montant):
        print("Commande valide")
except ValueError:
    print("Erreur : veuillez entrer un nombre valide.")
except CommandeInvalideError as e:
    print(f"Commande invalide : {e}")
