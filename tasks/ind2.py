#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from Packet.select import select
from Packet.list import list
from Packet.add import add
from Packet.help import help


def main():
    # Список работников.
    students = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == "exit":
            break

        elif command == "add":
            student = add()
            # Добавить словарь в список.
            students.append(student)
            # Отсортировать список в случае необходимости.

            if len(students) > 1:
                students.sort(
                    key=lambda item: sum(item["marks"]) / len(item["marks"]),
                    reverse=True,
                )

        elif command == "list":
            list(students)

        elif command == "select":
            list(select(students))

        elif command == "help":
            help()
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == "__main__":
    main()
