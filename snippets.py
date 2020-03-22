# A medley of code snippets for Python

# :::::::::::::::::: Boolean :::::::::::::::::

""" In programming, the Boolean data type is
used to work with statements that can either
be True or False. Booleans compare two values
and return whether or not those values are
similar. """
"""
loyalty_customer = True

if loyalty_customer == True:
	print("This customer is a Loyalty Customer!")
else:
	print("No record.")
"""
# -----------------
REFRAIN = '''
%d bottles of beer on the wall,
%d bottles of beer,
take one down, pass it around,
%d bottles of beer on the wall!
'''
"""
bottles_of_beer = 10
while bottles_of_beer > 1:
    print (REFRAIN % (bottles_of_beer, bottles_of_beer,
        bottles_of_beer - 1))
    bottles_of_beer -= 1
"""
"""
def drink_me(param):
	msg = 'Drinking ' + param + 'glass'
	print (msg)
	param = 'empty'

glass = 'full'
drink_me(glass)
print('The glass is', glass)
"""
