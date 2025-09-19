import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

# img = cv.imread('pics/face1.jpg')

cap = cv.VideoCapture('pics/trevor_eyes.mp4')

while cap.isOpened():
  _, img = cap.read()

  gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, 1.1, 13)

  for (x,y,w,h) in faces:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
      cv.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0, 0, 255), 5)

  cv.imshow('img', img)
  if cv.waitKey(1) & 0xFF == ord('q'):
    break