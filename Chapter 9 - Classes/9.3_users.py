class User:
    """Create a User class"""
    def __init__(self, first_name, last_name, middle_name, age, birthplace):
        """Initialize the user class."""
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.age = age
        self.birthplace = birthplace

    def describe_user(self):
        """Describe the user class."""
        print(f"\n{self.first_name.title()} {self.middle_name.title()} {self.last_name.title()}"
              f" was born in {self.birthplace.title()} and is {self.age} years old.")

    def greet_user(self):
        """Greet the user class."""
        print(f"Hello, {self.first_name.title()}. Isn't Python fun?")


elliot = User('elliot', 'conner', 'preston', 43, 'huntsville, alabama')
jamie = User('jamie', 'conner', 'nicole', 43, 'washington dc')
emery = User('emery', 'conner', 'ann', 1, 'charlotte, north carolina')


elliot.describe_user()
elliot.greet_user()
jamie.describe_user()
jamie.greet_user()
emery.describe_user()
emery.greet_user()


