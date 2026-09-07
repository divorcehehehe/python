"""JSON: словари и списки сохраняются в файл и читаются обратно."""
import json

FILE_NAME = 'records.json'


def load_records():
    """Читает список рекордов. Если файла нет, возвращает пустой список."""
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_records(records):
    """Записывает список рекордов в файл."""
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, indent=2)


records = load_records()
print('Было записей:', len(records))

records.append({'name': 'Аня', 'attempts': 4})
records.sort(key=lambda record: record['attempts'])
save_records(records[:5])

# Посмотрим, что получилось в файле: это обычный текст
with open(FILE_NAME, 'r', encoding='utf-8') as f:
    print(f.read())

for i, record in enumerate(load_records(), 1):
    print(f"{i}. {record['name']} {record['attempts']}")
