import matplotlib.pyplot as plt

# 1. Créer une liste de 20 à 30 valeurs
revenus = [
    2000, 2500, 3000, 2800, 5000, 6000, 2200, 2700, 4500, 5200,
    3100, 3300, 2900, 4100, 3800, 2600, 2400, 5500, 5800, 6100,
    1900, 2300, 4700, 4900, 5300
]

# 2. Tracer l’histogramme
plt.hist(revenus, bins=5)           # bins = nombre de « bacs »
plt.title("Distribution des revenus journaliers")
plt.xlabel("Revenu (€)")
plt.ylabel("Fréquence")

# 3. Afficher le graphique
plt.show()
