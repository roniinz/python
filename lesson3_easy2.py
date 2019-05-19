#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__autor__ = 'паршин и.к'



def nums2(f, r, n):
    t = max(f, r, n)
    return t

def nums(x, y, z):
    if x > z and x > y:
        return x

    elif z > x and z > y:
        return z

    elif y > z and y > x:
        return y

    else:
        ops = 'что то не так'
        return ops


a = []
i = 0
while i < 3:
    a.append(input("В ведите число: "))
    i += 1


print(nums(int(a[0]), int(a[1]), int(a[2])))

print(nums(int(a[0]), int(a[1]), int(a[2])))