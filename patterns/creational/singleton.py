#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Одиночка - У класса есть только один экземпляр, и он предоставляет к нему глобальную точку доступа.
При попытке создания данного объекта он создаётся только в том случае, если ещё не существует,
в противном случае возвращается ссылка на уже существующий экземпляр и нового выделения памяти не происходит.
"""
def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getinstance


@singleton
class MyClass:
    def __init__(self):
        self.value = 0

    def set_value(self, value):
        self.value = value


if __name__ == "__main__":
    mc1 = MyClass()
    mc1.set_value(value=5)
    print("mc1 value: {}".format(mc1.value))

    mc2 = MyClass()
    print("mc2 value: {}".format(mc2.value))

    mc2.set_value(value=3)
    print("mc1 value: {}".format(mc1.value))
    print("mc2 value: {}".format(mc2.value))
