# for_review
from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        super().__init__()
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started == False:
            if self.fuel > 0:
                self.started = True
                print("Fuel in the tank!")
            else:
                raise LowFuelError("Warning!No fuel in the tank!")

    def move(self, distance):
        required_fuel = distance * self.fuel_consumption
        if self.fuel >= required_fuel:
            self.fuel -= required_fuel
            print(f"Vehicle can cover a distance of {distance} km")
        else:
            raise NotEnoughFuel("Warning!Not enough fuel to cover the required distance!")
