person_1 = {
    'first_name': 'steve',
    'last_name': 'jobs',
    'age': 34,
    'address': '7345 Willow Drive',
    'city': 'Dallas',
    'state': 'Texas',
    'zip_code': 34535
    }

person_2 = {
    'first_name': 'mike',
    'last_name': 'jones',
    'age': 34,
    'address': '24387 Elm St',
    'city': 'Jackson',
    'state': 'Tennessee',
    'zip_code': 42356
    }

person_3 = {
    'first_name': 'william',
    'last_name': 'gates',
    'age': 33,
    'address': '1634 caracara court',
    'city': 'New York',
    'state': 'New York',
    'zip_code': 56436
}

people = [person_1, person_2, person_3]

for people in [person_1, person_2, person_3]:
    print(f"\n{people['first_name'].title()} {people['last_name'].title()} is {people['age']} years old.\n\t",
    f"They live at {people['address'].title()}, {people['city'].title()}, {people['state'].title()}, {people['zip_code']}.")
