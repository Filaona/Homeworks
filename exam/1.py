import re
import os


def main():
    answer = open("answer1.txt", 'w')
    folder = 'news'
    for f in os.listdir(folder):
        with open(os.path.join(folder, f)) as text:
            answer.write(f + '\t' + str(len(re.findall('<w>', text.read()))) + '\n')
            text.close()
    answer.close()
            
    
if __name__ == '__main__':
    main()
