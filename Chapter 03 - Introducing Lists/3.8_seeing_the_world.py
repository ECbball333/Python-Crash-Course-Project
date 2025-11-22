#Create list
from fontTools.ufoLib import fontInfoAttributesVersion1

fav_location = ['London', 'Paris', 'Tokyo', 'Barcelona', 'LA']
print(fav_location)

#Use sorted to print without modifying list
print(sorted(fav_location))

#Show list still in original order
print(fav_location)

#Print list in reverse alphabetical order without modifying list
fav_location.reverse()
print(fav_location)

#Reverse the list back
fav_location.reverse()
print(fav_location)

#Sort alphabetically and change the list order permanently
fav_location.sort()
print(fav_location)

#Sort by reverse alphabetical order permanently
fav_location.sort(reverse=True)
print(fav_location)





