sandwich_orders = {'cuban', 'ham and cheese', 'blt', 'turkey', 'meatball'}
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"Verifying your {sandwich} sandwich order.")
    finished_sandwiches.append(sandwich)

print("All the sandwiches have been made.")


