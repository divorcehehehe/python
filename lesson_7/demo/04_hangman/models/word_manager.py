"""Загаданное слово и открытые буквы."""
import random


class WordManager:
    """Читает список слов из файла и следит за тем, что уже открыто."""

    def __init__(self, filename: str):
        self._words = self._load(filename)
        self._secret = random.choice(self._words)
        self._opened = set()

    def _load(self, filename: str) -> list[str]:
        with open(filename, encoding='utf-8') as f:
            words = [line.strip().lower() for line in f if line.strip()]
        if not words:
            raise ValueError('Файл со словами пуст')
        return words

    @property
    def secret(self) -> str:
        """Загаданное слово: только для чтения."""
        return self._secret

    def open_letter(self, letter: str) -> bool:
        """Открывает букву. True, если она есть в слове и раньше не называлась."""
        if letter in self._opened:
            return False
        self._opened.add(letter)
        return letter in self._secret

    def is_guessed(self) -> bool:
        for letter in self._secret:
            if letter not in self._opened:
                return False
        return True

    def masked(self) -> str:
        """Слово с закрытыми буквами: p _ t h _ n."""
        shown = []
        for letter in self._secret:
            shown.append(letter if letter in self._opened else '_')
        return ' '.join(shown)

    def __str__(self) -> str:
        return f'Слово из {len(self._secret)} букв: {self.masked()}'
