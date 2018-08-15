#coding=utf-8
import os
from PIL import Image
import re

iphone5_height=1136
iphone5_width=640

def cimage():
    pics=os.listdir('images')
    for pic in pics:
        path='images/'+pic
#        print(path)
        img=Image.open(path)
        w,h=img.size
        
#        temp=0
#        if h<w:
#           temp=h
#           h=w
#           w=temp
        if h>iphone5_height:
            w=iphone5_height/h*w
            h=iphone5_height
            newimg=img.resize((int(w),int(h)),Image.ANTIALIAS)
        if w>iphone5_width:
            h=iphone5_width/w*h
            w=iphone5_width
            newimg=img.resize((int(w),int(h)),Image.ANTIALIAS)
        new_pic=re.sub(pic[:-4],pic[:-4]+'_new',pic)
        new_path='new/'+new_pic
        
        newimg.save(new_path)

        
if __name__=='__main__':
    cimage()
