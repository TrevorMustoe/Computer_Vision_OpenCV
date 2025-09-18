# import cv2

# img = cv2.imread('pics/boat.png', 1)

# img = cv2.arrowedLine(img, (0,0), (300,300), (0, 0, 255), 3)

# cv2.imshow('image', img)


# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2
import datetime
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3, 1080)
cap.set(4, 1920)

# print(cap.get(3))
# print(cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:


        font = cv2.FONT_HERSHEY_COMPLEX
        text = str(datetime.datetime.now())
        cv2.putText(frame, text, (50,50), font, 2, (0,0,255), 5)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    else:
        break

cap.release()
cv2.destroyAllWindows()