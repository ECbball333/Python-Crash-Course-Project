import string

class Restaurant:
    """Create a Restaurant class."""
    def __init__(self, name, cuisine_type):
        """Initialize the Restaurant class."""
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe the Restaurant class."""
        print(f"\nAt {string.capwords(self.name)}, you can get {self.cuisine_type.title()} cuisine.")

    def open_restaurant(self):
        """Open the Restaurant"""
        print(f"\n{string.capwords(self.name)} is now open for business!")

my_restaurant = Restaurant("e's lounge", 'soul food')
chilis = Restaurant('chilis', 'american/texmex')



my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
chilis.describe_restaurant()
chilis.open_restaurant()
