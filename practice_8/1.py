# with open('example.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#     for letter in text:
#         print(letter)


# with open('example.txt', 'r', encoding='utf-8') as file:
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print(line[:-1])

# with open('example.txt', 'r', encoding='utf-8') as file:
#     line = file.readline()
#     while line:
#         print(line[:-1])
#         line = file.readline()


# with open('example.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#     print(text.splitlines())

# with open('example.txt', 'r', encoding='utf-8') as file:
#     text = file.readlines()
#     print(text)

# Пользователь вводит кол-во строк, затем сами строки. Нужно записать в новый текстовый файл
# все эти строки
# Далее пользователь вводит символ, нужно найти кол-во этого символа в новом файле.

num_strings = int(input('Введите число строк'))
string_list = []
print ("Введите строку ")
for string in range (num_strings):
    string_list.append (input(f'{string}:')+'\n')
with open('example.txt', 'w', encoding='utf-8') as file:
    file.writelines(string_list)
user_sign = input ("Введите символ для поиска")
with open('example.txt', 'r', encoding='utf-8') as file:
    find_sign = file.read()
count = 0
for i in find_sign:
    if user_sign == i:
        count += 1
print (f"Количество символов {count}")
