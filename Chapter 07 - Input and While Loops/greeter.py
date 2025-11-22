#Create a prompt
# name = input("Please enter your name: ")
#print(f"\nHello, {name}!")

prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello {name.title()}! Thank you for using my app!")