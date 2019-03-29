import sys as p_ss
import numpy as p_np
import cv2 as p_cv
from matplotlib import pyplot as p_pt

img = p_cv.imread('../../img/india.jpg', 1)
ih, iw, ic = img.shape
print(ih, iw, ic)

C = [[109, 268], [233, 324], [233, 332], [223, 346], [247, 364], [303, 343]]

for i in range(len(C)):
	img[C[i][0]][C[i][1]] = [0, 0, 255]
    
ret = p_cv.imwrite('../../img/output.jpg', img)

from IPython.display import Image
Image('../../img/output.jpg', width=500, height=500)
