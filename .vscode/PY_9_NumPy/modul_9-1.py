# Дан список кортежей ratings с рейтингами кафе. Кортеж состоит из названия и рейтинга кафе.
#
# Необходимо отсортировать кортеж по убыванию рейтинга. Если рейтинги совпадают, то отсортировать кафе дополнительно по названию в алфавитном порядке.
#
# Получите словарь cafes с упорядоченными ключами из отсортированного списка, где ключи — названия кафе, а значения — их рейтинг.

from collections import OrderedDict

ratings = [('Old York', 3.3), ('New Age', 4.6), ('Old Gold', 3.3), ('General Foods', 4.8),
           ('Belissimo', 4.5), ('CakeAndCoffee', 4.2), ('CakeOClock', 4.2), ('CakeTime', 4.1),
           ('WokToWork', 4.9), ('WokAndRice', 4.9), ('Old Wine Cellar', 3.3), ('Nice Cakes', 3.9)]

ratings.sort(key=lambda x: (-x[1], x[0]))
cafes = OrderedDict(ratings)
print(cafes)
print()

# Напишите функцию brackets(line), которая определяет, является ли последовательность из круглых скобок line правильной.
# Посимвольно переберите строку. Если встретилась открывающаяся скобка, положите её в стек. Если встретилась закрывающаяся скобка, извлеките скобку из стека.
#
#     Если стек пустой, то есть извлечь скобку нельзя, последовательность неправильная.
#     Если строка закончилась и стек стал пустым, последовательность правильная.
#     Если в стеке остались скобки, последовательность неправильная.
def brackets(line):
    meet = 0
    for i in line:
        if i == '(':
            meet += 1
        elif i == ')':
            meet -= 1
            if meet < 0:
                return False
    return meet == 0


print(brackets("(()())"))
print(brackets(""))
print(brackets("(()()))"))
print()

from collections import defaultdict
from collections import deque
tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]

# Напишите функцию task_manager(tasks), которая принимает список задач tasks для нескольких серверов. Каждый элемент списка состоит из кортежа (<номер задачи>, <название сервера>, <высокий приоритет задачи>).
#
# Функция должна создавать словарь и заполнять его задачами по следующему принципу: название сервера — ключ, по которому хранится очередь задач для конкретного сервера.
#
# Если поступает задача без высокого приоритета (последний элемент кортежа — False), добавить номер задачи в конец очереди. Если приоритет высокий, добавить номер в начало.
#
# Для словаря используйте defaultdict, для очереди — deque.
#
# Функция возвращает полученный словарь с задачами.
#
# Пример
#
# tasks = [(36871, 'office', False),
# (40690, 'office', False),
# (35364, 'voltage', False),
# (41667, 'voltage', True),
# (33850, 'office', False)]
#
# print(task_manager(tasks))
# # defaultdict(, {'voltage': deque([41667, 35364]),
# # 'office': deque([36871, 40690, 33850])})
def task_manager(tasks):
    servers = defaultdict(deque)
    for task in tasks:
        if task[-1]:
            servers[task[1]].appendleft(task[0])
        else:
            servers[task[1]].append(task[0])
    return servers
print(task_manager(tasks))









