import random

def strip_elem(elem):
    elem = elem.strip()
    elem = elem.strip('.,?!()')
    return elem

def split_text():
    f = open('словосочетания.csv', 'r')
    b = {}
    string = f.read()
    string.lower()
    temp = string.split()
    if string:
            for i in range(0,len(temp),2):
                b[strip_elem(temp[i])] = strip_elem(temp[i + 1])
                
    f.close()
    return b

def printing(b, key_word):
    print(key_word + ' ', end = '');
    for elem in b[key_word]:
        print('.', end = '')


def enigma(b):
    key_word = random.choice(list(b.keys()))
    flag = '1'
    while flag == '1':
        printing(b, key_word)
        flag = '2'
        ans = input()
        if ans.strip() == b[key_word]:
            print('Красавчик!')
            flag_main = input('Хотите отгадывать? Нажмите 1\nХотите закончить?  Нажмите 2')
        else:
            print('Невдача :(')
            flag = input('Ещё раз попробовать этот же: 1\nПопробовать другой:          2\nЗакончить:                   3')
            if flag == '2':
                flag_main = '1'
            elif flag == '3':
                flag_main = '2'
    return flag_main

def game(b):
    flag_main = input('Хотите отгадывать? Нажмите 1\nХотите закончить?  Нажмите 2')
    while flag_main == '1':
        flag_main = enigma(b)
    else:
        print('Пока!')

def main():
    b = split_text()
    game(b)


main()
