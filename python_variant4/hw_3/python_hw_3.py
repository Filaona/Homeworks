inf = []
word = input('Введите латинскую словоформу: ')
word = word.strip()
while word != '':
    word = word.lower()
    if word.find(' ') == -1:
        if (word[-3:] == 'ire') or (word[-3:] == 'are') or (word[-3:] == 'ere') or (word[-1] == 'i') or (word[-4:] == 'isse'):     
           inf.append(word)   
    else:
        part_1 = word[:word.find(' ')]
        part_2 = word[word.find(' '):]
        part_2 = part_2.strip()
        if part_2.find(' ') == -1:
            if (part_2[-3:] == 'iri') and (part_1[-2:] == 'um'):
                inf.append(part_1 + ' ' + part_2)
            elif (part_2[-4:] == 'esse') and ((part_1[-1] == 'a') or (part_1[-2:] == 'um') or (part_1[-2:] == 'us')):
                inf.append(part_1 + ' ' + part_2)    
    word = input('Введите латинскую словоформу: ')
    word = word.strip()
for i in range(len(inf)):
    print(inf[i])    
