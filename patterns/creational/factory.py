# coding: utf-8

"""
Фабрика - создает объект заданного типа
"""


class Circle:
    def __init__(self):
        self.name = 'circle'


class Square:
    def __init__(self):
        self.name = 'square'


class Factory:
    def get_object(self, obj_type: str) -> object:
        """
        Return object for given type name
        :param obj_type: object type name
        :return: object
        """

        ret_obj = None

        if obj_type == 'circle':
            ret_obj = Circle()

        elif obj_type == 'square':
            ret_obj = Square()

        return ret_obj


if __name__ == "__main__":
    obj1 = Factory().get_object('circle')
    print(obj1.name)

    obj2 = Factory().get_object('square')
    print(obj2.name)
