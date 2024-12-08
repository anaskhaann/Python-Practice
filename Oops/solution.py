class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
    
    # Good practice to make name of getter like this
    def get_brand(self):
        return self.__brand +"!!!"

    def full_name(self):
        return f"{self.__brand} {self.model}"

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_new_car=ElectricCar("Tesla", "CyberTruck", "80kWH")

# print(my_new_car.__brand) #THis will give the error
print(my_new_car.get_brand())
