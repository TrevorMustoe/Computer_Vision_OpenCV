import cv2
import matplotlib.pyplot as plt
import numpy as np

from zipfile import ZipFile
from urllib.request import urlretrieve

# Read image as gray scale.
img_rec = cv2.imread("pics/circle.jpg", cv2.IMREAD_GRAYSCALE)
img_cir = cv2.imread("pics/boat.png", cv2.IMREAD_GRAYSCALE)

img_cir_resized = cv2.resize(img_cir, (img_rec.shape[1], img_rec.shape[0]))
result = cv2.bitwise_or(img_rec, img_cir_resized)
plt.imshow(result, cmap="gray")

plt.show()  # <- This line is essential!
