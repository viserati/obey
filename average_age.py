

users = {}
users['Kim'] = {'email' : 'kim@abc.com', 'gender' : 'f', 'age' : 27,
                'friends' : ['John', 'Josh']}
users['John'] = {'email' : 'john@def.com', 'gender' : 'm', 'age' : 24,
                'friends' : ['Kim', 'Josh']}
users['Josh'] = {'email' : 'josh@ghi.com', 'gender' : 'm', 'age' : 55,
                'friends' : ['Kim']}

def average_age(username):
    global users

    user = users[username]
    friends = user['friends']

    sum = 0

    for name in friends:
        friend = users[name]
        sum = sum + friend['age']

    average = sum/len(friends)
    print(username + "'s friends have an average age of", average)




average_age('Kim')
average_age('John')
average_age('Josh')
