# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
n = int(input("Введите положительное число: "))
if n==1:
    print(1)
i = 1
while n >= 2**i:

    print (2**i)
    i+=1
