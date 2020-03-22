# Creating an avatar.

def get_attribute(query, default):
    question = query + ' [' + default + ']? '
    answer = input(question)
    if (answer == ''):
        answer = default
        print ('You chose', answer)
        return answer

hair = get_attribute('what_hair_color', 'brown')
hair_length = get_attribute('what_hair_length', 'short')
eye = get_attribute('what_eye_color', 'blue')
gender = get_attribute('what_gender', 'female')
glasses = get_attribute('has_glasses', 'no')
beard = get_attribute('has_beard', 'no')
