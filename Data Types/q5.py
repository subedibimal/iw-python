def change_string(str1):
    if len(str1) >= 3:
        char = str1[-3:]
        if char != 'ing':
            return str1 + 'ing'
        else:
             return str1 + 'ly'
    else:
        return str1

print(change_string('abc'))

