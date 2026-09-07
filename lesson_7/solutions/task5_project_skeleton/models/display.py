"""Весь вывод и ввод викторины."""


class Display:
    def show(self, text: str):
        print(text)

    def ask(self, question: str) -> str:
        return input(f'{question} ')

    def __str__(self) -> str:
        return 'Вывод в консоль'
