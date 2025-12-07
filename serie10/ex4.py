import requests

class JsonPlaceholderClient:
    def __init__(self):
        # URL de base de l'API
        self.base_url = "https://jsonplaceholder.typicode.com"

    def _get(self, endpoint):
        """
        Méthode interne pour faire des requêtes GET robustes :
        - construit l'URL complète
        - envoie une requête GET
        - gère les exceptions réseau
        - vérifie le statut HTTP
        - retourne les données JSON ou None
        """
        url = self.base_url + endpoint

        try:
            response = requests.get(url, timeout=5)
        except requests.exceptions.Timeout:
            print("Erreur : la requête a expiré (timeout).")
            return None
        except requests.exceptions.ConnectionError:
            print("Erreur : impossible de se connecter à l'API.")
            return None
        except requests.exceptions.RequestException as e:
            print("Erreur inconnue lors de la requête :", e)
            return None

        # Vérifier le code HTTP
        if response.status_code != 200:
            print(f"Erreur : code HTTP {response.status_code}")
            return None

        return response.json()

    # ------------------ MÉTHODES PUBLIQUES ------------------

    def get_posts(self):
        """Retourne la liste complète des posts"""
        return self._get("/posts")

    def get_post(self, post_id):
        """Retourne un post unique selon son id"""
        return self._get(f"/posts/{post_id}")


# ------------------------------------------------------------
# BLOC PRINCIPAL
# ------------------------------------------------------------
if __name__ == "__main__":
    client = JsonPlaceholderClient()

    # Récupérer tous les posts
    posts = client.get_posts()
    if posts is not None:
        print("Nombre total de posts :", len(posts))

    print()

    # Récupérer le post d'id 1
    post1 = client.get_post(1)
    if post1 is not None:
        print("Titre du post 1 :", post1["title"])
        print("Contenu du post 1 :")
        print(post1["body"])
