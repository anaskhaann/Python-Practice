class Car:
    total_cars=0
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        Car.total_cars +=1
    
    def get_brand(self):
        return self.__brand +"!!!"

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of Transport and are Amazing"
    
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric Current"


class Battery:
    def batteryInfo(self):
        return "This is Battery"

class Engine:
    def engineInfo(self):
        return "This is Engine"

class ElectricCarTwo(Car,Battery,Engine):
    pass

my_car = ElectricCarTwo("Tesla", "Model S")

print(my_car)
print(my_car.full_name())
print(my_car.model)
print(my_car.get_brand())
print(my_car.batteryInfo())
print(my_car.engineInfo())