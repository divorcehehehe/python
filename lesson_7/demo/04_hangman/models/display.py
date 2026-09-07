"""Весь ввод и вывод игры собран в одном классе."""


class Display:
    """Печатает состояние игры и спрашивает букву."""

    def greet(self, player):
        print('Игра «Виселица». Отгадайте слово по буквам.')
        print(player)

    def show(self, words, player):
        print()
        print(words.masked(), f'   жизней: {player.lives}')

    def ask_letter(self) -> str:
        """Спрашивает, пока не введут ровно одну букву."""
        while True:
            answer = input('Буква: ').strip().lower()
            if len(answer) == 1 and answer.isalpha():
                return answer
            print('Нужна ровно одна буква, попробуйте ещё раз.')

    def show_result(self, words, player):
        print()
        if words.is_guessed():
            print(f'Победа! Слово: {words.secret}')
        else:
            print(f'Жизни кончились. Слово было: {words.secret}')
        print(player)

    def __str__(self) -> str:
        return 'Вывод в консоль'
