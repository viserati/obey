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
"""
REFRAIN =
%d bottles of beer on the wall,
%d bottles of beer,
take one down, pass it around,
%d bottles of beer on the wall!

bottles_of_beer = 10
while bottles_of_beer > 1:
    print (REFRAIN % (bottles_of_beer, bottles_of_beer,
        bottles_of_beer - 1))
    bottles_of_beer -= 1

def drink_me(param):
	msg = 'Drinking ' + param + 'glass'
	print (msg)
	param = 'empty'

glass = 'full'
drink_me(glass)
print('The glass is', glass)
"""
'''
balance = 10500
camera_on = True

def steal(balance, amount):
	global camera_on
	camera_on = False
	if (amount < balance):
		balance = balance - amount

	return amount
	camera_on = True

proceeds = steal(balance, 1250)
print ('Criminal: you stole', proceeds)
'''
# -------------------------------------

# grades
grade = 91

# letter grade.
#  "A" - 90 and above
#  "B" - 80 to 89
#  "C" - 70 to 79
#  "D" - 60 to 69
#"FAIL" - less than 59
#

# each letter grade has a nested "if" statement
print(grade)
if (grade < 90):

	# not A
	if (grade < 80):

		# not B
		if (grade < 70):

			# not C
			if (grade < 60):

				# not D
				print("FAIL")
			else:
				print("D")

		else:
			print("C")

	else:
		print("B")

else:
	print("A")
