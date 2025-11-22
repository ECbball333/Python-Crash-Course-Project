# Import a single Class
from car import Car

my_car = Car('audi', 'a4', 2024)
print(my_car.descriptive_name())
my_car.odometer_reading = 23
my_car.read_odometer()
my_car.increment_odometer(10)
my_car.read_odometer()
my_car.increment_odometer(20)
my_car.read_odometer()
my_car.increment_odometer(30)
