
import numpy as np

# Напишите функцию get_chess, которая принимает на вход длину стороны квадрата a
#
# и возвращает двумерный массив формы (a, a), заполненный 0 и 1 в шахматном порядке.
#
# В левом верхнем углу всегда должен быть ноль.

def get_chess(a):
    zarray = np.zeros((a, a), dtype=float)
    zarray[::2, 1::2] = 1
    zarray[1::2, ::2] = 1
    return zarray
print(get_chess(7))
print()

"""Вы разрабатываете приложение для прослушивания музыки. Конечно же, там будет 
доступна функция перемешивания плейлиста. Пользователю может настолько понравиться 
перемешанная версия плейлиста, что он захочет сохранить его копию. Однако вы не хотите 
хранить в памяти новую версию плейлиста, а просто хотите сохранять тот seed, с которым 
он был сгенерирован.

Для этого напишите функцию shuffle_seed(array), которая принимает на вход массив
 из чисел, генерирует случайное число для seed в диапазоне от 0 до 2**32 - 1 (включительно) 
 и возвращает кортеж: перемешанный с данным seed массив (исходный массив должен 
 оставаться без изменений), а также seed, с которым этот массив был получен."""

import numpy as np
array = [1, 2, 3, 4, 5]
def shuffle_seed(array):
    n = 2**16-1
    rand_seed = np.random.randint(0, n)
    np.random.seed(rand_seed)
    seed_array = array
    np.random.shuffle(seed_array)
    return seed_array, rand_seed
print(shuffle_seed(array))
print()

"""Напишите функцию min_max_dist(*vectors), которая принимает на вход неограниченное 
число векторов через запятую. Гарантируется, что все векторы, которые передаются,
 одинаковой длины.

Функция возвращает минимальное и максимальное расстояние между векторами в виде кортежа."""

vec1 = np.array([1,2,3])
vec2 = np.array([4,5,6])
vec3 = np.array([7, 8, 9])
vec4 = np.array([10, 11, 12])

import numpy as np
def min_max_dist(*vectors):

    result = []
    for i in range(len(vectors)):
        for j in range(i+1, len(vectors)):
            result.append(np.linalg.norm(vectors[i] - vectors[j]))
    return(min(result), max(result))
print(min_max_dist(vec1, vec2, vec3, vec4))
print()

"""Напишите функцию any_normal, которая принимает на вход неограниченное число векторов 
через запятую. Гарантируется, что все векторы, которые передаются, одинаковой длины.

Функция возвращает True, если есть хотя бы одна пара перпендикулярных векторов.
 Иначе возвращает False"""

vec1 = np.array([2, 1])
vec2 = np.array([-1, 2])
vec3 = np.array([3,4])
import numpy as np
def any_normal (*vectors):

    for i in range(len(vectors)):
        for j in range(i + 1, len(vectors)):
            if np.dot(vectors[i], vectors[j]) == 0:
                return True
            else:
                return False

print(any_normal(vec1, vec2, vec3))
print()

"""Напишите функцию get_loto(num), генерирующую трёхмерный массив случайных целых чисел
 от 1 до 100 (включительно). Это поля для игры в лото.

Трёхмерный массив должен состоять из таблиц чисел формы 5х5, то есть итоговая форма —
 (num, 5, 5).

Функция возвращает полученный массив."""

import numpy as np
def get_loto(num):
    number = np.random.randint(1, 101, size=(num,5,5))

    return number
print(get_loto(3))
print()

"""Напишите функцию get_unique_loto(num). Она так же, как и функция в задании 10.10, 
генерирует num полей для игры в лото, однако теперь на каждом поле 5х5 числа не могут
 повторяться.

Функция также должна возвращать массив формы num x 5 x 5."""

import numpy as np

def get_unique_loto(num):
    in_list = np.arange(1,101)
    array = []
    for i in range(num):
        array.append(np.random.choice(in_list, size=(5, 5), replace=False))

    return np.array(array)

print(get_unique_loto(3))
print()

simplelist = [19, 242, 14, 152, 142, 1000]
l = np.average(simplelist)
print(l)