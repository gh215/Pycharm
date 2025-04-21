from time import sleep


def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

print(sum([1,2,3,4,5]))

def count_elements(lst):
    if not lst:  # Базовый случай: пустой список
        return 0
    return 1 + count_elements(lst[1:])  # 1 элемент + длина оставшегося списка

print(count_elements([1,2,3,4,5]))

def find_max(lst):
    if len(lst) == 1:  # Базовый случай: если один элемент, он и есть максимум
        return lst[0]
    sub_max = find_max(lst[1:])  # Находим максимум в оставшейся части списка
    return lst[0] if lst[0] > sub_max else sub_max  # Сравниваем первый элемент с sub_max

print(find_max([1,2,3,4,5]))

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10,5,2,3]))

def print_items(list):
    for item in list:
        sleep(1)
        print(item)

print(print_items([10,5,2,3]))