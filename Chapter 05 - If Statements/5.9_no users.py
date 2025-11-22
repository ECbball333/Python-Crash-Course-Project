#Checking an empty list with if statement

usernames = []

if usernames == []:
    print("We need to find some users!")

for user in usernames:
 #   print(f"Hello {user.title()}, it's nice to meet you.")
    if user == 'admin':
        print("\nHello admin, would you like to run the world?")
    else:
        print(f"\nHello {user.title()}, what would you like to do?")