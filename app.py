from flask import Flask, request, jsonify
from flask_cors import CORS
import hashlib
from jwt_utils import build_token, decode_token
from database import (
    create_question,
    get_quiz_info,
    rebuild_database,
    get_all_questions,
    get_question_by_id,
    get_question_by_position,
    update_question_by_id,
    delete_question_by_id,
    delete_all_questions,
    delete_all_participations,
    add_participation
)

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return "Hello, world"

@app.route('/rebuild-db', methods=['POST'])
def rebuild_db():
    try:
        rebuild_database()
        return "Ok", 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
    size, scores = get_quiz_info()
    return jsonify({"size": size, "scores": scores}), 200


from flask import request, jsonify
from jwt_utils import build_token

@app.route('/login', methods=['POST'])
def login():
    payload = request.get_json()
    print("[DEBUG] /login reçu avec payload :", payload)  # AJOUTE CECI
    if not payload or 'password' not in payload:
        return jsonify({"error": "Missing password"}), 400

    if payload["password"] == "iloveflask":
        token = build_token()
        return jsonify({"token": token}), 200
    else:
        return jsonify({
            "error": "Incorrect password",
            "received": payload["password"]  # <- Affiche ce qu'il a reçu
        }), 401


@app.route('/questions', methods=['POST'])
def post_question():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({'error': 'Unauthorized'}), 401

    token = auth_header.replace("Bearer ", "")
    try:
        decode_token(token)
    except:
        return jsonify({'error': 'Unauthorized'}), 401

    payload = request.get_json()
    try:
        question_id = create_question(payload)
        return jsonify({'id': question_id}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/questions', methods=['GET'])
def get_questions():
    position = request.args.get("position", type=int)
    if position:
        question = get_question_by_position(position)
        if question:
            return jsonify(question), 200
        else:
            return jsonify({'error': 'Not Found'}), 404
    else:
        try:
            questions = get_all_questions()
            return jsonify(questions), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

@app.route('/questions/<int:id>', methods=['GET'])
def get_question_by_id_route(id):
    question = get_question_by_id(id)
    if question:
        return jsonify(question), 200
    else:
        return jsonify({'error': 'Not Found'}), 404

@app.route('/questions/<int:id>', methods=['PUT'])
def update_question(id):
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({'error': 'Unauthorized'}), 401
    token = auth_header.replace("Bearer ", "")
    try:
        decode_token(token)
    except:
        return jsonify({'error': 'Unauthorized'}), 401

    payload = request.get_json()
    success = update_question_by_id(id, payload)
    if success:
        return '', 204
    else:
        return jsonify({'error': 'Not Found'}), 404

@app.route('/questions/<int:id>', methods=['DELETE'])
def delete_question(id):
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({'error': 'Unauthorized'}), 401
    token = auth_header.replace("Bearer ", "")
    try:
        decode_token(token)
    except:
        return jsonify({'error': 'Unauthorized'}), 401

    success = delete_question_by_id(id)
    if success:
        return '', 204
    else:
        return jsonify({'error': 'Not Found'}), 404

@app.route('/questions/all', methods=['DELETE'])
def delete_all_q():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({'error': 'Unauthorized'}), 401
    token = auth_header.replace("Bearer ", "")
    try:
        decode_token(token)
    except:
        return jsonify({'error': 'Unauthorized'}), 401

    delete_all_questions()
    return '', 204

@app.route('/participations/all', methods=['DELETE'])
def delete_all_p():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({'error': 'Unauthorized'}), 401
    token = auth_header.replace("Bearer ", "")
    try:
        decode_token(token)
    except:
        return jsonify({'error': 'Unauthorized'}), 401

    delete_all_participations()
    return '', 204

@app.route('/participations', methods=['POST'])
def post_participation():
    payload = request.get_json()
    try:
        result = add_participation(payload)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    
@app.route('/questions/position/<int:position>', methods=['GET'])
def get_question_by_position_route(position):
    question = get_question_by_position(position)
    if question:
        return jsonify(question), 200
    else:
        return jsonify({'error': 'Not Found'}), 404


if __name__ == "__main__":
    app.run()
