favorite_numbers = {
    'tim': [3, 6, 9],
    'john': [6, 12,18],
    'steve': [13, 26, 39],
    'bart': [10, 20, 30],
    'jay': [4, 8, 12]
    }

for number in favorite_numbers:
    print(f"\n{number.title()}'s favorite numbers are {favorite_numbers[number]}")