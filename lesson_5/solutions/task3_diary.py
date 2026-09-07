"""Задача 3. Дневник: команды add, show, clear и stop."""

FILE_NAME = 'diary.txt'


def read_entries():
    """Возвращает список записей. Если файла нет, список пустой."""
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []


def add_entry(text):
    """Дописывает запись в конец файла."""
    with open(FILE_NAME, 'a', encoding='utf-8') as f:
        f.write(text + '\n')


def clear_entries():
    """Открывает файл на запись и тут же закрывает: содержимое пропадает."""
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        f.write('')


def main():
    while True:
        command = input().strip()
        if command == 'stop':
            break
        elif command.startswith('add '):
            add_entry(command[4:])
            print('Добавлено')
        elif command == 'show':
            entries = read_entries()
            if not entries:
                print('Дневник пуст')
            for i, entry in enumerate(entries, 1):
                print(f'{i}. {entry}')
        elif command == 'clear':
            clear_entries()
            print('Дневник очищен')
        else:
            print('Не понимаю команду')


if __name__ == '__main__':
    main()
