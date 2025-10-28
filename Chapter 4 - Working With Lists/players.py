#Slicing a list
#players = ['charles', 'martina', 'michael', 'florence', 'eli', 'ed', 'ted', 'john', 'nate', 'bart']
#print(players[0:3])

#print(players[1:4])

#See the end of the list from any position
#print(players[4:9])

#print(players[-3:])
#print(players)

#Looping through a slice

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[0:3]:
    print(player.title())