import cv2
from matplotlib import pyplot as plt

img_marker = cv2.imread('./res/marker_cut_rgb_512.png', 0)
img = cv2.imread('./res/wheel_to_search_marker.png', 0)


orb = cv2.ORB_create()

kp1 = orb.detect(img_marker, None)
kp2 = orb.detect(img, None)

kp1, des1 = orb.compute(img_marker, kp1)
kp2, des2 = orb.compute(img, kp2)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

img3 = cv2.drawMatchesKnn(img_marker,kp1,img,kp2,good, None, flags=2)
plt.imshow(img3)
plt.show()
