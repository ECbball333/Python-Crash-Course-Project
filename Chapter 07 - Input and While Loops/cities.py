prompt = "\nPlease enter the name of a city you have visited."
prompt += "\n\tEnter 'quit' when you are finished. "

while True:
    city = input(prompt)
#Using the break command to end a program
    if city == 'quit':
        break
    else:
        print(f"\nI'd love to go to {city.title()}")
