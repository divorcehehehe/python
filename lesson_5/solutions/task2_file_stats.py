"""Задача 2. Статистика текстового файла: строки, слова, символы, самое частое слово."""


def most_common(words):
    """Возвращает пару (самое частое слово, сколько раз оно встретилось)."""
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    top = max(counts, key=counts.get)
    return top, counts[top]


def main():
    name = input().strip()
    try:
        with open(name, 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        print('Файл не найден')
        return

    words = []
    for line in lines:
        words += line.lower().split()
    print('Строк:', len(lines))
    print('Слов:', len(words))
    print('Символов:', sum(len(line) for line in lines))
    if words:
        word, count = most_common(words)
        print(f'Чаще всего: {word} ({count})')


if __name__ == '__main__':
    main()
