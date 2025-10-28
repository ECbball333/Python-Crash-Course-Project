#Positional Arguments
def describe_pet(animal_type, pet_name):
    """Display information about a per"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


#describe_pet('pig', 'elon')

#Multiple Function Calls
#describe_pet('dog', 'hudson')

#Keyword Arguments
describe_pet(animal_type='hamster', pet_name='george')