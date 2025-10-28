#Loop through a dictionary

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
#Create 2 variables to store key/value pair
#The method items() returns a sequence of key/value pairs
for k, v in user_0.items():
    #print(f"\nKey: {k}")
    print(f"Value: {v}")