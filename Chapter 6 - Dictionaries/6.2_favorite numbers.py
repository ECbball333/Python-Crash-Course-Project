favorite_numbers = {
    'mike': 3,
    'tim': 6,
    'steve': 13,
    'jerry': 10,
    'bob': 4,
    }
favorite_numbers['mike'] = 5
favorite_numbers['tim'] = 15
for number in favorite_numbers:
    print(f"{number.title()}'s favorite number is {favorite_numbers[number]}")

