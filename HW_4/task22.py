
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания
# все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
import random
rand_min=1
rand_max=10
n = int(input("Введите длину списка 1: "))
some_list1=[]
for i in range (n):
    some_list1.append (random.randint(rand_min, rand_max))
print(some_list1)
m = int(input("Введите длину списка 2: "))
some_list2=[]
for i in range (m):
    some_list2.append (random.randint(rand_min, rand_max))
print(some_list2)

result=set(some_list1).intersection(set(some_list2))
print(sorted(result))