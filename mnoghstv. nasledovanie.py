class Vehicle:
    def __init__(self):
        self.vehicle_type = "none"


class Car:
    def __init__(self):
        super().__init__()
        self.price = 1000000

    def horse_powers(self):
        return 200


class Nissan(Car, Vehicle):
    def __init__(self):
        super().__init__()
        self.vehicle_type = "Auto"
        self.price = 1500000

    def horse_powers(self):
        return 250


car = Nissan()
print(car.vehicle_type)
print(car.price)

