
# Importing Multiple Classes from a Module

#from car import Car, ElectricCar

#my_mustang = Car('ford', 'mustang', 2024)
#print(my_mustang.descriptive_name())
#my_leaf = ElectricCar('nissan', 'leaf', 2024)
#print(my_leaf.descriptive_name())

# Importing an entire module
import car

my_mustang = car.Car('ford', 'mustang', 2024)
print(my_mustang.descriptive_name())

my_leaf = car.ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.descriptive_name())



