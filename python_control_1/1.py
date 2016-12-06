f = open('input.txt', encoding = 'utf - 8')
string = f.readline()
while string != '':
    list_of_word = string.split(' ')
    if list_of_word[2] == 'союз':
        print(string)
    string = f.readline()
    list_of_word = []

