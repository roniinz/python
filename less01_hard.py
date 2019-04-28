#!/usr/bin/env Python3
# -*- coding: utf-8 -*-

__autor__ = 'Паршин И.К'

while True:
    first_name = (input("Введите ваше Имя:"))
    if first_name == "exit":
        break
    second_name = (input("Введите вашу Фамилию:"))
    while True:
        age = (input("Введите свой возраст: "))
        if age.isdigit():
            break
        else:
            print("не верно введен возраст!")

    while True:
        weight = (input("Введите свой Вес: "))
        if weight.isdigit():
            break
        else:
            print("не верно введен вес!")

    state = ['Следует заняться собой', 'Хорошее состояние',
             'Следует обратится к врачу!', 'Хорошо сохранились!']

    if int(age) => 40 and (int(weight) > 120 or int(weight) < 50):
        st = state[2]

    elif int(age) < 30 and (int(weight) < 120 or int(weight) > 50):
        st = state[1]

    elif int(age) > 30 and (int(weight) < 120 or int(weight) > 50):
        st = state[0]

    elif int(age) > 100:
        st = state[3]

    print(first_name, second_name, ',', age, 'год, вес', weight, st)
