# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму
n = int(input("Введите число (N). N = "))

list = []
for i in range(1, n+1):
    number = round((1+(1/i))**i, 2)
    list.append(number)

print(list)
print(sum(list))
