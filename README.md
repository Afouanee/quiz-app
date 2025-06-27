# Quiz App

Application web de quiz avec un backend en Python (Flask) et un frontend en Vue.js (Vite).

---

## Fonctionnalités

### Frontend (Vue.js)

- Interface utilisateur pour :
  - répondre à un quiz interactif
  - afficher le score final
- Interface d’administration (authentifiée par mot de passe) permettant :
  - ajout, modification, suppression de questions
  - visualisation des participations et scores
- Le token admin est stocké dans le navigateur (`localStorage`)

### Backend (Flask)

- Accès réservé aux administrateurs (authentification par mot de passe)
- Ajout, modification et suppression de questions
- Visualisation des participants et de leurs scores

### Base de données (SQLite)

Deux tables principales :

- `QUESTIONS` : liste des questions, titres, textes, images et réponses possibles (sous forme JSON)
- `PARTICIPATIONS` : nom du joueur, score et date de participation

Les données de départ sont automatiquement injectées à partir du fichier `ui/public/quizz.json` lors de la réinitialisation via `/rebuild-db`.

---

## Installation et lancement

### Prérequis

- Python ≥ 3.12
- Node.js et npm

---

### 1. Cloner le dépôt

```bash
git clone https://github.com/Afouanee/quiz-app.git
cd quiz-app
```

---

### 2. Installation du back-end

1. Créez un environnement virtuel et activez-le :

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

2. Installez les dépendances Python :

```bash
pip install -r requirements.txt
pip install requests
```

3. Lancez le serveur Flask :

```bash
python app.py
```

Le backend tourne sur : `http://localhost:5000`

---

### 3. Installation du front-end

1. Placez-vous dans le dossier du frontend :

```bash
cd quiz-ui
```

2. Installez les dépendances Node.js :

```bash
npm install
```

3. Lancez le serveur Vue.js :

```bash
npm run dev
```

Le frontend tourne sur : `http://localhost:3000`

### 4. Base de données 

![image](https://github.com/user-attachments/assets/51b7e727-ed69-4dd3-bcbf-b639267f7631)

