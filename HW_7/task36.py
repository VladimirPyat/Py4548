# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая
# принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые
# должны быть распечатаны. Нумерация строк и столбцов идет с единицы

def print_operation_table(operation, rows=6, columns=6):

    for i in range(1, rows+1):
        result = list([operation(i, j) for j in range(1, columns + 1)])
        print(*result, sep=' ')


print_operation_table(lambda x, y: x * y)
