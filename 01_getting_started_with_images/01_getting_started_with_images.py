import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# img = np.ones((3, 3, 3))
# print(img)
# print(img.shape)
# print(cv.add(img, 20))

img = cv.imread("assets/black-hole.jpg", 1)
print(img)
print(img.shape)
print(img.dtype)

# img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# or 
img_rev_channels = img[:, :, ::-1]
# plt.imshow(img_rev_channels)
# plt.axis("off")
# plt.show()


# Split the image into the B,G,R components
img_NZ_bgr = cv.imread("assets/black-hole.jpg", cv.IMREAD_COLOR)
b, g, r = cv.split(img_NZ_bgr)

# Show the channels
plt.figure(figsize=[20, 5])

plt.subplot(141);plt.imshow(r, cmap="gray");plt.title("Red Channel")
plt.subplot(142);plt.imshow(g, cmap="gray");plt.title("Green Channel")
plt.subplot(143);plt.imshow(b, cmap="gray");plt.title("Blue Channel")

# Merge the individual channels into a BGR image
imgMerged = cv.merge((b, g, r))
# Show the merged output
plt.subplot(144)
plt.imshow(imgMerged[:, :, ::-1])
plt.title("Merged Output")
plt.show()