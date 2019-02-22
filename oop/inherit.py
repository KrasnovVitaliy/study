#coding: utf-8

"""
Наследование - дочерний класс наследует все поля и методы родительского класса.
"""


class Shape:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, new_x: int, new_y: int):
        self.x = new_x
        self.y = new_y

    def get_position(self) -> tuple:
        return self.x, self.y


class Circle(Shape):
    def __init__(self, x: int, y: int, r: int):
        super(Circle, self).__init__(x, y)
        self.r = r

    def get_radius(self) -> int:
        return self.r


if __name__ == "__main__":
    circle = Circle(x=5, y=6, r=10)
    print("Circle position: {}".format(circle.get_position()))
    print("Circle radius: {}".format(circle.get_radius()))

