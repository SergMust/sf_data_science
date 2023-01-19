"""Игра угадай число
Компьютер сам загадывает и сам угадывает число"""


import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число
    
    Args:
        number (int, optional): Загадываем число. Default to 1.
        
    Returns:
        int: Число попыток
    """

    count = 0

    while True:
        count+=1
        predict_number = np.random.randint(1, 101) # предполагаемое число
    
        if predict_number == number:
            break
    
    return(count) # выход из циклаесли угадали

#print(f'Количество попыток: {random_progect(10)}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


if __name__=='__main__':
    # RUN
    score_game(random_predict)