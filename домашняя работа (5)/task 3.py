# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают Список уникальных элементов
# [1, 4, 2, 3, 6, 7]

def task_3():
    size = 10
    random_list = list(random.randint(1, 10) for i in range(size))
    print(f'Cписок случайных чисел от 1 до 10: {random_list}')

    same = list(map(lambda x: list.count(random_list, x) > 1, random_list)).count(True)


    print(f'Количество совпадающих элементов: {same}')

    print(f"Список уникальных элементов {list(set(random_list))}")
    print()
task_3()
