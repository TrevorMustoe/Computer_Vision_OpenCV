import cv2 as cv
import numpy as np

img = cv.imread('pics/shapes.png')
output = img.copy()

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 5)
circles = cv.HoughCircles(gray,
                         cv.HOUGH_GRADIENT, 1, 20, param1=30, 
                         param2=50,
                         minRadius=0, 
                         maxRadius=0)
detected_cirles = np.uint16(np.around(circles))
for (x,y,r) in detected_cirles[0, :]:
  cv.circle(output, (x,y), r, (0, 255, 0), 3)
  cv.circle(output, (x,y), 2, (0, 0, 255), 5)
  
  

cv.imshow('Output', output)
cv.waitKey(0)
cv.destroyAllWindows()