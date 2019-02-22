#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Прототип - задаёт виды создаваемых объектов с помощью экземпляра-прототипа и создаёт новые объекты путём копирования этого прототипа. Он позволяет уйти от реализации и позволяет следовать принципу «программирование через интерфейсы». В качестве возвращающего типа указывается интерфейс/абстрактный класс на вершине иерархии, а классы-наследники могут подставить туда наследника, реализующего этот тип.
Проще говоря, это паттерн создания объекта через клонирование другого объекта вместо создания через конструктор.
"""
import copy


class Prototype:

    def __init__(self):
        self._objects = {}

    def register_object(self, name: str, obj: object):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name: str):
        """Unregister an object"""
        del self._objects[name]

    def clone(self, name: str, **attr):
        """Clone a registered object and update inner attributes dictionary"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class A:
    def __init__(self):
        self.x = 3
        self.y = 8
        self.z = 15
        self.garbage = [38, 11, 19]

    def __str__(self):
        return '{} {} {} {}'.format(self.x, self.y, self.z, self.garbage)


if __name__ == '__main__':
    a = A()
    prototype = Prototype()
    prototype.register_object('objecta', a)
    b = prototype.clone('objecta')
    c = prototype.clone('objecta', x=1, y=2, garbage=[88, 1])
    print([str(i) for i in (a, b, c)])
