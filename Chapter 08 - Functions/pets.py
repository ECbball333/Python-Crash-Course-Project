#Positional Arguments
#def describe_pet(animal_type, pet_name):
#    """Display information about a per"""
#    print(f"\nI have a {animal_type}.")
#    print(f"My {animal_type}'s name is {pet_name.title()}.")


#describe_pet('pig', 'elon')

#Multiple Function Calls
#describe_pet('dog', 'hudson')

#Keyword Arguments
#describe_pet(animal_type='hamster', pet_name='george')


#Default Values
#You can define a default value for any parameter. Simplifies code.

def describe_pet(pet_name, animal_type='dog'): #Dog is now the default value#
    '''Display info about a pet'''
    print(f"\nI have a {animal_type}. ")
    print(f"My {animal_type}'s name is {pet_name.title()}. ")

#Equivalent Function Calls
describe_pet('hudson')
describe_pet('marty', 'bird')
describe_pet('ace', 'cat')
describe_pet(pet_name= 'willie', animal_type='horse')
#describe_pet() #Will receive argument error!!!