
def city_country(city, country, population):
    """Define a city/country/population string"""
    full_country = f"{city}, {country}, {population}"
    return full_country.title()

while True:
    city = input("Enter a city: ")
    if city == 'q':
        break
    country = input("Enter a country: ")
    if country == 'q':
        break
    population = input("Enter a population: ")
    if population == 'q':
        break
    else:
        full_name = f"{city}, {country}"
        print(f"\n{full_name} has a population of {population}.")
