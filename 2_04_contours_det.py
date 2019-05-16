import cv2
from matplotlib import pyplot as plt


img_fpath = './res/marker_cut_gray_42.png'
# img_fpath = './res/marker_cut_gray_42_noise.png'
img_gray = cv2.imread(img_fpath, cv2.IMREAD_GRAYSCALE)

img = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)

_, img_thr = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(img_thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0, 255, 0), 1)

plt.imshow(img, cmap='gray')
plt.show()
