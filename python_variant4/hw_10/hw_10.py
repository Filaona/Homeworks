import re

def split_text(file_name):
    file = open(file_name, 'r', encoding = 'utf-8')
    string = file.read()
    file.close()
    return string

def output(elem):
    res_file = open('Научная сфера.txt', 'w', encoding = 'utf-8')
    res_file.write(elem)

def check(string):
    res = re.findall('Научная сфера[\w\W]*?title[\w\W]*?>([\w\W]*?)<', string)
    for elem in res:
        output(elem)

def main():
    string = split_text(input('Введите название файла: '))
    check(string)

if __name__ == '__main__':
    main()
