class CompteBancaire:
    def __init__(self, titulaire: str, solde: float = 0.0) -> None:
        """
        Crée un compte bancaire avec un titulaire et un solde initial (par défaut 0).
        """
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant: float) -> None:
        """
        Dépose un montant positif sur le compte.
        """
        if montant <= 0:
            print("Erreur : le montant à déposer doit être positif.")
            return
        self.solde += montant
        print(f"{montant}€ déposés. Nouveau solde : {self.solde}€.")

    def retirer(self, montant: float) -> None:
        """
        Retire un montant si le solde est suffisant.
        """
        if montant <= 0:
            print("Erreur : le montant à retirer doit être positif.")
            return

        if montant > self.solde:
            print("Erreur : solde insuffisant pour effectuer le retrait.")
            return

        self.solde -= montant
        print(f"{montant}€ retirés. Nouveau solde : {self.solde}€.")

    def afficher(self) -> None:
        """
        Affiche le titulaire et le solde actuel.
        """
        print(f"Titulaire : {self.titulaire}")
        print(f"Solde actuel : {self.solde}€")
        print("------------------------------")
