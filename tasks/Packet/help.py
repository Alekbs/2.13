#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from datetime import date


def help():
    # Вывести справку о работе с программой.
    print("Список команд:\n")
    print("add - добавить студента;")
    print("select - вывод студентов с оценками 4 и 5;")
    print("list - вывод студентов;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")
    year = date.today().year
    print(year)
