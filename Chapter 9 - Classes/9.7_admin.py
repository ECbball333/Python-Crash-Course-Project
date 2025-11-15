class User:
    """Create a User class"""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"\n{self.first_name.title()} {self.last_name.title()}")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()}. Isn't Python fun?")


class Admin(User):
    """Create an Admin class that inherits from User."""
    def __init__(self, first_name, last_name, admin_roles=None):
        super().__init__(first_name, last_name)
        # store a list of strings; default to empty list if none provided
        self.admin_roles = list(admin_roles) if admin_roles else []

    def greet_admin(self):
        """Greet the admin and list their privileges."""
        if not self.admin_roles:
            print(f"\nHello {self.first_name.title()} — you have no admin roles assigned yet.")
        else:
            roles = ", ".join(self.admin_roles)


    def add_role(self, role):
        if role not in self.admin_roles:
            self.admin_roles.append(role)
            print(f'{self.admin_roles}')

    #def remove_role(self, role):
    #    if role in self.admin_roles:
    #        self.admin_roles.remove(role)

# Example usage
mike = Admin('mike', 'smith', admin_roles=['admin', 'manager'])
james = Admin( 'james', 'smith', admin_roles=['user', 'admin'])
nicole = Admin('nicole', 'smith')


mike.greet_admin()
