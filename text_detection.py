import cv2 as cv
import numpy
import matplotlib.pyplot as plt
import easyocr as easy 

book_img1= 'pics/books2.jpg'
book_img2 = 'pics/books.webp'
stop = 'pics/sign.png'
img = cv.imread(book_img1, cv.IMREAD_GRAYSCALE)

reader = easy.Reader(['en'])

text = reader.readtext(img)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2) #This works better for books


text_lines = []

for t in text:
  # print(t)
  
  bbox, returned_text, score = t
  #this section is creating top left corner and bottom right corner but cv2 likes the points to be tuples and integers only.
  pt1 = (int(bbox[0][0]), int(bbox[0][1]))  # top left
  pt2 = (int(bbox[2][0]), int(bbox[2][1]))  # bottom-right
  # Calculate area
  width  = pt2[0] - pt1[0]
  height = pt2[1] - pt1[1]
  area   = width * height
  text_lines.append((area, returned_text, pt1, pt2))

  color = (255, 0, 0) #color red
  thick = 5
  cv.rectangle(th2, pt1, pt2, color, thick)

text_lines.sort(reverse=True, key=lambda x: x[0])

# Step 3: Optional - print sorted lines
for area, text_lines, pt1, pt2 in text_lines:
    print(f"Area: {area}, Text: {text_lines}")

plt.imshow(th2, cmap='gray')
plt.show()