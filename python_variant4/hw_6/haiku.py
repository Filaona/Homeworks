import random



def verb(num, syl):
    if num == 'sg':
            return random.choice(verb_sg_3)
    else:
        if syl == 3:
            return random.choice(verb_pl_3)
        else:
            return random.choice(verb_pl_4)

        

def noun(num, syl):
    if num == 'sg':
        if syl == 2:
            return random.choice(noun_sg_2)
        else:
            return random.choice(noun_sg_4)
    else:
        if syl == 2:
            return random.choice(noun_pl_2)
        elif syl == 3:
            return random.choice(noun_pl_3)
        else:
            return random.choice(noun_pl_4)

        

def connegative():
    global conneg
    return random.choice(conneg)

def neg():
    global neg_part
    return random.choice(neg_part)

def punc():
    mark = ['.', '...', '!']
    return random.choice(mark)

def var_7_1():
    return noun('sg', 4) + ' ' + verb('sg', 3) + punc()
    
def var_7_2():
    return noun('pl', 3) + ' ' + verb('pl', 4) + punc()
    
def var_7_3():
    return noun('pl', 4) + ' ' + verb('pl', 3) + punc()

def var_5_1():
    return noun('sg', 2) + ' ' + verb('sg', 3) + punc()

def var_5_2():
    return noun('pl', 2) + ' ' + verb('pl', 3) + punc()
    
def var_5_3():
    return neg() + ' ' + connegative() + punc()
    

    
def make_var_7():
    var = random.choice([1,2,3])
    if var == 1:
        return var_7_1()
    elif var == 2:
        return var_7_2()
    else:
        return var_7_3()

def make_var_5():
    var = random.choice([1,2,3])
    if var == 1:
        return var_5_1()
    elif var == 2:
        return var_5_2()
    else:
        return var_5_3()

    

def make_list(file):
    f = open(file, 'r', encoding = 'utf-8')
    n = []
    s = f.read()
    n = s.split()
    f.close()
    return n
    
    

def finnish_haiku():
    print(make_var_5())
    print(make_var_7())
    print(make_var_5())


    
noun_sg_2 = make_list('noun_sg_2.txt')
noun_pl_2 = make_list('noun_pl_2.txt')
noun_pl_3 = make_list('noun_pl_3.txt')
noun_pl_4 = make_list('noun_pl_4.txt')
noun_sg_4 = make_list('noun_sg_4.txt')
verb_sg_3 = make_list('verb_sg_3.txt')
verb_pl_3 = make_list('verb_pl_3.txt')
verb_pl_4 = make_list('verb_pl_4.txt')
conneg = make_list('conneg.txt')
neg_part = make_list('neg_part.txt')

finnish_haiku()
