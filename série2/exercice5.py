# Lecture des notes depuis un fichier texte

# vérifier votre dossier de travail 
# import os
# print("Dossier courant :", os.getcwd())

notes = []

with open("notes.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        ligne = ligne.strip()
        if ligne == "":
            continue
        note = float(ligne)
        notes.append(note)

print("Notes lues :", notes)

note_min = min(notes)
note_max = max(notes)
somme = sum(notes)
moyenne = somme / len(notes)
nb_reussites = sum(1 for n in notes if n >= 10)

print("Min :", note_min)
print("Max :", note_max)
print("Moyenne :", moyenne)
print("Nombre de notes >= 10 :", nb_reussites)