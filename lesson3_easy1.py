#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__autor__ = 'паршин и.к'


def my_func(*args):
    i = '{}, {} год(а), проживает в городе {}'.format(args[0], args[1], args[2])
    return i


name = input("введите свое имя: ")
age = input("введите свой возраст:")
city = input("введите город:")

print(my_func(name, age, city))
