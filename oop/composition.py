"""
Ассоциация описывается словом «имеет». Автомобиль имеет двигатель. Вполне естественно, что он не будет являться наследником двигателя (хотя такая архитектура тоже возможна в некоторых ситуациях).
Композиция - Разновидность ассоциации, экземпляр класса создается внутри.
Двигатель не существует отдельно от автомобиля. Он создается при создании автомобиля и полностью управляется автомобилем.
"""


class Engine:
    def __init__(self, power: int):
        self.power = power

    def get_power(self) -> int:
        return self.power


class Car:
    def __init__(self, model: str):
        # Созадем объект класса двигатель
        self.engine = Engine(power=350)
        self.model = model

    def get_model(self) -> str:
        return self.model


if __name__ == "__main__":
    # Создаем объект класса машина передавая в конструктор объект двигатель
    car = Car(model='audi')