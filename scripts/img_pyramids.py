import cv2 as cv
import numpy as np

img = cv.imread("pics/books2.jpg")
layer = img.copy()

gp = [layer]

# Gaussian Pyramid
for i in range(6):
    layer = cv.pyrDown(layer)
    gp.append(layer)

layer = gp[5]
cv.imshow("upper_level", layer)
cv.imshow("OG Image", img)

# Laplacian Pyramid
for i in range(5, 0, -1):
    gauss_ext = cv.pyrUp(gp[i])
    
    # Make sure gauss_ext matches gp[i-1]
    gauss_ext = cv.resize(gauss_ext, (gp[i-1].shape[1], gp[i-1].shape[0]))
    
    lp = cv.subtract(gp[i-1], gauss_ext)
    cv.imshow(f"Laplacian {i}", lp)

cv.waitKey(0)
cv.destroyAllWindows()
