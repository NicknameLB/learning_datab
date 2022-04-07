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


f = open('trains.txt', 'r', encoding='utf-8')
dat = []
while True:
    x = f.readline()
    if not x: break
    x = x.split(',')
    train = Train()
    train.wFrom = x[0]
    train.where = x[1]
    train.time = x[2]
    train.tClass = x[3]
    train.travelTime = x[4]
    train.cost = x[5]
    dat.append(train)
    print(train.wFrom, train.where, train.time, train.tClass, train.travelTime, train.cost)

fout = open('trains.dat', 'wb')
pickle.dump(dat, fout)
fout.close()


f = open('trains.dat', 'rb')
newd = pickle.load(f)
f.close()

while True:
    print('Введите число для выполнения одной из операций')
    print('1-вывод БД')
    print('2-выход из программы')
    n = int(input())
    if n == 1:
        end()
        for x in newd:
            print(x.wFrom, x.where, x.time, x.tClass, x.travelTime, x.cost)
        end()
    elif n == 2:
        print('Выйти? Y/N')
        if input() == 'Y':
            exit()
