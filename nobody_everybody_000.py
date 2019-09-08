#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 21:21:43 2019

@author: gykovacs
"""

from PIL import Image
import glob
import numpy as np

files= glob.glob('/home/gykovacs/pics/test/*resized.jpg')

images= np.array([np.array(Image.open(f).getdata()) for f in files])

i= Image.open(files[0])

image= np.median(images, axis=0)
image=image.astype(int)

i.putdata(list(tuple(pixel) for pixel in image))

i.save('/home/gykovacs/median.png')

median_img= image.copy()

for f in files:
    print(f)
    img= np.array(Image.open(f).getdata())
    diff= img - image
    n= np.linalg.norm(diff, axis=1)
    n= np.array([n, n, n]).T
    median_img= np.where(n > 40, img, median_img)
    
i.putdata(list(tuple(pixel) for pixel in median_img))
i.save('/home/gykovacs/everybody.png')
