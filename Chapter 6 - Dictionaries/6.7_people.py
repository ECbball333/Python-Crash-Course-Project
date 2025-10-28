person_1 = {
    'first_name': 'jamie',
    'last_name': 'conner',
    'age': 43,
    'address': '768 knightswood road',
    'city': 'Fort Mill',
    'state': 'South Carolina',
    'zip_code': 29708
    }

person_2 = {
    'first_name': 'elliot',
    'last_name': 'conner',
    'age': 44,
    'address': '768 knightswood road',
    'city': 'Fort Mill',
    'state': 'South Carolina',
    'zip_code': 29708
    }

person_3 = {
    'first_name': 'evan',
    'last_name': 'conner',
    'age': 33,
    'address': '12444 caracara court',
    'city': 'charlotte',
    'state': 'North Carolina',
    'zip_code': 29278
}

people = [person_1, person_2, person_3]

for people in [person_1, person_2, person_3]:
    print(f"\n{people['first_name'].title()} {people['last_name'].title()} is {people['age']} years old.\n\t",
    f"They live at {people['address'].title()}, {people['city'].title()}, {people['state'].title()}, {people['zip_code']}.")
