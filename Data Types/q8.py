def remove_item(str,n):
    first_part = str[:n]
    last_part = str[n+1:]
    return first_part + last_part

print(remove_item('Python',2))
