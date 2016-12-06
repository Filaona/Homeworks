f = open('input.txt', encoding = 'utf - 8')
string = f.readline()
begin = True
sum = 0
while string != '':
    list_of_word = string.split(' ')
    if list_of_word[2] == 'сущ':
        if (list_of_word[4] == 'ед') and (list_of_word[5] == 'жен'):
            if begin:
                print(list_of_word[0], end = '')
                begin = False
            else:
                print(', ', list_of_word[0], end = '')
            sum += (float(list_of_word[len(list_of_word)-1][0:-1])) 
    string = f.readline()
    list_of_word = []
print('sum of ipms: ',sum)
