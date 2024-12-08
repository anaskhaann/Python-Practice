class Car():
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

my_car = Car("Toyota", "Supra")
print(my_car) 
print(my_car.brand) 
print(my_car.model) 
# paranthesis because it is a functionality
print(my_car.full_name()) 