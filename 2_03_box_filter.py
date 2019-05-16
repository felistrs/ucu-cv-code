import cv2
import numpy as np
from matplotlib import pyplot as plt


img_fpath = './data/marker_cut_gray_42.png'
img = cv2.imread(img_fpath, cv2.IMREAD_GRAYSCALE)

height = img.shape[0]
width = img.shape[1]
img_res = np.zeros((height - 2, width - 2))


kernel = [
    [0.111, 0.111, 0.111],
    [0.111, 0.111, 0.111],
    [0.111, 0.111, 0.111]
]


for y in range(0, height-2):
    for x in range(0, width-2):

        sum = 0.0
        for yi in range(0, 3):
            for xi in range(0, 3):
                sum += kernel[yi][xi] * img[y + yi, x + xi]
        img_res[y, x] = sum

print(img_res)

plt.figure(1)
plt.imshow(img, cmap='gray')
plt.colorbar()

plt.figure(2)
plt.imshow(img_res, cmap='gray')
plt.colorbar()

plt.show()
