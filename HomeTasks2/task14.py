# Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.
# 10 -> 1 2 4 8
from math import *

num = int(input("Введите число: "))
list_num = list()
for i in range(num):
    i = pow(2,i)
    i = int(i)
    if i < num:
        list_num.append(i)

print(f"{num} -> ", *list_num)