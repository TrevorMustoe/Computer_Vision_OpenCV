import cv2

img = cv2.imread('pics/boat.png', 0)

print(img.shape)
print(img.size)
print(img.dtype)

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

sail = img[400:475, 500:574]
sail_resized = cv2.resize(sail, (219, 285))  # (width, height)

img[119:404, 281:500] = sail_resized

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
