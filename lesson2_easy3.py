#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__autor__ = 'паршин и.к'

l = [10, 2, 3, 5, 5, 7, 9, 23, 5, 5, 71, 90, 32, 13]

new_list = []
for i in l:
    if i % 2 == 0:
        new_l = i / 4
        new_list.append(new_l)
    else:
        new_l = i * 2
        new_list.append(new_l)

print(new_list)