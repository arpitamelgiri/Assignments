def wordcount (string):
    frequency = dict()
    words = string.split()

    for word in words:
        if word in frequency:
            frequency[wors] +=1
        else:
            frequency[word] = 1

    return frequency

sentence = input("Enter sentence: ").lower()
print(wordcount(sentence))


