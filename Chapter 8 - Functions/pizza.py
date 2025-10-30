# Passing an Arbitrary Number of Arguments

def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested."""
    """ Summarize the pizza we are about to make"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16,'pepperoni')
make_pizza(8, 'mushrooms', 'green peppers', 'extra cheese')
make_pizza(20, 'sausage', 'mushrooms', 'bacon', 'pineapple')
