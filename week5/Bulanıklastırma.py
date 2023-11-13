# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 23:59:15 2023

@author: aydin
"""

import cv2
import numpy as np

#reading the image
image = cv2.imread('img.jpg')

#Creating the kernel(2d convolution matrix)
kernel1 = np.ones((5,5), np.float32)/30

#Applying the filter2D() function
img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)

#Showing the original and output image
cv2.imshow('Original',image)
cv2.imshow('Kernel Blur', img)

cv2.waitKey()
cv2.destroyAllWindows()