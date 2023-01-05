# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в отдельном списке( пример n=4, lst1=[4,-2,1,3] - списко на основе n, а позиции элементов lst2=[3,1].

import random
n = int(input("Введите число(N). N = "))

list = []
for i in range(n):
    from random import randint
    list.append(randint(-n, n))
print(list)

a = list[3]*list[1]
print(a)
