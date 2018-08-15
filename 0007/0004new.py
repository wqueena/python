import re
from collections import Counter
FILESOURCE = '0004.txt'

def getMostCommonWord(articlefilesource):
    '''输入一个英文的纯文本文件，统计其中的单词出现的个数'''
    pattern = r'''[A-Za-z]+|\$?\d+%?$'''
    with open(articlefilesource) as f:
        r = re.findall(pattern,f.read())
        words=[]
        for word in r:
            word=word.lower()
            words.append(word)
#        print(type(Counter(words)))
        m=Counter(words)
        f=open('0004new_out.txt','w')
        for each in m:
            f.write(each+':'+str(m[each])+'\n')

        return Counter(words)

if __name__ == '__main__':
    getMostCommonWord(FILESOURCE)
