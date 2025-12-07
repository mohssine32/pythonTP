class Produit:
    def __init__(self, id, nom, categorie, prix, stock):
        self.id = id
        self.nom = nom
        self.categorie = categorie
        self.prix = prix
        self.stock = stock

    def est_en_rupture(self):
        return self.stock == 0


    def afficher_resume(self):
        return f"[{self.categorie}] {self.nom} - {self.prix}€ (stock: {self.stock})"
class Catalogue:
    def __init__(self):
        self.produits = []

    def ajouter_produit(self, produit):
        """Ajoute un produit au catalogue."""
        self.produits.append(produit)

    def produits_par_categorie(self, categorie):
        """Retourne une liste des produits appartenant à la catégorie donnée."""
        return [p for p in self.produits if p.categorie == categorie]
    

    
    def prix_moyen(self):
        """Retourne le prix moyen de tous les produits du catalogue."""
        if not self.produits:
            return 0
        total = sum(p.prix for p in self.produits)
        return total / len(self.produits)
    
    def produits_en_rupture(self):
        """Retourne la liste des produits dont le stock est 0."""
        return [p for p in self.produits if p.stock == 0]
