import re
from collections import Counter
import os

FILE_PATH='diary'

def GetCounter(articlefilesource):
    pattern=r'[a-zA-Z]+|\$?\d+%?$'
    with open(articlefilesource) as f:
        r=re.findall(pattern,f.read())
        return Counter(r)
stop_word = ['the', 'in', 'of', 'and', 'to', 'has', 'that', 's', 'is', 'are', 'a', 'with', 'as', 'an']    
def Run(FILE_PATH):
    os.chdir(FILE_PATH)
#    print(os.getcwd())
    for path in os.listdir(os.getcwd()):
        total_counter=Counter()
        total_counter+=GetCounter(path)
        for i in stop_word:
            total_counter[i]=0
        print(path.replace('.txt','')+':'+total_counter.most_common()[0][0])
    
if __name__=='__main__':
    Run(FILE_PATH)