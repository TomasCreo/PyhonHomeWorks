from random import *

n = int(input("Введите размер грядки: "))
my_list = [randint(1, 10) for i in range(n)]

print(my_list)
max_value = 0

for i in range(len(my_list)):
    if i == n-1:
        temp = my_list[i] + my_list[i-1] + my_list[0]
        if max_value < temp:
            max_value = temp
    else:
        temp = my_list[i] + my_list[i-1] + my_list[i+1]
        if max_value < temp:
            max_value = temp
print(max_value)
