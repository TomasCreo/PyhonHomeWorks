# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = [int(input("Введите число: ")) for i in range(int(input("Введите размер множества 1: ")))]
m = [int(input("Введите число: ")) for i in range(int(input("Введите размер множества 2: ")))]
n = set(n)
m = set(m)

print(m.intersection(n))