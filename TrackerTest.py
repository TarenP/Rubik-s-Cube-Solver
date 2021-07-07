import picamera
import matplotlib.image as img
from PIL import Image
import cv2
import numpy as np

with picamera.PiCamera() as camera:
    camera.resolution = (720, 720)
    camera.capture("/home/pi/Desktop/tracker.jpg")

cap = cv2.VideoCapture(0)
while True:

    _, frame = cap.read()
    rows, cols, _=frame.shape
    
    x_medium = int(cols / 2)
    center = int(cols/ 2)
    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#White color
    low_white = np.array([0, 0, 0])
    high_white = np.array([255, 99, 255])
    white_mask = cv2.inRange(hsv_img, low_white, high_white)
    contours1, _ = cv2.findContours(white_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours1 = sorted(contours1, key=lambda x:cv2.contourArea(x), reverse=True)
        
    for cnt in contours1:
        area1 = cv2.contourArea(cnt)
        if area1 > 5000:
            faceColors[counter-1] = "white"
            contoursColor = contours1


    #yellow color
    low_yellow = np.array([23, 108, 90])
    high_yellow = np.array([40, 255, 255])
    yellow_mask = cv2.inRange(hsv_img, low_yellow, high_yellow)
    contours2, _ = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours2 = sorted(contours2, key=lambda x:cv2.contourArea(x), reverse=True)
        
    for cnt in contours2:
        area2 = cv2.contourArea(cnt)
        if area2 > 5000:
            faceColors[counter-1] = "yellow"
            contoursColor = contours2

    #blue color
    low_blue = np.array([111, 155, 100])
    high_blue = np.array([122, 255, 255])
    blue_mask = cv2.inRange(hsv_img, low_blue, high_blue)
    contours3, _ = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours3 = sorted(contours3, key=lambda x:cv2.contourArea(x), reverse=True)
        
    for cnt in contours3:
        area3 = cv2.contourArea(cnt)
        if area3 > 5000:
            faceColors[counter-1] = "blue"
            contoursColor = contours3
            
    #green color
    low_green = np.array([36, 171, 0])
    high_green = np.array([71, 255, 255])
    green_mask = cv2.inRange(hsv_img, low_green, high_green)
    contours4, _ = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours4 = sorted(contours4, key=lambda x:cv2.contourArea(x), reverse=True)
        
    for cnt in contours4:
        area4 = cv2.contourArea(cnt)
        if area4 > 5000:
            faceColors[counter-1] = "green"
            contoursColor = contours4
            
    #Orange color
    low_orange = np.array([0, 2, 179])
    high_orange = np.array([15, 255, 255])
    orange_mask = cv2.inRange(hsv_img, low_orange, high_orange)
    contours5, _ = cv2.findContours(orange_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours5 = sorted(contours5, key=lambda x:cv2.contourArea(x), reverse=True)
        
    for cnt in contours5:
        area5 = cv2.contourArea(cnt)
        if area5 > 5000:
            faceColors[counter-1] = "orange"
            contoursColor = contours5

    if faceColors[counter-1]=="pink":
        
        faceColors[counter-1] = "red"
        print("red, flip cube")


    for cnt in contoursColor:
        (x, y, w, h)= cv2.boundingRect(cnt)

    #cv2.rectangle(frame, (x, y), (x + w, y+h), (0, 255, 0), 2)
        x_medium = int((x + x + w) / 2)
        break

    cv2.line(frame, (x_medium, 0), (x_medium, 480), (255, 0, 0), 2)
    #cv2.imshow("", mask)    
    cv2.imshow('RGB', frame)

    key = cv2.waitKey(1)
    if key == 27:
        break