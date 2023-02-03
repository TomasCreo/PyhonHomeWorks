#  Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X

from random import *

N = int(input("Введите размер массива: "))
X = int(input("Введите число для поиска бижайшего числа в массиве:"))

my_list = [randint(1, 100) for i in range(N)]
print(my_list)
my_list.append(X)
print(my_list)
list.sort(my_list)
print(my_list)
if X == my_list[0]:
    print(my_list[1])
else:
    b = my_list.index(X)
    b = b-1
    print(my_list[b])