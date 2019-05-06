#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

__autor__ = 'паршин и.к'

while True:
    enum = input("В ведите объем списка :")
    if enum.isdigit():
        break
    else:
        pass

lists = []
i = 0
while int(enum) > i:
    print(i)
    lists.append(random.randint(-100, 100))
    i += 1

print(lists)

