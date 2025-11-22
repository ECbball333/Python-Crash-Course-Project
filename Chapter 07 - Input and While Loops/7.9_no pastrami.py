sandwich_orders = {'cuban', 'ham and cheese', 'blt', 'turkey', 'meatball', 'pastrami', 'pastrami', 'pastrami',}
finished_sandwiches = []

print("We have run out of pastrami sandwiches.")

while 'pastrami' in sandwich_orders:
  sandwich_orders.remove('pastrami')

print(f"\nWe have the following sandwiches: \n{sandwich_orders}:")

