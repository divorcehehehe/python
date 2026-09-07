import json

from models.question import Question


class Quiz:
    """Список вопросов и счёт игрока."""

    def __init__(self, questions):
        self._questions = questions
        self.__score = 0

    @property
    def questions(self):
        return self._questions

    @property
    def score(self):
        return self.__score

    def answer(self, question, index):
        """Проверяет ответ и увеличивает счёт, если он верный."""
        if question.check(index):
            self.__score += 1
            return True
        return False

    def __str__(self):
        return f'Итог: {self.score} из {len(self._questions)}'


def load_quiz(path):
    """Читает вопросы из json и собирает Quiz."""
    with open(path, encoding='utf-8') as source:
        data = json.load(source)
    questions = [Question(item['text'], item['options'], item['correct_index']) for item in data]
    return Quiz(questions)
