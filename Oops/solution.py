class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"


# this means it is inheriting from parent class named Car
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        # we have already created brand and model in parent class in __init__ method
        super().__init__(brand,model)
        self.battery_size = battery_size

my_new_car=ElectricCar("Tesla", "CyberTruck", "80kWH")

print(my_new_car)
print(my_new_car.brand)
print(my_new_car.model)
print(my_new_car.battery_size)
print(my_new_car.full_name())