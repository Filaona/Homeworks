def split_text(d):
    f = open(d, 'r', encoding = 'utf-8')
    b = []
    string = f.read()
    string.lower()
    if string:
            for word in string.split():
                word = word.strip()
                b.append(word.strip('.,?!()'))
    f.close()
    return b

def syllable(b, n):
    a = []
    for word in b:
        k = 0
        for i in word:
            if i in 'уеаыэояюи':
                k += 1
        if k == n:
            a.append(word)
    return a

def letter(b, let):
    a = []
    for word in b:
            if word[0] == let:
                a.append(word)
    return a


def choice(b):
    d = input('Если вы хотите узнать, сколько слов имеют определённое кол-во слогов, нажмите 1;\nесли вы хотите узнать, сколько слов начинаются на определённую букву, нажмите 2:\n')
    if d == '1':
        n = int(input('Введите кол-во слогов: '))
        if n <= 0:
            print('Дурак, попробуй ещё разок!')
        else:
            for elem in syllable(b, n):
                print(elem, end = ' ')
    elif d == '2':
        let = input('Введите букву: ').lower()
        if not(1072 <= ord(let[0]) <= 1103):
            print('Дурак, попробуй ещё разок!')
            
        else:
            for elem in letter(b, let):
                print(elem, end = ' ')
    else:
        print('Дурак, попробуй ещё разок!')
        choice(b)
        

def main():
    s = input('Введите название файла: ')
    b = split_text(s)
    choice(b)

main()
