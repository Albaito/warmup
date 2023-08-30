# note: doesn't work if there's more than 1 consecutive space in sentence
def camelCase(sentence):
    words = sentence.split(' ')
    index = 0
    
    for word in words:
        if word != words[0]:
            word = word.title()
            words[index] = word
        else:
            print(word)
        index += 1

    combinedWords = ''.join(words)

    print(combinedWords)

sentence = input('Type a sentence to convert to a camelCase: ')
camelCase()