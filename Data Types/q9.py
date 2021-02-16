def interchange(str):
    first_char = str[0]
    last_Char = str[-1]
    return last_Char + str[1:-1] + first_char

print(interchange('subedi'))