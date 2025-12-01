age = int(input("plaise saisir votre age:"))
if age < 12:
    print("le tarif c'est 5 euro")
elif age >= 12 and age < 17:
    print("le tarif c'est 7 euro")
elif age >= 18 and age < 25:
    print("le tarif c'est 8.5 euro")
else:
    print("le tarif c'est 10 euro")

print("par ce que l'age c'est", age)