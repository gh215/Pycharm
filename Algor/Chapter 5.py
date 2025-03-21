import time
import hashlib

# Простейший пример (плохая хэш-функция, только для иллюстрации!)
def simple_hash(s):
    hash_val = 0
    for char in s:
        hash_val += ord(char)  # ord() возвращает Unicode-код символа
    return hash_val

print(simple_hash("hello"))  # Вывод: 532
print(simple_hash("world"))  # Вывод: 552
print(simple_hash("hello"))  # Вывод: 532 (детерминированность)

# Более надежная встроенная функция hash()
print(hash("hello"))  # Вывод: -9113196949577157978 (примерное значение)
print(hash("world"))  # Вывод: 7438627719672216465
print(hash("hello")) # Вывод: -9113196949577157978


print("\n")

# Словарь в Python - это хэш-таблица
my_dict = {"apple": 1, "banana": 2, "cherry": 3}

# Доступ к значению по ключу очень быстрый
print(my_dict["banana"])  # Вывод: 2

# Добавление нового элемента
my_dict["date"] = 4
print(my_dict)  # Вывод: {'apple': 1, 'banana': 2, 'cherry': 3, 'date': 4}

# Проверка наличия ключа
print("apple" in my_dict)  # Вывод: True
print("grape" in my_dict)  # Вывод: False

print("\n")

fruit_counts = {}  # Пустой словарь (хэш-таблица)

# Добавляем данные
fruit_counts["яблоки"] = 100
fruit_counts["бананы"] = 50
fruit_counts["апельсины"] = 75

# Получаем информацию
print(f"На складе {fruit_counts['яблоки']} яблок.")  # Вывод: На складе 100 яблок.

# Обновляем данные
fruit_counts["яблоки"] = 120
print(f"На складе {fruit_counts['яблоки']} яблок.")  # Вывод: На складе 120 яблок.


print("\n")


def remove_duplicates(items):
    """Удаляет дубликаты из списка, сохраняя порядок."""
    seen = set()  # Используем множество (set) для хранения уникальных элементов
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

my_list = [1, 2, 2, 3, 4, 4, 4, 5]
unique_list = remove_duplicates(my_list)
print(unique_list)  # Вывод: [1, 2, 3, 4, 5]

# Более короткий вариант с сохранением порядка (Python 3.7+):
def remove_duplicates_short(items):
     return list(dict.fromkeys(items))

print(remove_duplicates_short(my_list)) # Вывод: [1, 2, 3, 4, 5]

# Вариант без сохранения порядка
def remove_duplicates_shortest(items):
    return list(set(items))

print(remove_duplicates_shortest(my_list)) # Вывод: [1, 2, 3, 4, 5] (порядок может быть другим)

print("\n")

cache = {}  # Наш кэш - словарь (хэш-таблица)

def expensive_function(n):
    """Функция, имитирующая долгие вычисления."""
    if n in cache:
        print(f"Извлечение из кэша: {n}")
        return cache[n]

    print(f"Вычисление для: {n}")
    time.sleep(1)  # Имитируем задержку
    result = n * n
    cache[n] = result  # Сохраняем результат в кэш
    return result

# Первое вычисление - долгое
print(expensive_function(5))  # Вычисление для: 5, затем 25
# Второе вычисление - быстрое, из кэша
print(expensive_function(5))  # Извлечение из кэша: 5, затем 25
print(expensive_function(10)) # Вычисление для: 10, затем 100
print(expensive_function(10)) # Извлечение из кэша: 10, затем 100


print("\n")


# SHA-256 - один из стандартных алгоритмов хэширования
data = "This is some data to hash".encode('utf-8') # Строку нужно перевести в байты
hash_object = hashlib.sha256(data)
hex_dig = hash_object.hexdigest() # Получаем хэш в виде шестнадцатеричной строки
print(hex_dig) # Вывод: 68e656b251e67e8358bef8483ab0d51c6619f3e7a1a9f0e75838d41ff368f728

# Всегда один и тот же результат для одного и того же входа,
# даже между разными запусками программы