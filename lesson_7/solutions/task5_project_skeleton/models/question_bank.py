"""Вопросы викторины. Пока заглушка: чтение файла добавим позже."""


class QuestionBank:
    def __init__(self, filename: str):
        self.filename = filename
        self.questions: list[str] = []      # TODO: прочитать вопросы из файла

    def count(self) -> int:
        return len(self.questions)

    def __str__(self) -> str:
        return f'вопросов {self.count()} (файл {self.filename})'
