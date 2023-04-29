# Определить индексы элементов массива (списка), значения которых принадлежат заданному
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
import random


def random_list (n, min, max):
    result = [random.randint(min, max) for i in range (n)]
    return result

def tres_search (some_list, min, max):
    result = []
    for i in range(0, len(some_list)):

        if ((some_list[i] >= min) and (some_list[i] <= max)):
            result.append(i)

    return result


arr_min = 0
arr_max = 100
arr_length = int (input("Задайте длину списка: "))
user_list = (random_list (arr_length, arr_min, arr_max))
print (user_list)

min_tres = int (input("Задайте минимум для поиска: "))
max_tres = int (input("Задайте максимум для поиска: "))

result_numbers = tres_search (user_list, min_tres, max_tres)
print (result_numbers)
