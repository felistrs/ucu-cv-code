import numpy as np
from matplotlib import pyplot as plt
from scipy import signal
import cv2


img_fpath = './data/marker_cut_gray_42.png'
img = cv2.imread(img_fpath, cv2.IMREAD_GRAYSCALE)

img = img.astype(np.float32)


# Horizontal edge detection
kernel_h = [
    [-1, 1]
]

# Vertical edge detection
kernel_v = [
    [-1],
    [ 1]
]


img_h = signal.convolve2d(img, kernel_h, boundary='symm', mode='same')
img_v = signal.convolve2d(img, kernel_v, boundary='symm', mode='same')

img2 = np.sqrt(img_h * img_h + img_v * img_v)


plt.figure(1)
plt.imshow(img, cmap='gray')
plt.colorbar()

plt.figure(2)
plt.imshow(img2, cmap='gray')
plt.colorbar()

plt.figure(3)
plt.imshow(img_h, cmap='gray')
plt.colorbar()

plt.figure(4)
plt.imshow(img_v, cmap='gray')
plt.colorbar()

plt.show()
