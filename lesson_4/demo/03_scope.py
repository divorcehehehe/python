# константа пишется ЗАГЛАВНЫМИ, её видно во всех функциях
MAX_ATTEMPTS = 7
score = 0


def add_point():
    score = 1        # это новая локальная переменная
    print('внутри:', score, MAX_ATTEMPTS)


add_point()
print('снаружи:', score)


# global меняет глобальную переменную, но так лучше не делать
def add_point_global():
    global score
    score += 1


add_point_global()
print('после global:', score)


# правильный способ: передать аргумент и вернуть результат
def with_point(current):
    return current + 1


score = with_point(score)
print('через return:', score)
