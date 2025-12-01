prix_ht = float(input("Saisir le prix HT : "))
taux_tva = float(input("Entrez le taux de TVA (en %) : "))

tva = prix_ht * taux_tva / 100
prix_ttc = prix_ht + tva

print(f"Pour un prix HT de {prix_ht}€ et une TVA de {taux_tva}%, le prix TTC est de {prix_ttc}€.")