import re

def text(file_name):
    file = open(file_name, 'r', encoding = 'utf-8')
    string = file.read()
    file.close()
    return string

def answer(string):
    res_file = open('result.txt', 'w', encoding = 'utf-8')
    res_file.write(string)
    res_file.flush()
    res_file.close()

def main():
    string = text('Философия.txt')
    string = re.sub('([^a-яА-Я]«?)филос(о|(о́))фи', '\\1астрол\\2ги', string)
    string = re.sub('([^а-яА-Я]«?)Филос(о|(о́))фи', '\\1Астрол\\2ги', string)
    answer(string)

if __name__ == '__main__':
    main()
