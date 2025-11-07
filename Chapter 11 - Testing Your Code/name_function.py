
#def get_formatted_name(first, last):
#    """Generate a neatly formatted name"""
#    full_name = f"{first} {last}"
#    return full_name.title()



# This function will generate a failing test
def get_formatted_name(first, last, middle=''):
    """Generate a formatted name."""
    # Make the middle name optional for successful test
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"




