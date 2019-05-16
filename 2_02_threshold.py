import cv2
from matplotlib import pyplot as plt


img_fpath = './res/marker_cut_gray_42.png'
img = cv2.imread(img_fpath, cv2.IMREAD_GRAYSCALE)


_, img_thr = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

plt.imshow(img_thr, cmap='gray')
plt.show()
