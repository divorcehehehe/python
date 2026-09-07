class Question:
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


questions = [
    Question('Столица Франции?', ['Берлин', 'Париж'], 1),
    Question('2 + 2 * 2 = ?', ['6', '8'], 0),
]

score = 0
for question in questions:
    print(question)
    if question.check(int(input()) - 1):
        print('Верно')
        score += 1
    else:
        print('Неверно')
print(f'Итог: {score} из {len(questions)}')
