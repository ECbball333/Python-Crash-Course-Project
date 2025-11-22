#favorite_languages = {
#    'jen': 'python',
#    'sarah': 'c',
#    'edward': 'rust',
#    'phil': 'python',
#    }


#language = favorite_languages['jen'].title()
#print(f"Jen's favorite language is {language}.")

#Looping through a dictionary. From exercise on page 100
#for name, language in favorite_languages.items():
#    print(f"\n{name.title()}'s favorite language is {language.title()}")

#Looping through all Keys in a Dictionary with keys() method
#favorite_languages = {
#    'jen': 'python',
#    'sarah': 'c',
#    'edward': 'ruby',
#    'phil': 'python',
#    'eve': 'ruby'
#    }

#friends = ['phil', 'sarah', 'jen']
#for name in favorite_languages.keys():
#    print(f"\nHi {name.title()}!")

#    if name in friends:
#        language = favorite_languages[name].title()
#        print(f"\t{name.title()}, I see you love {language},")

#if 'erin' not in favorite_languages.keys():
#    print("\nErin, please take our poll!")

#Looping through Dictionary Keys in a Particular Order with sorted() function
#favorite_languages = {
#    'sarah': 'c',
#    'edward': 'rust',
#    'phil': 'python',
#    'elliot': 'python',
#    'jamie': 'java',
#    'jalen': 'c++'
#    }
#for name in sorted(favorite_languages.keys()):
#    print(f"{name.title()}, thank you for taking the poll.")

#Looping Through All Values in a Dictionary
#favorite_languages = {
 #   'jen': 'python',
  #  'sarah': 'c',
   # 'edward': 'rust',
   # 'phil': 'python'
    #}
#print("The following languages have been mentioned:")
#for language in set(favorite_languages.values()): #Use a set to see values without repitition
##for language in favorite_languages.values():
 #   print(language.title())

#A List in a Dictionary
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
