class Display:
    """Весь вывод на экран и ввод с клавиатуры собран здесь."""

    def show(self, text):
        # одно место, где программа печатает: легко заменить на цветной вывод
        print(text)

    def ask_text(self, prompt):
        return input(prompt)

    def ask_number(self, prompt, high):
        # спрашиваем, пока не получим целое число от 1 до high
        while True:
            try:
                number = int(input(prompt))
            except ValueError:
                self.show('Нужно целое число, попробуйте ещё раз.')
                continue
            if 1 <= number <= high:
                return number
            self.show(f'Число должно быть от 1 до {high}.')

    def __str__(self):
        return 'Экран: вывод в консоль'
