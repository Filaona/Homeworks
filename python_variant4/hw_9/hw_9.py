import re

def split_text(file_name):
    file = open(file_name, 'r', encoding = 'utf-8')
    list_words = []
    string = file.read()
    string.lower()
    if string:
            for word in string.split():
                word = word.strip()
                list_words.append(word.strip('.,?!()') + ' ')
    file.close()
    return list_words

def check(list_words):
    for word in list_words:
        if re.match('вып((ит((а|о|ы|ого|ому|ая|ую|ою|ых|ыми|((о|ы)(й|м|е)))?))|(ивш(и|их|ими|ею|его|ему|ая|ую|((и|е)(й|м|е))))|(ил((и|а|о)?))|(ь((ю(т?))|(е(шь|т|м|те))))|(ей(те)?)|ив|ть) ', word):
            print(word)


def main():
    list_words = split_text(input('Введите название файла: '))
    check(list_words)

main()
