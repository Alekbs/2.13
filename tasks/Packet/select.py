#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def select(students):
    result = []
    for idx, student in enumerate(students, 1):
        res = all(int(x) > 3 for x in student["marks"])
        if res:
            result.append(student)
    return result
