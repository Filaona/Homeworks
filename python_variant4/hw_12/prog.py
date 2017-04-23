import re
    

def main():
    file = open('text.txt', 'r', encoding = 'utf-8')
    string = re.sub('[!?.]', '@', file.read())
    if string:
            list_sen = [[word.strip('.,?!-(«»)') for word in sen.split()] for sen in string[:-1].split('@')]
    file.close()
    print({' '.join(sen): {word: len(word) for word in sen} for sen in list_sen})
    

if __name__ == '__main__':
    main()
