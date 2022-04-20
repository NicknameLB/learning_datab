import pickle


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
    print('0-выход из программы')
    n = int(input())
    if n == 1:
        end()
        for x in newd:
            print(x.wFrom, x.where, x.time, x.tClass, x.travelTime, x.cost)
        end()
    elif n == 2:
        try:
            with open(input('Введите название файла: '), 'wb') as f:
                newd = pickle.load(f)
                f.close()
        except OSError:
            print('Не удалось создать файл')
        else:
            print('Файл успешно создан')

    elif n == 0:
        print('Выйти? Y/N')
        if input() == 'Y':
            exit()
