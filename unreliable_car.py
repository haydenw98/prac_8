from random import randint
from car import Car


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        chance = randint(1, 100)
        if chance > self.reliability or chance == self.relaibility:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
