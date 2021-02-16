def remove_odd(str):
    str1 = ''
    for n in range(len(str)):
        if(n % 2 == 0):
            str1 += str[n]
    return str1

print(remove_odd('Bimal'))