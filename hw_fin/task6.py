# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя  логирование.

import argparse
import os
import logging
from collections import namedtuple

FileInfo = namedtuple('FileInfo', ['filename', 'extension', 'is_dir', 'parent_dirname'])


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        logging.basicConfig(filename='file_info.txt', level=logging.INFO, filemode='w', encoding='utf-8')
        try:
            result = func(*args, **kwargs)
            for file_info in result:
                logging.info(f"Информация о файле: {file_info}\n")
            return result
        except FileNotFoundError as e:
            logging.error(f"Ошибка: {e}")
        except ValueError as e:
            logging.error(f"Ошибка: {e}")

    return wrapper


@logger_decorator
def create_file_info(path):
    parent_dirname = os.path.basename(path)
    file_info_list = []
    for filename in os.listdir(path):
        full_path = os.path.join(path, filename)
        is_dir = os.path.isdir(full_path)
        extension = os.path.splitext(filename)[1]

        file_info = FileInfo(filename=filename, extension=extension, is_dir=is_dir, parent_dirname=parent_dirname)
        file_info_list.append(file_info)

    return file_info_list

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Dir info')
    parser.add_argument('path', metavar='path', type=str, nargs=1, help='directory path')
    args = parser.parse_args()
    create_file_info(args.path[0])

