# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8
import random

def task_1():
    size = 10
    more_than = 5
    numbers = [random.randint(1,10) for i in range (size)]
    print(f'Cписок случайных чисел от 1 до 10: {numbers}')
    numbers = list(filter(lambda x: x>more_than,numbers))
    print(f'Элементы которые больше чем {more_than}: {numbers}')
    print()
task_1()