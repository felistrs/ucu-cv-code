import cv2
from matplotlib import pyplot as plt


img_fpath = './res/marker_cut_rgb_512.png'
img = cv2.imread(img_fpath)  #, cv2.IMREAD_GRAYSCALE)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img2 = cv2.GaussianBlur(img, (11, 11), 3.0)

fast = cv2.FastFeatureDetector_create()

kp = fast.detect(img, None)
kp2 = fast.detect(img2, None)

img_out = img.copy()
img_out2 = img.copy()

cv2.drawKeypoints(img, kp, img_out, color=(255,0,0))
cv2.drawKeypoints(img, kp2, img_out2, color=(255,0,0))


plt.figure(1)
plt.imshow(img)
plt.figure(2)
plt.imshow(img_out)
plt.figure(3)
plt.imshow(img_out2)

plt.show()
