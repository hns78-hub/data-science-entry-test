class Car:
    # This function runs when the object is created
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # This function prints car details
    def describe_car(self):
        print(self.year, self.make, self.model)


# Create an object of the Car class
car1 = Car("Toyota", "Corolla", 2020)

# Call the function
car1.describe_car()
