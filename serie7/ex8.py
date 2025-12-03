import csv
import matplotlib.pyplot as plt

# --- 1. Lecture des revenus journaliers depuis le CSV ---
revenus = []

with open("ventes_journalieres.csv", "r", encoding="utf-8") as f:
    lecteur = csv.reader(f)
    next(lecteur)  # sauter l'en-tête
    for ligne in lecteur:
        revenus.append(float(ligne[3]))  # colonne 3 = revenu

# --- 2. Boxplot simple des revenus ---
plt.figure(figsize=(6, 6))
plt.boxplot(revenus)
plt.title("Distribution des revenus journaliers")
plt.ylabel("Revenu (€)")
plt.grid(True)
plt.show()

# --- 3. Bonus : comparer semaine 1–2 vs semaine 3–4 ---
# Supposons que le fichier contient 28 jours (4 semaines)
revenus_sem1_2 = revenus[:14]  # jours 1 à 14
revenus_sem3_4 = revenus[14:]  # jours 15 à 28

plt.figure(figsize=(8, 6))
plt.boxplot([revenus_sem1_2, revenus_sem3_4], labels=["Semaine 1–2", "Semaine 3–4"])
plt.title("Comparaison des revenus par période")
plt.ylabel("Revenu (€)")
plt.grid(True)
plt.show()
