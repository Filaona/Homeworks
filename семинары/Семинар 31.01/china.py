import re

def split_text(file_name):
    file = open(file_name, 'r', encoding = 'utf-8')
    list_words = []
    string = file.read()
    file.close()
    return string

def check(string):
    res = re.findall('«([^ ]*?-[0-9].*?)?»', string)
    for name in res:
        print(name)


def main():
    string = split_text(input('Введите название файла: '))
    check(string)

main()
