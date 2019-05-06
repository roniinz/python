#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
__autor__ = 'паршин и.к'

table = {1: '31', 2: '28',
         3: '31', 4: '30',
         5: '31', 6: '30',
         7: '31', 8: '31',
         9: '30', 10: '31',
         11: '30', 12: '31'
         }

d_week = {1: "Понедельник",
          2: "Вторник",
          3: "Среда",
          4: "Четверг",
          5: "Пятница",
          6: "Суббота",
          0: "Воскресенье"}

ower = 'Вы ввели в не верном формате!'

while True:
    date = input('В ведите дату числами:')
    d = date.split(".")
    day = d[0].isdigit()
    mount = d[1].isdigit()
    yers = d[2].isdigit()
    if day == 0:
        print("Не прравильный введен день!")
        pass
    elif mount == 0:
        print("Не правильно введен месяц!")
        pass
    elif yers == 0:
        print("Не правильно введен год!")
        pass
    else:
        if len(d[0]) == 2 and len(d[1]) == 2 and len(d[2]) == 4:
            if int(d[1]) <= 12:
                dd = table.get(int(d[1]))
                print(dd)
                if int(d[1]) == 2 and int(d[0]) == 29 and (int(d[2]) % 4) == 0:
                    print("это февраль высокосного года!!!")

                elif int(d[0]) <= int(dd):
                    dictlist = []
                    dsumm = 0
                    for key, value in table.items():
                        if int(d[1]) == key:
                            print(key, value)
                            break
                        else:
                            temp = [key, value]
                            print(value)
                            dsumm += int(value)

                    summ = (int(d[0])-1) + dsumm
                    all_day = (365 * (int(d[2]) - 1)) + summ + (int(d[2]) // 4)
                    m_d = all_day % 7
                    print('Дата верная!', 'день недели: ', d_week.get(m_d))
                else:
                    print(ower)
            else:
                print(ower)
        else:
            print(ower)
