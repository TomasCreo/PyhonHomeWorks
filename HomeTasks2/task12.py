# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

# Примеры/Тесты:
# 4 4 -> 2 2
# 5 6 -> 2 3
# Решение через циклы
# from math import *

# first_number, second_number = int(input("Сумма чисел: ")), int(input("Произведение чисел: "))
# for i in range(1, first_number+1):
#     for j in range(1, first_number+1):
#         if i + j == first_number and i * j == second_number:
#             print(f"Задуманные Петей Числа {first_number} {second_number} -> {i} {j}")
            
# Решение через алгебру
import math
def find_numbers(S, P):
    D = S**2 - 4 * P
    
    if D < 0:
        return None

    X1 = (S + math.sqrt(D)) / 2
    X2 = (S - math.sqrt(D)) / 2
    
    if X1 > 0 and X1.is_integer() and X2 > 0 and X2.is_integer():
        return (int(X1), int(X2))
    elif X1 > 0 and X1.is_integer():
        return (int(X1),)
    elif X2 > 0 and X2.is_integer():
        return (int(X2),)
    else:
        return None

S=int(input("Введите первое число "))
P=int(input("Введите второе число "))
print(find_numbers(S, P))