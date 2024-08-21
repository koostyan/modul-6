class Car:
    price = 1000000

    def horse_powers(self):
        return 200


class Nissan(Car):
    price = 1500000

    def horse_powers(self):
        return 250


class Kia(Car):
    price = 1200000

    def horse_powers(self):
        return 220


car1 = Nissan()
car2 = Kia()

print("Цена автомобиля Nissan:", car1.price)
print("Лошадиные силы автомобиля Nissan:", car1.horse_powers())

print("Цена автомобиля Kia:", car2.price)
print("Лошадиные силы автомобиля Kia:", car2.horse_powers())
