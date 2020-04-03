

users = {}

users['Kim'] = {'email' : 'kim@abc.com', 'gender' : 'f', 'age' : 27,
                'friends' : ['John', 'Josh']}
users['John'] = {'email' : 'john@def.com', 'gender' : 'm', 'age' : 24,
                'friends' : ['Kim']}
users['Josh'] = {'email' : 'josh@ghi.com', 'gender' : 'm', 'age' : 55,
                'friends' : ['Kim','John']}

max = 1000
for name in users:
    user = users[name]
    friends = user['friends']
    if len(friends) < max:
        most_anti_social = name
        max = len(friends)

print('The most_anti_social user is', most_anti_social)
