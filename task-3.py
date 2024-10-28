import timeit
from utils import kmp_search, boyer_moore_search, rabin_karp_search

# Завантаження статей
with open("article-1.txt", "r", encoding="utf-8") as f:
    text1 = f.read()

with open("article-2.txt", "r", encoding="utf-8") as f:
    text2 = f.read()

# Вимірювання часу за допомогою timeit
for algorithm, name in [
    (kmp_search, "Knuth-Morris-Pratt"),
    (boyer_moore_search, "Boyer-Moore"),
    (rabin_karp_search, "Rabin-Karp")
]:
    # Тест для існуючого підрядка
    time_existing_text1 = timeit.timeit(lambda: algorithm(text1, "цей алгоритм від двійкового пошуку відрізняється рухом виключно вперед"), number=10)
    time_existing_text2 = timeit.timeit(lambda: algorithm(text2, "Створена програмна імітаційна модель рекомендаційної системи для проведення"), number=10)

    # Тест для вигаданого підрядка
    time_non_existing_text1 = timeit.timeit(lambda: algorithm(text1, "Вигаданий рядок"), number=10)
    time_non_existing_text2 = timeit.timeit(lambda: algorithm(text2, "Вигаданий рядок"), number=10)

    print(f"{name} для статті 1 (існуючий): {time_existing_text1:.6f} секунд")
    print(f"{name} для статті 1 (неіснуючий): {time_non_existing_text1:.6f} секунд")
    print(f"{name} для статті 2 (існуючий): {time_existing_text2:.6f} секунд")
    print(f"{name} для статті 2 (неіснуючий): {time_non_existing_text2:.6f} секунд")
    print("\n")