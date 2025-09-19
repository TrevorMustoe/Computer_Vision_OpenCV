import matplotlib.pylab as plt
import cv2 as cv
import numpy as np


img = cv.imread('pics/road3.png')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

height = img.shape[0]
width = img.shape[1]

region_of_interest_vertices = [
    (0, height),
    (width/1.95 , height/1.50),
    (width, height)
]

def region_of_interest(img, vertices):
  mask = np.zeros_like(img)
  channel_count = img.shape[2]
  match_mask_color = (255, ) * channel_count
  cv.fillPoly(mask, vertices, match_mask_color)
  masked_img = cv.bitwise_and(img, mask)
  return masked_img


masked_img = region_of_interest(img, np.array([region_of_interest_vertices], np.int32))

plt.imshow(masked_img)
plt.show()
