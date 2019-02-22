# coding: utf-8

"""
Строитель - строитель предоставляет способ создания составного объекта
"""


class Animal:
    """
    Абстрактное Животное
    """

    def __init__(self, legs=0, tail=False, roar=''):
        self.legs = legs
        self.tail = tail
        self.roar = roar


class Mutator:
    """
    Ответственный за размножение
    """

    def mutate(self):
        self.animal = Animal()


class Cat(Mutator):
    """
    Кошка
    """

    def create_legs(self):
        self.animal.legs = 4

    def create_tail(self):
        self.animal.tail = True

    def create_roar(self):
        self.animal.roar = 'meowww!'


class Dog(Mutator):
    """
    Собака
    """

    def create_legs(self):
        self.animal.legs = 4

    def create_tail(self):
        self.animal.tail = True

    def create_roar(self):
        self.animal.roar = 'woffff!'


class AnimalOwner:
    """
    Владелец питомника
    """
    __mutator = None

    def set_animal(self, mutator):
        self.__mutator = mutator

    def create_an_animal_for_me(self):
        self.__mutator.mutate()
        self.__mutator.create_legs()
        self.__mutator.create_tail()
        self.__mutator.create_roar()

    def get_animal(self):
        return self.__mutator.animal


if __name__ == "__main__":
    c = Cat()
    d = Dog()
    ao = AnimalOwner()
    ao.set_animal(mutator=c)
    ao.create_an_animal_for_me()
    animal = ao.get_animal()
    print(animal.roar)
