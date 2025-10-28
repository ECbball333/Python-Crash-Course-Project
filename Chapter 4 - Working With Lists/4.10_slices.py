



big_cats = ['lion', 'tiger', 'panther', 'cheetah', 'jaguar', 'leopard', 'bobcat', 'mountain lion', 'minx']

print("The first three items in the list are:")
for cat in big_cats[0:3]:
    print(cat.title())

print("\nThree items in the middle of the list are:")
for cat in big_cats[3:6]:
    print(cat.title())

print("\nThe last three items in the list are:")
for cat in big_cats[-3:]:
    print(cat.title())
