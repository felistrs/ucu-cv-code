import math
import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt


img_fpath = './res/marker_cut_rgb_512.png'
img = cv2.imread(img_fpath, cv2.IMREAD_GRAYSCALE)

dst = cv2.cornerHarris(img, 2, 3, 0.04)

plt.figure(0)
plt.imshow(img, cmap='gray')

plt.figure(1)
plt.imshow(dst)
plt.colorbar()

plt.show()
