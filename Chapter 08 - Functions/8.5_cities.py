def describe_city(city, country = 'canada'):
    """Describe a city"""
    print(f"\n{city.title()}, is in {country.title()}.")

describe_city('toronto')
describe_city(city = 'ottawa')
describe_city(city = 'madrid', country = 'spain')
