favorite_numbers = {
    'elliot': 3,
    'jamie': 6,
    'evan': 13,
    'zae': 10,
    'shawn': 4,
    }
favorite_numbers['jamie'] = 5
favorite_numbers['zae'] = 15
for number in favorite_numbers:
    print(f"{number.title()}'s favorite number is {favorite_numbers[number]}")

