from pandas.tseries.holiday import before_nearest_workday

list = ['michael jordan', 'barack obama', 'denzel washington']
print(f'{list[2].title()} will not be able to attend dinner.')

#Replace Denzel with Halle Berry
list.insert(2, 'halle barry')
print(f'{list[0].title()}, you are invited to dinner.')
print(f'{list[1].title()}, you are invited to dinner.')
print(f'{list[2].title()}, you are invited to dinner.')
print(f'Dear {list[0].title()}, {list[1].title()}, and {list[2].title()} we have found a bigger table.')

#Add new guests
list.insert(0, 'aaron judge')
list.insert(2, 'jay z')
list.append('elliot conner')
print(f'{list[0].title()}, you are invited to dinner.\n')
print(f'{list[1].title()}, you are invited to dinner.\n')
print(f'{list[2].title()}, you are invited to dinner.\n')
print(f'{list[3].title()}, you are invited to dinner.\n')
print(f'{list[4].title()}, you are invited to dinner.\n')
print(f'{list[5].title()}, you are invited to dinner.\n')
print(f'{list[6].title()}, you are invited to dinner.\n')
print(f'I can only invite two people to dinner.\n')

#Remove Guests and empty the List
aaron = list.pop(0)
print(f'Sorry {aaron.title()}, you are not invited.')
michael = list.pop(0)
print(f'Sorry {michael.title()}, you are not invited.')
jay_z = list.pop(0)
print(f'Sorry {jay_z.title()}, you are not invited.')
barack = list.pop(0)
print(f'Sorry {barack.title()}, you are not invited.')
halle = list.pop(0)
print(f'Sorry {halle.title()}, you are not invited.')
print(list)
#Empty List
del list [0]
del list[0]
print(list)

