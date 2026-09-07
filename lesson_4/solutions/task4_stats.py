"""Задача 4: stats(numbers) возвращает минимум, максимум, среднее и медиану."""


def stats(numbers: list[float]) -> tuple[float, float, float, float]:
    """Кортеж из минимума, максимума, среднего и медианы списка."""
    ordered = sorted(numbers)
    n = len(ordered)
    middle = n // 2
    if n % 2 == 1:
        median = ordered[middle]
    else:
        median = (ordered[middle - 1] + ordered[middle]) / 2
    return min(ordered), max(ordered), sum(ordered) / n, median


def main() -> None:
    count = int(input())
    values = []
    for _ in range(count):
        values.append(float(input()))
    low, high, mean, median = stats(values)
    print(f'min={low:.2f} max={high:.2f} mean={mean:.2f} median={median:.2f}')


if __name__ == '__main__':
    main()
