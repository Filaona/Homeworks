import re

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

def search_3syll(b):
    for elem in b:
        if re.search('.*[ёуеаыоэяию].*[ёуеаыоэяию].*[ёуеаыоэяию].*', elem):
            print(elem + ' ', end = '' )

def main():
    b = split_text(input())
    search_3syll(b)

main()
