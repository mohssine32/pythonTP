commande = {
    "id": 1,
    "client": "alice@example.com",
    "montant": 49.90,
    "statut": "payee"
}

commandes = [
    {"id": 1, "client": "alice@example.com", "montant": 49.90, "statut": "payee"},
    {"id": 2, "client": "bob@example.com",   "montant": 15.00, "statut": "annulee"},
]

# Affichage des commandes
for cmd in commandes:
    print(cmd["id"], cmd["client"], cmd["montant"], cmd["statut"])

# Calcul du chiffre d’affaires
chiffre_affaires = sum(
    cmd["montant"] for cmd in commandes if cmd["statut"] == "payee"
)

print("\nChiffre d’affaires total :", chiffre_affaires)

# 2️⃣ Compter le nombre de commandes par statut
statuts = {"payee": 0, "annulee": 0, "en_attente": 0}

for cmd in commandes:
    statuts[cmd["statut"]] += 1

print("Nombre de commandes par statut :", statuts)

# 3️⃣ Total dépensé par client
depenses_clients = {}

for cmd in commandes:
    client = cmd["client"]
    montant = cmd["montant"]

    if client not in depenses_clients:
        depenses_clients[client] = 0

    depenses_clients[client] += montant

print("Total dépensé par client :", depenses_clients)