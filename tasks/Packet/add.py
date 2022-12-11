#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def add():
    # Запросить данные о работнике.
    name = input("Фамилия и инициалы? ")
    groop = input("Группа? ")
    marks = [
        int(i) for i in input("Введите оценки по 5 предметам через пробел: ").split()
    ]

    # Создать словарь.
    return {
        "name": name,
        "groop": groop,
        "marks": marks,
    }
