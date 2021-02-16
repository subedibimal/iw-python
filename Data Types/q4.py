def swap(str1,str2):
    char1 = str1[:2]
    char2 = str2[:2]
    char = char2 + str1[2:] + ' ' + char1 + str2[2:]
    return char

print(swap('abc','xyz'))
