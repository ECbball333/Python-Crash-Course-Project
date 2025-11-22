#A simple function
#def greet_user():
#    """Display a simple greeting."""
#    print("Hello!")

#greet_user()

#Passing Information to a Function
#def greet_user(username):
#    """Display a simple greeting."""
#    print(f"Hello, {username.title()}!")

#greet_user('james')

#Using a Function with a while loop
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f'{first_name} {last_name}'
    return full_name.title()

# This is an infinite loop!
while True:
    print(f"\nPlease tell me your name:")
    print("(enter 'q' at any time to quit") # Add quit statement for the user

    f_name = input("\nFirst name: ")
    if f_name == 'q': # Add if statement and break action for user
        break

    l_name = input("Last name: ")
    if l_name == 'q': # Add if statement and break action for user
        break

    formatted_name= get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}! ")
