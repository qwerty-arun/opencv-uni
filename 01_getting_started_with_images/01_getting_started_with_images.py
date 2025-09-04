import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img_bgr = cv.imread("New_Zealand_Lake.jpg", 1)

img_hsv = cv.cvtColor(img_bgr, cv.COLOR_RGB2BGR)
h, s, v = cv.split(img_hsv)

plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(h, cmap="gray");plt.title("H Channel");
plt.subplot(142);plt.imshow(s, cmap="gray");plt.title("S Channel");
plt.subplot(143);plt.imshow(v, cmap="gray");plt.title("V Channel");
plt.subplot(144);plt.imshow(img_bgr);   plt.title("Original");
plt.show()