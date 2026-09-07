"""Задача 4. Окружность из звёздочек в файле circle.txt."""

FILE_NAME = 'circle.txt'


def circle_lines(radius):
    """Строит список строк с окружностью заданного радиуса."""
    lines = []
    for y in range(-radius, radius + 1):
        row = ''
        for x in range(-radius, radius + 1):
            on_circle = abs(x * x + y * y - radius * radius) <= radius
            row += '*' if on_circle else ' '
        lines.append(row)
    return lines


def main():
    radius = int(input())
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        for line in circle_lines(radius):
            f.write(line + '\n')

    with open(FILE_NAME, 'r', encoding='utf-8') as f:
        print(f.read(), end='')


if __name__ == '__main__':
    main()
