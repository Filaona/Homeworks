def split_text(d):
    f = open(d, 'r', encoding = 'utf-8')
    a = []
    string = f.read()
    if string != '':
            f = string.split()
            for word in f:
                word = word.strip()
                a.append(word.strip('.,?!()'))
    print(a)
    return(len(a))

s = input('Введите название файла: ')
b = split_text(s)
print(b)
