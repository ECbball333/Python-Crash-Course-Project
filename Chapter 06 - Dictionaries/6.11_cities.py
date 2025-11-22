cities = {
    'charlotte': {
        'state': 'North Carolina',
        'population': 800000,
        'fact': 'it is known as " the Queen City"',
    },
    'huntsville': {
        'state': 'Alabama',
        'population': 215500,
        'fact': 'it is known as "the Rocket City"',
    },
    'columbia': {
        'state': 'South Carolina',
        'population': 135000,
        'fact': 'it is the Capitol of South Carolina'
    }
}

for city, info in cities.items():
    print(f"\n{city.title()} has the following characteristics:"
          f"\n\t it is located {info['state']}"
          f"\n\t the population is {info['population']}"
          f"\n\t one fun fact about {city.title()}, {info['fact']}.")