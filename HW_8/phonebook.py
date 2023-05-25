#в файле данные пользователя записываются в одну строку разделенные знаком ";"
#по принципу - Фамилия;Имя;Отчество;Телефон
#в словаре содержится порядковый номер каждого поля в строке

fields = {0: 'Фамилия: ', 1: 'Имя: ', 2: 'Отчество: ', 3: 'Телефон: '}
def add_number():
    data = []
    print ('в поле номер телефона вводить 10 цифр без пробелов')
    for i in fields.keys():
        data.append(input (fields[i]))

    with open('data.txt', 'a', encoding='utf-8') as file:
        file.write(";".join(data)+'\n')


def search_number():
    name_search = input ('Введите имя/фамилию для поиска: ')
    with open('data.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')

    print_list = []
    for users, i in zip (data, range (len(data))):
        if (name_search in users):
            print_list.append(i)
    for usernum in  print_list:
        print_data = data[usernum].split(';')
        for users, i in zip(print_data, range (len(print_data))):
            print (fields[i], users)
    if (print_list == []):
        print ('Значение не найдено')


def main_menu():
    choice = 0
    while (choice !='1' and choice !='2' and choice !='3'):
        choice = input ('Выберите действие: \n 1-добавить запись \n 2-найти запись \n 3-выход \n')
    if choice == '1':
        add_number()
    elif choice == '2':
        search_number()
    else:
        exit(0)


while True:
    main_menu()