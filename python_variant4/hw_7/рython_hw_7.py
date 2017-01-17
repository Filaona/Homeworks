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


def ending(b):
    a = 0
    f = 0
    for word in b:
                if word[-2:] == 'ed':
                    a += 1
                if word[-3:] == 'ied':
                    f += 1
    return a, f

def print_ans(a, f):
    printing(a, '"ed"')
    printing(f, '"ied"')
    
def printing(d, end):
    if d % 10 == 1:
        print(d, 'слово оканчивается на ' + end)
    elif d % 10 in [2,3,4]:
        print(d, 'слова оканчивается на ' + end)
    else:
        print(d, 'слов оканчивается на ' + end)

def main():
    s = input('Введите название файла: ')
    b = split_text(s)
    a,f = ending(b)
    print_ans(a,f)

main()
