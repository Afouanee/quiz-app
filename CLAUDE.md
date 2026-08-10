# CLAUDE.md

Contexte rapide pour reprendre ce projet.

## Vue d'ensemble

Application quiz full-stack : API Flask (Python) + frontend Vue 3 / Vite (`quiz-ui/`).
Les questions sont stockées en SQLite (`bdd.db`), avec ré-injection possible d'un jeu de
questions de départ (`quiz-ui/public/quizz.json`) via `POST /rebuild-db`.

## Structure

```
app.py                 # routes Flask (voir liste ci-dessous)
database.py            # accès SQLite : CRUD questions/participations
question.py            # helpers de validation/formatage des questions
jwt_utils.py           # génération/vérification du token admin (JWT maison)
inject_question.py     # script de peuplement de la base à partir de quizz.json
bdd.db                 # base SQLite (committée, contient des données de démo)
quiz-ui/               # frontend Vue 3 (Vite)
  src/views/            # pages : HomePage, NewQuizPage, QuestionsManager (quiz),
                        # AdminPage, LoginPage
  src/components/       # QuestionDisplay, QuestionForm, QuestionList, ScoreDisplay
  src/services/         # QuizApiService (appels HTTP vers le backend Flask),
                        # ParticipationStorageService (localStorage du joueur)
  src/assets/           # base.css (variables Vue) + main.css (styles globaux)
```

## Routes API principales

- `GET /quiz-info` — liste des scores enregistrés
- `POST /login` — auth admin, retourne un JWT
- `GET/POST /questions`, `GET/PUT/DELETE /questions/<id>` — CRUD questions (écriture protégée par JWT)
- `GET /questions/position/<n>` — récupère la question à une position donnée (mode quiz)
- `POST /participations`, `DELETE /participations/all` — enregistrement et reset des scores
- `POST /rebuild-db` — réinitialise la base et réinjecte les questions de `quizz.json`

## Lancer en local

```bash
# Backend (port 5000)
python -m venv venv && venv\Scripts\activate   # Windows
pip install -r requirements.txt
pip install requests
python app.py

# Frontend (port 3000, dans quiz-ui/)
npm install
npm run dev
```

Le frontend attend le backend sur `http://localhost:5000` (voir `quiz-ui/.env.development`
et `QuizApiService.js`).

## Points d'attention

- L'authentification admin est un JWT maison (`jwt_utils.py`), pas une lib standard type
  `PyJWT` — à garder en tête si le token pose un souci de compat.
- Le layout global (`quiz-ui/src/assets/main.css`) ne doit pas réintroduire le grid
  deux colonnes du template Vue par défaut (`#app { display: grid; grid-template-columns: 1fr 1fr }`) :
  ça a causé un bug visuel (grand espace vide à droite du contenu) déjà corrigé.
- `bdd.db` est committée avec des données de test ; un `POST /rebuild-db` la réinitialise
  proprement à partir de `quizz.json`.
