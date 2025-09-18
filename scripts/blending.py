import cv2 as cv
import numpy as np

kiwi = cv.imread('pics/kiwi.jpg')
orange = cv.imread('pics/orange.jpg')

# Resize both images to the same size (important!)
orange = cv.resize(orange, (kiwi.shape[1], kiwi.shape[0]))

# Quick half-and-half image for reference
cols = kiwi.shape[1]
kW_Or = np.hstack((kiwi[:, :cols//2], orange[:, cols//2:]))

# ---------------- Gaussian Pyramids ----------------
# Kiwi
gp_kw = [kiwi.copy()]
for i in range(6):
    gp_kw.append(cv.pyrDown(gp_kw[-1]))

# Orange
gp_og = [orange.copy()]
for i in range(6):
    gp_og.append(cv.pyrDown(gp_og[-1]))

# ---------------- Laplacian Pyramids ----------------
# Kiwi
lp_kw = [gp_kw[-1]]  # smallest level
for i in range(5, 0, -1):
    gauss_ext = cv.pyrUp(gp_kw[i])
    gauss_ext = cv.resize(gauss_ext, (gp_kw[i-1].shape[1], gp_kw[i-1].shape[0]))
    lap = cv.subtract(gp_kw[i-1], gauss_ext)
    lp_kw.append(lap)

# Orange
lp_og = [gp_og[-1]]  # smallest level
for i in range(5, 0, -1):
    gauss_ext = cv.pyrUp(gp_og[i])
    gauss_ext = cv.resize(gauss_ext, (gp_og[i-1].shape[1], gp_og[i-1].shape[0]))
    lap = cv.subtract(gp_og[i-1], gauss_ext)
    lp_og.append(lap)

# ---------------- Blend pyramids ----------------
Kiwi_orange_pyramid = []
for kiwi_lap, orange_lap in zip(lp_kw, lp_og):
    cols, rows, ch = kiwi_lap.shape
    laplacian = np.hstack((kiwi_lap[:, :cols//2], orange_lap[:, cols//2:]))
    Kiwi_orange_pyramid.append(laplacian)

# ---------------- Reconstruct image ----------------
kiwi_orange_reconstruct = Kiwi_orange_pyramid[0]
for i in range(1, len(Kiwi_orange_pyramid)):
    kiwi_orange_reconstruct = cv.pyrUp(kiwi_orange_reconstruct)
    kiwi_orange_reconstruct = cv.resize(kiwi_orange_reconstruct,
                                        (Kiwi_orange_pyramid[i].shape[1], Kiwi_orange_pyramid[i].shape[0]))
    kiwi_orange_reconstruct = cv.add(Kiwi_orange_pyramid[i], kiwi_orange_reconstruct)

# ---------------- Show results ----------------
cv.imshow("Half & Half", kW_Or)
cv.imshow("Blended", kiwi_orange_reconstruct)
cv.waitKey(0)
cv.destroyAllWindows()
