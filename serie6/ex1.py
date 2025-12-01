class Rectangle:
    def __init__(self, largeur: float, hauteur: float) -> None:
        """
        Constructeur du rectangle.

        Paramètres
        ----------
        largeur : float
            La largeur du rectangle.
        hauteur : float
            La hauteur du rectangle.
        """
        self.largeur = largeur
        self.hauteur = hauteur

    def surface(self) -> float:
        """Retourne l'aire du rectangle."""
        return self.largeur * self.hauteur

    def perimetre(self) -> float:
        """Retourne le périmètre du rectangle."""
        return 2 * (self.largeur + self.hauteur)

    def afficher(self) -> None:
        """Affiche les informations du rectangle."""
        print(f"Rectangle : {self.largeur} x {self.hauteur}")
        print(f" - Surface   : {self.surface()}")
        print(f" - Périmètre : {self.perimetre()}")
        print("---------------------------------")


# ----- Bloc principal -----

if __name__ == "__main__":

    rect1 = Rectangle(4, 5)
    rect2 = Rectangle(10, 2)

    rect1.afficher()
    rect2.afficher()
