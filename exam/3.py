import re
import os




def printing(res, number, answer):
     answer.write(res[number-1] + ' ' + res[number] + '\t')
     for i in range(0, len(res)-1):
         answer.write(res[i] + ' ')
     answer.write('\n')


def main():
    answer = open("answer3.txt", 'w')
    folder = 'news'
    for f in os.listdir(folder):
        with open(os.path.join(folder, f)) as text:
            for sent in text.read().split('<se>')[1:]:
                words = sent.split('<w>')
                res = [words[x][words[x].rfind('a>') + 2:words[x].rfind('<')] for x in range(0, len(words)-1)]
                for number in range(1,len(words)-1):
                    if (re.search('S', words[number])) and (re.search('gen', words[number])):
                        if (re.search('A', words[number - 1])) and (re.search('gen', words[number -1])):
                            printing(res, number, answer)
                        
                    
    
        text.close()
    
            
    
if __name__ == '__main__':
    main()
