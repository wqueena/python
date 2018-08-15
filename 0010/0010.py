import random
from PIL import Image, ImageFont, ImageDraw, ImageFilter

size = (200, 50)
len = 4


def Ver_Code(len):
    source = []
    for i in range(0, 10):
        source.append(str(i))
    for i in range(ord('a'), ord('z') + 1):
        source.append(chr(i))
    for i in range(ord('A'), ord('Z') + 1):
        source.append(chr(i))


#    for i in range(len):
#    code = random.choices(source, k=len)
    code = ''.join(random.choices(source, k=len))
    return code


def get_color():
    return (random.randint(0, 256), random.randint(0, 256),
            random.randint(0, 256))


def Img_Code():
    width, height = size
    image = Image.new('RGB', (width, height), (192, 192, 192))
    font = ImageFont.truetype('arial.ttf', 36)
    draw = ImageDraw.Draw(image)
    code = Ver_Code(len)
    for i in range(len):
        draw.text((55 * i + 5, 0), code[i], font=font, fill=get_color())
    image = image.filter(ImageFilter.BLUR)
    for i in range(random.randint(2000, 3000)):  # 添加噪点
        draw.point(
            (random.randint(0, width), random.randint(0, height)),
            get_color())
    image.show()
    image.save('test.jpg')
    


if __name__ == '__main__':
    Img_Code()

# from PIL import ImageDraw,Image
# im = Image.new('RGB',(400,400),'white')
# draw = ImageDraw.Draw(im)
# draw.point((150,150),'black')
# im.show()