"""Задача 5. «Угадай число» с таблицей рекордов в records.json."""
import json
import random

FILE_NAME = 'records.json'
MAX_ATTEMPTS = 7
TOP_SIZE = 5


def load_records():
    """Читает рекорды. Если файла нет или он испорчен, начинает с пустого списка."""
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_records(records):
    """Записывает рекорды в файл."""
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, indent=2)


def ask_int():
    """Читает целое число, пока не получит его."""
    while True:
        try:
            return int(input())
        except ValueError:
            print('Нужно целое число')


def play(secret):
    """Партия игры. Возвращает число попыток или None, если игрок не угадал."""
    for attempt in range(1, MAX_ATTEMPTS + 1):
        guess = ask_int()
        if guess == secret:
            return attempt
        print('Больше' if guess < secret else 'Меньше')
    return None


def main():
    name = input().strip()
    attempts = play(random.randint(1, 100))
    if attempts is None:
        print('Попытки закончились')
        return

    print(f'Угадано! Попыток: {attempts}')
    records = load_records()
    records.append({'name': name, 'attempts': attempts})
    records.sort(key=lambda record: record['attempts'])
    records = records[:TOP_SIZE]
    save_records(records)

    print('Рекорды:')
    for i, record in enumerate(records, 1):
        print(f"{i}. {record['name']} {record['attempts']}")


if __name__ == '__main__':
    main()
