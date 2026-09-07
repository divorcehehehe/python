import json
from pathlib import Path

FILE_NAME = 'records.json'    # файл рекордов лежит рядом с main.py
TOP_SIZE = 3                  # сколько строк показываем в таблице


class Records:
    """Таблица результатов: чтение и запись records.json."""

    def __init__(self):
        # parent это папка models, parent.parent это папка проекта
        self._path = Path(__file__).resolve().parent.parent / FILE_NAME
        # нет файла или он испорчен: начинаем с пустой таблицы
        try:
            self._rows = json.loads(self._path.read_text(encoding='utf-8'))
        except (FileNotFoundError, json.JSONDecodeError):
            self._rows = []

    def add(self, name, attempts, won, level):
        # проигравший тратит все попытки, поэтому он окажется внизу таблицы
        self._rows.append({'name': name, 'level': level,
                           'attempts': attempts, 'won': won})
        self._rows.sort(key=lambda row: row['attempts'])
        text = json.dumps(self._rows, ensure_ascii=False, indent=2)
        self._path.write_text(text, encoding='utf-8')

    def __str__(self):
        if not self._rows:
            return 'Рекордов пока нет.'
        lines = [f'Лучшие результаты (топ-{TOP_SIZE}), попыток:']
        for i, row in enumerate(self._rows[:TOP_SIZE], start=1):
            mark = ''
            if not row['won']:
                mark = ', не угадал'
            lines.append(f'{i}. {row["name"]:<12} {row["attempts"]}'
                         f', {row["level"]}{mark}')
        return '\n'.join(lines)
