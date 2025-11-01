
class Restaurant:
    """Create a Restaurant class."""
    def __init__(self, name, cuisine_type, number_served=0):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"\nAt {self.name.title()}, you can get {self.cuisine_type.title()} cuisine.")

    def open_restaurant(self):
        print(f"\t{self.name.title()} is now open for business!")

    def set_number_served(self, number_served):
        self.number_served = number_served
        print(f"\nWe served {number_served} customers for lunch today.")

    def increment_number_served(self, people):
        self.number_served += people
        print(f"\tWe had an additional {people} dinner customers later.")
        print(f"\nWe had {self.number_served} people come to the restaurant today.")


class IceCreamStand(Restaurant):
    """Create an Ice Cream Stand class."""

    def __init__(self, name, cuisine_type="ice cream", number_served=0, flavors=None):
        super().__init__(name, cuisine_type, number_served)
        self.flavors = list(flavors) if flavors else []

    def describe_flavors(self):
        """List the available ice cream flavors."""
        if not self.flavors:
            print("\nWe're out of flavors at the moment!")
        else:
            flavor_list = ", ".join(self.flavors)
            print(f"\nWe sell the following flavors of ice cream: {flavor_list}")

    # Optional convenience methods
    def add_flavor(self, flavor):
        if flavor not in self.flavors:
            self.flavors.append(flavor)
            print(f"{flavor.title()} was added to the flavors list.")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"{flavor.title()} was removed from the flavors list.")


my_stand = IceCreamStand('epc ice cream', flavors=['chocolate', 'strawberry', 'peach', 'vanilla'])
my_stand.describe_restaurant()
my_stand.open_restaurant()
my_stand.set_number_served(50)
my_stand.increment_number_served(44)
my_stand.describe_flavors()
my_stand.add_flavor('cookies and cream')

