

def division_securisee():
    try:
     x = int(input("Entrez le numérateur : "))
     y = int(input("Entrez le dénominateur : "))
     resultat = x / y
    except ValueError:
         print("Veuillez entrer des entiers uniquement.")
    except ZeroDivisionError:
            print("Erreur : division par zéro impossible.")
    else:
     print("Résultat :", resultat)

division_securisee()

