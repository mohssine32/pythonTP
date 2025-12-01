class Produit:
    def __init__(self, nom: str, prix_ht: float, stock: int) -> None:
        """
        Initialise un produit avec un nom, un prix hors taxe et une quantité en stock.
        """
        self.nom = nom
        self.prix_ht = prix_ht
        self.stock = stock

    def prix_ttc(self, taux_tva: float) -> float:
        """
        Retourne le prix TTC du produit.
        taux_tva doit être donné en pourcentage (ex : 20 pour 20%).
        """
        return self.prix_ht * (1 + taux_tva / 100)

    def valeur_stock_ttc(self, taux_tva: float) -> float:
        """
        Retourne la valeur totale TTC du stock pour ce produit.
        """
        return self.stock * self.prix_ttc(taux_tva)
