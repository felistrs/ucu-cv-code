import cv2
from matplotlib import pyplot as plt


img_in_fpath = './res/marker_cut_rgb_512.png'
img_in = cv2.imread(img_in_fpath)
img_in_gray = cv2.cvtColor(img_in, cv2.COLOR_BGR2GRAY)

img_out_path = './res/tracking/'


# Translation
for i in range(10):
    x = i*12
    y = i*5

    img_cut = img_in_gray[y:y+400, x:x+400]

    cv2.imshow('img_cut', img_cut)
    cv2.waitKey(-1)

    img_out_fpath = img_out_path + 'translation_' + str(i) + '.png'
    cv2.imwrite(img_out_fpath, img_cut)


# Rotation
rows = img_in_gray.shape[0]
cols = img_in_gray.shape[1]

for i in range(10):
    angle_deg = i * 10
    M = cv2.getRotationMatrix2D((cols/2,rows/2), angle_deg, 1)
    img_rot = cv2.warpAffine(img_in_gray, M, (cols,rows))

    img_rot_cut = img_rot[128:384, 128:384]

    cv2.imshow('img_rot_cut', img_rot_cut)
    cv2.waitKey(-1)

    img_out_fpath = img_out_path + 'rotation_' + str(i) + '.png'
    cv2.imwrite(img_out_fpath, img_rot_cut)

