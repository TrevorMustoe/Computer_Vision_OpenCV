# what is a histogram?
# as a graph or plot which gives you a overall ideas of intensity distrobution of an image. 


import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# Crates a 200 x 200 pixel black image
# img = np.zeros((200, 200), np.uint8 )

img = cv.imread('pics/boat.png', 0)

# cv.rectangle(img, (0, 100), (200, 200), (255), -1)
# cv.rectangle(img, (0, 50), (100, 100), (127), -1)

hist = cv.calcHist([img], [0], None, [256], [0, 256])

plt.plot(hist)

# b, g, r = cv.split(img)

# cv.imshow('img', img)
# cv.imshow('b', b)
# cv.imshow('g', g)
# cv.imshow('r', r)

# plt.hist(img.ravel(), 256, [0, 256])
# plt.hist(b.ravel(), 256, [0, 256])
# plt.hist(g.ravel(), 256, [0, 256])
# plt.hist(r.ravel(), 256, [0, 256])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()