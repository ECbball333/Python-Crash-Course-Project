# Importing an Entire Module
#import make_pizza

# Import specific Functions
from pizza import make_pizza

# Using 'as' to give a Function an Alias
#from pizza import make_pizza as mp

#mp(16, 'pepperoni')
#mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using 'as' to give a Module an Alias
#import pizza as p

#p.make_pizza(16, "pepperoni")
#p.make_pizza(12, "everything")


# Importing All Function in a Module
from pizza import *

make_pizza(12, "pepperoni")
make_pizza(16, 'everything')