#Looping through a list
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title())

#Add a message to the loop
#for magician in magicians:
#    print(f"{magician.title()}, that was a great trick!")
#    print(f"I can't wait to see your next trick, {magician.title()}.\n")

#print("Thank you, everyone. That was a great magic show!")

#Indentation examples
# Always indent the line after for statements in a loop. If you forget, Python will remind you

#magicians = ['alice', 'david', 'carolina']
#for magician in magicians:
#print(magician)    # Will receive indentation error!

#Forgetting to Indent Additional Lines
#magicians = ['alice', 'david', 'carolina']
#for magician in magicians:
#    print(f"{magician.title()}, that was a great trick!")
#print(f"I can't wait to see your next trick, {magician.title()}.\n") #Logical Error!! Only Carolina receives the second print command.

#Forgetting the Colon
magicians = ['alice', 'david', 'carolina']
for magician in magicians:       # Will receive a syntax error for missing colon
    print(magician)
