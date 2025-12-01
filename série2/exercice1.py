motspasse = input("Saisir un mot de passe : ")

if len(motspasse) < 8:
    print("Le mot de passe doit contenir au moins 8 caractères")
elif not any(c.isupper() for c in motspasse):
    print("Le mot de passe doit contenir au moins une majuscule")
elif not any(c.islower() for c in motspasse):
    print("Le mot de passe doit contenir au moins une minuscule")
elif not any(c.isdigit() for c in motspasse):
    print("Le mot de passe doit contenir au moins un chiffre")
else:
    print("Mot de passe valide")
