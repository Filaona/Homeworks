import re


def split_text():
    file = open('melany.txt', 'r', encoding = 'utf-8')
    string = file.read()
    file.close()
    return string

def main():
    string = split_text()
    string1 = re.sub('((\. )|(\n))', '\1@',string)
    print(string1)

if __name__ == '__main__':
    main()
