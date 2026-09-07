class Question:
    """Один вопрос викторины: текст, варианты ответа и номер верного."""

    def __init__(self, text, options, correct_index):
        self.text = text
        self.options = options
        self.correct_index = correct_index

    def check(self, index):
        return index == self.correct_index

    def __str__(self):
        lines = [self.text]
        for number, option in enumerate(self.options, 1):
            lines.append(f'{number}) {option}')
        return '\n'.join(lines)
