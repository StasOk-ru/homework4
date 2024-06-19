#homework4
# Создайте переменную my_string и присвойте ей значение строки с произвольным текстом (функция input()).
# Вывести длину символов введённого текста
# 3. Работа с методами строк:
# Используя методы строк, выполните следующие действия:
# Выведите строку my_string в верхнем регистре.
# Выведите строку my_string в нижнем регистре.
# Измените строку my_string, удалив все пробелы.
# Выведите первый символ строки my_string.
# Выведите последний символ строки my_string.
# Примечания:
# Для вывода значений на экран используйте функцию print().
# Для вызова методов строк используйте операцию точки '.'.
# Дополнительно о всех методах строк можно узнать здесь.
# Пример результата выполнения программы:
#
# Код:
# name = input()
# print(name.upper())
#
# Ввод в консоль:
# Urban
#
# Вывод на консоль:
# URBAN

my_string = input('Введите набор слов: ')
length = len(my_string)
#print(my_string[length])
print('Длина строки: ',length)
print('Строка в верхнем регистре: ',my_string.upper())
print('Строка в нижнем регистре: ',my_string.lower())
print('Строка без пробелов: ',my_string.replace(' ',''))
print('Первый символ строки: ',my_string[0])
print('Последний символ строки: ',my_string[-1])
