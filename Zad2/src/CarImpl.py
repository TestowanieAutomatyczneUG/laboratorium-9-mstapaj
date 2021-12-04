from src.Car import Car


class CarImpl:
    def __init__(self, car: Car):
        self.car = car

    def car_checkFuel(self):
        if self.car.needsFuel():
            return 'Paliwo w normie'
        return 'Mało paliwa'

    def car_checkEngineTemperature(self):
        if self.car.getEngineTemperature() > 100:
            return 'Za wysoka temperatura silnika'
        return 'Temperatura silnika w normie'

    def car_setDesitnation(self, destination):
        return f'Cel ustawiono na {destination}'
