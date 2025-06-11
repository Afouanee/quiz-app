from flask import Flask, request, jsonify
from flask_cors import CORS
import hashlib
from jwt_utils import build_token

app = Flask(__name__)
CORS(app)

# Route par défaut
@app.route('/')
def hello_world():
    return "Hello, world"

# Route quiz-info initiale
@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
    return {"size": 0, "scores": []}, 200

# Ajout de la route /login
@app.route('/login', methods=['POST'])
def login():
    payload = request.get_json()
    if not payload or 'password' not in payload:
        return jsonify({"error": "Missing password"}), 400

    # Hash du mot de passe reçu
    password = payload['password']
    password_hash = hashlib.md5(password.encode()).hexdigest()

    # Hash attendu : md5("admin")
    correct_hash = "21232f297a57a5a743894a0e4a801fc3"  # => "admin"

    if password_hash == correct_hash:
        token = build_token()
        return jsonify({"token": token}), 200
    else:
        return 'Unauthorized', 401

if __name__ == "__main__":
    app.run()
