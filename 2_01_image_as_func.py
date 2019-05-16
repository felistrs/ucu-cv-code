import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy.misc
import cv2


img_fpath = './res/marker_cut_gray_42.png'
img = cv2.imread(img_fpath, cv2.IMREAD_GRAYSCALE)


plt.figure(1)
plt.imshow(img, cmap='gray')
plt.colorbar()

xx, yy = np.mgrid[0:img.shape[0], 0:img.shape[1]]
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(xx, yy, img ,rstride=1, cstride=1, cmap=plt.cm.gray, linewidth=0)

plt.show()
