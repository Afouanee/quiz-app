import json

class Question:
    def __init__(self, id, title, text, image, position, possible_answers):
        self.id = id
        self.title = title
        self.text = text
        self.image = image
        self.position = position
        self.possible_answers = possible_answers

    def question_to_json(self):
        return json.dumps({
            'id': self.id,
            'title': self.title,
            'text': self.text,
            'image': self.image,
            'position': self.position,
            'possibleAnswers': self.possible_answers
        })

    @staticmethod
    def json_to_question(json_data):
        data = json.loads(json_data)
        possible_answers = []
        for rep in data['possibleAnswers']:
            dict_reponse = {
                'text': str(rep['text']),
                'isCorrect': bool(rep['isCorrect'])
            }
            possible_answers.append(dict_reponse)
        return Question(
            None,
            title=data['title'],
            text=data['text'],
            image=data['image'],
            position=data['position'],
            possible_answers=possible_answers
        )
