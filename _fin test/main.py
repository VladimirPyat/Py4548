# Необходимо написать проект, содержащий функционал работы с заметками.
# Программа должна уметь создавать заметку, сохранять её, читать список
# заметок, редактировать заметку, удалять заметку.


import Controller
from Notebook import Notebook


def main_menu():

    while True:
        read_line = input(f"Введите команду ({', '.join(Controller.commands.keys())}) или 'exit' для выхода: ")
        if read_line.lower().strip() == 'exit':
            break
        else:
            if read_line.lower().strip() not in Controller.commands:
                print('Неизвестная команда')
            else:
                Controller.commands[read_line]()

new_note1 = Notebook("head1", "body1")
Notebook.notes.append(new_note1)
new_note2 = Notebook("head2", "body2")
Notebook.notes.append(new_note2)

main_menu()

