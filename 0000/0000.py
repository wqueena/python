# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 14:02:56 2018

@author: queena
"""

from PIL import Image,ImageDraw,ImageFont
#import matplotlib.pyplot as plt

font=ImageFont.truetype("arial.ttf",150)
img=Image.open('picture.jpg')
w,h=img.size
draw=ImageDraw.Draw(img)
draw.text((4*w/5,0),'4',fill=(255,0,0),font=font)
img.save('picture.jpg')
Image.open('picture.jpg').show()
#plt.figure("wechat")
#plt.axis('off')
#plt.imshow(img)
#plt.show()
