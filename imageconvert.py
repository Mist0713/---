import numpy as np
from PIL import Image
from tabulate import tabulate
import csv

#image file name : "C:\Users\전남과학고-09\Desktop\전곽톤\Image_created_with_a_mobile_phone.png.webp"
img_name = ('Image_created_with_a_mobile_phone.png.webp')
im = Image.open('C:\\Users\\전남과학고-09\\Desktop\\전곽톤\\'+img_name)
pix = np.array(im)

size_x, size_y = im.size[0], im.size[1] #size 픽셀값

print(size_x, size_y)
result = 0

rgb_list = [[] for _ in range(601)]

for i in range(0, size_x):
    for j in range(0, size_y):
        rgb_list[i].append(pix[i][j])

print(tabulate(rgb_list, headers=["1", "2", "3", "4"], tablefmt='firstrow'))

