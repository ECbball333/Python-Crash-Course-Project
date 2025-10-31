#Working with Classes and Instances
class Car:
    """A simple attempt to make a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        #Set a Default Value for an Attribute
        self.odometer_reading = 23500

    def descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's milage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    # Modify Attribute's Value Through a Method
    def update_odometer(self, milage):
        """Set the odometer reading to the given value
           Reject the change if it attempts to roll the odometer back."""
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back the odometer!")

    # Increment an Attributes Value Through a Method
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles
        if miles == 0:
            print("You can't roll back the odometer!")



my_new_car = Car('audi', 'a4', 2024)
my_used_car = Car('subaru', 'outback', 2019)

print(f'\n{my_new_car.descriptive_name()}')
print(f'\n{my_used_car.descriptive_name()}\n')

# Modify an Attributes Value Directly
my_new_car.odometer_reading = 23
my_new_car.update_odometer(89)
my_new_car.read_odometer() # Read odometer value


my_used_car.update_odometer(23_600)
my_used_car.read_odometer()
my_used_car.increment_odometer(75445)
my_used_car.read_odometer()




