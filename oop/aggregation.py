#coding: utf-8

"""
Ассоциация описывается словом «имеет». Автомобиль имеет двигатель. Вполне естественно, что он не будет являться наследником двигателя (хотя такая архитектура тоже возможна в некоторых ситуациях).
Аггрегация - Разновидность ассоциации, экземпляр класса создается вне и передается в конструктор аргументом.
"""


class Engine:
    def __init__(self, power: int):
        self.power = power

    def get_power(self) -> int:
        return self.power


class Car:
    def __init__(self, engine: object, model: str):
        self.engine = engine
        self.model = model

    def get_model(self) -> str:
        return self.model


if __name__ == "__main__":
    # Созадем объект класса двигатель
    engine = Engine(power=350)

    # Создаем объект класса машина передавая в конструктор объект двигатель
    car = Car(engine=engine, model='audi')
