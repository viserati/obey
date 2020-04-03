
users = {'Kim' : 'kim@oreilly.com',
         'John' : 'john@abc.com',
         'Glen' : 'glen@gmail.com'}


users['Josh'] : 'Josh@house.com'

del users['John']

if 'Glen' in users:
    print("Glen's email address is:", users['Glen'])
