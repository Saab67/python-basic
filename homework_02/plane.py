from . base import Vehicle
from . exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0, max_cargo=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, cargo_amount):
        if self.cargo + cargo_amount <= self.max_cargo:
            self.cargo += cargo_amount
            print("Cargo on the plane!")
        else:
            raise CargoOverload("Overload!")

    def remove_all_cargo(self):
        previous_cargo = self.cargo
        self.cargo = 0
        print("Cargo has been removed from the plane!")
        return previous_cargo
