import csv
import matplotlib.pyplot as plt
from datetime import datetime

# --- 1. Lecture des données ---
dates = []
trafic = []
nb_commandes = []
revenus = []

with open("ventes_journalieres.csv", "r", encoding="utf-8") as f:
    lecteur = csv.reader(f)
    next(lecteur)  # sauter l'en-tête
    for ligne in lecteur:
        dates.append(datetime.strptime(ligne[0], "%Y-%m-%d"))
        trafic.append(int(ligne[1]))
        nb_commandes.append(int(ligne[2]))
        revenus.append(float(ligne[3]))

# --- 2. Calcul du CA hebdomadaire (exercice 7) ---
taille_semaine = 7
totaux_semaines = []
for i in range(0, len(revenus), taille_semaine):
    bloc = revenus[i:i+taille_semaine]
    totaux_semaines.append(sum(bloc))
labels_semaines = [f"S{i+1}" for i in range(len(totaux_semaines))]

# --- 3. Création du tableau de bord ---
plt.figure(figsize=(14, 10))
plt.suptitle("Tableau de bord e-commerce", fontsize=16)

# (1,1) Courbe du trafic
plt.subplot(2, 2, 1)
plt.plot(dates, trafic, marker="o", color="blue")
plt.title("Trafic journalier")
plt.xlabel("Date")
plt.ylabel("Visiteurs")
plt.grid(True)

# (1,2) Courbe du revenu
plt.subplot(2, 2, 2)
plt.plot(dates, revenus, marker="o", color="green")
plt.title("Revenu journalier")
plt.xlabel("Date")
plt.ylabel("Revenu (€)")
plt.grid(True)

# (2,1) Histogramme des revenus
plt.subplot(2, 2, 3)
plt.hist(revenus, bins=10, color="orange", edgecolor="black")
plt.title("Histogramme des revenus")
plt.xlabel("Revenu (€)")
plt.ylabel("Nombre de jours")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# (2,2) Barres du CA hebdomadaire
plt.subplot(2, 2, 4)
plt.bar(labels_semaines, totaux_semaines, color="purple")
plt.title("CA total par semaine")
plt.xlabel("Semaine")
plt.ylabel("Revenu total (€)")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Ajustement global
plt.tight_layout(rect=[0, 0, 1, 0.95])  # laisse de la place pour suptitle

# --- 4. Sauvegarde en image ---
plt.savefig("dashboard.png")

# Affichage
plt.show()
