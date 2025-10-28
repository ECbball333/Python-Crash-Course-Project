responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("What is your dream vacation? ")

    responses[name] = response
    repeat = input("Would you like to continue the poll? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\nHere are the poll results:")
for name, response in responses.items():
    print(f"{name.title()} would like a trip to {response.title()}. ")


print(f'\n{responses}')
