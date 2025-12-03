import csv
import matplotlib.pyplot as plt

# --- 1. Lecture des revenus journaliers ---
revenus = []

with open("ventes_journalieres.csv", "r", encoding="utf-8") as f:
    lecteur = csv.reader(f)
    next(lecteur)  # sauter l'en-tête
    for ligne in lecteur:
        revenus.append(float(ligne[3]))  # colonne 3 = revenu

# --- 2. Calcul du total par semaine ---
taille_semaine = 7
totaux_semaines = []

for i in range(0, len(revenus), taille_semaine):
    bloc = revenus[i:i+taille_semaine]  # sous-liste de 7 jours
    totaux_semaines.append(sum(bloc))

# Création des labels ["S1", "S2", ...]
labels = [f"S{i+1}" for i in range(len(totaux_semaines))]

# --- 3. Tracé du diagramme en barres ---
plt.figure(figsize=(8, 6))
plt.bar(labels, totaux_semaines, color="orange")
plt.title("Chiffre d'affaires total par semaine")
plt.xlabel("Semaine")
plt.ylabel("Revenu total (€)")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
