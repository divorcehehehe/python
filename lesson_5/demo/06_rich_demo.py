"""Внешняя библиотека rich: цветной вывод и таблицы.

Поставьте её через окно Python Packages внизу PyCharm или командой
    pip install rich
Файл работает и без rich: тогда он просто напечатает подсказку.
"""
try:
    from rich import print
    from rich.table import Table
    HAS_RICH = True
except ImportError:
    HAS_RICH = False
    print('Сначала: pip install rich')

if HAS_RICH:
    print('[bold green]Победа![/bold green] Осталось [cyan]3[/cyan] попытки')
    print('[red]Ошибка:[/red] такого файла нет')

    table = Table(title='Рекорды')
    table.add_column('Игрок')
    table.add_column('Очки', justify='right')
    table.add_row('Аня', '12')
    table.add_row('Игорь', '9')
    print(table)
else:
    print('Победа! Осталось 3 попытки')
    print('Рекорды: Аня 12, Игорь 9')
