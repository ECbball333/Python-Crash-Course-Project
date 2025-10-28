number = input("\nGive me a number, and I will tell you if it's a multiple of 10: ")
number = int(number)

if number % 10 == 0:
    print(f"\n{number} is a multiple of 10.")
else:
    print(f"\n{number} is not a multiple of 10. ")
