# Запускать из этой папки: python main.py
from pathlib import Path

from models.quiz import load_quiz

DATA_FILE = Path(__file__).parent / 'questions.json'


def ask_number():
    """Спрашивает номер варианта, пока не введут целое число."""
    while True:
        try:
            return int(input())
        except ValueError:
            print('Нужен номер варианта')
        except EOFError:
            return 0


def main():
    quiz = load_quiz(DATA_FILE)
    for question in quiz.questions:
        print(question)
        if quiz.answer(question, ask_number() - 1):
            print('Верно')
        else:
            print('Неверно')
    print(quiz)


if __name__ == '__main__':
    main()
