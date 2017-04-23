import os


def printing(dic):
    for key in dic:
        if dic[key] == max(dic.values()):
            print(key + ':', dic[key])
            break

        
def main():
    dic = {}
    for root, dirs, files in os.walk('.'):
        for d in dirs:
            if d.split('.')[0][0] not in dic:
                dic[d.split('.')[0][0]] = 1
            else:
                dic[d.split('.')[0][0]] += 1
    printing(dic)
            
    

if __name__=='__main__':
    main()
