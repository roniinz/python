#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

__autor__ = 'паршин и.к'

while True:
    name = input("Введите свое имя: ")
    if re.match('^[A-ZА-Я]+[a-z|а-я]+', name):
        break
    else:
        print('В ведите имя с большой буквы!')

while True:
    surname = input("Введите свою фамилию:")
    if re.match('^[A-ZА-Я]+[a-z|а-я]+', surname):
        break
    else:
        print('В ведите Фамилию с большой буквы!')

while True:
    email = input('В ведите свой эмаил: ')
    if re.match('^[a-z_0-9]+@+[a-z]+\.+(ru|com|org)', email):
        print("Все верно)")
        break
    else:
        print('Почта указана не верно!')
