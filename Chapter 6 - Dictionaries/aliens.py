#alien_0 = {'color': 'green', 'points': 5}
#alien_1 = {'color': 'yellow', 'points': 10}
#alien_2 = {'color': 'red', 'points': 15}

#aliens = [alien_0, alien_1, alien_2]

#for alien in aliens:
 #   print(alien)

# Make an empty list for storing aliens
aliens = []

#Make 30 green aliens and 30 Yellow aliens
for alien_number in range(30):
    new_alien_0 = {'color': 'green', 'points': 5, 'speed': 'slow'}
    new_alien_1 = {'color': 'yellow', 'points': 10, 'speed': 'medium'}
    aliens.append(new_alien_0)
    aliens.append(new_alien_1)

for alien in aliens[0:10]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 25


#Show the first 5 aliens
for alien in aliens[:15]:
    print(alien)
print("...")

#Show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")