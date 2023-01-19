"""Игра угадай число
Компьютер сам загадывает и сам угадывает число"""


import numpy as np

def random_progect(number:int=1) -> int:
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

print(f'Количество попыток: {random_progect(10)}')