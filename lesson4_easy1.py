#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

__autor__ = 'паршин и.к'


def rand(weg):
    inter = 0
    lis = []
    while inter < weg:
        lis.append(random.randint(-30, 30))
        inter += 1

    return lis


def lists(num):
    nwl = []
    for nums in num:
        nwl.append(nums**2)

    return nwl


m = input("В ведите длинну списка:")

print(lists(rand(int(m))))
