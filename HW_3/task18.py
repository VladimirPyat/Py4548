# Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в списке. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

import random
rand_min=-9
rand_max=9
n = int(input("Введите длину списка: "))
some_list=[]
for i in range (n):
    some_list.append (random.randint(rand_min,rand_max))
print(some_list)

x = int(input("Введите искомое число: "))
count=0
flag=True
while flag:
    for i in range (n):
        if (some_list[i]+count==x) or (some_list[i]-count==x):
            print("Ближайшее число", some_list[i])
            flag=False
            break
    count+=1

