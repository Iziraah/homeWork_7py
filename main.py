import json
from search import search
from entry import enter_person
from delete import delete

g = int(input('Что Вы желаете сделать?\
                1. Поиск? \
                2. Запись?\
                3. Удаление?\
                Ведите цифру: '))
if g ==1:
    search()
elif g == 2:
    enter_person()
elif g == 3:
    delete()
else: print('Некорректный ввод. попробуйте еще раз.')