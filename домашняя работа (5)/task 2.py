# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, описывающие возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

def task_2(user_list):
    
    random_list = []
    random_list.append(user_list[0])
    for i in range(len(user_list)):
        if user_list[i] in random_list:
            continue
        elif user_list[i] > user_list[0] and user_list[i] > random_list[len(random_list)-1]:
            random_list.append(user_list[i])
    return random_list

size = 20
random_list = list(random.randint(1, 30) for i in range(size))
print(f'Случайный список: {random_list}')

result = (f'Случайная возрастающая последовательность: {task_2(random_list)}') 
print(result)
print()