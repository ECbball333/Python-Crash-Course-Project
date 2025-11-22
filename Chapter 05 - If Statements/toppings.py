#Checking for Inequality

#requested_topping = 'mushrooms'

#if requested_topping != 'anchovies':
# print("Hold the anchovies")

#requested_toppings = ['mushrooms', 'extra cheese', 'pepperoni']

#if 'mushrooms' in requested_toppings:
#   print("Adding mushrooms.")
#if 'pepperoni' in requested_toppings:
#    print("Adding pepperoni.")
#if 'extra cheese' in requested_toppings:
#    print("Adding extra cheese.")

#print(f"\nFinished making your pizza!")

#Checking for Special Items
#requested_toppings = ['mushrooms', 'green peppers', 'extra cheese', 'pineapple']

#for requested_topping in requested_toppings:
#    if requested_topping == 'mushrooms':
#    else:
#        print(f"Adding {requested_topping}")

#print("\nFinished making your pizza!")

#Checking and empty list
#requested_toppings = ['cheese']

#if requested_toppings:
#    for requested_topping in requested_toppings:
#        print(f"Adding {requested_topping}")
#    print("\nFinished making your pizza!")
#else:
#    print("Are you sure you want a plane pizze?")


#Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")





