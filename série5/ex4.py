from typing import List


def appliquer_remise(prix: float, remise: float) -> float:
    """
    Applique une remise à un prix et retourne le prix final.

    Paramètres
    ----------
    prix : float
        Le prix initial avant remise.
    remise : float
        La remise exprimée en pourcentage (ex : 10 pour 10%).

    Retour
    ------
    float
        Le prix après application de la remise.

    Exemple
    -------
    >>> appliquer_remise(100.0, 20.0)
    80.0
    """
    return prix * (1 - remise / 100)



def calculer_moyenne(notes: List[float]) -> float:
    """
    Calcule la moyenne d'une liste de notes.

    Paramètres
    ----------
    notes : list[float]
        Liste de notes entre 0 et 20.

    Retour
    ------
    float
        La moyenne des notes. Retourne 0.0 si la liste est vide.

    Exemple
    -------
    >>> calculer_moyenne([10, 12, 14])
    12.0
    """
    if not notes:
        return 0.0
    return sum(notes) / len(notes)



def filtrer_notes_valides(notes: List[float]) -> List[float]:
    """
    Filtre et retourne uniquement les notes supérieures ou égales à 10.

    Paramètres
    ----------
    notes : list[float]
        Liste de notes.

    Retour
    ------
    list[float]
        Liste contenant les notes >= 10.

    Exemple
    -------
    >>> filtrer_notes_valides([5, 12, 9, 14])
    [12, 14]
    """
    return [note for note in notes if note >= 10]


# ----- Bloc principal -----

if __name__ == "__main__":
    print(help(appliquer_remise))
