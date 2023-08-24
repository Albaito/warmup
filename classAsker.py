def classAsker():
    numOfClasses = input('How many classes are you taking this semster?')

    classList = []
    for num in numOfClasses:
        className = input('What\'s the name of class ' + num)
        classList.append(className)
        
    # item is each individual class
    for item in classList:
        print(item)

classAsker()