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

def printing(d):
    for elem in d:
        if d[elem] > 10:
            print(elem, d[elem])

def freq(b):
    d = {}
    for word in b:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d
    
        

def main():
    s = input('Введите название файла: ')
    b = split_text(s)
    d = freq(b)
    printing(d)
main()
