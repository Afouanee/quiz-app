import sqlite3
from json import dumps, loads
from datetime import datetime

DB_PATH = "./bdd.db"

def rebuild_database():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS PARTICIPATIONS")
    cur.execute("DROP TABLE IF EXISTS QUESTIONS")

    cur.execute("""
        CREATE TABLE PARTICIPATIONS (
            id INTEGER PRIMARY KEY,
            playerName TEXT NOT NULL,
            score INTEGER NOT NULL,
            date TEXT,
            answers TEXT
        )
    """)


    cur.execute("""
        CREATE TABLE QUESTIONS (
            position INTEGER NOT NULL,
            title TEXT NOT NULL,
            text TEXT NOT NULL,
            image TEXT,
            id INTEGER PRIMARY KEY,
            possibleAnswers TEXT
        )
    """)

    conn.commit()
    conn.close()

def create_question(payload):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT id FROM QUESTIONS WHERE position = ?", (payload["position"],))
    if cur.fetchall():
        cur.execute("UPDATE QUESTIONS SET position = position + 1 WHERE position >= ?", (payload["position"],))

    cur.execute("INSERT INTO QUESTIONS (position, title, text, image, possibleAnswers) VALUES (?, ?, ?, ?, ?)",
                (payload["position"], payload["title"], payload["text"], payload["image"], dumps(payload["possibleAnswers"])))

    question_id = cur.lastrowid
    conn.commit()
    conn.close()

    return question_id

def get_quiz_info():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM QUESTIONS")
    size = cur.fetchone()[0]

    cur.execute("SELECT id, playerName, score, date FROM PARTICIPATIONS ORDER BY score DESC")
    scores = [dict(zip(["id", "playerName", "score", "date"], row)) for row in cur.fetchall()]

    conn.close()
    return size, scores

def add_participation(payload):
    if len(payload["answers"]) != 10:
        raise ValueError("Il faut exactement 10 réponses")

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    score = 0
    date = datetime.now().strftime('%Y-%m-%d')
    answers_summaries = []

    for idx, ans_position in enumerate(payload["answers"]):
        question = cur.execute("SELECT * FROM QUESTIONS WHERE position = ?", (idx + 1,)).fetchone()
        if not question:
            raise ValueError(f"Question {idx+1} introuvable")

        try:
            possible_answers = loads(question[5])
        except Exception:
            raise ValueError(f"Réponses illisibles pour la question {idx+1}")

        if not 1 <= ans_position <= len(possible_answers):
            raise ValueError(f"Réponse invalide pour la question {idx+1}")

        correct_index = next((i for i, ans in enumerate(possible_answers) if ans.get("isCorrect")), -1)

        is_correct = possible_answers[ans_position - 1].get("isCorrect", False)
        if is_correct:
            score += 1

        answers_summaries.append({
            "correctAnswerPosition": correct_index + 1,
            "wasCorrect": is_correct
        })

    cur.execute("INSERT INTO PARTICIPATIONS (playerName, score, date) VALUES (?, ?, ?)",
                (payload["playerName"], score, date))
    conn.commit()
    conn.close()

    return {
        "playerName": payload["playerName"],
        "score": score,
        "answersSummaries": answers_summaries
    }


def get_all_questions():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT id, title, text, image, position, possibleAnswers FROM QUESTIONS ORDER BY position ASC")
    rows = cur.fetchall()
    questions = []
    for row in rows:
        questions.append({
            "id": row[0],
            "title": row[1],
            "text": row[2],
            "image": row[3],
            "position": row[4],
            "possibleAnswers": loads(row[5])
        })

    conn.close()
    return questions

def get_question_by_id(id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT id, title, text, image, position, possibleAnswers FROM QUESTIONS WHERE id = ?", (id,))
    row = cur.fetchone()
    conn.close()

    if row:
        return {
            "id": row[0],
            "title": row[1],
            "text": row[2],
            "image": row[3],
            "position": row[4],
            "possibleAnswers": loads(row[5])
        }
    return None

def get_question_by_position(position):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT id, title, text, image, position, possibleAnswers FROM QUESTIONS WHERE position = ?", (position,))
    row = cur.fetchone()
    conn.close()

    if row:
        return {
            "id": row[0],
            "title": row[1],
            "text": row[2],
            "image": row[3],
            "position": row[4],
            "possibleAnswers": loads(row[5])
        }
    return None

def update_question_by_id(id, payload):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT position FROM QUESTIONS WHERE id = ?", (id,))
    result = cur.fetchone()
    if not result:
        conn.close()
        return False

    old_position = result[0]
    new_position = payload["position"]

    if old_position != new_position:
        if new_position < old_position:
            cur.execute("UPDATE QUESTIONS SET position = position + 1 WHERE position >= ? AND position < ?", (new_position, old_position))
        elif new_position > old_position:
            cur.execute("UPDATE QUESTIONS SET position = position - 1 WHERE position <= ? AND position > ?", (new_position, old_position))

    cur.execute("""
        UPDATE QUESTIONS SET
            position = ?, title = ?, text = ?, image = ?, possibleAnswers = ?
        WHERE id = ?
    """, (new_position, payload["title"], payload["text"], payload["image"], dumps(payload["possibleAnswers"]), id))

    conn.commit()
    conn.close()
    return True

def delete_question_by_id(id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT position FROM QUESTIONS WHERE id = ?", (id,))
    result = cur.fetchone()
    if not result:
        conn.close()
        return False

    deleted_position = result[0]

    cur.execute("DELETE FROM QUESTIONS WHERE id = ?", (id,))
    cur.execute("UPDATE QUESTIONS SET position = position - 1 WHERE position > ?", (deleted_position,))

    conn.commit()
    conn.close()
    return True

def delete_all_questions():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("DELETE FROM QUESTIONS")
    conn.commit()
    conn.close()

def delete_all_participations():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("DELETE FROM PARTICIPATIONS")
    conn.commit()
    conn.close()