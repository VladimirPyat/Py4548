# Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

def progression (a1, d, n):
   a_n = a1 + (n-1) * d
   return a_n

a1_start = int(input("Введите первый элемент прогрессии: "))
d_step = int(input("Введите шаг прогрессии: "))
n_num = int(input("Введите число элементов прогрессии: "))
prog_list = []

for i in range(n_num):
    prog_list.append (progression (a1_start, d_step, i+1))

print (prog_list)
