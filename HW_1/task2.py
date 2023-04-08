# Задача 2: Найдите сумму цифр трехзначного числа.
flag = True
while flag :
    num = int (input("Введите 3-значное число: "))
    if 99 < num < 1000 : #проверка что в числе 3 знака
        flag = False
sum = 0
while num != 0 :
    sum += num%10
    num = num // 10

print (sum)