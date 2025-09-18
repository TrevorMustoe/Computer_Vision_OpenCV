import cv2 as cv
import numpy as np

img = cv.imread('pics/books2.jpg')
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

#Notes about the above: 

# CONTOURS are a python list of all the contours in an image. Each indicidual contour is a nnumpy array of coordinates (x,y) of boundry points of an object

print("Number of contours:" + str(len(contours)))

print(contours[0])

cv.drawContours(img, contours, -1, (0, 255, 0), 2)


cv.imshow('OG', img)
cv.imshow('Gray', imgray)
cv.waitKey(0)
cv.destroyAllWindows()