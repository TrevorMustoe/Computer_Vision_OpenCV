import numpy as np
import cv2 as cv

def nothing(x):
  print(x)

img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow('image')

cv.createTrackbar('BLUE', 'image', 0, 255, nothing)
cv.createTrackbar('GREEN', 'image', 0, 255, nothing)
cv.createTrackbar('RED', 'image', 0, 255, nothing)

while(1):
  cv.imshow('image', img)
  k = cv.waitKey(1) & 0xFF
  if k==27:
    break
  
  b = cv.getTrackbarPos('BLUE', 'image')
  g = cv.getTrackbarPos('GREEN', 'image')
  r = cv.getTrackbarPos('RED', 'image')
  
  img[:] = [b, g, r]
  
cv.destroyAllWindows()