def customized_string(str1):
    length = len(str1)
    if length == 2:
        return str1 + str1
    elif length <=1:
        return "Empty String"
    else:
        return str1[:2] + str1[-2:]

print(customized_string('Python'))
