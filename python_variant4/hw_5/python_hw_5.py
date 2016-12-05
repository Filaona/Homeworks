text = False;
word = 0
word_punc = 0
f = open('somefile.txt','r',encoding = 'utf-8')
string = f.read()
string.strip(' ,.')
for i in range(0,len(string)):
        if string[i] == ' ':
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
print(word_punc, word)
print(word_punc/word*100, '%')
    

            

            
                
                   
     
     
