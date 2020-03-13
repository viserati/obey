# A few exercises with lists, AKA Python Arrays

smoothies = ['coconut', 'strawberry', 'banana', 'pineapple', 'acai berry' ]

most_recent = len(smoothies)

print('There are', most_recent, 'items in this list')

recent = smoothies[most_recent -1]

print(recent, 'is the last item in the list')

#----------Enumerate-------------------------------

array_name = ['Item One', 'Item Two', 'Item Three']
for index, value in enumerate(array_name):
	print(index, value)
