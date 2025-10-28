fav_pizza = ['sausage', 'pepperoni', 'hawaiian']
friend_pizzas = fav_pizza[:]

fav_pizza.append('mushroom')
fav_pizza.append('pineapple')
friend_pizzas.append('chicken')

print("My favorite pizzas are:")
for item in fav_pizza:
    print(item.title())

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())
#print("\nMy friends's favorite pizzas are:")

