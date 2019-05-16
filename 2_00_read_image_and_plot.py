import numpy as np
import cv2

img_h_fpath = './res/grey_h_gradient_9x9.png'
img_v_fpath = './res/grey_v_gradient_9x9.png'


img_h = cv2.imread(img_h_fpath, cv2.IMREAD_GRAYSCALE)
img_v = cv2.imread(img_v_fpath, cv2.IMREAD_GRAYSCALE)


cv2.imshow('img_h', img_h)
cv2.imshow('img_v', img_v)
cv2.waitKey(-1)

img_div2 = img_h // 2
cv2.imshow('img_h // 2', img_div2)
cv2.waitKey(-1)

img_mul2 = img_h * 2
cv2.imshow('img_h * 2', img_mul2)
cv2.waitKey(-1)

sum_ = img_h + img_v
cv2.imshow('img_h + img_v', sum_)
cv2.waitKey(-1)

# eq128 = (img_h == 128).astype(np.uint8) * 255
# cv2.imshow('img_h == 128', eq128)

# gt128 = (img_h > 128).astype(np.uint8) * 255
# cv2.imshow('img_h > 128', gt128)
# cv2.waitKey(-1)
