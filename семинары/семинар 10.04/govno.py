import os
word = input()
word = word.strip('.,?!"')
word = word.replace(' ', '\\')
os.makedirs(word)
