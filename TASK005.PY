# Реализуйте алгоритм перемешивания списка

import random
a = int(input("Введите размерность списка: "))
list = []
for i in range(a):
    from random import randint
    list.append(randint(-10, 10))

print(f"исходный список:\n {list}")
random.shuffle(list)
print(f"список после перемешивания:\n{list}")
