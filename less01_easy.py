__autor___ = 'Паршин И.К'


a = input("Введите число: ")
x = 0
print(a)
b = 0
print('Длинна а =', len(a))

while len(a) >= x:
    print("Итерация:", x)
    c = list(str(a[x]))
    print(c)
    if int(c) > b:
        b = int(c)
        print(b)
    else:
        pass

print('Итог', b)

