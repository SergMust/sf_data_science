"""Игра угадай число
Компьютер сам загадывает и сам угадывает число"""

import numpy as np

def random_predict(number: int = 1) -> int:
    """Рандомно компьютер загадывает число

    Args:
        number (int, optional): Загадываем число. Default to 1.

    Returns:
        int: Число попыток
    """

    a = 1 # минимальное значение диапазона
    b = 101 # максимальное значение диапазона
    number = np.random.randint(a, b) # Компьютер загадывает число
    count = 0
    while a != b: # выполняем цикл пока значения границ диапазона не равны
        count += 1
        average_value = int((a+b) // 2) # вычисляем среднее значение диапазона
        if number <= average_value: 
            b = average_value  # если число меньше  среднего значения, 
            # то это значение становиться максимальной границей диапазона
        elif number > average_value:
            a = average_value + 1 # если число больше среднего значения, 
            # то это значение становиться минимальной границей диапазона + 1
        else:
            break # выход из цикла если угадали
    
    return count  
        

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    a = 1
    b = 101
    count_ls = []  # список для сохранения количества попыток
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(a, b, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))  # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return (score)


if __name__=='__main__':
    score_game(random_predict)
 