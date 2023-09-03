#№1# # В предложение были добавлены лишние пробелы.
# # Напишите функцию, которая будет принимать такое
# # предложение и возвращать его же в исправленном виде.
#
# def correct(text):
#     text = text.replace('  ', ' ')
#     return text
# text = input('Введите предложение: ')
# print(correct(text))

#№2# Заданы длины сторон треугольника. Определить, является ли этот треугольник прямоугольным.
# Входные данные
# Три натуральных числа - длины сторон треугольника, не превышающие 1000.
# Выходные данные
# Вывести "YES", если треугольник прямоугольный, и "NO" в противном случае.

# def triangle(a, b, c):
#     if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == b**2:
#         return 'YES'
#     else:
#         return 'NO'
# a = int(input('input length of side a: '))
# b = int(input('input length of side b: '))
# c = int(input('input length of side c: '))
# print('right triangle(a, b, c)',triangle(a, b, c))