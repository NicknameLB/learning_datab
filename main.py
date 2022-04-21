import pickle
import operator
from datetime import datetime
import cowsay
cowsay.cow('Добро пожаловать в систему управления электричками')

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
    print('3-корректировка или дополнение расписания')
    print('4-Сортировка')
    print('0-выход из программы')
    n = int(input())
    try:
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
                print('\033[91m' + 'Не удалось создать файл' + '\033[0m')
            else:
                print('Файл успешно создан')
        elif n == 3:
            s = input('Выберете, что вы хотетите сделать: редактировать или дополнить расписание: ')
            if s == 'редактировать':
                s = input(
                    'Введите через запятую, без пробелов место отправления, место прибытия и время отправления, распиание которых вы '
                    'хотите редактировать: ').split(',')
                f = False
                for x in newd:
                    if x.wFrom == s[0] and x.where == s[1] and x.time == s[2]:
                        f = True
                        new = input(
                            'Введите через пробел: новое время отправления в формате (10:10), класс, время поездки в '
                            'формате (1ч 1мин), цену в формате (100р) которые вы хотите '
                            'редактировать: ').split()
                        x.time = new[0]
                        x.tClass = new[1]
                        x.travelTime = new[2] + ' ' + new[3]
                        x.cost = new[4] + '\n'
                if not f:
                    print(
                        '\033[91m' + 'В нашем расписании нет поезда с данными местом отправления и местом прибытия' + '\033[0m')
                    continue
            elif s == 'дополнить' or s == 'дополнить расписание':
                s = input(
                    'Введите через запятую, без пробелов место отправления, место прибытия, время отправления в формате (10:10), '
                    'класс, время поездки в формате (1ч 1мин), цену в формате (100р): ').split(',')
                new_train = Train()
                new_train.wFrom = s[0]
                new_train.where = s[1]
                new_train.time = s[2]
                new_train.tClass = s[3]
                new_train.travelTime = s[4] + ' ' + s[5]
                new_train.cost = s[6] + '\n'
                newd.append(new_train)
            else:
                print('\033[91m' + 'Вы ввели некорректную комманду' + '\033[0m')
                continue
            f = open('trains.dat', 'wb+')
            pickle.dump(newd, f)
            f.close()
            print('База данных успешно обновлена')
        elif n == 4:
            a = []
            for x in newd:
                a.append(x)
            typeS = input(
                'Введите параметр сортировки (станции отправления, станции назначения, время отправления, '
                'время в пути):')
            if typeS == 'станции отправления':
                a = sorted(a, key=operator.attrgetter('wFrom'))
            elif typeS == 'станции назначения':
                a = sorted(a, key=operator.attrgetter('where'))
            elif typeS == 'время отправления':
                a.sort(key=lambda date: datetime.strptime(date.time, '%H:%M'))
            elif typeS == 'время в пути':
                a.sort(key=lambda date: datetime.strptime(date.travelTime, '%Hч %Mмин'))
            else:
                print('\033[91m' + 'Вы ввели некорректную комманду' + '\033[0m')
                continue
            end()
            for x in a:
                print(x.wFrom, x.where, x.time, x.tClass, x.travelTime, x.cost)

        elif n == 0:
            print('Выйти? Y/N')
            if input() == 'Y':
                break
            else:
                print('Возвращение к программе')
                end()
    except:
        print('\033[91m' + 'В программе произошла ошибка' + '\033[0m')