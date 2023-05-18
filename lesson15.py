print("Задание 1")

class Transport:
   def __init__(self, name, max_speed, mileage):
    self.name = name
    self.max_speed = max_speed
    self.mileage = mileage
    def seating_capacity(self, capacity):
       return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"

Autobus = Transport("Renaul Logan", 180, 12)
print(f"Название автомобиля: {Autobus.name} Скорость: {Autobus.max_speed} Пробег: {Autobus.mileage}")

print("Задание 2")

class Autobus(Transport):
    capacity = 50
    def seating_capacity(self):
       return f"Вместимость одного автобуса {self.name}  {self.capacity} пассажиров"

Real_autobus = Autobus("Renaul Logan", 180, 12)
print(Real_autobus.seating_capacity())