# # Дан список чисел. Определите, сколько в нем встречается различных чисел.
# import random
# n=int(input("Введите длину списка: "))
# someList=[]
# for i in range (n):
#     someList.append (random.randint(1,10))
# print(someList)
# print(len(set(someList)))

# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.
# import random
# n=int(input("Введите длину списка: "))
# someList=[]
# for i in range (n):
#     someList.append (random.randint(1,10))
# print(someList)
# k=int(input("Введите сдвиг: "))
#
# newList=[]
# newList.extend(someList[k:len(someList)])
# newList.extend(someList[:k])
# print(newList)

#Напишите программу для печати всех уникальных значений в словаре.

# d = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII":"S007"}]
# unique_values = set()
# for item in d:
#     for value in item.values():
#         unique_values.add(value.strip())
# print("Уникальные значения: ", unique_values)

# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером)