#!/usr/bin/env python3

from PIL import ImageEnhance
from PIL import Image

def get_average_color(img):
    img = Image.open('/home/pi/Desktop/img5.jpg')
    img = img.resize((50,50))
    #print(img.size)
    img = img.crop((15, 15, 35, 35))
    converter = ImageEnhance.Color(img)
    img = converter.enhance(2.5)
    #img.show()
    #print(img.size)
    w,h = img.size

    r_tot = 0
    g_tot = 0
    b_tot = 0

    count = 0
    for i in range(0, w):
        for j in range(0, h):
            r, g, b = img.getpixel((i,j))
            r_tot += r
            g_tot += g
            b_tot += b
            count += 1

    return (r_tot/count, g_tot/count, b_tot/count)

my_img = Image.open('/home/pi/Desktop/button.jpg')
average_color = get_average_color(my_img)
#print(average_color)
