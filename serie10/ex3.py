import requests

# 1. Télécharger les données de l'API
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
posts = response.json()

# 2. Dictionnaire qui va contenir les stats par user
stats_par_user = {}

for post in posts:
    user_id = post["userId"]
    titre = post["title"]
    
    if user_id not in stats_par_user:
        stats_par_user[user_id] = {
            "nb_posts": 0,
            "total_longueur_titres": 0
        }
    
    # Incrémenter le nombre de posts
    stats_par_user[user_id]["nb_posts"] += 1
    
    # Ajouter la longueur du titre
    stats_par_user[user_id]["total_longueur_titres"] += len(titre)

# 3. Calcul de la longueur moyenne des titres
for user_id, stats in stats_par_user.items():
    nb = stats["nb_posts"]
    total_longueur = stats["total_longueur_titres"]
    stats["longueur_moyenne_titre"] = total_longueur / nb

    # On n'a plus besoin du total ▸ on peut le supprimer
    del stats["total_longueur_titres"]

# 4. Trier par nombre de posts (décroissant)
utilisateurs_tries = sorted(
    stats_par_user.items(),
    key=lambda item: item[1]["nb_posts"],
    reverse=True
)

# 5. Afficher seulement le TOP 3
for user_id, stats in utilisateurs_tries[:3]:
    print(
        f"User {user_id} : {stats['nb_posts']} posts "
        f"(longueur moyenne titre : {stats['longueur_moyenne_titre']:.1f})"
    )
