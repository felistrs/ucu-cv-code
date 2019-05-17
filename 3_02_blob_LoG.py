import math
import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt


def create_log_kernel(siz, std):
    x = y = np.linspace(-siz, siz, 2*siz+1)
    x, y = np.meshgrid(x, y)
    arg = -(x**2 + y**2) / (2*std**2)
    h = np.exp(arg)
    h[h < sys.float_info.epsilon * h.max()] = 0
    h = h/h.sum() if h.sum() != 0 else h
    h1 = h*(x**2 + y**2 - 2*std**2) / (std**4)
    return h1 - h1.mean()


img_fpath = './res/sunflowers_sq_512.png'
img = cv2.imread(img_fpath, cv2.IMREAD_GRAYSCALE)



kernel1 = create_log_kernel(21, 3.0)
kernel2 = create_log_kernel(21, 5.0)


img_out1 = cv2.filter2D(img, -1, np.array(kernel1))
img_out2 = cv2.filter2D(img, -1, np.array(kernel2))


plt.figure(0)
plt.imshow(img, cmap='gray')

plt.figure(1)
plt.imshow(kernel1)
plt.colorbar()
plt.figure(2)
plt.imshow(img_out1)
plt.colorbar()

plt.figure(3)
plt.imshow(kernel2)
plt.colorbar()
plt.figure(4)
plt.imshow(img_out2)
plt.colorbar()

plt.show()
