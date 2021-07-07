import cv2
import numpy as np
from picamera import PiCamera
from PIL import Image
import RPi.GPIO as GPIO
from time import sleep

DIR1 = 20
STEP1 = 21
DIR2 = 13
STEP2 = 6
DIR3 = 19
STEP3 = 26
DIR4 = 15
STEP4 = 14
DIR5 = 3
STEP5 = 2
DIR6 = 17
STEP6 = 4
DIR7 = 11
STEP7 = 0
DIR8 = 27
STEP8 = 22

CW = 1
CCW = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR1, GPIO.OUT)
GPIO.setup(STEP1, GPIO.OUT)
GPIO.setup(DIR3, GPIO.OUT)
GPIO.setup(STEP3, GPIO.OUT)
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(STEP2, GPIO.OUT)
GPIO.setup(DIR4, GPIO.OUT)
GPIO.setup(STEP4, GPIO.OUT)
GPIO.setup(DIR5, GPIO.OUT)
GPIO.setup(STEP5, GPIO.OUT)
GPIO.setup(DIR6, GPIO.OUT)
GPIO.setup(STEP6, GPIO.OUT)
GPIO.setup(DIR7, GPIO.OUT)
GPIO.setup(STEP7, GPIO.OUT)
GPIO.setup(DIR8, GPIO.OUT)
GPIO.setup(STEP8, GPIO.OUT)

#delay between steps for motor turns
delay = .0108
#Sensitivity for reseting cube position after turn
sensitivity = 3


      
#camera setup
camera = PiCamera()
#Res must be divisible by 3
res = 720
camera.resolution = (res, res)

faceColors = ["pink", "pink", "pink", "pink", "pink", "pink", "pink", "pink", "pink"]

#Solved cube corners for reference
AQN = ["yellow", "blue", "orange"]
BJM = ["yellow", "green", "orange"]
DRE = ["yellow", "blue", "red"]
CFI = ["yellow", "red", "green"]
HSU = ["red", "blue", "white"]
GLV = ["red", "green", "white"]
XTO = ["white", "blue", "orange"]
WKP = ["white", "green", "orange"]

am = ["yellow", "orange"]
bi = ["yellow", "green"]
ce = ["yellow", "red"]
dq = ["yellow", "blue"]
fl = ["red", "green"]
gu = ["red", "white"]
hr = ["red", "blue"]
tn = ["blue", "orange"]
sx = ["blue", "white"]
kv = ["green", "white"]
ow = ["orange", "white"]
jp = ["green", "orange"]

solvedC2 = False
solvedC3 = False
solvedC4 = False
solvedC5 = False
solvedC6 = False
solvedC7 = False
solvedC8 = False

solvedE2 = False
solvedE3 = False
solvedE4 = False
solvedE5 = False
solvedE6 = False
solvedE7 = False
solvedE8 = False
solvedE9 = False
solvedE10 = False
solvedE11 = False
solvedE12 = False


def Xturn():
    GPIO.output(DIR5, CW)
    GPIO.output(DIR8, CCW)
    GPIO.output(DIR2, CW)
    GPIO.output(DIR4, CW)
    for x in range(5):
        GPIO.output(STEP2, GPIO.HIGH)
        GPIO.output(STEP4, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP2, GPIO.LOW)
        GPIO.output(STEP4, GPIO.LOW)
        sleep(delay)

    GPIO.output(DIR1, CCW)
    GPIO.output(DIR3, CCW)
    for x in range(30):
        GPIO.output(STEP1, GPIO.HIGH)
        GPIO.output(STEP3, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP1, GPIO.LOW)
        GPIO.output(STEP3, GPIO.LOW)
        sleep(delay)
        
    for x in range(50):
        GPIO.output(STEP5, GPIO.HIGH)
        GPIO.output(STEP8, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP5, GPIO.LOW)
        GPIO.output(STEP8, GPIO.LOW)
        sleep(delay)
        
    GPIO.output(DIR1, CW)
    GPIO.output(DIR3, CW)
    for x in range(35):
        GPIO.output(STEP1, GPIO.HIGH)
        GPIO.output(STEP3, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP1, GPIO.LOW)
        GPIO.output(STEP3, GPIO.LOW)
        sleep(delay)
    
    GPIO.output(DIR2, CCW)
    GPIO.output(DIR4, CCW)
    for x in range(30):
        GPIO.output(STEP2, GPIO.HIGH)
        GPIO.output(STEP4, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP2, GPIO.LOW)
        GPIO.output(STEP4, GPIO.LOW)
        sleep(delay)

    GPIO.output(DIR5, CCW)
    GPIO.output(DIR8, CW)
    for x in range(50):
        GPIO.output(STEP5, GPIO.HIGH)
        GPIO.output(STEP8, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP5, GPIO.LOW)
        GPIO.output(STEP8, GPIO.LOW)
        sleep(delay)

    GPIO.output(DIR2, CW)
    GPIO.output(DIR4, CW)
    for x in range(35):
        GPIO.output(STEP2, GPIO.HIGH)
        GPIO.output(STEP4, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP2, GPIO.LOW)
        GPIO.output(STEP4, GPIO.LOW)
        sleep(delay)

def Xprimeturn():
    GPIO.output(DIR5, CCW)
    GPIO.output(DIR8, CW)
    GPIO.output(DIR2, CW)
    GPIO.output(DIR4, CW)
    for x in range(5):
        GPIO.output(STEP2, GPIO.HIGH)
        GPIO.output(STEP4, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP2, GPIO.LOW)
        GPIO.output(STEP4, GPIO.LOW)
        sleep(delay)
    
    GPIO.output(DIR1, CCW)
    GPIO.output(DIR3, CCW)
    for x in range(30):
        GPIO.output(STEP1, GPIO.HIGH)
        GPIO.output(STEP3, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP1, GPIO.LOW)
        GPIO.output(STEP3, GPIO.LOW)
        sleep(delay)
    
    
    for x in range(50):
        GPIO.output(STEP5, GPIO.HIGH)
        GPIO.output(STEP8, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP5, GPIO.LOW)
        GPIO.output(STEP8, GPIO.LOW)
        sleep(delay)
        
    GPIO.output(DIR1, CW)
    GPIO.output(DIR3, CW)
    for x in range(35):
        GPIO.output(STEP1, GPIO.HIGH)
        GPIO.output(STEP3, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP1, GPIO.LOW)
        GPIO.output(STEP3, GPIO.LOW)
        sleep(delay)
    
    GPIO.output(DIR2, CCW)
    GPIO.output(DIR4, CCW)
    for x in range(30):
        GPIO.output(STEP2, GPIO.HIGH)
        GPIO.output(STEP4, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP2, GPIO.LOW)
        GPIO.output(STEP4, GPIO.LOW)
        sleep(delay)

    GPIO.output(DIR5, CW)
    GPIO.output(DIR8, CCW)
    for x in range(50):
        GPIO.output(STEP5, GPIO.HIGH)
        GPIO.output(STEP8, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP5, GPIO.LOW)
        GPIO.output(STEP8, GPIO.LOW)
        sleep(delay)
        
    GPIO.output(DIR2, CW)
    GPIO.output(DIR4, CW)
    for x in range(35):
        GPIO.output(STEP2, GPIO.HIGH)
        GPIO.output(STEP4, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP2, GPIO.LOW)
        GPIO.output(STEP4, GPIO.LOW)
        sleep(delay)

def Yturn():
    GPIO.output(DIR6, CW)
    GPIO.output(DIR7, CCW)
    GPIO.output(DIR1, CW)
    GPIO.output(DIR3, CW)
    for x in range(5):
        GPIO.output(STEP1, GPIO.HIGH)
        GPIO.output(STEP3, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP1, GPIO.LOW)
        GPIO.output(STEP3, GPIO.LOW)

    GPIO.output(DIR2, CCW)
    GPIO.output(DIR4, CCW)
    for x in range(30):
        GPIO.output(STEP2, GPIO.HIGH)
        GPIO.output(STEP4, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP2, GPIO.LOW)
        GPIO.output(STEP4, GPIO.LOW)
        sleep(delay)
    

    
    for x in range(50):
        GPIO.output(STEP6, GPIO.HIGH)
        GPIO.output(STEP7, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP6, GPIO.LOW)
        GPIO.output(STEP7, GPIO.LOW)
        sleep(delay)
        
    GPIO.output(DIR2, CW)
    GPIO.output(DIR4, CW)
    for x in range(35):
        GPIO.output(STEP2, GPIO.HIGH)
        GPIO.output(STEP4, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP2, GPIO.LOW)
        GPIO.output(STEP4, GPIO.LOW)
        sleep(delay)
    
    GPIO.output(DIR1, CCW)
    GPIO.output(DIR3, CCW)
    for x in range(30):
        GPIO.output(STEP1, GPIO.HIGH)
        GPIO.output(STEP3, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP1, GPIO.LOW)
        GPIO.output(STEP3, GPIO.LOW)
        sleep(delay)

    GPIO.output(DIR6, CCW)
    GPIO.output(DIR7, CW)
    for x in range(50):
        GPIO.output(STEP6, GPIO.HIGH)
        GPIO.output(STEP7, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP6, GPIO.LOW)
        GPIO.output(STEP7, GPIO.LOW)
        sleep(delay)

    GPIO.output(DIR1, CW)
    GPIO.output(DIR3, CW)
    for x in range(35):
        GPIO.output(STEP1, GPIO.HIGH)
        GPIO.output(STEP3, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP1, GPIO.LOW)
        GPIO.output(STEP3, GPIO.LOW)
        sleep(delay)

def Yprimeturn():
    GPIO.output(DIR6, CCW)
    GPIO.output(DIR7, CW)
    GPIO.output(DIR1, CW)
    GPIO.output(DIR3, CW)
    for x in range(5):
        GPIO.output(STEP1, GPIO.HIGH)
        GPIO.output(STEP3, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP1, GPIO.LOW)
        GPIO.output(STEP3, GPIO.LOW)

    GPIO.output(DIR2, CCW)
    GPIO.output(DIR4, CCW)
    for x in range(30):
        GPIO.output(STEP2, GPIO.HIGH)
        GPIO.output(STEP4, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP2, GPIO.LOW)
        GPIO.output(STEP4, GPIO.LOW)
        sleep(delay)
    
    
    for x in range(50):
        GPIO.output(STEP6, GPIO.HIGH)
        GPIO.output(STEP7, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP6, GPIO.LOW)
        GPIO.output(STEP7, GPIO.LOW)
        sleep(delay)
        
    GPIO.output(DIR2, CW)
    GPIO.output(DIR4, CW)
    for x in range(35):
        GPIO.output(STEP2, GPIO.HIGH)
        GPIO.output(STEP4, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP2, GPIO.LOW)
        GPIO.output(STEP4, GPIO.LOW)
        sleep(delay)
    
    GPIO.output(DIR1, CCW)
    GPIO.output(DIR3, CCW)
    for x in range(30):
        GPIO.output(STEP1, GPIO.HIGH)
        GPIO.output(STEP3, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP1, GPIO.LOW)
        GPIO.output(STEP3, GPIO.LOW)
        sleep(delay)

    GPIO.output(DIR6, CW)
    GPIO.output(DIR7, CCW)
    for x in range(50):
        GPIO.output(STEP6, GPIO.HIGH)
        GPIO.output(STEP7, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP6, GPIO.LOW)
        GPIO.output(STEP7, GPIO.LOW)
        sleep(delay)
        
    GPIO.output(DIR1, CW)
    GPIO.output(DIR3, CW)
    for x in range(35):
        GPIO.output(STEP1, GPIO.HIGH)
        GPIO.output(STEP3, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP1, GPIO.LOW)
        GPIO.output(STEP3, GPIO.LOW)
        sleep(delay)

def Rturn():
    color = faceColor()
    xcord, ycord = resetCordinates(color)
    print(xcord)
    print(ycord)
    GPIO.output(DIR4, CW)
    GPIO.output(DIR3, CW)
    GPIO.output(DIR1, CW)
    GPIO.output(DIR2, CW)
    
        
    GPIO.output(DIR5, CW)
    for x in range(50):
        GPIO.output(STEP5, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP5, GPIO.LOW)
        sleep(delay)
    
    GPIO.output(DIR2, CCW)
    for x in range(30):
        GPIO.output(STEP2, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP2, GPIO.LOW)
        sleep(delay)

    GPIO.output(DIR5, CCW)
    for x in range(50):
        GPIO.output(STEP5, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP5, GPIO.LOW)
        sleep(delay)

    GPIO.output(DIR2, CW)
    for x in range(35):
        GPIO.output(STEP2, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP2, GPIO.LOW)
        sleep(delay)
    resetx(xcord, color)
    

def Rprimeturn():
    color = faceColor()
    xcord, ycord = resetCordinates(color)
    print(xcord)
    print(ycord)

    GPIO.output(DIR4, CW)
    GPIO.output(DIR3, CW)
    GPIO.output(DIR1, CW)
    GPIO.output(DIR2, CW)
    
    GPIO.output(DIR5, CCW)
    for x in range(50):
        GPIO.output(STEP5, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP5, GPIO.LOW)
        sleep(delay)
    
    
    GPIO.output(DIR2, CCW)
    for x in range(30):
        GPIO.output(STEP2, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP2, GPIO.LOW)
        sleep(delay)

    GPIO.output(DIR5, CW)
    for x in range(50):
        GPIO.output(STEP5, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP5, GPIO.LOW)
        sleep(delay)

    GPIO.output(DIR2, CW)
    for x in range(35):
        GPIO.output(STEP2, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP2, GPIO.LOW)
        sleep(delay)
    resetx(xcord, color)

def Lturn():
    color = faceColor()
    xcord, ycord = resetCordinates(color)
    print(xcord)
    print(ycord)
    GPIO.output(DIR4, CW)
    GPIO.output(DIR3, CW)
    GPIO.output(DIR1, CW)
    GPIO.output(DIR2, CW)

        
    GPIO.output(DIR8, CW)
    for x in range(50):
        GPIO.output(STEP8, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP8, GPIO.LOW)
        sleep(delay)
    
    
    GPIO.output(DIR4, CCW)
    for x in range(30):
        GPIO.output(STEP4, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP4, GPIO.LOW)
        sleep(delay)

    GPIO.output(DIR8, CCW)
    for x in range(50):
        GPIO.output(STEP8, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP8, GPIO.LOW)
        sleep(delay)

    GPIO.output(DIR4, CW)
    for x in range(35):
        GPIO.output(STEP4, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP4, GPIO.LOW)
        sleep(delay)
    
    resetx(xcord, color)

def Lprimeturn():
    color = faceColor()
    xcord, ycord = resetCordinates(color)
    print(xcord)
    print(ycord)
    GPIO.output(DIR4, CW)
    GPIO.output(DIR3, CW)
    GPIO.output(DIR1, CW)
    GPIO.output(DIR2, CW)

        
    GPIO.output(DIR8, CCW)
    for x in range(50):
        GPIO.output(STEP8, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP8, GPIO.LOW)
        sleep(delay)
    
    
    GPIO.output(DIR4, CCW)
    for x in range(30):
        GPIO.output(STEP4, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP4, GPIO.LOW)
        sleep(delay)

    GPIO.output(DIR8, CW)
    for x in range(50):
        GPIO.output(STEP8, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP8, GPIO.LOW)
        sleep(delay)

    GPIO.output(DIR4, CW)
    for x in range(35):
        GPIO.output(STEP4, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP4, GPIO.LOW)
        sleep(delay)

    resetx(xcord, color)

def Bturn():
    color = faceColor()
    xcord, ycord = resetCordinates(color)
    print(xcord)
    print(ycord)
    GPIO.output(DIR4, CW)
    GPIO.output(DIR3, CW)
    GPIO.output(DIR1, CW)
    GPIO.output(DIR2, CW)

        
    GPIO.output(DIR7, CW)
    for x in range(50):
        GPIO.output(STEP7, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP7, GPIO.LOW)
        sleep(delay)
        
    GPIO.output(DIR3, CCW)
    for x in range(30):
        GPIO.output(STEP3, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP3, GPIO.LOW)
        sleep(delay)

    GPIO.output(DIR7, CCW)
    for x in range(50):
        GPIO.output(STEP7, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP7, GPIO.LOW)
        sleep(delay)

    GPIO.output(DIR3, CW)
    for x in range(35):
        GPIO.output(STEP3, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP3, GPIO.LOW)
        sleep(delay)
    
    resety(ycord, color)

def Bprimeturn():
    color = faceColor()
    xcord, ycord = resetCordinates(color)
    print(xcord)
    print(ycord)

    GPIO.output(DIR4, CW)
    GPIO.output(DIR3, CW)
    GPIO.output(DIR1, CW)
    GPIO.output(DIR2, CW)

        
    GPIO.output(DIR7, CCW)
    for x in range(50):
        GPIO.output(STEP7, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP7, GPIO.LOW)
        sleep(delay)
        
    GPIO.output(DIR3, CCW)
    for x in range(30):
        GPIO.output(STEP3, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP3, GPIO.LOW)
        sleep(delay)

    GPIO.output(DIR7, CW)
    for x in range(50):
        GPIO.output(STEP7, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP7, GPIO.LOW)
        sleep(delay)

    GPIO.output(DIR3, CW)
    for x in range(35):
        GPIO.output(STEP3, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP3, GPIO.LOW)
        sleep(delay)

    resety(ycord, color)

def Fturn():
    color = faceColor()
    xcord, ycord = resetCordinates(color)
    print(xcord)
    print(ycord)

    GPIO.output(DIR4, CW)
    GPIO.output(DIR3, CW)
    GPIO.output(DIR1, CW)
    GPIO.output(DIR2, CW)

    GPIO.output(DIR6, CW)
    for x in range(50):
        GPIO.output(STEP6, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP6, GPIO.LOW)
        sleep(delay)
        
    GPIO.output(DIR1, CCW)
    for x in range(30):
        GPIO.output(STEP1, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP1, GPIO.LOW)
        sleep(delay)

    GPIO.output(DIR6, CCW)
    for x in range(50):
        GPIO.output(STEP6, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP6, GPIO.LOW)
        sleep(delay)

    GPIO.output(DIR1, CW)
    for x in range(35):
        GPIO.output(STEP1, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP1, GPIO.LOW)
        sleep(delay)

    resety(ycord, color)

def Fprimeturn():
    color = faceColor()
    xcord, ycord = resetCordinates(color)
    print(xcord)
    print(ycord)

    GPIO.output(DIR4, CW)
    GPIO.output(DIR3, CW)
    GPIO.output(DIR1, CW)
    GPIO.output(DIR2, CW)

        
    GPIO.output(DIR6, CCW)
    for x in range(50):
        GPIO.output(STEP6, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP6, GPIO.LOW)
        sleep(delay)
        
    GPIO.output(DIR1, CCW)
    for x in range(30):
        GPIO.output(STEP1, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP1, GPIO.LOW)
        sleep(delay)

    GPIO.output(DIR6, CW)
    for x in range(50):
        GPIO.output(STEP6, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP6, GPIO.LOW)
        sleep(delay)

    GPIO.output(DIR1, CW)
    for x in range(35):
        GPIO.output(STEP1, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP1, GPIO.LOW)
        sleep(delay)

    resety(ycord, color)

def Dturn():
    Xturn()
    Fturn()
    Xprimeturn()

def Dprimeturn():
    Xturn()
    Fprimeturn()
    Xprimeturn()
    
def Uturn():
    Xprimeturn()
    Fturn()
    Xturn()
    
def Uprimeturn():
    Xprimeturn()
    Fprimeturn()
    Xturn()

def lturn():
    Rturn()
    Xprimeturn()

def lprimeturn():
    Rprimeturn()
    Xturn()

def dturn():
    Xturn()
    Bturn()
    Fprimeturn()
    Yturn()
    Fturn()
    Xprimeturn()

def dprimeturn():
    Xturn()
    Bprimeturn()
    Fturn()
    Yprimeturn()
    Fprimeturn()
    Xprimeturn()

def AlteredYPermutation():
    Rturn()
    Uprimeturn()
    Rprimeturn()
    Uprimeturn()
    Rturn()
    Uturn()
    Rprimeturn()
    Fprimeturn()
    Rturn()
    Uturn()
    Rprimeturn()
    Uprimeturn()
    Rprimeturn()
    Fturn()
    Rturn()

def Tpermutation():
    Rturn()
    Uturn()
    Rprimeturn()
    Uprimeturn()
    Rprimeturn()
    Fturn()
    Rturn()
    Rturn()
    Uprimeturn()
    Rprimeturn()
    Uprimeturn()
    Rturn()
    Uturn()
    Rprimeturn()
    Fprimeturn()

def Jpermutation():
    Rturn()
    Uturn()
    Rprimeturn()
    Fprimeturn()
    Rturn()
    Uturn()
    Rprimeturn()
    Uprimeturn()
    Rprimeturn()
    Fturn()
    Rturn()
    Rturn()
    Uprimeturn()
    Rprimeturn()
    Uprimeturn()

def colorfinder():
    counter = 1
    faceColors = ["pink", "pink", "pink", "pink", "pink", "pink", "pink", "pink", "pink"]
    camera.capture("/home/pi/Desktop/cube.jpg")
    while counter <= 9:
        
        
        im = Image.open("/home/pi/Desktop/cube.jpg")
        
        
        if counter == 1:
            im_crop = im.crop((80, 80, (res/3)-80, (res/3)-80))
        if counter == 2:
             im_crop = im.crop(((res/3)+80, 80, (res/3) + (res/3)-80, (res/3)-80))
        if counter == 3:
             im_crop = im.crop(((res/3) + (res/3) + 80, 80, res-80, (res/3)-80))
        if counter == 4:
             im_crop = im.crop((80, (res/3)+80, (res/3)-80, (res/3) + (res/3) - 80))
        if counter == 5:
             im_crop = im.crop(((res/3)+80, (res/3)+80, (res/3) + (res/3) - 80, (res/3) + (res/3)-80))
        if counter == 6:
             im_crop = im.crop(((res/3) + (res/3) + 80, (res/3) + 80, (res/3) + (res/3) + (res/3) -80, (res/3) + (res/3) - 80))
        if counter == 7:
             im_crop = im.crop((80, (res/3) + (res/3) + 80, (res/3) - 80, res - 80))
        if counter == 8:
             im_crop = im.crop(((res/3) + 80, (res/3) + (res/3) + 80, (res/3) + (res/3) - 80, res - 80))
        if counter == 9:
             im_crop = im.crop(((res/3) + (res/3) + 80, (res/3) + (res/3) + 80, res - 80, res - 80))
        im_crop.save("/home/pi/Desktop/cubecropped.jpg")
        img = cv2.imread("/home/pi/Desktop/cubecropped.jpg")
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            
        # store in array
        
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
        
        
    #         #White color
    #         low_white = np.array([110, 100, 100])
    #         high_white = np.array([130, 255, 255])
    #         white_mask = cv2.inRange(hsv_img, low_white, high_white)
    #         contours6, _ = cv2.findContours(white_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #         contours6 = sorted(contours6, key=lambda x:cv2.contourArea(x), reverse=True)
    #          
    #         for cnt in contours6:
    #             area6 = cv2.contourArea(cnt)
    #             if area6 > 5000:
        if faceColors[counter-1]=="pink":
            
            faceColors[counter-1] = "red"
                
        
        counter+=1
                
        #cv2.imshow("Frame", img)
    #         cv2.imshow("RedMask", red_mask)
    #         cv2.imshow("YellowMask", yellow_mask)
    #         cv2.imshow("GreenMask", green_mask)
    #         cv2.imshow("BlueMask", blue_mask)
        key =cv2.waitKey(1)
        
        if key== 27:
            break
    return faceColors    

def faceColor():
    #Determine the color of the face
    face = "red"

    camera.capture("/home/pi/Desktop/cube.jpg")
        
        
    im = Image.open("/home/pi/Desktop/cube.jpg")

    im_crop = im.crop(((res/3)+80, (res/3)+80, (res/3) + (res/3) - 80, (res/3) + (res/3)-80))
    im_crop.save("/home/pi/Desktop/cubecropped.jpg")
    img = cv2.imread("/home/pi/Desktop/cubecropped.jpg")
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    #White color
    low_white = np.array([0, 0, 0])
    high_white = np.array([255, 99, 255])
    white_mask = cv2.inRange(hsv_img, low_white, high_white)
    contours1, _ = cv2.findContours(white_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours1 = sorted(contours1, key=lambda x:cv2.contourArea(x), reverse=True)
        
    for cnt in contours1:
        area1 = cv2.contourArea(cnt)
        if area1 > 5000:
            face = "white"

    
    #yellow color
    low_yellow = np.array([23, 108, 90])
    high_yellow = np.array([40, 255, 255])
    yellow_mask = cv2.inRange(hsv_img, low_yellow, high_yellow)
    contours2, _ = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours2 = sorted(contours2, key=lambda x:cv2.contourArea(x), reverse=True)
        
    for cnt in contours2:
        area2 = cv2.contourArea(cnt)
        if area2 > 5000:
            face = "yellow"
    
    #blue color
    low_blue = np.array([111, 155, 100])
    high_blue = np.array([122, 255, 255])
    blue_mask = cv2.inRange(hsv_img, low_blue, high_blue)
    contours3, _ = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours3 = sorted(contours3, key=lambda x:cv2.contourArea(x), reverse=True)
        
    for cnt in contours3:
        area3 = cv2.contourArea(cnt)
        if area3 > 5000:
            face = "blue"
            
    #green color
    low_green = np.array([36, 171, 0])
    high_green = np.array([71, 255, 255])
    green_mask = cv2.inRange(hsv_img, low_green, high_green)
    contours4, _ = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours4 = sorted(contours4, key=lambda x:cv2.contourArea(x), reverse=True)
        
    for cnt in contours4:
        area4 = cv2.contourArea(cnt)
        if area4 > 5000:
            face = "green"
            
    #Orange color
    low_orange = np.array([0, 2, 179])
    high_orange = np.array([15, 255, 255])
    orange_mask = cv2.inRange(hsv_img, low_orange, high_orange)
    contours5, _ = cv2.findContours(orange_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours5 = sorted(contours5, key=lambda x:cv2.contourArea(x), reverse=True)
        
    for cnt in contours5:
        area5 = cv2.contourArea(cnt)
        if area5 > 5000:
            face = "orange"
            
    return face

def resetCordinates(color):
    camera.capture("/home/pi/Desktop/track.jpg")
        
        
    img = cv2.imread("/home/pi/Desktop/track.jpg")

    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    if color == "white":
        low_white = np.array([0, 0, 0])
        high_white = np.array([255, 99, 255])
        white_mask = cv2.inRange(hsv_img, low_white, high_white)
        contours1, _ = cv2.findContours(white_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours1 = sorted(contours1, key=lambda x:cv2.contourArea(x), reverse=True)
            
        for cnt in contours1:
            area1 = cv2.contourArea(cnt)
            if area1 > 5000:
                contoursColor = contours1

    if color == "yellow":
        #yellow color
        low_yellow = np.array([23, 108, 90])
        high_yellow = np.array([40, 255, 255])
        yellow_mask = cv2.inRange(hsv_img, low_yellow, high_yellow)
        contours2, _ = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours2 = sorted(contours2, key=lambda x:cv2.contourArea(x), reverse=True)
            
        for cnt in contours2:
            area2 = cv2.contourArea(cnt)
            if area2 > 5000:
                contoursColor = contours2
    if color == "blue":
        #blue color
        low_blue = np.array([111, 155, 100])
        high_blue = np.array([122, 255, 255])
        blue_mask = cv2.inRange(hsv_img, low_blue, high_blue)
        contours3, _ = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours3 = sorted(contours3, key=lambda x:cv2.contourArea(x), reverse=True)
            
        for cnt in contours3:
            area3 = cv2.contourArea(cnt)
            if area3 > 5000:
                contoursColor = contours3

    if color == "green":
        #green color
        low_green = np.array([36, 171, 0])
        high_green = np.array([71, 255, 255])
        green_mask = cv2.inRange(hsv_img, low_green, high_green)
        contours4, _ = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours4 = sorted(contours4, key=lambda x:cv2.contourArea(x), reverse=True)
            
        for cnt in contours4:
            area4 = cv2.contourArea(cnt)
            if area4 > 5000:
                contoursColor = contours4

    if color == "orange":  
        #Orange color
        low_orange = np.array([0, 2, 179])
        high_orange = np.array([15, 255, 255])
        orange_mask = cv2.inRange(hsv_img, low_orange, high_orange)
        contours5, _ = cv2.findContours(orange_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours5 = sorted(contours5, key=lambda x:cv2.contourArea(x), reverse=True)
            
        for cnt in contours5:
            area5 = cv2.contourArea(cnt)
            if area5 > 5000:
                contoursColor = contours5
    
    if color == "red":  
        #Red color
        low_red = np.array([150, 43, 142])
        high_red = np.array([255, 255, 255])
        red_mask = cv2.inRange(hsv_img, low_red, high_red)
        contours6, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours6 = sorted(contours6, key=lambda x:cv2.contourArea(x), reverse=True)
            
        for cnt in contours6:
            area6 = cv2.contourArea(cnt)
            if area6 > 5000:
                contoursColor = contours6


    for cnt in contoursColor:
        (x, y, w, h)= cv2.boundingRect(cnt)

        x_medium = int((x + x + w) / 2)
        y_medium = int((y + y + h)/ 2)
        break
    #cv2.rectangle(img, (x, y), (x + w, y+h), (0, 255, 0), 2)

    #cv2.line(img, (x_medium, 0), (x_medium, 720), (255, 255, 0), 2)
    #cv2.line(img, (0, y_medium), (720, y_medium), (255, 255, 0), 2)
    return x_medium, y_medium
    #cv2.imshow("", mask)
    # print("x_med")
    # print(x_medium)
    # print("y_med")
    # print(y_medium)
    #print(y)
    # cv2.imshow('RGB', img)
    # cv2.imshow('mask', orange_mask)

def resety(ycord, color):
    #xafter, yafter = resetCordinates(color)
    #while (not ycord + sensitivity > yafter and ycord - sensitivity < yafter):
    xafter, yafter = resetCordinates(color)
    if yafter < ycord - sensitivity:
        for x in range(2):
            GPIO.output(DIR1, CCW)
            GPIO.output(DIR3, CW)
            GPIO.output(STEP1, GPIO.HIGH)
            GPIO.output(STEP3, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP1, GPIO.LOW)
            GPIO.output(STEP3, GPIO.LOW)
            sleep(.3)
        print("back")

    elif yafter > ycord + sensitivity:
        for x in range(2):
            GPIO.output(DIR1, CW)
            GPIO.output(DIR3, CCW)
            GPIO.output(STEP1, GPIO.HIGH)
            GPIO.output(STEP3, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP1, GPIO.LOW)
            GPIO.output(STEP3, GPIO.LOW)
            sleep(.3)
        print("forward")
    print(xafter)
    print(yafter)

def resetx(xcord, color):
    xafter, yafter = resetCordinates(color)
    #while (not xcord + sensitivity > xafter and xcord - sensitivity < xafter):
    #xafter, yafter = resetCordinates(color)
    if xafter < xcord - sensitivity:
        for x in range(2):
            GPIO.output(DIR2, CW)
            GPIO.output(DIR4, CCW)
            GPIO.output(STEP2, GPIO.HIGH)
            GPIO.output(STEP4, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP2, GPIO.LOW)
            GPIO.output(STEP4, GPIO.LOW)
            sleep(.3)
        print("left")

    elif xafter > xcord + sensitivity:
        for x in range(2):
            GPIO.output(DIR2, CCW)
            GPIO.output(DIR4, CW)
            GPIO.output(STEP2, GPIO.HIGH)
            GPIO.output(STEP4, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP2, GPIO.LOW)
            GPIO.output(STEP4, GPIO.LOW)
            sleep(.3)
        print("right")
    print(xafter)
    print(yafter)
#it will do the algo to get that specific corner to where it should go.
def cornerActions():
    mAQN = [A, Q, N]
    mBJM = [B, J, M]
    mDRE = [D, R, E]
    mCFI = [C, F, I]
    mHSU = [H, S, U]
    mGLV = [G, L, V]
    mXTO = [X, T, O]
    mWKP = [W, K, P]
    #checking if anycorners are already solved
    if (mBJM == BJM):
        solvedC2 = True
    if (mDRE == DRE):
        solvedC3 = True
    if (mCFI == CFI):
        solvedC4 = True
    if (mHSU == HSU):
        solvedC5 = True
    if (mGLV == GLV):
        solvedC6 = True
    if (mXTO == XTO):
        solvedC7 = True
    if (mWKP == WKP):
        solvedC8 = True

    bankCorner = mAQN

    corner1 = AQN
    corner1.sort()
    corner2 = BJM
    corner2.sort()
    corner3 = DRE
    corner3.sort()
    corner4 = CFI
    corner4.sort()
    corner5 = HSU
    corner5.sort()
    corner6 = GLV
    corner6.sort()
    corner7 = XTO
    corner7.sort()
    corner8 = WKP
    corner8.sort()


    everythingSolved = False
    cornerSolveList = []


    #Use a list of the moves to the positions the bank pieces need to go.

    while everythingSolved == False:
        bankCornerSorted = bankCorner
        bankCornerSorted.sort()
        if (bankCornerSorted == corner1):
            index = AQN.index(bankCorner[0])
            if (index == 0 and solvedC2 == True and solvedC3 == True and solvedC4 == True and solvedC5 == True and solvedC6 == True and solvedC7 == True and solvedC8 == True):
                print("already set")
                everythingSolved = True
            elif (solvedC2 == False):
                cornerSolveList.append('B')
                mBJM2 = bankCorner
                bankCorner = mBJM
                mBJM = mBJM2
            elif(solvedC3 == False):
                cornerSolveList.append('D')
                mDRE2 = bankCorner
                bankCorner = mDRE
                mDRE = mDRE2
            elif(solvedC4 == False):
                cornerSolveList.append('C')
                mCFI2 = bankCorner
                bankCorner = mCFI
                mCFI = mCFI2
            elif(solvedC5 == False):
                cornerSolveList.append('D')
                mHSU2 = bankCorner
                bankCorner = mHSU
                mHSU = mHSU2
            elif (solvedC6 == False):
                cornerSolveList.append('G')
                mGLV2 = bankCorner
                bankCorner = mGLV
                mGLV = mGLV2
            elif (solvedC7 == False):
                cornerSolveList.append('X')
                mXTO2 = bankCorner
                bankCorner = mXTO
                mXTO = mXTO2
            elif (solvedC8 == False):
                cornerSolveList.append('W')
                mWKP2 = bankCorner
                bankCorner = mWKP
                mWKP = mWKP2
            #Swap with an unsolved corner because it is in the bank place and cannot be solved
    
        elif(bankCornerSorted == corner2):
            index = BJM.index(bankCorner[0])
            if (index == 0):
                cornerSolveList.append('B')
                bankCorner = mBJM
                solvedC2 = True
            elif (index == 1):
                cornerSolveList.append('J')
                bankCorner = [J, M, B]
                solvedC2 = True
            else:
                cornerSolveList.append('M')
                bankCorner = [M, B, J]
                solvedC2 = True

        elif (bankCornerSorted == corner3):
            index = DRE.index(bankCorner[0])
            if (index == 0):
                cornerSolveList.append('D')
                bankCorner = mDRE
                solvedC3 = True
            elif (index == 1):
                cornerSolveList.append('R')
                bankCorner = [R, E, D]
                solvedC3 = True
            else:
                cornerSolveList.append('E')
                bankCorner = [E, D, R]
                solvedC3 = True

        elif(bankCornerSorted == corner4):
            index = CFI.index(bankCorner[0])
            if (index == 0):
                cornerSolveList.append('C')
                bankCorner = mCFI
                solvedC4 = True
            elif (index == 1):
                cornerSolveList.append('F')
                bankCorner = [F, I, C]
                solvedC4 = True
            else:
                cornerSolveList.append('I')
                bankCorner = [I, C, F]
                solvedC4 = True
        
        elif(bankCornerSorted == corner5):
            index = HSU.index(bankCorner[0])
            if (index == 0):
                cornerSolveList.append('H')
                bankCorner = mHSU
                solvedC5 = True
            elif (index == 1):
                cornerSolveList.append('S')
                bankCorner = [S, U, H]
                solvedC5 = True
            else:
                cornerSolveList.append('U')
                bankCorner = [U, H, S]
                solvedC5 = True

        elif(bankCornerSorted == corner6):
            index = GLV.index(bankCorner[0])
            if (index == 0):
                cornerSolveList.append('G')
                bankCorner = mGLV
                solvedC6 = True
            elif (index == 1):
                cornerSolveList.append('L')
                bankCorner = [L, V, G]
                solvedC6 = True
            else:
                cornerSolveList.append('V')
                bankCorner = [V, G, L]
                solvedC6 = True
        
        elif(bankCornerSorted == corner7):
            index = XTO.index(bankCorner[0])
            if (index == 0):
                cornerSolveList.append('X')
                bankCorner = mXTO
                solvedC7 = True
            elif (index == 1):
                cornerSolveList.append('T')
                bankCorner = [T, O, X]
                solvedC7 = True
            else:
                cornerSolveList.append('O')
                bankCorner = [O, X, T]
                solvedC7 = True

        elif (bankCornerSorted == corner8):
            index = WKP.index(bankCorner[0])
            if (index == 0):
                cornerSolveList.append('W')
                bankCorner = mWKP
                solvedC8 = True
            elif (index == 1):
                cornerSolveList.append('K')
                bankCorner = [K, P, W]
                solvedC8 = True
            else:
                cornerSolveList.append('P')
                bankCorner = [P, W, K]
                solvedC8 = True
    return cornerSolveList
    # #use "list".sort() method for comparing the two corners.

def cornerSwapper(cornerSolveList):
    odd = False
    counter = 0
    if len(cornerSolveList)%2 != 0:
        odd = True
    for i in cornerSolveList:
        letter = cornerSolveList[counter]
        if letter == 'B':
            Rturn()
            Dprimeturn()
            AlteredYPermutation()
            Dturn()
            Rprimeturn()
        elif letter == 'C':
            Fturn()
            AlteredYPermutation()
            Fprimeturn()
        elif letter == 'D':
            Fturn()
            Rprimeturn()
            AlteredYPermutation()
            Rturn()
            Fprimeturn()
        elif letter == 'E':
            Fprimeturn()
            Dturn()
            AlteredYPermutation()
            Dprimeturn()
            Fturn()
        elif letter == 'F':
            Fturn()
            Fturn()
            Dturn()
            AlteredYPermutation()
            Dprimeturn()
            Fprimeturn()
            Fprimeturn()
        elif letter == 'G':
            Dturn()
            Rturn()
            AlteredYPermutation()
            Rprimeturn()
            Dprimeturn()
        elif letter == 'H':
            Dturn()
            AlteredYPermutation()
            Dprimeturn()
        elif letter == 'I':
            Rprimeturn()
            AlteredYPermutation()
            Rturn()
        elif letter == 'J':
            Rturn()
            Rturn()
            AlteredYPermutation()
            Rprimeturn()
            Rprimeturn()
        elif letter == 'K':
            Rturn()
            AlteredYPermutation()
            Rprimeturn()
        elif letter == 'L':
            AlteredYPermutation()
        elif letter == 'M':
            Rprimeturn()
            Fturn()
            AlteredYPermutation()
            Fprimeturn()
            Rturn()
        elif letter == 'N':
            AlteredYPermutation()
        elif letter == 'O':
            Dprimeturn()
            Rturn()
            AlteredYPermutation()
            Rprimeturn()
            Dturn()
        elif letter == 'P':
            Dprimeturn()
            AlteredYPermutation()
            Dturn()
        elif letter == 'R':
            Fturn()
            Fturn()
            AlteredYPermutation()
            Fprimeturn()
            Fprimeturn()
        elif letter == 'S':
            Dturn()
            Dturn()
            Rturn()
            AlteredYPermutation()
            Rprimeturn()
            Dprimeturn()
            Dprimeturn()
        elif letter == 'T':
            Dturn()
            Dturn()
            AlteredYPermutation()
            Dprimeturn()
            Dprimeturn()
        elif letter == 'U':
            Fprimeturn()
            AlteredYPermutation()
            Fturn()
        elif letter == 'V':
            Dprimeturn()
            Fprimeturn()
            AlteredYPermutation()
            Fturn()
            Dturn()
        elif letter == 'W':
            Dturn()
            Dturn()
            Fprimeturn()
            AlteredYPermutation()
            Fturn()
            Dprimeturn()
            Dprimeturn()
        elif letter == 'X':
            Dturn()
            Fprimeturn()
            AlteredYPermutation()
            Fturn()
            Dprimeturn

        counter = counter + 1
    if odd == True:
        Xturn()
        Yturn()
        Xprimeturn()

        Lturn()
        Uprimeturn()
        Uprimeturn()
        Lprimeturn()
        Uprimeturn()
        Uprimeturn()
        Lturn()
        Fprimeturn()
        Lprimeturn()
        Uprimeturn()
        Lturn()
        Uturn()
        Lturn()
        Fturn()
        Lprimeturn()
        Lprimeturn()
        Uturn()

        Xturn()
        Yprimeturn()
        Xprimeturn()

def cornerMain():
    cList = cornerActions()
    print(cList)
    cornerSwapper(cList)

def edgeSwapper():
    mam = [a, m]
    mbi = [b, i]
    mce = [c, e]
    mdq = [d, q]
    mfl = [f, l]
    mgu = [g, u]
    mhr = [h, r]
    mtn = [t, n]
    msx = [s, x]
    mkv = [k, v]
    mow = [o, w]
    mjp = [j, p]

    bankEdge = mbi

    edge1 = bi
    edge1.sort()
    edge2 = am
    edge2.sort()
    edge3 = ce
    edge3.sort()
    edge4 = dq
    edge4.sort()
    edge5 = fl
    edge5.sort()
    edge6 = gu
    edge6.sort()
    edge7 = hr
    edge7.sort()
    edge8 = tn
    edge8.sort()
    edge9 = sx
    edge9.sort()
    edge10 = kv
    edge10.sort()
    edge11 = ow
    edge11.sort()
    edge12 = jp
    edge12.sort()

    #checking if anycorners are already solved
    if (mam == am):
        solvedE2 = True
    if (mce == ce):
        solvedE3 = True
    if (mdq == dq):
        solvedE4 = True
    if (mfl == fl):
        solvedE5 = True
    if (mgu == gu):
        solvedE6 = True
    if (mhr == hr):
        solvedE7 = True
    if (mtn == tn):
        solvedE8 = True
    if (msx == sx):
        solvedE9 = True
    if (mkv == kv):
        solvedE10 = True
    if (mow == ow):
        solvedE11 = True
    if (mjp == jp):
        solvedE12 = True

    everythingSolved = False
    edgeSolveList = []

    #Use a list of the moves to the positions the bank pieces need to go.

    #finish
    while everythingSolved == False:
        bankEdgeSorted = bankEdge
        bankEdgeSorted.sort()
        if (bankEdgeSorted == edge1):
            index = bi.index(bankEdge[0])
            if (index == 0 and solvedE2 == True and solvedE3 == True and solvedE4 == True and solvedE5 == True and solvedE6 == True and solvedE7 == True and solvedE8 == True and solvedE9 == True and solvedE10 == True and solvedE11 == True and solvedE12 == True):
                print("Edges already set")
                everythingSolved = True
            elif (solvedE2 == False):
                edgeSolveList.append('a')
                mam2 = bankEdge #old bank edge
                bankEdge = mam #Changes
                mam = mam2 #equals old bank edge
            elif(solvedE3 == False):
                edgeSolveList.append('c')
                mce2 = bankEdge
                bankEdge = mce
                mce = mce2
            elif(solvedE4 == False):
                edgeSolveList.append('d')
                mdq2 = bankEdge
                bankEdge = mdq
                mdq = mdq2
            elif(solvedE5 == False):
                edgeSolveList.append('f')
                mfl2 = bankEdge
                bankEdge = mfl
                mfl = mfl2
            elif (solvedE6 == False):
                edgeSolveList.append('g')
                mgu2 = bankEdge
                bankEdge = mgu
                mgu = mgu2
            elif (solvedE7 == False):
                edgeSolveList.append('h')
                mhr2 = bankEdge
                bankEdge = mhr
                mhr = mhr2
            elif (solvedE8 == False):
                edgeSolveList.append('t')
                mtn2 = bankEdge
                bankEdge = mtn
                mtn = mtn2
            elif (solvedE9 == False):
                edgeSolveList.append('s')
                msx2 = bankEdge
                bankEdge = msx
                msx = msx2
            elif (solvedE10 == False):
                edgeSolveList.append('k')
                mkv2 = bankEdge
                bankEdge = mkv
                mkv = mkv2
            elif (solvedE11 == False):
                edgeSolveList.append('o')
                mow2 = bankEdge
                bankEdge = mow
                mow = mow2
            elif (solvedE12 == False):
                edgeSolveList.append('j')
                mjp2 = bankEdge
                bankEdge = mjp
                mjp = mjp2
            #Swap with an unsolved Edge because it is in the bank place and cannot be solved
    
        elif(bankEdgeSorted == edge2):
            index = am.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('a')
                bankEdge = mam
                solvedE2 = True
            elif (index == 1):
                edgeSolveList.append('m')
                bankEdge = [m, a]
                solvedE2 = True

        elif(bankEdgeSorted == edge3):
            index = ce.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('c')
                bankEdge = mce
                solvedE3 = True
            elif (index == 1):
                edgeSolveList.append('e')
                bankEdge = [e, c]
                solvedE3 = True
        
        elif(bankEdgeSorted == edge4):
            index = dq.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('d')
                bankEdge = mdq
                solvedE4 = True
            elif (index == 1):
                edgeSolveList.append('q')
                bankEdge = [q, d]
                solvedE4 = True
            
        elif(bankEdgeSorted == edge5):
            index = fl.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('f')
                bankEdge = mfl
                solvedE5 = True
            elif (index == 1):
                edgeSolveList.append('l')
                bankEdge = [l, f]
                solvedE5 = True
        
        elif(bankEdgeSorted == edge6):
            index = gu.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('g')
                bankEdge = mgu
                solvedE6 = True
            elif (index == 1):
                edgeSolveList.append('u')
                bankEdge = [u, g]
                solvedE6 = True

        elif(bankEdgeSorted == edge7):
            index = hr.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('h')
                bankEdge = mhr
                solvedE7 = True
            elif (index == 1):
                edgeSolveList.append('r')
                bankEdge = [r, h]
                solvedE7 = True
        
        elif(bankEdgeSorted == edge8):
            index = tn.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('t')
                bankEdge = mtn
                solvedE8 = True
            elif (index == 1):
                edgeSolveList.append('n')
                bankEdge = [n, t]
                solvedE8 = True

        elif(bankEdgeSorted == edge9):
            index = sx.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('s')
                bankEdge = msx
                solvedE9 = True
            elif (index == 1):
                edgeSolveList.append('x')
                bankEdge = [x, s]
                solvedE9 = True

        elif(bankEdgeSorted == edge10):
            index = kv.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('k')
                bankEdge = mkv
                solvedE10 = True
            elif (index == 1):
                edgeSolveList.append('v')
                bankEdge = [v, k]
                solvedE10 = True
        
        elif(bankEdgeSorted == edge11):
            index = ow.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('o')
                bankEdge = mow
                solvedE11 = True
            elif (index == 1):
                edgeSolveList.append('w')
                bankEdge = [w, o]
                solvedE11 = True

        elif(bankEdgeSorted == edge12):
            index = jp.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('j')
                bankEdge = mjp
                solvedE12 = True
            elif (index == 1):
                edgeSolveList.append('p')
                bankEdge = [p, j]
                solvedE12 = True

    return edgeSolveList

def edgeSwapper(edgeSolveList):
    counter = 0
    for i in len(edgeSolveList):
        letter = edgeSolveList[counter]
        if letter == 'a':
            lturn()
            lturn()
            Dprimeturn()
            Lturn()
            Lturn()
            Tpermutation()
            Lprimeturn()
            Lprimeturn()
            Dturn()
            lprimeturn()
            lprimeturn()
        elif letter == 'c':
            Jpermutation()
        elif letter == 'd':
            Tpermutation()
        elif letter == 'e':
            lturn()
            Dprimeturn()
            Lturn()
            Lturn()
            Tpermutation()
            Lprimeturn()
            Lprimeturn()
            Dturn()
            lprimeturn()
        elif letter == 'f':
            dturn()
            dturn()
            Lturn()
            Tpermutation()
            Lprimeturn()
            dprimeturn()
            dprimeturn()
        elif letter == 'g':
            lprimeturn()
            Jpermutation()
            lturn()
        elif letter == 'h':
            Lprimeturn()
            Tpermutation()
            Lturn()
        elif letter == 'J':
            dturn()
            Lturn()
            Tpermutation()
            Lprimeturn()
            dprimeturn()
        elif letter == 'k':
            Dprimeturn()
            lprimeturn()
            Jpermutation()
            lturn()
            Dturn()
        elif letter == 'l':
            dprimeturn()
            Lprimeturn()
            Tpermutation()
            Lturn()
            dturn()
        elif letter == 'm':
            lturn()
            Jpermutation()
            lprimeturn()
        elif letter == 'n':
            Lturn()
            Tpermutation()
            Lprimeturn()
        elif letter == 'o':
            Dturn()
            Dturn()
            lprimeturn()
            Jpermutation()
            lturn()
            Dprimeturn()
            Dprimeturn()
        elif letter == 'p':
            dturn()
            dturn()
            Lprimeturn()
            Tpermutation()
            Lturn()
            dprimeturn()
            dprimeturn()
        elif letter == 'q':
            Lturn()
            Lturn()
            dturn()
            lprimeturn()
            Jpermutation()
            lturn()
            dprimeturn()
            Lprimeturn()
            Lprimeturn()
        elif letter == 'r':
            dprimeturn()
            Lturn()
            Tpermutation()
            Lprimeturn()
            dturn()
        elif letter == 's':
            Dturn()
            lprimeturn()
            Jpermutation()
            lturn()
            Dprimeturn()
        elif letter == 't':
            dturn()
            Lprimeturn()
            Tpermutation()
            Lturn()
            dprimeturn()
        elif letter == 'u':
            Dprimeturn()
            Lturn()
            Lturn()
            Tpermutation()
            Lprimeturn()
            Lprimeturn()
            Dturn()
        elif letter == 'v':
            Dturn()
            Dturn()
            Lturn()
            Lturn()
            Tpermutation()
            Lprimeturn()
            Lprimeturn()
            Dprimeturn()
            Dprimeturn()
        elif letter == 'w':
            Dturn()
            Lturn()
            Lturn()
            Tpermutation()
            Lprimeturn()
            Lprimeturn()
            Dprimeturn()
        elif letter == 'X':
            Lturn()
            Lturn()
            Tpermutation()
            Lprimeturn()
            Lprimeturn()

        counter = counter + 1

def edgeMain():
    eList = edgeMain()
    print(eList)
    edgeSwapper(eList)

def main():
    cornerMain()
    edgeMain()

#region cubeMapping
# print("Place Orange side facing Motor 6. Stop program if needed!")
# GPIO.output(DIR1, CW)
# GPIO.output(DIR3, CW)
# GPIO.output(DIR2, CW)
# GPIO.output(DIR4, CW)
# for x in range(5):
#     GPIO.output(STEP1, GPIO.HIGH)
#     GPIO.output(STEP3, GPIO.HIGH)
#     GPIO.output(STEP2, GPIO.HIGH)
#     GPIO.output(STEP4, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP1, GPIO.LOW)
#     GPIO.output(STEP3, GPIO.LOW)
#     GPIO.output(STEP2, GPIO.LOW)
#     GPIO.output(STEP4, GPIO.LOW)
#     sleep(delay)


#  #Turn Motor 5
# GPIO.output(DIR2, CCW)
# for x in range(30):
#     GPIO.output(STEP2, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP2, GPIO.LOW)
#     sleep(delay)


# GPIO.output(DIR5, CW)
# for x in range(50):
#     GPIO.output(STEP5, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP5, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR2, CW)
# for x in range(35):
#     GPIO.output(STEP2, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP2, GPIO.LOW)
#     sleep(delay)

# #Turn Motor 8
# GPIO.output(DIR4, CCW)
# for x in range(30):
#     GPIO.output(STEP4, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP4, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR8, CCW)
# for x in range(50):
#     GPIO.output(STEP8, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP8, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR4, CW)
# for x in range(35):
#     GPIO.output(STEP4, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP4, GPIO.LOW)
#     sleep(delay)


# GPIO.output(DIR1, CCW)
# GPIO.output(DIR3, CCW)
# for x in range(30):
#     GPIO.output(STEP1, GPIO.HIGH)
#     GPIO.output(STEP3, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP1, GPIO.LOW)
#     GPIO.output(STEP3, GPIO.LOW)
#     sleep(delay)
    

# yellowFace = colorfinder()
# A = yellowFace[0]
# a = yellowFace[1]
# B = yellowFace[2]
# d = yellowFace[3]
# up = yellowFace[4]
# b = yellowFace[5]
# D = yellowFace[6]
# c = yellowFace[7]
# C = yellowFace[8]
# print(yellowFace)

# GPIO.output(DIR1, CW)
# GPIO.output(DIR3, CW)
# for x in range(35):
#     GPIO.output(STEP1, GPIO.HIGH)
#     GPIO.output(STEP3, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP1, GPIO.LOW)
#     GPIO.output(STEP3, GPIO.LOW)
#     sleep(delay)

#  #Turn Motor 5
# GPIO.output(DIR2, CCW)
# for x in range(30):
#     GPIO.output(STEP2, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP2, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR5, CW)
# for x in range(50):
#     GPIO.output(STEP5, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP5, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR2, CW)
# for x in range(35):
#     GPIO.output(STEP2, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP2, GPIO.LOW)
#     sleep(delay)

# #Turn Motor 8
# GPIO.output(DIR4, CCW)
# for x in range(30):
#     GPIO.output(STEP4, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP4, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR8, CCW)
# for x in range(50):
#     GPIO.output(STEP8, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP8, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR4, CW)
# for x in range(35):
#     GPIO.output(STEP4, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP4, GPIO.LOW)
#     sleep(delay)

# #Done with Yellow






# Xprimeturn()


#  #Turn Motor 5
# GPIO.output(DIR2, CCW)
# for x in range(30):
#     GPIO.output(STEP2, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP2, GPIO.LOW)
#     sleep(delay)


# GPIO.output(DIR5, CW)
# for x in range(50):
#     GPIO.output(STEP5, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP5, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR2, CW)
# for x in range(35):
#     GPIO.output(STEP2, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP2, GPIO.LOW)
#     sleep(delay)

# #Turn Motor 8
# GPIO.output(DIR4, CCW)
# for x in range(30):
#     GPIO.output(STEP4, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP4, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR8, CCW)
# for x in range(50):
#     GPIO.output(STEP8, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP8, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR4, CW)
# for x in range(35):
#     GPIO.output(STEP4, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP4, GPIO.LOW)
#     sleep(delay)


# GPIO.output(DIR1, CCW)
# GPIO.output(DIR3, CCW)
# for x in range(30):
#     GPIO.output(STEP1, GPIO.HIGH)
#     GPIO.output(STEP3, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP1, GPIO.LOW)
#     GPIO.output(STEP3, GPIO.LOW)
#     sleep(delay)
    

# redFace = colorfinder()
# E = redFace[0]
# e = redFace[1]
# F = redFace[2]
# h = redFace[3]
# front = redFace[4]
# f = redFace[5]
# H = redFace[6]
# g = redFace[7]
# G = redFace[8]
# print(redFace)

# GPIO.output(DIR1, CW)
# GPIO.output(DIR3, CW)
# for x in range(35):
#     GPIO.output(STEP1, GPIO.HIGH)
#     GPIO.output(STEP3, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP1, GPIO.LOW)
#     GPIO.output(STEP3, GPIO.LOW)
#     sleep(delay)

#  #Turn Motor 5
# GPIO.output(DIR2, CCW)
# for x in range(30):
#     GPIO.output(STEP2, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP2, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR5, CW)
# for x in range(50):
#     GPIO.output(STEP5, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP5, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR2, CW)
# for x in range(35):
#     GPIO.output(STEP2, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP2, GPIO.LOW)
#     sleep(delay)

# #Turn Motor 8
# GPIO.output(DIR4, CCW)
# for x in range(30):
#     GPIO.output(STEP4, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP4, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR8, CCW)
# for x in range(50):
#     GPIO.output(STEP8, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP8, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR4, CW)
# for x in range(35):
#     GPIO.output(STEP4, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP4, GPIO.LOW)
#     sleep(delay)







# #Done With Red

# Xprimeturn()

#  #Turn Motor 5
# GPIO.output(DIR2, CCW)
# for x in range(30):
#     GPIO.output(STEP2, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP2, GPIO.LOW)
#     sleep(delay)


# GPIO.output(DIR5, CW)
# for x in range(50):
#     GPIO.output(STEP5, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP5, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR2, CW)
# for x in range(35):
#     GPIO.output(STEP2, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP2, GPIO.LOW)
#     sleep(delay)

# #Turn Motor 8
# GPIO.output(DIR4, CCW)
# for x in range(30):
#     GPIO.output(STEP4, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP4, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR8, CCW)
# for x in range(50):
#     GPIO.output(STEP8, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP8, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR4, CW)
# for x in range(35):
#     GPIO.output(STEP4, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP4, GPIO.LOW)
#     sleep(delay)


# GPIO.output(DIR1, CCW)
# GPIO.output(DIR3, CCW)
# for x in range(30):
#     GPIO.output(STEP1, GPIO.HIGH)
#     GPIO.output(STEP3, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP1, GPIO.LOW)
#     GPIO.output(STEP3, GPIO.LOW)
#     sleep(delay)
    

    
# whiteFace = colorfinder()
# U = whiteFace[0]
# u = whiteFace[1]
# V = whiteFace[2]
# x = whiteFace[3]
# down = whiteFace[4]
# v = whiteFace[5]
# X = whiteFace[6]
# w = whiteFace[7]
# W = whiteFace[8]
# print(whiteFace)

# GPIO.output(DIR1, CW)
# GPIO.output(DIR3, CW)
# for x in range(35):
#     GPIO.output(STEP1, GPIO.HIGH)
#     GPIO.output(STEP3, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP1, GPIO.LOW)
#     GPIO.output(STEP3, GPIO.LOW)
#     sleep(delay)

#  #Turn Motor 5
# GPIO.output(DIR2, CCW)
# for x in range(30):
#     GPIO.output(STEP2, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP2, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR5, CW)
# for x in range(50):
#     GPIO.output(STEP5, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP5, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR2, CW)
# for x in range(35):
#     GPIO.output(STEP2, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP2, GPIO.LOW)
#     sleep(delay)

# #Turn Motor 8
# GPIO.output(DIR4, CCW)
# for x in range(30):
#     GPIO.output(STEP4, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP4, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR8, CCW)
# for x in range(50):
#     GPIO.output(STEP8, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP8, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR4, CW)
# for x in range(35):
#     GPIO.output(STEP4, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP4, GPIO.LOW)
#     sleep(delay)


# Xprimeturn()

# #Done with white



#  #Turn Motor 5
# GPIO.output(DIR2, CCW)
# for x in range(30):
#     GPIO.output(STEP2, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP2, GPIO.LOW)
#     sleep(delay)


# GPIO.output(DIR5, CW)
# for x in range(50):
#     GPIO.output(STEP5, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP5, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR2, CW)
# for x in range(35):
#     GPIO.output(STEP2, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP2, GPIO.LOW)
#     sleep(delay)

# #Turn Motor 8
# GPIO.output(DIR4, CCW)
# for x in range(30):
#     GPIO.output(STEP4, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP4, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR8, CCW)
# for x in range(50):
#     GPIO.output(STEP8, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP8, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR4, CW)
# for x in range(35):
#     GPIO.output(STEP4, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP4, GPIO.LOW)
#     sleep(delay)


# GPIO.output(DIR1, CCW)
# GPIO.output(DIR3, CCW)
# for x in range(30):
#     GPIO.output(STEP1, GPIO.HIGH)
#     GPIO.output(STEP3, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP1, GPIO.LOW)
#     GPIO.output(STEP3, GPIO.LOW)
#     sleep(delay)
    

# orangeFace = colorfinder()
# O = orangeFace[0]
# o = orangeFace[1]
# P = orangeFace[2]
# n = orangeFace[3]
# back = orangeFace[4]
# p = orangeFace[5]
# N = orangeFace[6]
# m = orangeFace[7]
# M = orangeFace[8]
# print(orangeFace)

# GPIO.output(DIR1, CW)
# GPIO.output(DIR3, CW)
# for x in range(35):
#     GPIO.output(STEP1, GPIO.HIGH)
#     GPIO.output(STEP3, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP1, GPIO.LOW)
#     GPIO.output(STEP3, GPIO.LOW)
#     sleep(delay)

#  #Turn Motor 5
# GPIO.output(DIR2, CCW)
# for x in range(30):
#     GPIO.output(STEP2, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP2, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR5, CW)
# for x in range(50):
#     GPIO.output(STEP5, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP5, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR2, CW)
# for x in range(35):
#     GPIO.output(STEP2, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP2, GPIO.LOW)
#     sleep(delay)

# #Turn Motor 8
# GPIO.output(DIR4, CCW)
# for x in range(30):
#     GPIO.output(STEP4, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP4, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR8, CCW)
# for x in range(50):
#     GPIO.output(STEP8, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP8, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR4, CW)
# for x in range(35):
#     GPIO.output(STEP4, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP4, GPIO.LOW)
#     sleep(delay)


# Xprimeturn()

# #Done with Orange

# Yprimeturn()

#  #Turn Motor 5
# GPIO.output(DIR2, CCW)
# for x in range(30):
#     GPIO.output(STEP2, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP2, GPIO.LOW)
#     sleep(delay)


# GPIO.output(DIR5, CW)
# for x in range(50):
#     GPIO.output(STEP5, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP5, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR2, CW)
# for x in range(35):
#     GPIO.output(STEP2, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP2, GPIO.LOW)
#     sleep(delay)

# #Turn Motor 8
# GPIO.output(DIR4, CCW)
# for x in range(30):
#     GPIO.output(STEP4, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP4, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR8, CCW)
# for x in range(50):
#     GPIO.output(STEP8, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP8, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR4, CW)
# for x in range(35):
#     GPIO.output(STEP4, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP4, GPIO.LOW)
#     sleep(delay)


# GPIO.output(DIR1, CCW)
# GPIO.output(DIR3, CCW)
# for x in range(30):
#     GPIO.output(STEP1, GPIO.HIGH)
#     GPIO.output(STEP3, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP1, GPIO.LOW)
#     GPIO.output(STEP3, GPIO.LOW)
#     sleep(delay)
    

# blueFace = colorfinder()
# T = blueFace[0]
# t = blueFace[1]
# Q = blueFace[2]
# s = blueFace[3]
# left = blueFace[4]
# q = blueFace[5]
# S = blueFace[6]
# r = blueFace[7]
# R = blueFace[8]
# print(blueFace)

# GPIO.output(DIR1, CW)
# GPIO.output(DIR3, CW)
# for x in range(35):
#     GPIO.output(STEP1, GPIO.HIGH)
#     GPIO.output(STEP3, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP1, GPIO.LOW)
#     GPIO.output(STEP3, GPIO.LOW)
#     sleep(delay)

#  #Turn Motor 5
# GPIO.output(DIR2, CCW)
# for x in range(30):
#     GPIO.output(STEP2, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP2, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR5, CW)
# for x in range(50):
#     GPIO.output(STEP5, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP5, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR2, CW)
# for x in range(35):
#     GPIO.output(STEP2, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP2, GPIO.LOW)
#     sleep(delay)

# #Turn Motor 8
# GPIO.output(DIR4, CCW)
# for x in range(30):
#     GPIO.output(STEP4, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP4, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR8, CCW)
# for x in range(50):
#     GPIO.output(STEP8, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP8, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR4, CW)
# for x in range(35):
#     GPIO.output(STEP4, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP4, GPIO.LOW)
#     sleep(delay)

# #Done with blue

# Yprimeturn()
# Yprimeturn()

#  #Turn Motor 5
# GPIO.output(DIR2, CCW)
# for x in range(30):
#     GPIO.output(STEP2, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP2, GPIO.LOW)
#     sleep(delay)


# GPIO.output(DIR5, CW)
# for x in range(50):
#     GPIO.output(STEP5, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP5, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR2, CW)
# for x in range(35):
#     GPIO.output(STEP2, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP2, GPIO.LOW)
#     sleep(delay)

# #Turn Motor 8
# GPIO.output(DIR4, CCW)
# for x in range(30):
#     GPIO.output(STEP4, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP4, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR8, CCW)
# for x in range(50):
#     GPIO.output(STEP8, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP8, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR4, CW)
# for x in range(35):
#     GPIO.output(STEP4, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP4, GPIO.LOW)
#     sleep(delay)


# GPIO.output(DIR1, CCW)
# GPIO.output(DIR3, CCW)
# for x in range(30):
#     GPIO.output(STEP1, GPIO.HIGH)
#     GPIO.output(STEP3, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP1, GPIO.LOW)
#     GPIO.output(STEP3, GPIO.LOW)
#     sleep(delay)
    

# greenFace = colorfinder()
# J = greenFace[0]
# j = greenFace[1]
# K = greenFace[2]
# i = greenFace[3]
# right = greenFace[4]
# k = greenFace[5]
# I = greenFace[6]
# l = greenFace[7]
# L = greenFace[8]
# print(greenFace)

# GPIO.output(DIR1, CW)
# GPIO.output(DIR3, CW)
# for x in range(35):
#     GPIO.output(STEP1, GPIO.HIGH)
#     GPIO.output(STEP3, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP1, GPIO.LOW)
#     GPIO.output(STEP3, GPIO.LOW)
#     sleep(delay)

#  #Turn Motor 5
# GPIO.output(DIR2, CCW)
# for x in range(30):
#     GPIO.output(STEP2, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP2, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR5, CW)
# for x in range(50):
#     GPIO.output(STEP5, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP5, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR2, CW)
# for x in range(35):
#     GPIO.output(STEP2, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP2, GPIO.LOW)
#     sleep(delay)

# #Turn Motor 8
# GPIO.output(DIR4, CCW)
# for x in range(30):
#     GPIO.output(STEP4, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP4, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR8, CCW)
# for x in range(50):
#     GPIO.output(STEP8, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP8, GPIO.LOW)
#     sleep(delay)

# GPIO.output(DIR4, CW)
# for x in range(35):
#     GPIO.output(STEP4, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP4, GPIO.LOW)
#     sleep(delay)

# Yprimeturn()

#Done With green

#endregion


#main()

Rturn()