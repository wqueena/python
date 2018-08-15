import re
#import string

def read():
    words=[]
    words_=[]
    dic={}
    for line in open('0004.txt','r'):
        line = re.sub(r"\W", ' ',line)    #把所有的标点都变成空格
        line=line.lower()                 #把所有的大写都变成小写
        line=line.split()                 #拆分单词
        words.append(line)
    index1,index2=0,0
    for index1 in range(len(words)):
        for index2 in range(len(words[index1])):
            words_.append(words[index1][index2])
            index2+=1
        index1+=1
    for word in words_:
        if dic.__contains__(word):
            dic[word]+=1
        else:
            dic[word]=1
#    print(dic)
#    print(words_)
    
    return dic

def write(dic):
    f=open('0004_out.txt','w')
    for key,value in dic.items():
        f.write(key+':'+str(value)+'\n')
    f.close()

if __name__=='__main__':
    write(read())