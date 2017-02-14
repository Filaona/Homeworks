import re

def f_text(file_name):
    file = open(file_name, 'r', encoding = 'utf-8')
    string = file.read()
    file.close()
    return string

def f_strings(file_name):
    file = open(file_name, 'r', encoding = 'utf-8')
    q_strings = 0
    for line in file:
        q_strings += 1
    file.close()
    return str(q_strings)

def dic(res):
    d = {}
    for lemma_type in res:
        if lemma_type in d:
            d[lemma_type] += 1
        else:
            d[lemma_type] = 1
    return d

def tuple_type(text):
    res = re.findall('lemma.*&?type="(.*?)"',text)
    return res

def answer_str(string):
    res_file = open('result.txt', 'w', encoding = 'utf-8')
    res_file.write(string + '\n')
    res_file.flush()
    res_file.close()

def answer_dic(d):
    res_file = open('result.txt', 'a', encoding = 'utf-8')
    list_key = list(d.keys())
    for key in list_key:
        res_file.write(key + '\n')
    res_file.flush()
    res_file.close()

def answer_adj(d):
    res_file = open('result_adj.txt', 'w', encoding = 'utf-8')
    for type_adj in d:
        res_file.write(type_adj + ' ' + str(d.get(type_adj)) + '\n')
    res_file.flush()
    res_file.close()

def tuple_adj(text):
    res = re.findall('lemma.*&?type="(l.f.*?)"', text)
    return res

def dic_adj(res):
    d = {}
    for adj_type in res:
        if adj_type in d:
            d[adj_type] += 1
        else:
            d[adj_type] = 1
    return d


def main():
    answer_str(f_strings('corpus.xml'))
    answer_dic(dic(tuple_type(f_text('corpus.xml'))))
    answer_adj(dic_adj(tuple_adj(f_text('corpus.xml'))))
    
    

if __name__ == '__main__':
    main()
