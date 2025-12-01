from typing import Optional, List


def calculer_moyenne(notes: List[float]) -> float:
    """Retourne la moyenne d'une liste de notes."""
    if not notes:
        return 0.0
    return sum(notes) / len(notes)


def filtrer_notes_valides(notes: List[float]) -> List[float]:
    """Retourne une nouvelle liste contenant seulement les notes >= 10."""
    return [note for note in notes if note >= 10]


def formater_message_etudiant(nom: str, moyenne: float, notes_valides: List[float]) -> str:
    """Retourne un message formaté pour l'étudiant."""
    return (
        f"Étudiant : {nom}\n"
        f"Moyenne : {moyenne:.2f}\n"
        f"Notes >= 10 : {notes_valides}"
    )


# ------ Bloc principal ------

if __name__ == "__main__":

    notes = [12.5, 9.0, 14.0, 7.5, 10.0]
    etudiant = "Mohammed"

    moyenne = calculer_moyenne(notes)
    notes_valides = filtrer_notes_valides(notes)
    message = formater_message_etudiant(etudiant, moyenne, notes_valides)

    print(message)