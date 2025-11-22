glossary = {
    'string': 'a line of text',
    'integers': 'a set of numbers',
    'floats': 'a set of numbers with decimal points',
    'lists': 'a group of values',
    'dictionaries': 'a group of key/value pairs'
    }
for value in glossary:
    #Multiple ways to print the info!
    #print(f"\nThe definition of {value.title()} is, {glossary[value]}.")
    print(f"\nThe definition of {value.title()} is: \n\t {glossary[value]}.")