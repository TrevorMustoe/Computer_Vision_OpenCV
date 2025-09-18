import cv2 as cv
import numpy as np

def nothing(x):
  pass

cap = cv.VideoCapture(0)

cv.namedWindow("Tracking")
cv.createTrackbar("LOWER HUE", "Tracking", 0, 255, nothing)
cv.createTrackbar("LOWER SATURATION", "Tracking", 0, 255, nothing)
cv.createTrackbar("LOWER VALUE", "Tracking", 0, 255, nothing)

cv.createTrackbar("UPPER HUE", "Tracking", 255, 255, nothing)
cv.createTrackbar("UPPER SATURATION", "Tracking", 255, 255, nothing)
cv.createTrackbar("UPPER VALUE", "Tracking", 255, 255, nothing)

while True:
  # frame = cv.imread('pics/boat.png')
  
  _, frame = cap.read()
  frame = cv.resize(frame, (640, 480))  # smaller frame = faster

  
  hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) #this is converting to an HSV image 
  
  l_h = cv.getTrackbarPos("LOWER HUE", "Tracking",)
  l_s = cv.getTrackbarPos("LOWER SATURATION", "Tracking",)
  l_v = cv.getTrackbarPos("LOWER VALUE", "Tracking",)
  
  u_h = cv.getTrackbarPos("UPPER HUE", "Tracking",)
  u_s = cv.getTrackbarPos("UPPER SATURATION", "Tracking",)
  u_v = cv.getTrackbarPos("UPPER VALUE", "Tracking",)
  
  
  
  l_r = np.array([l_h, l_s, l_v])
  u_r = np.array([u_h, u_s, u_v])
  
  mask = cv.inRange(hsv, l_r, u_r)
  
  res = cv.bitwise_and(frame, frame, mask=mask)
  
  cv.imshow("result", res)
  
  key = cv.waitKey(1)
  if key == 27:
    break
cap.release()
cv.destroyAllWindows()
