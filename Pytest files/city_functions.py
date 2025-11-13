def city_country(city, state, country):
    """Define a city/country string"""
    full_country = f"{city}, {state} {country}"
    return full_country.title()

while True:
    city = input("Enter a city: ")
    if city == 'q':
        break
    state = input("enter a state: ")
    if state == 'q':
        break
    country = input("Enter a country: ")
    if country == 'q':
        break
    else:
        full_name = f"{city}, {state} {country}"
    print(f"\nNeatly formatted name: {full_name}")