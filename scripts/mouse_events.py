import cv2

# events = [i for i in dir(cv2)] 
img = cv2.imread('pics/boat.png', 1)


def click_event(event, x, y, flags, param):
  if event == cv2.EVENT_LBUTTONDOWN:
    print(x, ', ', y)
    font = cv2.FONT_HERSHEY_COMPLEX
    strXY = str(x) + ', ' + str(y)
    cv2.putText(img, strXY, (x,y), font, 1, (255,255,0,), 2 )
    cv2.imshow('image', img)
    
  if event == cv2.EVENT_RBUTTONDOWN:
    blue = img[y, x, 0]
    green = img[y, x, 1]
    red = img[y, x, 2]
    font = cv2.FONT_HERSHEY_COMPLEX
    strBRG_Values = 'BLUE: ' + str(blue) + ', ' + 'GREEN: ' +  str(green) + ', ' + 'RED: ' +  str(red) 
    cv2.putText(img, strBRG_Values, (x,y), font, 1, (0,0,255,), 2 )
    cv2.imshow('image', img)
    print(green, blue, red)
    
img = cv2.imread('pics/boat.png', 1)
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()