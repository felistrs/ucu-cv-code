import cv2

img_fpath = './res/colors_8x8.png'
img = cv2.imread(img_fpath)

width = img.shape[0]
height = img.shape[1]


def rgb_to_cmyk(rgb):
    r_ = rgb[0] / 255
    g_ = rgb[1] / 255
    b_ = rgb[2] / 255

    k = 1 - max([b_, g_, r_])
    if k != 1:
        c = (1 - r_ - k) / (1 - k)
        m = (1 - g_ - k) / (1 - k)
        y = (1 - b_ - k) / (1 - k)
    else:
        c = 0
        m = 0
        y = 0

    return c, m, y, k


for y in range(1):  # 1st row only
    for x in range(width):
        bgr = img[y, x]
        r = bgr[2]
        g = bgr[1]
        b = bgr[0]

        rgb = r, g, b
        cmyk = rgb_to_cmyk(rgb)
        print('RGB: %s = CMYK: %s' %(bgr, cmyk))
