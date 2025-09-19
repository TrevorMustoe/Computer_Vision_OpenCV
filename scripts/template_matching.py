import cv2 as cv
import numpy as np

img = cv.imread('pics/boat.png')
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
template = cv.imread("pics/small_boat.png", 0)
w, h = template.shape[::-1]

res = cv.matchTemplate(imgray, template, cv.TM_CCOEFF_NORMED)
print(res)
threshold = 0.97848
loc = np.where(res >= threshold)
print(loc)

for pt in zip(*loc[::-1]):
  cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0 , 255 , 0), 1)

cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()