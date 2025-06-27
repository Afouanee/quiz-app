import requests

API_URL = "http://localhost:5000"

# Authentification pour obtenir le token admin
login_response = requests.post(f"{API_URL}/login", json={"password": "iloveflask"})
if login_response.status_code != 200:
    print("❌ Erreur d'authentification :", login_response.text)
    exit()

token = login_response.json()["token"]
headers = {"Authorization": f"Bearer {token}"}

# Liste des 10 questions
questions = [
    {
        "position": 1,
        "title": "Capitales",
        "text": "Quelle est la capitale de la France ?",
        "image": "",
        "possibleAnswers": [
            { "text": "Paris", "isCorrect": True },
            { "text": "Londres", "isCorrect": False },
            { "text": "Madrid", "isCorrect": False }
        ]
    },
    {
        "position": 2,
        "title": "Math",
        "text": "Combien font 2 + 2 ?",
        "image": "",
        "possibleAnswers": [
            { "text": "4", "isCorrect": True },
            { "text": "22", "isCorrect": False }
        ]
    },
    {
        "position": 3,
        "title": "Animaux",
        "text": "Quels sont des mammifères ?",
        "image": "",
        "possibleAnswers": [
            { "text": "Chien", "isCorrect": True },
            { "text": "Chat", "isCorrect": True },
            { "text": "Crocodile", "isCorrect": False }
        ]
    },
    {
        "position": 4,
        "title": "Langages",
        "text": "Lequel n'est pas un langage de programmation ?",
        "image": "",
        "possibleAnswers": [
            { "text": "Python", "isCorrect": False },
            { "text": "HTML", "isCorrect": True },
            { "text": "C++", "isCorrect": False }
        ]
    },
    {
        "position": 5,
        "title": "Géographie",
        "text": "L'Australie est un...",
        "image": "",
        "possibleAnswers": [
            { "text": "Continent", "isCorrect": True },
            { "text": "Pays", "isCorrect": True },
            { "text": "Océan", "isCorrect": False }
        ]
    },
    {
        "position": 6,
        "title": "Fruits",
        "text": "Laquelle de ces options est un fruit ?",
        "image": "",
        "possibleAnswers": [
            { "text": "Tomate", "isCorrect": True },
            { "text": "Carotte", "isCorrect": False },
            { "text": "Pomme", "isCorrect": True }
        ]
    },
    {
        "position": 7,
        "title": "Vide",
        "text": "Aucune réponse correcte ici",
        "image": "",
        "possibleAnswers": [
            { "text": "Option 1", "isCorrect": False },
            { "text": "Option 2", "isCorrect": False }
        ]
    },
    {
        "position": 8,
        "title": "Histoire",
        "text": "En quelle année a débuté la Seconde Guerre mondiale ?",
        "image": "",
        "possibleAnswers": [
            { "text": "1939", "isCorrect": True },
            { "text": "1945", "isCorrect": False },
            { "text": "1914", "isCorrect": False }
        ]
    },
    {
        "position": 9,
        "title": "Couleurs primaires",
        "text": "Lesquelles sont des couleurs primaires ?",
        "image": "",
        "possibleAnswers": [
            { "text": "Rouge", "isCorrect": True },
            { "text": "Vert", "isCorrect": False },
            { "text": "Bleu", "isCorrect": True },
            { "text": "Jaune", "isCorrect": True }
        ]
    },
    {
        "position": 10,
        "title": "Logique",
        "text": "Complétez : Si A > B et B > C alors...",
        "image": "",
        "possibleAnswers": [
            { "text": "A > C", "isCorrect": True },
            { "text": "C > A", "isCorrect": False }
        ]
    }
]

# Envoi des questions
for question in questions:
    res = requests.post(f"{API_URL}/questions", headers=headers, json=question)
    if res.status_code == 200:
        print(f"✅ Question '{question['title']}' ajoutée avec succès.")
    else:
        print(f"❌ Erreur pour '{question['title']}' :", res.text)
