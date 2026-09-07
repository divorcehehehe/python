words = input().lower().split()

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

printed = 0
while printed < 3 and counts:
    best, best_count = '', 0
    for word, number in counts.items():
        if number > best_count:      # строгое сравнение оставляет первое из равных
            best, best_count = word, number
    print(best, best_count)
    del counts[best]
    printed += 1
