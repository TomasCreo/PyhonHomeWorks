# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

def pow_of_numbers(a, b):
    if b == 1:
        return a
    else:
        return a * pow_of_numbers(a, b - 1)

a = int(input("Введите число: "))
b = int(input("Введите стпень: "))
print("Результат: ", pow_of_numbers(a, b))