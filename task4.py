# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

 # остаок от деления на два записываем как цифру в массив, а целочисленный результат снова делим на 2. 

a = int(input('Введите десятичное число: '))
result = a
binary = []

while result != 0:
    binary.append(result%2)
    result = result//2

binary.reverse()

binary_str = str()

for i in range (len(binary)):
    binary_str = binary_str+str(binary[i])

print(binary_str)



