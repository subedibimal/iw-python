def longest_length(word_list):
    word_str2 = []
    for n in word_list:
        word_str2.append((len(n),n))
    word_str2.sort()
    return word_str2[-1][0], word_str2[-1][1]

result = longest_length(['PHP','Exercises','Backend'])
print('\nLongest Word:',result[1])
print('\nLength of the longest word: ',result[0])