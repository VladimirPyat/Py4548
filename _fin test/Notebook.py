import datetime
import re


date_formats = {
    "%Y-%m-%d": r"^\d{4}-\d{2}-\d{2}$",          # Формат: YYYY-MM-DD
    "%y-%m-%d": r"^\d{2}-\d{2}-\d{2}$",          # Формат: YY-MM-DD
    "%d/%m/%Y": r"^\d{2}/\d{2}/\d{4}$",          # Формат: DD/MM/YYYY
}
DATEFORMAT = "%Y-%m-%d"                         # Формат даты  для поиска
DATETIMEFORMAT = DATEFORMAT+" %H:%M:%S"         # Формат даты и времени для datetime
date_pattern = date_formats.get(DATEFORMAT)     # Выбор паттерна для проверки корректности ввода даты


def is_valid_date(date_string):
    match = re.match(date_pattern, date_string)
    return bool(match)


def set_time(d_format=DATETIMEFORMAT):
    return datetime.datetime.now().strftime(d_format)


class Notebook:  # тут собственно хранятся заметки и методы для работы с ними
    notes = []                              # При инициализации читаем заметки из файла
    _id_counter = len(notes)                 #Первоначальный счетчик по кол-ву элементов списка



    def __init__(self, head, body):
        self.head = head
        self.body = body
        self.id = Notebook.get_next_id()
        self.mod_time = set_time()


    def __str__(self):
        return f"ID: {self.id}\nЗаголовок: {self.head}\nЗаметка: {self.body}\nИзменено: {self.mod_time}"

    def short_list(self):                           #сокращенный вывод
        return f"ID: {self.id} Заголовок: {self.head} Изменено: {self.mod_time}"

    @staticmethod
    def find_id(find_id):
        for index, note in enumerate (Notebook.notes):
            if note.id == find_id:
                return index
        return None

    @staticmethod
    def find_by_date(start_date, end_date):
        result = Notebook.notes                     #при фильтрации отбросим время создания
        if start_date:
            result = [note for note in result if note.mod_time.split(" ")[0] >= start_date]
        if end_date:
            result = [note for note in result if note.mod_time.split(" ")[0] <= end_date]
        return result


    @staticmethod
    def get_next_id():
        Notebook._id_counter += 1               # увеличиваем счетчик при создании нового экземпляра
        return Notebook._id_counter



