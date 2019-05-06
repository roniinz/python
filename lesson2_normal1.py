#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__autor__ = 'паршин и.к'


l = [2, -5, 8, 9, -25, 25, 4, 144, 21, 169]
new_list = []
for i in l:
    f = (i ** .5)
    if type(f) == complex:
        pass
    elif f.is_integer():
        new_list.append(f)
    else:
        pass

print(new_list)
