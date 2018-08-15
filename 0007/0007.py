import os

PATH=os.getcwd()

def code():
    total_line=0
    comment_line=0
    blank_line=0
 #    print(os.listdir())
    for i in os.listdir():
        with open(i,'r',encoding='utf-8') as each:
            for line in each:
                total_line+=1
                if line.strip().startswith('#'):
                    comment_line+=1
                if line.strip()=='':
                    blank_line+=1
                
    print('total_line:'+str(total_line))
    print('comment_line:'+str(comment_line))
    print('blank_line:'+str(blank_line))
if __name__=='__main__':
    code()