#Copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

#this doesn't work, will copy identical info, not info from append command:
#friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(food.title())


