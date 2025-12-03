import csv
import matplotlib.pyplot as plt
from datetime import datetime

# --- 1. Lecture du CSV et récupération des listes ---
dates = []
trafic = []
revenus = []

with open("ventes_journalieres.csv", "r", encoding="utf-8") as f:
    lecteur = csv.reader(f)
    next(lecteur)  # sauter l'en-tête

    for ligne in lecteur:
        # Conversion de la date en objet datetime pour un affichage correct
        dates.append(datetime.strptime(ligne[0], "%Y-%m-%d"))  # adapter le format si nécessaire
        trafic.append(int(ligne[1]))
        revenus.append(float(ligne[3]))  # colonne 3 = revenu

# --- 2. Création des sous-graphiques ---
plt.figure(figsize=(12, 8))

# Subplot 1 : Trafic
plt.subplot(2, 1, 1)
plt.plot(dates, trafic, marker="o", color="blue")
plt.title("Trafic journalier")
plt.xlabel("Date")
plt.ylabel("Trafic")
plt.grid(True)

# Subplot 2 : Revenu
plt.subplot(2, 1, 2)
plt.plot(dates, revenus, marker="o", color="green")
plt.title("Revenu journalier")
plt.xlabel("Date")
plt.ylabel("Revenu (€)")
plt.grid(True)

# Amélioration de l'affichage des dates
plt.gcf().autofmt_xdate()  # rotation automatique des dates
plt.tight_layout()         # ajustement des sous-graphique
plt.show()
