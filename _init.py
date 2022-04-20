import pickle


class Train:
    wFrom = None
    where = None
    time = None
    tClass = None
    travelTime = None
    cost = None

f = open('trains.txt', 'r', encoding='utf-8')
dat = []
while True:
    x = f.readline()
    print('x')
    if not x or  x == 'end':
        print('xx')
        break
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