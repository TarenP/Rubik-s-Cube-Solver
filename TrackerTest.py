from picamera import PiCamera
import matplotlib.image as img
from PIL import Image
import cv2
import numpy as np

#camera setup
camera = PiCamera()
#Res must be divisible by 3
res = 720
camera.resolution = (res, res)
while True:
    camera.capture("/home/pi/Desktop/track.jpg")
        
        
    img = cv2.imread("/home/pi/Desktop/track.jpg")


    #im_crop = im.crop(((res/3), (res/3),(res/3) + (res/3), (res/3) + (res/3)))
    #im_crop.save("/home/pi/Desktop/trackcropped.jpg")
    #img = cv2.imread("/home/pi/Desktop/trackcropped.jpg")
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    low_white = np.array([0, 0, 0])
    high_white = np.array([255, 99, 255])
    white_mask = cv2.inRange(hsv_img, low_white, high_white)
    contours1, _ = cv2.findContours(white_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours1 = sorted(contours1, key=lambda x:cv2.contourArea(x), reverse=True)
        
    for cnt in contours1:
        area1 = cv2.contourArea(cnt)
        if area1 > 5000:
            contoursColor = contours1


    
    for cnt in contoursColor:
        (x, y, w, h)= cv2.boundingRect(cnt)

        x_medium = int((x + x + w) / 2)
        y_medium = int((y + y + h)/ 2)
        break
    cv2.rectangle(img, (x, y), (x + w, y+h), (0, 255, 0), 2)

    cv2.line(img, (x_medium, 0), (x_medium, 720), (255, 255, 0), 2)
    cv2.line(img, (0, y_medium), (720, y_medium), (255, 255, 0), 2)
    #cv2.imshow("", mask)
    print("x_med")
    print(x_medium)
    print("y_med")
    print(y_medium)
    #print(y)
    cv2.imshow('RGB', img)
    cv2.imshow('mask', white_mask)

    key = cv2.waitKey(1)
    if key == 27:
        break