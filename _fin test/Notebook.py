import datetime
import re

from File_utils import file_write, file_read

date_formats = {
    "%Y-%m-%d": r"^\d{4}-\d{2}-\d{2}$",  # Формат: YYYY-MM-DD
    "%y-%m-%d": r"^\d{2}-\d{2}-\d{2}$",  # Формат: YY-MM-DD
    "%d/%m/%Y": r"^\d{2}/\d{2}/\d{4}$",  # Формат: DD/MM/YYYY
}
DATEFORMAT = "%Y-%m-%d"  # Формат даты  для поиска
DATETIMEFORMAT = DATEFORMAT + " %H:%M:%S"  # Формат даты и времени для datetime
date_pattern = date_formats.get(DATEFORMAT)  # Выбор паттерна для проверки корректности ввода даты


def is_valid_date(date_string):
    match = re.match(date_pattern, date_string)
    return bool(match)


def set_time(d_format=DATETIMEFORMAT):
    return datetime.datetime.now().strftime(d_format)


class Notebook:  # тут хранятся заметки и методы для работы с ними
    notes = []  # тут храним все заметки, по умолчанию список пуст
    _id_counter = 0  # генерация id по кол-ву элементов списка

# конструктор по умолчанию принимает два параметра, заголовок заметки и заметку. id и дата изменения автоматически
# однако при чтении из файла нам нужно считать все поля. для этого используется полный конструктор
    def __init__(self, head, body, id=None, mod_time=None):
        self.head = head
        self.body = body
        self.id = int(id) if id is not None else Notebook.get_next_id()         #преобразовываем id в текст
        self.mod_time = mod_time if mod_time is not None else set_time()

    def __str__(self):
        return f"ID: {self.id}\nЗаголовок: {self.head}\nЗаметка: {self.body}\nИзменено: {self.mod_time}"

    def short_list(self):  # сокращенный вывод при листинге
        return f"ID: {self.id} Заголовок: {self.head} Изменено: {self.mod_time}"

    def to_string(self, delimiter=';'):  # создаем строку с разделителями  из экземпляра для записи в файл
        values = [str(value) for value in list(vars(self).values())]
        return delimiter.join(values)

    @classmethod  # создаем экземпляр из строки (или None если строка невалидная)
    def from_string(cls, string, delimiter=';'):
        values = string.split(delimiter)
        try:
            return cls(*values)
        except:
            return None

    @classmethod            # перед началом работы переносим заметки из файла в репозиторий Notebook.notes
    def get_from_file(cls):
        filedata = file_read()
        for file_str in filedata:
            new_note = cls.from_string(file_str)
            if new_note is not None:        # пропускаем пустые экземпляры, которые создаются при обнаружении невалидной строки в файле
                cls.notes.append(new_note)
                cls._id_counter = max(cls._id_counter, new_note.id)     #счетчик id выставляем по максимальному из имеющихся

    @staticmethod       #сохранение файла заметок после каждого изменения. преобразование списка в строку
    def put_to_file():
        note_list = Notebook.notes
        filedata = [note.to_string() for note in note_list]
        file_write(filedata)

    @staticmethod                       #поиск индекса элемента по id для последующего удаления или редактирования
    def find_id(find_id):
        for index, note in enumerate(Notebook.notes):
            if note.id == find_id:
                return index
        return None

    @staticmethod                   # два фильтра "от" и "до" по дате создания включая указанную дату, без учета времени
    def find_by_date(start_date, end_date):
        result = Notebook.notes
        if start_date:
            result = [note for note in result if note.mod_time.split(" ")[0] >= start_date]
        if end_date:
            result = [note for note in result if note.mod_time.split(" ")[0] <= end_date]
        return result

    @staticmethod                       # увеличиваем счетчик при создании нового экземпляра
    def get_next_id():
        Notebook._id_counter += 1
        return Notebook._id_counter
