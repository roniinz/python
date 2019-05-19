#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint as rand

__autor__ = 'паршин и.к'


def genrand():
    i = 0
    lists = []
    lens = rand(10, 25)
    print(lens)
    while lens > i:
        lists.append(rand(-100, 100))
        i += 1

    print(lists)
    return lists


def reserch(lis):
    newlis = []
    for i in lis:
        if int(i) % 3 == 0:
            if int(i) > 0:
                if int(i) % 4 != 0:
                    newlis.append(i)
    return newlis


print(reserch(genrand()))

