# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = list(input('Введите список цифр через пробел: ').split())
second_list = []

for i in range (len(my_list)):
    str = my_list[i].split(sep='.')
    if len(str) > 1:
        second_list.append(float(str[1])/10) # я не знаю, как превратить 01 во float, чтобы ноль не исчез, поэтому с 1 сотой не работает

max_item = second_list[0]
min_item = second_list[0]

for j in range (len(second_list)):
    if second_list[i] > max_item:
        max_item = second_list[i]
    elif second_list[i] < min_item:
        min_item = second_list[i]

dif = max_item - min_item

print(dif)
