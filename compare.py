import cv2
import matplotlib.pyplot as plt
import numpy as np

from zipfile import ZipFile
from urllib.request import urlretrieve

# Read image as gray scale.
img_rec = cv2.imread("pics/circle.jpg", cv2.IMREAD_GRAYSCALE)
img_cir = cv2.imread("pics/boat.png", cv2.IMREAD_GRAYSCALE)

# Detect ORB features and compute descriptors.
MAX_NUM_FEATURES = 500
orb = cv2.ORB_create(MAX_NUM_FEATURES)
keypoints1, descriptors1 = orb.detectAndCompute(img_rec, None)
keypoints2, descriptors2 = orb.detectAndCompute(img_cir, None)

# Display
im1_display = cv2.drawKeypoints(img_rec, keypoints1, outImage=np.array([]), 
                                color=(255, 0, 0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

im2_display = cv2.drawKeypoints(img_cir, keypoints2, outImage=np.array([]), 
                                color=(255, 0, 0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

plt.show()  # <- This line is essential!