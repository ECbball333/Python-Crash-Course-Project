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

class IceCreamStand(Restaurant):
    """Create an Ice Cream Stand class."""

    def __init__(self, name, cuisine_type, number_served, flavors):
        """Initialize the IceCreamStand class."""
        super().__init__(name, cuisine_type, number_served)



    def describe_flavors(self):
        """Describe the flavor of Ice Cream sold."""
        flavors = ['chocolate', 'vanilla', 'strawberry', 'peach', 'butter pecan']
        print(f"\nWe sell the following flavors of ice cream: {flavors}")


my_stand = IceCreamStand('epc ice cream', 'ice cream', number_served=0, flavors = [])
my_stand.describe_restaurant()
my_stand.open_restaurant()
my_stand.set_number_served(50)
my_stand.increment_number_served(44)
my_stand.describe_flavors()

