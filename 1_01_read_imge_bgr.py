import cv2

img_fpath = './res/marker_cut_rgb_42.png'
img = cv2.imread(img_fpath)

print(img.shape)
print(img)

cv2.imshow('img', img)
cv2.waitKey(-1)



img_fpath = './res/colors_8x8.png'
img = cv2.imread(img_fpath)

print(img.shape)
print(img[0,:])

cv2.imshow('img', img)
cv2.waitKey(-1)
