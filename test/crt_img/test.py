import sys as p_ss
import numpy as p_np
import cv2 as p_cv
from matplotlib import pyplot as p_pt

if len(p_ss.argv) > 1:
    img_nm = p_ss.argv[1]
else:
    img_nm = 'blank.png'

img = p_cv.imread(img_nm, -1)
# print(img)

"""
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
"""

#plt.axis("off")
# p_pt.imshow(img)
# p_pt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# p_pt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# p_pt.show()

ih, iw, ic = img.shape
print(ih, iw, ic)

for i in range(ih):
    for j in range(iw):
        if img[i, j][3] != 0:
            img[i, j] = [0, 0, 0, 255]
#        else:
#            img[i, j] = [255, 255, 255, 255]

p_pt.imshow(img)
p_pt.show()

ret = p_cv.imwrite('india.png', img)

# print("Done!")
