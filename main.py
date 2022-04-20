import pickle
import operator
from datetime import datetime


class Train:
    wFrom = None
    where = None
    time = None
    tClass = None
    travelTime = None
    cost = None


def end():
    print('-' * 25)
    print()


f = open('trains.dat', 'rb')
newd = pickle.load(f)
f.close()

while True:
    print('Введите число для выполнения одной из операций')
    print('1-вывод расписания')
    print('2-запись в файл')
    print('4-Сортировка')
    print('0-выход из программы')
    n = int(input())
    if n == 1:
        end()
        for x in newd:
            print(x.wFrom, x.where, x.time, x.tClass, x.travelTime, x.cost)
        end()
    elif n == 2:
        try:
            with open(input('Введите название файла: '), 'wb+') as f:
                pickle.dump(newd, f)
        except OSError:
            print('Не удалось создать файл')
        else:
            print('Файл успешно создан')
    elif n == 4:
        a = []
        for x in newd:
            a.append(x)
        typeS = input(
            'Введите параметр сортировки (станции отправления, станции назначения, время отправления, время в пути):')
        if typeS == 'станции отправления':
            a = sorted(a, key=operator.attrgetter('wFrom'))
        elif typeS == 'станции назначения':
            a = sorted(a, key=operator.attrgetter('where'))
        elif typeS == 'время отправления':
            a.sort(key=lambda date: datetime.strptime(date.time, '%H:%M'))
        elif typeS == 'время в пути':
            a.sort(key=lambda date: datetime.strptime(date.travelTime, '%Hч %Mмин'))
        end()
        for x in a:
            print(x.wFrom, x.where, x.time, x.tClass, x.travelTime, x.cost)



    elif n == 0:
        print('Выйти? Y/N')
        if input() == 'Y':
            exit()
