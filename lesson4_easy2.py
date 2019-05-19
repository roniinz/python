#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint as rand

__autor__ = 'паршин и.к'


def genfruitlist():
    i = 0
    fru = []
    while i < rand(14, 19):
        fru.append(fruit[rand(0, 23)])
        i += 1
    return fru


def sprend(fruit1, fruit2):
    print(fruit1, fruit2, sep='\n')
    newfru = []
    for i in fruit1:
        for ix in fruit2:
            if i == ix:
                newfru.append(ix)
            else:
                pass

    return newfru


fruit = ['Банан', 'Абрикос', 'Ава', 'Апельсин',
         'Арбуз', 'Алыча', 'Виноград', 'Гранат',
         'Грейпфрут', 'Груша', 'Гуава', 'Дыня',
         'Инжир', 'Канталупа', 'Карамбола', 'Киви',
         'Красный банан', 'Лимон', 'Лайм',
         'Манго', 'Марания', 'Мушмула', 'Пепино',
         'Персик', 'Питайя', 'Помело', 'Сахарное яблоко',
         'Физалис', 'Финик', 'Хурма', 'Гуарана']


print(sprend(genfruitlist(), genfruitlist()))
