#Returning a Simple Value
#Takes first and last name, and returns a formatted full name

#def get_formatted_name(first_name, last_name):
#    """Return a full name, neatly formatted."""
#    full_name = f"{first_name} {last_name}"
#    return full_name.title()

#musician = get_formatted_name('jimi', 'hendrix')
#print(musician)

#Making an argument optional
def get_formatted_name(first_name, last_name, middle_name = ''):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix', 'marshall')
player = get_formatted_name('elliot', 'conner')
print(musician)
print(f"\n{player}")


