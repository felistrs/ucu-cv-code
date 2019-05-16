import cv2

img_fpath = './res/marker_cut_gray_42.png'
img = cv2.imread(img_fpath, cv2.IMREAD_GRAYSCALE)

print(img.shape)
print(img)

cv2.imshow('img', img)
cv2.waitKey(-1)
