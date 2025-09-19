import matplotlib.pylab as plt
import cv2 as cv
import numpy as np

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    match_mask_color = 255
    cv.fillPoly(mask, vertices, match_mask_color)
    masked_img = cv.bitwise_and(img, mask)
    return masked_img

def draw_lines(img, lines):
    img = np.copy(img)
    blank_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv.line(blank_img, (x1, y1), (x2, y2), (0, 255, 0), thickness=3)
    
    img = cv.addWeighted(img, 0.8, blank_img, 1, 0.0)
    return img

def process(img): 
    height = img.shape[0]
    width = img.shape[1]
    region_of_interest_vertices = [
        (0, height),
        (width/2 , height/1.80),
        (width, height)
    ]
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    canny_img = cv.Canny(gray_img, 50, 150)  # lower thresholds
    masked_img = region_of_interest(canny_img, np.array([region_of_interest_vertices], np.int32))
    lines = cv.HoughLinesP(masked_img, rho=1, theta=np.pi/180, threshold=50, minLineLength=100, maxLineGap=10)
    img_with_lines = draw_lines(img, lines)
    return img_with_lines

cap = cv.VideoCapture('pics/roadvid2.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame to smaller width to speed up processing
    scale_percent = 640 / frame.shape[1]  # target width = 640px
    new_width = int(frame.shape[1] * scale_percent)
    new_height = int(frame.shape[0] * scale_percent)
    frame_small = cv.resize(frame, (new_width, new_height))

    frame_processed = process(frame_small)

    cv.imshow('Frame', frame_processed)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
