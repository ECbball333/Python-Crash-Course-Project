def sandwiches(size, *toppings):
    """Print the toppings for sandwiches"""
    print(f"\nMaking a {size}-inch sandwich with the following toppings:")
    for topping in toppings:
        msg = (f"- {topping}")
        print(msg)

sandwiches(6, 'cheese', 'tomato')
sandwiches(8, 'onion', 'chicken', 'banana peppers')
sandwiches(12, 'ham', 'turkey', 'salami', 'provolone', 'salt and pepper')
