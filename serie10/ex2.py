import requests

def recuperer_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    
    try:
        response = requests.get(url)
        
        # Vérifier si la requête est OK
        if response.status_code == 200:
            return response.json()
        else:
            print("Erreur HTTP :", response.status_code)
            return []
    
    except requests.exceptions.RequestException as e:
        # Erreur réseau (internet coupé, DNS, timeout, ...)
        print("Erreur réseau :", e)
        return []


def afficher_resume_posts(posts, n=5):
    for post in posts[:n]:
        print(f"Post #{post['id']} (user {post['userId']}) : {post['title']}")


# Bloc principal
if __name__ == "__main__":
    posts = recuperer_posts()

    print("Nombre total de posts :", len(posts))
    print("\nAperçu des 5 premiers posts :")
    afficher_resume_posts(posts, 5)
