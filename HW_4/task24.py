# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты
# высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод —
# на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход,
# находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.
import random
rand_min=1
rand_max=10
n = int(input("Введите число кустов: "))
bush_number=[]
for i in range (n):
    bush_number.append (random.randint(rand_min, rand_max))

print(bush_number)
bush_number.append (bush_number[0])

max_picking=0
for i in range (n):
   now_picking= bush_number[i-1]+bush_number[i]+bush_number[i+1]
   if now_picking > max_picking:
       max_picking = now_picking

print ("Максимальный сбор за один раз: ", max_picking)