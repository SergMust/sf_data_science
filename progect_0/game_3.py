"""Игра угадай число
Компьютер сам загадывает и сам угадывает число"""

import numpy as np

def half_division(number) -> int:
    """Рандомно компьютер загадывает число

    Args:
        number (int, optional): Загадываем число. 

    Returns:
        int: Число попыток
    """

    min_value = 1 # минимальное значение диапазона
    max_value = 101 # максимальное значение диапазона
    number = np.random.randint(min_value, max_value) # Компьютер загадывает число
    count = 0
    while min_value != max_value: # выполняем цикл пока значения границ диапазона не равны
        count += 1
        average_value = int((min_value+max_value) // 2) # вычисляем среднее значение диапазона
        if number < average_value: 
            max_value = average_value  # если число меньше  среднего значения, 
            # то это значение становиться максимальной границей диапазона
        elif number > average_value:
            min_value = average_value + 1 # если число больше среднего значения, 
            # то это значение становиться минимальной границей диапазона + 1
        else:
            break # выход из цикла если угадали
    
    return count  
        

def score_game(half_division) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    min_value = 1
    max_value = 101
    count_ls = []  # список для сохранения количества попыток
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(min_value, max_value, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(half_division(number))

    score = int(np.mean(count_ls))  # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return (score)


if __name__=='__main__':
    score_game(half_division)
 