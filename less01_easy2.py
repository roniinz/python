#!/usr/bin/env Python3
# -*- coding: utf-8 -*-

__autor__ = 'Паршин И.К'

x = input("В ведите число: ")
print(x)

if x.isdigit():
    f = int(x)*2
    print(f)
else:
    print("Это не число!")
