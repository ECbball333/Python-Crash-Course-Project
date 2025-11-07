def city_country(city, country):
    """Define a city/country string"""
    full_country = f"{city}, {country}"
    return full_country.title()

while True:
    city = input("Enter a city: ")
    if city == 'q':
        break
    country = input("Enter a country: ")
    if country == 'q':
        break
    else:
        full_name = f"{city}, {country}"
        print(f"\nNeatly formatted name: {full_name}")