import string

class Restaurant:
    """Create a Restaurant class."""
    def __init__(self, name, cuisine_type, number_served):
        """Initialize the Restaurant class."""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        """Describe the Restaurant class."""
        print(f"\nAt {string.capwords(self.name)}, you can get {self.cuisine_type.title()} cuisine.")

    def open_restaurant(self):
        """Open the Restaurant"""
        print(f"\t{string.capwords(self.name)} is now open for business!")

    def set_number_served(self, number_served):
        """Set the number_served at restaurant."""
        self.number_served = number_served
        print(f"\nWe served {number_served} customers for lunch today.")

    def increment_number_served(self, people):
        """Increment the number_served at restaurant."""
        self.number_served += people
        print(f"\tWe had an additional {people} dinner customers later.")
        print(f"\nWe had {self.number_served} people come to the restaurant today.")


my_restaurant = Restaurant("e's lounge", 'soul food', number_served=0)

chilis = Restaurant('chilis', 'american/texmex', number_served=0)

restaurant = Restaurant('smokies', 'bbq', number_served=0)


my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.set_number_served(20)
my_restaurant.increment_number_served(39)

chilis.describe_restaurant()
chilis.open_restaurant()
chilis.set_number_served(45)
chilis.increment_number_served(102)

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(50)
restaurant.increment_number_served(68)




