word = input('Введите слово: ')
row = []
while word != '':
    row.append(word)
    word = input('Введите слово: ')
for i in range(0, len(row)):
    flag = False
    f = open('input.txt', encoding = 'utf-8')
    d = f.readline()
    while d != '':
        list_c = d.split(' ')
        if  list_c[0] == row[i]:
            for j in range(1, len(list_c)):
                if list_c[j] != '|':
                    print(list_c[j],' ', end = '')
            flag = True
        d = f.readline()
    if not(flag):
        print('Такого слова нет')
    f.close()    
    print()
