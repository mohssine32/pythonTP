def est_pair(n):
    if n % 2 == 0:
        return True
    else:
        return False

nombre = int(input("Saisir un nombre entier : "))
résultat = est_pair(nombre)
print(résultat)