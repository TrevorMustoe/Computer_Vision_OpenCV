import matplotlib.pylab as plt
import cv2 as cv
import numpy as np

def region_of_interest(img, vertices):
  mask = np.zeros_like(img)
  # channel_count = img.shape[2]
  match_mask_color = 255
  cv.fillPoly(mask, vertices, match_mask_color)
  masked_img = cv.bitwise_and(img, mask)
  return masked_img

def draw_lines(img, lines):
  img = np.copy(img)
  blank_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
  
  for line in lines:
    for x1, y1, x2, y2 in line:
      cv.line(blank_img, (x1, y1), (x2, y2), (0, 255, 0), thickness=3)
      
  img = cv.addWeighted(img, 0.8, blank_img, 1, 0.0)
  return img
  

img = cv.imread('pics/road3.png')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)


height = img.shape[0]
width = img.shape[1]

region_of_interest_vertices = [
    (100, height),
    (width/1.95 , height/1.50),
    (width, height)
]

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny_img = cv.Canny(gray_img, 300, 300)
masked_img = region_of_interest(canny_img, np.array([region_of_interest_vertices], np.int32))

lines = cv.HoughLinesP(masked_img, rho=6, theta= np.pi / 60, threshold=160, lines=np.array([]), minLineLength=100, maxLineGap= 10)

img_with_lines = draw_lines(img, lines)

plt.imshow(img_with_lines)
plt.show()
