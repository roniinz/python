#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__autor__ = 'паршин и.к'


while True:
    print("В ведите формулу вида y = kx + b")
    equation = input(':')
    x = input("В ведите x:")
    if x.isdigit() == 0:
        print("параметр задан не верно!")
    else:
        pass
    sp = equation.split(' ')
    print(sp)
    a = sp[2]
    print(a[:-1])
    if a[:-1].isdigit() == 0:
        k = float(a[:-1])
    else:
        print("параметр задан не верно!")

    t = sp[4]
    b = float(t)
    y = (k * float(x)) + b

    print(y)
