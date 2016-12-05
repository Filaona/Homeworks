text = False
word = 0
word_punc = 0
f = open('somefile.txt',encoding = 'utf-8')
string = f.read()
for i in range(1,len(string)):
        if (string[i] == "\n"):
            if text:
                word += 1
                text = False
        elif string[i] == ' ':
            if text: 
                word += 1
                text = False
        elif (string[i] == '.') or (string[i] == ','):
            if text:
                word += 1
                word_punc += 1
                text = False
        else:
            text = True
if text:
    word += 1
if word != 0:
        print('%.2f' % (word_punc/word*100), '%')
else:
        print('Файл пуст')
    

            

            
                
                   
     
     
