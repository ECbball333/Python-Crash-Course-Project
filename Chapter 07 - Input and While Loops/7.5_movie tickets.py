ticket = input("\nInput your age ")
ticket = int(ticket)

if ticket < 3:
    print("Your ticket is free")
elif ticket <= 12:
    print("Your ticket is $10")
elif ticket > 12:
    print("Your ticket is $15")


