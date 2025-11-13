class Employee:
    """Write a class to represent an employee"""
    def __init__(self, first_name, last_name, annual_salary):
        """Create model for employee"""
        self.first_name = input('Enter first name: ')
        self.last_name = input('Enter last name: ')
        self.annual_salary = float(input('Enter annual salary: '))


    def create_employee(self):
        """Create an employee model"""


    def give_raise(self):
        """Give the employee a $5000 raise"""
        self.annual_salary.append(5000)

Employee('Elliot', 'Conner', 50000)