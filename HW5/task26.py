# Напишите программу, которая на вход принимает два числа A и B, и возводит число
# А в целую степень B с помощью рекурсии.

def power_rec (base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    else :
        return (base*power_rec(base, exp-1))

A = int(input ("Введите основание степени: "))
B = int(input ("Введите показатель степени: "))
print (power_rec (A, B))