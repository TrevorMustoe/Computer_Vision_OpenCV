import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('pics/books2.jpg', cv.IMREAD_GRAYSCALE)
lap = cv.Laplacian(img, cv.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))
sobelX = cv.Sobel(img, cv.CV_64F, 1, 0)
sobelY = cv.Sobel(img, cv.CV_64F, 0, 1)
canny = cv.Canny(img, 100, 200)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobel_combine = cv.bitwise_or(sobelX, sobelY)


titles = ['images', 'lap', 'sobelX', 'sobelY', 'sobel_combine', 'Canny']
images = [img, lap, sobelX, sobelY, sobel_combine, canny]

for i in range(6):
  plt.subplot(3, 3, i+1), plt.imshow(images[i], 'gray')
  plt.title(titles[i])
  plt.xticks([]), plt.yticks([])
  
plt.show()