# Документ «article.txt» содержит следующий текст:
#
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела



# Требуется реализовать функцию longest_words(file), которая выводит слово,
# имеющее максимальную длину (или список слов, если таковых несколько).

# with open('article.txt', 'r', encoding='utf-8') as file:
#     file_text = file.read().replace('\n', ' ')
# list_text = file_text.split(' ')
# print (list_text)
# len_text = list(map (len, list_text))
# max_words = list(filter(lambda x: len(x)== max(len_text), list_text))
# print (max_words)

def read_last(lines, file):
    with open(file, 'r', encoding='utf-8') as file:
        file_text = file.read().split('\n')
    for i in range (len(file_text)-lines, len(file_text)):
        print (file_text[i])

read_last(3, 'article.txt')