dog_1= {
    'name': 'hudson',
    'breed': 'bully mix',
    'owner': 'elliot conner'
}

dog_2 = {
    'name': 'ace',
    'breed': 'mixed',
    'owner': 'n/a'
}

dog_3 = {
    'name': 'rocco',
    'breed': 'rotweiller',
    'owner': 'marge'
}

pets = [dog_1, dog_2, dog_3]

for pet in pets:
    print(f"\n{pet['name'].title()} is a {pet['breed']}. \n\t The pet owner is {pet['owner'].title()}")