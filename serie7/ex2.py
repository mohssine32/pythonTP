import matplotlib.pyplot as plt

categories = ["Électronique", "Mode", "Maison", "Sport"]
ca = [12000, 8000, 6000, 4000]



plt.bar(categories, ca)
plt.title("Chiffre d'affaires par catégorie")
plt.xlabel("Catégorie")
plt.ylabel("CA (€)")
plt.show()