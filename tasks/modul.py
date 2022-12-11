#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_func(tag):
    def func(string):
        string = ["<", tag, ">", string, "</", tag, ">"]
        return "".join(string)

    return func
