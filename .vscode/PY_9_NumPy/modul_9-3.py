import numpy as np
np.random.seed(23)
np.random.randint(10, size=(3,4))
# array([[3, 6, 8, 9],
#        [6, 8, 7, 9],
#        [3, 6, 1, 2]])
np.random.seed(100)
print(np.random.randint(10, size=3))
# [8 8 3]
print(np.random.randint(10, size=3))
# [7 7 0]
print(np.random.randint(10, size=3))
# [4 2 5]

#   В simple сохраните случайное число в диапазоне от 0 до 1

#    Сгенерируйте 120 чисел в диапазоне от -150 до 2021, сохраните их в переменную randoms

#    Получите массив из случайных целых чисел от 1 до 100 (включительно) из 3 строк и 2 столбцов. Сохраните результат в table

#    В переменную even сохраните четные числа от 2 до 16 (включительно)

 #   Скопируйте even в переменную mix. Перемешайте числа в mix так, чтобы массив изменился

 #   Получите из even 3 числа без повторений. Сохраните их в переменную select

 #   Получите переменную triplet, которая должна содержать перемешанные значения из массива select (сам select измениться не должен)


import numpy as np
np.random.seed(2021)
simple = np.random.rand()
randoms = np.random.randint(-1506, 2021, size=(120))
table = np.random.randint(1, 101, size=(3,2))
even = list(range(2, 17, 2))
mix = np.random.permutation(even)
select = np.random.choice(even, size=3, replace=False)
triplet = np.random.permutation(select)
print(triplet)

# Введите свое решение ниже
import numpy as np
np.random.seed(2021)
# В simple сохранте случайное число в диапазоне от 0 до 1
simple = np.random.rand()

# Сгенерируйте 120 чисел в диапазоне от -150 до 2021, сохраните их
# в переменную randoms
randoms = np.random.uniform(-150, 2021, size=120)

# Получите массив из случайных целых чисел от 1 до 100 (включительно)
# из 3 строк и 2 столбцов. Сохраните результат в table
table = np.random.randint(1, 101, size=(3,2))

# В переменную even сохраните четные числа от 2 до 16 (включительно)
even = np.arange(2,17,2)

# Скопируйте even в переменную mix. Перемешайте числа в mix так, чтобы массив mix изменился
mix = even.copy()
np.random.shuffle(mix)

# Получите из even 3 числа без повторений. Сохраните их в переменную select
select = np.random.choice(even, replace=False, size=3)

# Получите переменную triplet, которая должна содержать перемешанные
# значения из массива select (сам select измениться не должен)
triplet = np.random.permutation(select)

