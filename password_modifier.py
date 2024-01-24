# Helps to create stronger passwords from input
word = input("Please enter a phrase: ")
password = ''

word = word.replace('i', '!')
word = word.replace('a', '@')
word = word.replace('m', 'M')
word = word.replace('B', '8')
word = word.replace('o', '.')

word = word + 'ut*s'

print(word)
