import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

# img = cv.imread('pics/face1.jpg')

cap = cv.VideoCapture('pics/face_vid.mp4')

while cap.isOpened():
  _, img = cap.read()

  gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, 1.1, 10)

  for (x,y,w,h) in faces:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

  cv.imshow('img', img)
  if cv.waitKey(1) & 0xFF == ord('q'):
    break