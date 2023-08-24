# I will use snake case in future projects, whoops


def birthdayNameAsker():
    name = input('What is your name?\n')
    birthMonth = input('What month were you born?\n')

    print('Hello, ' + name + '\n')

    if birthMonth == 'August':
        print('Happy birthday month')

    numOfLetters = 0
    for letter in name:
        numOfLetters += 1

    print('There are ' + str(numOfLetters) + ' letters in your name')

birthdayNameAsker()



