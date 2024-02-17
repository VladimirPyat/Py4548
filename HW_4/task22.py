
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания
# все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
# import random
# rand_min=1
# rand_max=10
# n = int(input("Введите длину списка 1: "))
# some_list1=[]
# for i in range (n):
#     some_list1.append (random.randint(rand_min, rand_max))
# print(some_list1)
# m = int(input("Введите длину списка 2: "))
# some_list2=[]
# for i in range (m):
#     some_list2.append (random.randint(rand_min, rand_max))
# print(some_list2)
#
# result=set(some_list1).intersection(set(some_list2))
# print(sorted(result))

mol = [int(x) for x in input().split()]
n = mol[0]
m = mol[1]
set_1 = set()
set_2 = set()
list_1 = list()
a = [int(x) for x in input().split()]
k = set(a)
for i in k:
    set_1.add(i)
b = [int(x) for x in input().split()]
k1 = set(b)
for i in k1:
    set_2.add(i)
lok = set_1 & set_2
kool = list(lok)
kool.sort()
for i in kool:
    print(i, end=' ')
