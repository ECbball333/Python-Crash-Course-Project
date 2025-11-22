from car import ElectricCar

my_leaf = ElectricCar('nissan', 'leaf', 2004)
print(my_leaf.descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
