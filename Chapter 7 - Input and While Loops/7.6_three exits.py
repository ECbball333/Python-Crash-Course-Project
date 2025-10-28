prompt =("\nPlease choose your pizza toppings: ")
prompt += ("\n\tEnter 'quit' when finished entering toppings. ")



#topping = ""

#while topping != 'quit':
#   topping = input(prompt)

#    if topping == 'quit':
#      break
#    else:
#        print(f"\n{topping.title()} has been added to your pizza.")

#Using active statement
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    if message != 'quit':
        print(f"{message.title()} has been added.")
   