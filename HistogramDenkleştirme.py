# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 13:02:16 2023

@author: aydin
"""

import numpy as np 
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('img.jpg',0)
hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf*float(hist.max())/cdf.max()
plt.plot(cdf_normalized,color='b')
plt.hist(img.flatten(),256,[0,256],color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'),loc='upper left')
plt.show()

img= cv.imread('img.jpg',0)
equ = cv.equalizeHist(img)
res = np.hstack((img,equ))
cv.imwrite('res.png',res)