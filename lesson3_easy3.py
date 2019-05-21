#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__autor__ = 'паршин и.к'


def multi_len(*args):
    max_lens = 0
    a = len(str(args))
    print(a)
    if args == 'stop':
        return max_lens
    if a > max_lens:
        max_lens = a


f = input("В ведите сроки или stop для остановки:")
print(multi_len(f))
