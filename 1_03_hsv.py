import cv2

img_fpath = './res/colors_8x8.png'
img = cv2.imread(img_fpath)

width = img.shape[0]
height = img.shape[1]


def rgb_to_hsv(rgb):
    r_ = rgb[0] / 255
    g_ = rgb[1] / 255
    b_ = rgb[2] / 255

    max_ = max([r_, g_, b_])
    min_ = min([r_, g_, b_])

    v = max_

    s = 0
    if max_ != 0:
        s = 1 - min_ / max_

    h = 0

    if max_ == min_:
        h = 0

    elif r_ == max_ and r_ > b_ and g_ > b_:
        h = 60 * (g_ - b_) / (max_ - min_)

    elif r_ == max_ and r_ < b_ and g_ < b_:
        h = 60 *(g_ - b_) / (max_ - min_) + 360

    elif g_ == max_:
        h = 60 *(b_ - r_) / (max_ - min_) + 120

    elif b_ == max_:
        h = 60 *(r_ - g_) / (max_ - min_) + 240

    return int(h // 2), s, v


for y in range(1):  # 1st row only
    for x in range(width):
        bgr = img[y, x]
        r = bgr[2]
        g = bgr[1]
        b = bgr[0]

        rgb = r, g, b
        hsv = rgb_to_hsv(rgb)
        print('RGB: %s = HSV: %s' %(bgr, hsv))


img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# H in [0..179]
print(img_hsv[0,:,:])
