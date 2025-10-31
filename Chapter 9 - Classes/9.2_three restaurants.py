import string

from debugpy.launcher.debuggee import describe
from jinja2.lexer import describe_token_expr


class Restaurant:
    """Create a Restaurant class."""
    def __init__(self, name, cuisine_type):
        """Initialize the Restaurant class."""
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe the Restaurant class."""
        if self.name != 'wingstop':
            print(f"\nAt {string.capwords(self.name)}, you can get {self.cuisine_type.title()} cuisine.")
        else:
            print(f"\nAt {string.capwords(self.name)}, you can get {self.cuisine_type.title()}.")

    def open_restaurant(self):
        """Open the Restaurant"""
        print(f"\n{string.capwords(self.name)} is now open for business!")

my_restaurant = Restaurant("e's lounge", 'soul food')
chilis = Restaurant('chilis', 'american/texmex')
mio = Restaurant('mio', 'asian')
wingstop = Restaurant('wingstop', 'chicken wings')


my_restaurant.describe_restaurant()
chilis.describe_restaurant()
mio.describe_restaurant()
wingstop.describe_restaurant()

