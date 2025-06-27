import requests

API_URL = "http://localhost:5000"

# Authentification pour obtenir le token admin
login_response = requests.post(f"{API_URL}/login", json={"password": "iloveflask"})
if login_response.status_code != 200:
    print("❌ Erreur d'authentification :", login_response.text)
    exit()

token = login_response.json()["token"]
headers = {"Authorization": f"Bearer {token}"}

# Nouveau questionnaire séries
questions = [
    {
        "position": 1,
        "title": "Stranger Things",
        "text": "Comment s'appelle le monde parallèle dans la série Stranger Things ?",
        "image": "",
        "possibleAnswers": [
            {"text": "L'Autre Côté", "isCorrect": False},
            {"text": "Le Monde Inversé", "isCorrect": True},
            {"text": "L'Entre-Monde", "isCorrect": False},
            {"text": "Le No Man's Land", "isCorrect": False}
        ]
    },
    {
        "position": 2,
        "title": "Squid Game",
        "text": "Quel est le premier jeu auquel les participants jouent dans Squid Game ?",
        "image": "",
        "possibleAnswers": [
            {"text": "Le tir à la corde", "isCorrect": False},
            {"text": "Un, deux, trois, soleil", "isCorrect": True},
            {"text": "Le jeu des billes", "isCorrect": False},
            {"text": "Le pont de verre", "isCorrect": False}
        ]
    },
    {
        "position": 3,
        "title": "La Casa de Papel",
        "text": "Quel est le nom de code du personnage principal dans La Casa de Papel ?",
        "image": "",
        "possibleAnswers": [
            {"text": "Madrid", "isCorrect": False},
            {"text": "Le Professeur", "isCorrect": True},
            {"text": "Barcelone", "isCorrect": False},
            {"text": "Colonel", "isCorrect": False}
        ]
    },
    {
        "position": 4,
        "title": "Breaking Bad",
        "text": "Quel est le métier d’origine de Walter White dans Breaking Bad ?",
        "image": "",
        "possibleAnswers": [
            {"text": "Chimiste", "isCorrect": True},
            {"text": "Médecin", "isCorrect": False},
            {"text": "Avocat", "isCorrect": False},
            {"text": "Policier", "isCorrect": False}
        ]
    },
    {
        "position": 5,
        "title": "Sex Education",
        "text": "Quel est le prénom du personnage principal de Sex Education ?",
        "image": "",
        "possibleAnswers": [
            {"text": "Otis", "isCorrect": True},
            {"text": "Eric", "isCorrect": False},
            {"text": "Adam", "isCorrect": False},
            {"text": "Jackson", "isCorrect": False}
        ]
    },
    {
        "position": 6,
        "title": "13 Reasons Why",
        "text": "Pourquoi Hannah Baker laisse-t-elle des cassettes dans 13 Reasons Why ?",
        "image": "",
        "possibleAnswers": [
            {"text": "Pour parler de ses vacances", "isCorrect": False},
            {"text": "Pour expliquer son suicide", "isCorrect": True},
            {"text": "Pour annoncer une fête", "isCorrect": False},
            {"text": "Pour accuser son professeur", "isCorrect": False}
        ]
    },
    {
        "position": 7,
        "title": "You",
        "text": "Quel est le prénom du personnage principal dans la série You ?",
        "image": "",
        "possibleAnswers": [
            {"text": "Ben", "isCorrect": False},
            {"text": "Joe", "isCorrect": True},
            {"text": "Luke", "isCorrect": False},
            {"text": "Tom", "isCorrect": False}
        ]
    },
    {
        "position": 8,
        "title": "Dark",
        "text": "Quel pays est à l’origine de la série Dark ?",
        "image": "",
        "possibleAnswers": [
            {"text": "Allemagne", "isCorrect": True},
            {"text": "Suède", "isCorrect": False},
            {"text": "États-Unis", "isCorrect": False},
            {"text": "Canada", "isCorrect": False}
        ]
    },
    {
        "position": 9,
        "title": "Lupin",
        "text": "Quel acteur incarne le rôle principal dans Lupin ?",
        "image": "",
        "possibleAnswers": [
            {"text": "Omar Sy", "isCorrect": True},
            {"text": "Tahar Rahim", "isCorrect": False},
            {"text": "Reda Kateb", "isCorrect": False},
            {"text": "Vincent Cassel", "isCorrect": False}
        ]
    },
    {
        "position": 10,
        "title": "Arcane",
        "text": "Arcane est basé sur l’univers de quel jeu vidéo ?",
        "image": "",
        "possibleAnswers": [
            {"text": "Fortnite", "isCorrect": False},
            {"text": "League of Legends", "isCorrect": True},
            {"text": "Overwatch", "isCorrect": False},
            {"text": "Valorant", "isCorrect": False}
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
