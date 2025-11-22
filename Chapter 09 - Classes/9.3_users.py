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


mike = User('mike', 'conner', 'andrew', 34, 'huntsville, alabama')
john = User('john', 'conner', 'beverly', 28, 'washington dc')
jane = User('jane', 'conner', 'michelle', 4, 'charlotte, north carolina')


mike.describe_user()
mike.greet_user()
john.describe_user()
john.greet_user()
jane.describe_user()
jane.greet_user()


