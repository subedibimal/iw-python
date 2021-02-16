import operator 

def frequency(str):
    dict1 = {}
    for n in str:
        keys = dict1.keys()
        if  n in keys:
            dict1[n] +=1
        else:
            dict1[n] = 1
    sorted_dict = dict(sorted(dict1.items(),key=operator.itemgetter(1), reverse=True))
    return sorted_dict

print(frequency('google.com'))
