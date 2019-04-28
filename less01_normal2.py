#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__autor__ = 'паршин и.к'


a = input("Введите первое число: ")
b = input("Введите второе число: ")

if a.isdigit():
    pass
else:
    print("Вы вели не число!")

if b.isdigit():
    pass
else:
    print("Вы вели не число!")

a = int(a)+int(b)
b = int(a)-int(b)
a = int(a)-int(b)

print("переменная а =", a)
print("переменная b =", b)
