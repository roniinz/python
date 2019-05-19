
def line_reader(data):
    f = open('salary.txt', 'w')
    for key, value in data.items():
        sp = '{} - {} \n'.format(key, value)
        f.writelines(sp)

    f.close()
    a = open('salary.txt', 'r')
    for line in a:
        nd = line.split(' - ')
        if int(nd[1]) > 500000:
            pass
        else:
            print(nd[0], int(nd[1])*0.87)


name = ['vasya', 'vova', 'petr', 'nic', 'igor', 'nioshi', 'affred', 'alla', 'viktor', 'angrey']
plata = [80000, 31000, 100000, 65000, 1000000, 70000, 160000, 323000, 400000, 190000]
a = dict(zip(name, plata))

line_reader(a)

