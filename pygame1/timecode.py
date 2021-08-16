import timeit
mine = (timeit.timeit('''
def getCount(sentence):
    return sum(1 for char in sentence.lower() if char in 'aeiou')
''', number=100))
other = (timeit.timeit('''
def getCount(sentence):
    return sentence.lower().count('a') + sentence.lower().count('e') + sentence.lower().count('i') + sentence.lower().count('o') + sentence.lower().count('u')

''', number=100))
print("First test: " + mine)
print("Second test: " + other)


