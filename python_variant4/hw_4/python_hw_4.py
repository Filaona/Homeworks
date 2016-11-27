word = input('Введите слово: ')
length = len(word)
for i in range(length, 0, -1):
    for h in range(i, length):
        print(word[h], end = '')
    for h in range(0, i):
        print(word[h], end = '')
    print()
    
