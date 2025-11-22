"""A set of classes that can be used to represent gas and electric cars."""

#Working with Classes and Instances
class Car:
    """A simple attempt to make a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        #Set a Default Value for an Attribute
        self.odometer_reading = 0

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



#my_new_car = Car('audi', 'a4', 2024)
#my_used_car = Car('subaru', 'outback', 2019)

#print(f'\n{my_new_car.descriptive_name()}')
#print(f'\n{my_used_car.descriptive_name()}\n')

# Modify an Attributes Value Directly
#my_new_car.odometer_reading = 23
#my_new_car.update_odometer(89)
#my_new_car.read_odometer() # Read odometer value


#my_used_car.read_odometer()
#my_used_car.increment_odometer(75445)
#my_used_car.read_odometer()

# Storing Multiple Classes in a Module
class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size/"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)
        self.battery = Battery()