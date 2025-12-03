import csv
import matplotlib.pyplot as plt


# --- 1. Lecture du fichier CSV ---
dates = []
trafic = []
revenus = []

with open("ventes_journalieres.csv", "r", encoding="utf-8") as f:
    lecteur = csv.reader(f)
    next(lecteur)  # sauter l'en-tête

    for ligne in lecteur:
        dates.append(ligne[0])
        trafic.append(int(ligne[1]))
        revenus.append(float(ligne[2]))

# --- 2. Création des 2 sous-graphiques ---
plt.figure(figsize=(11, 10))

# Subplot 1 : Trafic
plt.subplot(2, 1, 1)
plt.plot(dates, trafic, marker="o")
plt.title("Trafic journalier")
plt.xlabel("Date")
plt.ylabel("Trafic")
plt.grid(True)

# Subplot 2 : Revenus
plt.subplot(2, 1, 2)
plt.plot(dates, revenus, marker="o", color="green")
plt.title("Revenu journalier")
plt.xlabel("Date")
plt.ylabel("Revenu (€)")
plt.grid(True)

# Ajustement des espaces
plt.tight_layout()

# Affichage
plt.show()