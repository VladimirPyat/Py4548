# Требуется вычислить, сколько раз встречается некоторое число X в списке A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

import random
rand_min=1
rand_max=10
n = int(input("Введите длину списка: "))
some_list=[]
for i in range (n):
    some_list.append (random.randint(rand_min,rand_max))
print(some_list)

x = int(input("Введите искомое число: "))
count=0
for i in range (n):
    if some_list[i]==x:
        count+=1

print (f"Число {x} встречается {count} раз")