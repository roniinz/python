#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__autor__ = 'паршин и.к'

lst = [1, 2, 4, 5, 6, 2, 5, 2]
print("Вариант а: ", list(set(lst)))
n_lst = []
for i in lst:
    if lst.count(i) == 1:
        n_lst.append(i)

print("Вариант б: ", n_lst)
