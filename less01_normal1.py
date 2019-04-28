#!/usr/bin/env Python3
# -*- coding: utf-8 -*-

__autor__ = 'Паршин И.К'

while True:
    num = input("Введите число: ")
    if num.isdigit() == 1:
        if int(num) > 0 and int(num) < 11:
            print(int(num)**2)
            break
        else:
            pass
    else:
        print(num, "Это не число!")
