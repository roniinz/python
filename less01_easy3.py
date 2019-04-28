#!/usr/bin/env Python3
# -*- coding: utf-8 -*-

__autor__ = 'Паршин И.К'

age = input("Введите свой возраст: ")
if int(age) > 18 and age.isdigit() == 1:
    print("Добро пожаловать!")
else:
    print("Доступ запрешен!")
