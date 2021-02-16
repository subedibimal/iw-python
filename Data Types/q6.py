def change_string(str1):
    s_not = str1.find('not')
    s_poor = str1.find('poor')
    if s_poor > s_not and s_not > 0 and s_poor > 0:
        str1 = str1.replace(str1[s_not:(s_poor+4)],'good')
        return str1
    else:
        return str1
    
print(change_string('The lyrics is not that poor!'))