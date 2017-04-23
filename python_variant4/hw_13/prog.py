import os
import shutil
import re


def printing(dic, k):
    if dic['dirs'] != []:
        print('Названия папок: ' + ', '.join(dic['dirs']) + '.')
    else:
        print('Нет папок.')
    if dic['files'] != []:
        print('Названия файлов: ' + ', '.join(dic['files']) + '.')
    else:
        print('Нет файлов.')
    print('Количество файлов, название которых состоит только из латинских букв: ' + str(k) + '.')


def main():
    dic = {}
    dic['dirs'] = []
    dic['files'] = []
    k = 0
    # сейчас буду создавать коды для латинских букв
    A = {item for item in range(65,123)}    
    B = {item for item in range(91,97)}
    latin_codes = A - B
    
    for name in os.listdir('.'):
        if os.path.isdir(name):
            if name not in dic['dirs']:
                dic['dirs'].append(name)
        else:
            if name not in dic['files']:
                dic['files'].append(name)
            flag = True
            for sym in name:
                if (ord(sym) not in latin_codes) and (sym != '.'):
                    flag = False
            if flag:
                k += 1
    printing(dic, k)
                    
    

if __name__=='__main__':
    main()
