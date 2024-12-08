# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.


class Car():
    # self is used to establish a connection to access the class attributes(variables)
    def __init__(self,brand,model):
        
        # Self.brand means class one and RHS brand means which user is giving as attribute while creating object
        self.brand = brand
        self.model = model

my_car = Car("BMW", "M5")
print(my_car) 
print(my_car.brand) 
print(my_car.model) 