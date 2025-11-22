favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'steve': 'java',
    'tim': 'xml',
    'jerry': 'rust'
    }

names = ['jen', 'tim', 'steve', 'elliot']

for name in names:
    if name in favorite_languages.keys():
        print(f"\n{name.title()}, you have completed the poll.")
    else:
        print(f"\n{name.title()}, you have not completed the poll! Please complete asap!")








