# Quiz App ❓

> **Application web de quiz interactif (Flask + Vue.js) avec score final et back-office d'administration.**

![Python](https://img.shields.io/badge/Python-14b8a6?style=flat-square)
![Type](https://img.shields.io/badge/Projet%20perso-555?style=flat-square)
[![Portfolio](https://img.shields.io/badge/Portfolio-afouanee.dev-14b8a6?style=flat-square)](https://afouanee.dev/projects/quiz-app)

## ✨ Aperçu
Application web full-stack composée d'une API backend en Flask et d'un frontend Vue.js (build Vite). L'utilisateur répond à un quiz interactif et obtient un score final. Une interface d'administration protégée par mot de passe permet de gérer les questions (ajout, modification, suppression) et de consulter les participations et les scores. Les données sont persistées dans une base SQLite, avec un jeu de questions de départ injecté automatiquement.

## 🚀 Fonctionnalités
- **Quiz interactif** : enchaînement des questions et affichage du score final.
- **Interface d'administration** : authentification par mot de passe, jeton admin stocké dans le `localStorage`.
- **CRUD des questions** : création, modification et suppression depuis le back-office.
- **Suivi des participations** : consultation des participants et de leurs scores.
- **Base SQLite** : tables `QUESTIONS` (titres, textes, images, réponses en JSON) et `PARTICIPATIONS` (joueur, score, date) ; réinitialisation et injection des données via `/rebuild-db` à partir de `ui/public/quizz.json`.

## 🛠️ Stack technique
- **Langage** : Python ≥ 3.12 (backend) + JavaScript (frontend)
- **Bibliothèques / frameworks** : Flask (API REST), JWT (`jwt_utils`), Vue.js
- **Outils** : Vite (build frontend), SQLite, collections Postman pour les tests

## ▶️ Lancer le projet
```bash
# Backend (API Flask)
python -m venv venv && source venv/bin/activate   # Windows : venv\Scripts\activate
pip install -r requirements.txt
pip install requests
python app.py

# Frontend (Vue.js / Vite) — dans quiz-ui/
npm install
npm run dev
```

## 📂 Structure
```
app.py                 # point d'entrée de l'API Flask
database.py            # accès SQLite (bdd.db)
question.py            # routes / logique des questions
inject_question.py     # injection des questions de départ
jwt_utils.py           # authentification par jeton
requirements.txt       # dépendances Python
quiz-ui/               # frontend Vue.js (Vite)
Quiz TDD.postman_collection.json  # tests d'API (Postman)
```

---
🔗 **Fiche projet** : [afouanee.dev/projects/quiz-app](https://afouanee.dev/projects/quiz-app)
👤 **Auteur** : Afouane MOUHAMAD — [Portfolio](https://afouanee.dev) · [LinkedIn](https://linkedin.com/in/afouane-mouhamad)
