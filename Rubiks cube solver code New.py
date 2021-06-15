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

delay = .0108


GPIO.setwarnings(False)
      
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

solvedC2 = False
solvedC3 = False
solvedC4 = False
solvedC5 = False
solvedC6 = False
solvedC7 = False
solvedC8 = False

def Xturn():
    GPIO.output(DIR5, CW)
    GPIO.output(DIR8, CCW)
    GPIO.output(DIR1, CCW)
    GPIO.output(DIR3, CCW)
    GPIO.output(DIR2, CW)
    GPIO.output(DIR4, CW)
    for x in range(5):
        GPIO.output(STEP2, GPIO.HIGH)
        GPIO.output(STEP4, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP2, GPIO.LOW)
        GPIO.output(STEP4, GPIO.LOW)
        sleep(delay)
        
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
    for x in range(30):
        GPIO.output(STEP2, GPIO.HIGH)
        GPIO.output(STEP4, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP2, GPIO.LOW)
        GPIO.output(STEP4, GPIO.LOW)
        sleep(delay)

def Xprimeturn():
    GPIO.output(DIR5, CCW)
    GPIO.output(DIR8, CW)
    GPIO.output(DIR1, CCW)
    GPIO.output(DIR3, CCW)
    GPIO.output(DIR2, CW)
    GPIO.output(DIR4, CW)
    for x in range(5):
        GPIO.output(STEP2, GPIO.HIGH)
        GPIO.output(STEP4, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP2, GPIO.LOW)
        GPIO.output(STEP4, GPIO.LOW)
        sleep(delay)

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
    for x in range(30):
        GPIO.output(STEP2, GPIO.HIGH)
        GPIO.output(STEP4, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP2, GPIO.LOW)
        GPIO.output(STEP4, GPIO.LOW)
        sleep(delay)

def Yturn():
    GPIO.output(DIR6, CW)
    GPIO.output(DIR7, CCW)
    GPIO.output(DIR2, CCW)
    GPIO.output(DIR4, CCW)
    GPIO.output(DIR1, CW)
    GPIO.output(DIR3, CW)
    for x in range(5):
        GPIO.output(STEP1, GPIO.HIGH)
        GPIO.output(STEP3, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP1, GPIO.LOW)
        GPIO.output(STEP3, GPIO.LOW)
        sleep(delay)
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
    for x in range(30):
        GPIO.output(STEP1, GPIO.HIGH)
        GPIO.output(STEP3, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP1, GPIO.LOW)
        GPIO.output(STEP3, GPIO.LOW)
        sleep(delay)

def Yprimeturn():
    GPIO.output(DIR6, CCW)
    GPIO.output(DIR7, CW)
    GPIO.output(DIR2, CCW)
    GPIO.output(DIR4, CCW)
    GPIO.output(DIR1, CW)
    GPIO.output(DIR3, CW)
    for x in range(5):
        GPIO.output(STEP1, GPIO.HIGH)
        GPIO.output(STEP3, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP1, GPIO.LOW)
        GPIO.output(STEP3, GPIO.LOW)
        sleep(delay)
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
    for x in range(30):
        GPIO.output(STEP1, GPIO.HIGH)
        GPIO.output(STEP3, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP1, GPIO.LOW)
        GPIO.output(STEP3, GPIO.LOW)
        sleep(delay)

def Rturn():
    GPIO.output(DIR4, CW)
    GPIO.output(DIR3, CW)
    GPIO.output(DIR1, CW)
    GPIO.output(DIR2, CW)
    for x in range(5):
        GPIO.output(STEP4, GPIO.HIGH)
        GPIO.output(STEP3, GPIO.HIGH)
        GPIO.output(STEP2, GPIO.HIGH)
        GPIO.output(STEP1, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP4, GPIO.LOW)
        GPIO.output(STEP3, GPIO.LOW)
        GPIO.output(STEP2, GPIO.LOW)
        GPIO.output(STEP1, GPIO.LOW)
        sleep(delay)
        
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

def Rprimeturn():
    GPIO.output(DIR4, CW)
    GPIO.output(DIR3, CW)
    GPIO.output(DIR1, CW)
    GPIO.output(DIR2, CW)
    for x in range(5):
        GPIO.output(STEP4, GPIO.HIGH)
        GPIO.output(STEP3, GPIO.HIGH)
        GPIO.output(STEP2, GPIO.HIGH)
        GPIO.output(STEP1, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP4, GPIO.LOW)
        GPIO.output(STEP3, GPIO.LOW)
        GPIO.output(STEP2, GPIO.LOW)
        GPIO.output(STEP1, GPIO.LOW)
        sleep(delay)
    
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

def Lturn():
    GPIO.output(DIR4, CW)
    GPIO.output(DIR3, CW)
    GPIO.output(DIR1, CW)
    GPIO.output(DIR2, CW)
    for x in range(5):
        GPIO.output(STEP4, GPIO.HIGH)
        GPIO.output(STEP3, GPIO.HIGH)
        GPIO.output(STEP2, GPIO.HIGH)
        GPIO.output(STEP1, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP4, GPIO.LOW)
        GPIO.output(STEP3, GPIO.LOW)
        GPIO.output(STEP2, GPIO.LOW)
        GPIO.output(STEP1, GPIO.LOW)
        sleep(delay)
        
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

def Lprimeturn():
    GPIO.output(DIR4, CW)
    GPIO.output(DIR3, CW)
    GPIO.output(DIR1, CW)
    GPIO.output(DIR2, CW)
    for x in range(5):
        GPIO.output(STEP4, GPIO.HIGH)
        GPIO.output(STEP3, GPIO.HIGH)
        GPIO.output(STEP2, GPIO.HIGH)
        GPIO.output(STEP1, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP4, GPIO.LOW)
        GPIO.output(STEP3, GPIO.LOW)
        GPIO.output(STEP2, GPIO.LOW)
        GPIO.output(STEP1, GPIO.LOW)
        sleep(delay)
        
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

def Bturn():
    GPIO.output(DIR4, CW)
    GPIO.output(DIR3, CW)
    GPIO.output(DIR1, CW)
    GPIO.output(DIR2, CW)
    for x in range(5):
        GPIO.output(STEP4, GPIO.HIGH)
        GPIO.output(STEP3, GPIO.HIGH)
        GPIO.output(STEP2, GPIO.HIGH)
        GPIO.output(STEP1, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP4, GPIO.LOW)
        GPIO.output(STEP3, GPIO.LOW)
        GPIO.output(STEP2, GPIO.LOW)
        GPIO.output(STEP1, GPIO.LOW)
        sleep(delay)
        
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

def Bprimeturn():
    GPIO.output(DIR4, CW)
    GPIO.output(DIR3, CW)
    GPIO.output(DIR1, CW)
    GPIO.output(DIR2, CW)
    for x in range(5):
        GPIO.output(STEP4, GPIO.HIGH)
        GPIO.output(STEP3, GPIO.HIGH)
        GPIO.output(STEP2, GPIO.HIGH)
        GPIO.output(STEP1, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP4, GPIO.LOW)
        GPIO.output(STEP3, GPIO.LOW)
        GPIO.output(STEP2, GPIO.LOW)
        GPIO.output(STEP1, GPIO.LOW)
        sleep(delay)
        
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

def Fturn():
    GPIO.output(DIR4, CW)
    GPIO.output(DIR3, CW)
    GPIO.output(DIR1, CW)
    GPIO.output(DIR2, CW)
    for x in range(5):
        GPIO.output(STEP4, GPIO.HIGH)
        GPIO.output(STEP3, GPIO.HIGH)
        GPIO.output(STEP2, GPIO.HIGH)
        GPIO.output(STEP1, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP4, GPIO.LOW)
        GPIO.output(STEP3, GPIO.LOW)
        GPIO.output(STEP2, GPIO.LOW)
        GPIO.output(STEP1, GPIO.LOW)
        sleep(delay)
        
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
    for x in range(30):
        GPIO.output(STEP1, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP1, GPIO.LOW)
        sleep(delay)

def Fprimeturn():
    GPIO.output(DIR4, CW)
    GPIO.output(DIR3, CW)
    GPIO.output(DIR1, CW)
    GPIO.output(DIR2, CW)
    for x in range(5):
        GPIO.output(STEP4, GPIO.HIGH)
        GPIO.output(STEP3, GPIO.HIGH)
        GPIO.output(STEP2, GPIO.HIGH)
        GPIO.output(STEP1, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP4, GPIO.LOW)
        GPIO.output(STEP3, GPIO.LOW)
        GPIO.output(STEP2, GPIO.LOW)
        GPIO.output(STEP1, GPIO.LOW)
        sleep(delay)
        
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
    for x in range(30):
        GPIO.output(STEP1, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP1, GPIO.LOW)
        sleep(delay)

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
        
        #red color
        low_red = np.array([151, 155, 84])
        high_red = np.array([179, 255, 255])
        red_mask = cv2.inRange(hsv_img, low_red, high_red)
        contours1, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours1 = sorted(contours1, key=lambda x:cv2.contourArea(x), reverse=True)
            
        for cnt in contours1:
            area1 = cv2.contourArea(cnt)
            if area1 > 5000:
                faceColors[counter-1] = "red"

        
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
        low_blue = np.array([106, 239, 215])
        high_blue = np.array([128, 255, 255])
        blue_mask = cv2.inRange(hsv_img, low_blue, high_blue)
        contours3, _ = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours3 = sorted(contours3, key=lambda x:cv2.contourArea(x), reverse=True)
         
        for cnt in contours3:
            area3 = cv2.contourArea(cnt)
            if area3 > 5000:
                faceColors[counter-1] = "blue"
                
        #green color
        low_green = np.array([36, 171, 159])
        high_green = np.array([71, 255, 255])
        green_mask = cv2.inRange(hsv_img, low_green, high_green)
        contours4, _ = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours4 = sorted(contours4, key=lambda x:cv2.contourArea(x), reverse=True)
         
        for cnt in contours4:
            area4 = cv2.contourArea(cnt)
            if area4 > 5000:
               faceColors[counter-1] = "green"
                
        #Orange color
        low_orange = np.array([0, 167, 112])
        high_orange = np.array([10, 255, 255])
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
            
            faceColors[counter-1] = "white"
                
        
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


    #checking if anycorners are already solved
    everythingSolved = False
    cornerSolveList = []


    #Use a list of the moves to the positions the bank pieces need to go.

    #finish
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
                bankCorner = mBJM
            elif(solvedC3 == False):
                cornerSolveList.append('D')
                bankCorner = mDRE
            elif(solvedC4 == False):
                cornerSolveList.append('C')
                bankCorner = mCFI
            elif(solvedC5 == False):
                cornerSolveList.append('D')
                bankCorner = mHSU
            elif (solvedC6 == False):
                cornerSolveList.append('G')
                bankCorner = mGLV
            elif (solvedC7 == False):
                cornerSolveList.append('X')
                bankCorner = mXTO
            elif (solvedC8 == False):
                cornerSolveList.append('W')
                bankCorner = mWKP
            #Swap with an unsolved corner because it is in the bank place and cannot be solved
    
        elif(bankCornerSorted == corner2):
            index = BJM.index(bankCorner[0])
            if (index == 0):
                cornerSolveList.append('B')
                bankCorner = mBJM
                solvedC2 = True
            elif (index == 1):
                cornerSolveList.append('J')
                bankCorner = mBJM
                solvedC2 = True
            else:
                cornerSolveList.append('M')
                bankCorner = mBJM
                solvedC2 = True

        elif (bankCornerSorted == corner3):
            index = DRE.index(bankCorner[0])
            if (index == 0):
                cornerSolveList.append('D')
                bankCorner = mDRE
                solvedC3 = True
            elif (index == 1):
                cornerSolveList.append('R')
                bankCorner = mDRE
                solvedC3 = True
            else:
                cornerSolveList.append('E')
                bankCorner = mDRE
                solvedC3 = True

        elif(bankCornerSorted == corner4):
            index = CFI.index(bankCorner[0])
            if (index == 0):
                cornerSolveList.append('C')
                bankCorner = mCFI
                solvedC4 = True
            elif (index == 1):
                cornerSolveList.append('F')
                bankCorner = mCFI
                solvedC4 = True
            else:
                cornerSolveList.append('I')
                bankCorner = mCFI
                solvedC4 = True
        
        elif(bankCornerSorted == corner5):
            index = HSU.index(bankCorner[0])
            if (index == 0):
                cornerSolveList.append('H')
                bankCorner = mHSU
                solvedC5 = True
            elif (index == 1):
                cornerSolveList.append('S')
                bankCorner = mHSU
                solvedC5 = True
            else:
                cornerSolveList.append('U')
                bankCorner = mHSU
                solvedC5 = True

        elif(bankCornerSorted == corner6):
            index = GLV.index(bankCorner[0])
            if (index == 0):
                cornerSolveList.append('G')
                bankCorner = mGLV
                solvedC6 = True
            elif (index == 1):
                cornerSolveList.append('L')
                bankCorner = mGLV
                solvedC6 = True
            else:
                cornerSolveList.append('V')
                bankCorner = mGLV
                solvedC6 = True
        
        elif(bankCornerSorted == corner7):
            index = XTO.index(bankCorner[0])
            if (index == 0):
                cornerSolveList.append('X')
                bankCorner = mXTO
                solvedC7 = True
            elif (index == 1):
                cornerSolveList.append('T')
                bankCorner = mXTO
                solvedC7 = True
            else:
                cornerSolveList.append('O')
                bankCorner = mXTO
                solvedC7 = True

        elif (bankCornerSorted == corner8):
            index = WKP.index(bankCorner[0])
            if (index == 0):
                cornerSolveList.append('W')
                bankCorner = mWKP
                solvedC8 = True
            elif (index == 1):
                cornerSolveList.append('K')
                bankCorner = mWKP
                solvedC8 = True
            else:
                cornerSolveList.append('P')
                bankCorner = mWKP
                solvedC8 = True
    print(cornerSolveList)
    return cornerSolveList
    # #use "list".sort() method for comparing the two corners.

def cornerSwapper(cornerSolveList):
    for i in len(cornerSolveList):
        letter = cornerSolveList.index(i-1)
        if letter == 'B':
            Rturn()
            Dprimeturn()
            AlteredYPermutation()
        elif letter == 'C':
            Fturn()
            AlteredYPermutation()
        elif letter == 'D':
            Fturn()
            Rprimeturn()
            AlteredYPermutation()
        elif letter == 'E':
            Fprimeturn()
            Dturn()
            AlteredYPermutation()
        elif letter == 'F':
            Fturn()
            Fturn()
            Dturn()
            AlteredYPermutation()
        elif letter == 'G':
            Dturn()
            Rturn()
            AlteredYPermutation()
        elif letter == 'H':
            Dturn()
            AlteredYPermutation()
        elif letter == 'I':
            Rprimeturn()
            AlteredYPermutation()
        elif letter == 'J':
            Rturn()
            Rturn()
            AlteredYPermutation()
        elif letter == 'K':
            Rturn()
            AlteredYPermutation()
        elif letter == 'L':
            AlteredYPermutation()
        elif letter == 'M':
            Rprimeturn()
            Fturn()
            AlteredYPermutation()
        elif letter == 'N':
            AlteredYPermutation()
        elif letter == 'O':
            Dprimeturn()
            Rturn()
            AlteredYPermutation()
        elif letter == 'P':
            Dprimeturn()
            AlteredYPermutation()
        elif letter == 'R':
            Fturn()
            Fturn()
            AlteredYPermutation()
        elif letter == 'S':
            Dturn()
            Dturn()
            Rturn()
            AlteredYPermutation()
        elif letter == 'T':
            Dturn()
            Dturn()
            AlteredYPermutation()
        elif letter == 'U':
            Fprimeturn()
        elif letter == 'V':
            Dprimeturn()
            Fprimeturn()
            AlteredYPermutation()
        elif letter == 'W':
            Dturn()
            Dturn()
            Fprimeturn()
            AlteredYPermutation()
        elif letter == 'X':
            Dturn()
            Fprimeturn()
            AlteredYPermutation()
        else:
            print("error occurred, no action assigned to corner swapper")
        



def cornerMain():
    cList = cornerActions()
    cornerSwapper(cList)



#Work in progress

def edgeAssigner():
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

def edgeSwapper():
    bankEdge = mbi
    bankEdge.sort()

    edge1 = mbi
    edge1.sort()
    edge2 = mam
    edge2.sort()
    edge3 = mce
    edge3.sort()
    edge4 = mdq
    edge4.sort()
    edge5 = mfl
    edge5.sort()
    edge6 = mgu
    edge6.sort()
    edge7 = mhr
    edge7.sort()
    edge8 = mtn
    edge8.sort()
    edge9 = msx
    edge9.sort()
    edge10 = mkv
    edge10.sort()
    edge11 = mow
    edge11.sort()
    edge12 = mjp
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

    bankEdge = mbi
    bankEdge.sort()

    Edge1 = bi
    Edge1.sort()
    Edge2 = am
    Edge2.sort()
    Edge3 = ce
    Edge3.sort()
    Edge4 = dq
    Edge4.sort()
    Edge5 = fl
    Edge5.sort()
    Edge6 = gu
    Edge6.sort()
    Edge7 = hr
    Edge7.sort()
    Edge8 = tn
    Edge8.sort()
    Edge9 = sx
    Edge9.sort()
    Edge10 = kv
    Edge10.sort()
    Edge11 = ow
    Edge11.sort()
    Edge12 = jp
    Edge12.sort()



    #Use a list of the moves to the positions the bank pieces need to go.

    #finish
    while everythingSolved == False:
        if (bankEdge == Edge1):
            index = bi.index(bankEdge[0])
            if (index == 0 and solvedE2 == True and solvedE3 == True and solvedE4 == True and solvedE5 == True and solvedE6 == True and solvedE7 == True and solvedE8 == True and solvedE9 == True and solvedE10 == True and solvedE11 == True and solvedE12 == True):
                print("Edges already set")
                everythingSolved = True
            elif (solvedE2 == False):
                edgeSolveList.append('a')
                bankEdge = mam
            elif(solvedE3 == False):
                edgeSolveList.append('c')
                bankEdge = mce
            elif(solvedE4 == False):
                edgeSolveList.append('d')
                bankEdge = mdq
            elif(solvedE5 == False):
                edgeSolveList.append('f')
                bankEdge = mfl
            elif (solvedE6 == False):
                edgeSolveList.append('g')
                bankEdge = mgu
            elif (solvedE7 == False):
                edgeSolveList.append('h')
                bankEdge = mhr
            elif (solvedE8 == False):
                edgeSolveList.append('t')
                bankEdge = mtn
            elif (solvedE9 == False):
                edgeSolveList.append('s')
                bankEdge = msx
            elif (solvedE10 == False):
                edgeSolveList.append('k')
                bankEdge = mkv
            elif (solvedE11 == False):
                edgeSolveList.append('o')
                bankEdge = mow
            elif (solvedE12 == False):
                edgeSolveList.append('j')
                bankEdge = mjp
            #Swap with an unsolved Edge because it is in the bank place and cannot be solved
    
        elif(bankEdge == Edge2):
            index = am.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('a')
                bankEdge = mam
                solvedE2 = True
            elif (index == 1):
                edgeSolveList.append('m')
                bankEdge = mam
                solvedE2 = True

        elif(bankEdge == Edge3):
            index = ce.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('c')
                bankEdge = mce
                solvedE3 = True
            elif (index == 1):
                edgeSolveList.append('e')
                bankEdge = mce
                solvedE3 = True
        
        elif(bankEdge == Edge4):
            index = dq.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('d')
                bankEdge = mdq
                solvedE4 = True
            elif (index == 1):
                edgeSolveList.append('q')
                bankEdge = mdq
                solvedE4 = True
            
        elif(bankEdge == Edge5):
            index = fl.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('f')
                bankEdge = mfl
                solvedE5 = True
            elif (index == 1):
                edgeSolveList.append('l')
                bankEdge = mfl
                solvedE5 = True
        
        elif(bankEdge == Edge6):
            index = gu.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('g')
                bankEdge = mgu
                solvedE6 = True
            elif (index == 1):
                edgeSolveList.append('u')
                bankEdge = mgu
                solvedE6 = True

        elif(bankEdge == Edge7):
            index = hr.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('h')
                bankEdge = mhr
                solvedE7 = True
            elif (index == 1):
                edgeSolveList.append('r')
                bankEdge = mhr
                solvedE7 = True
        
        elif(bankEdge == Edge8):
            index = tn.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('t')
                bankEdge = mtn
                solvedE8 = True
            elif (index == 1):
                edgeSolveList.append('n')
                bankEdge = mtn
                solvedE8 = True

        elif(bankEdge == Edge9):
            index = sx.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('s')
                bankEdge = msx
                solvedE9 = True
            elif (index == 1):
                edgeSolveList.append('x')
                bankEdge = msx
                solvedE9 = True

        elif(bankEdge == Edge10):
            index = kv.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('k')
                bankEdge = mkv
                solvedE10 = True
            elif (index == 1):
                edgeSolveList.append('v')
                bankEdge = mkv
                solvedE10 = True
        
        elif(bankEdge == Edge11):
            index = ow.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('o')
                bankEdge = mow
                solvedE11 = True
            elif (index == 1):
                edgeSolveList.append('w')
                bankEdge = mow
                solvedE11 = True

        elif(bankEdge == Edge12):
            index = jp.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('j')
                bankEdge = mjp
                solvedE12 = True
            elif (index == 1):
                edgeSolveList.append('p')
                bankEdge = mjp
                solvedE12 = True


def main():
    cornerMain()
    #Figure out new bank corner colors every time we swap

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

GPIO.output(DIR1, CCW)
GPIO.output(DIR3, CCW)
for x in range(30):
    GPIO.output(STEP1, GPIO.HIGH)
    GPIO.output(STEP3, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP1, GPIO.LOW)
    GPIO.output(STEP3, GPIO.LOW)
    sleep(delay)
    

yellowFace = colorfinder()
A = yellowFace[0]
a = yellowFace[1]
B = yellowFace[2]
d = yellowFace[3]
up = yellowFace[4]
b = yellowFace[5]
D = yellowFace[6]
c = yellowFace[7]
C = yellowFace[8]
print(A)

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

#Done with Yellow


GPIO.output(DIR5, CCW)
GPIO.output(DIR8, CW)
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
    
redFace = colorfinder()
E = redFace[0]
e = redFace[1]
F = redFace[2]
h = redFace[3]
front = redFace[4]
f = redFace[5]
H = redFace[6]
g = redFace[7]
G = redFace[8]
print(E)

GPIO.output(DIR5, CW)
GPIO.output(DIR8, CCW)
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

#Done With Red

Xprimeturn()
Xprimeturn()
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

GPIO.output(DIR1, CCW)
GPIO.output(DIR3, CCW)
for x in range(30):
    GPIO.output(STEP1, GPIO.HIGH)
    GPIO.output(STEP3, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP1, GPIO.LOW)
    GPIO.output(STEP3, GPIO.LOW)
    sleep(delay)
    
whiteFace = colorfinder()
U = whiteFace[0]
u = whiteFace[1]
V = whiteFace[2]
x = whiteFace[3]
down = whiteFace[4]
v = whiteFace[5]
X = whiteFace[6]
w = whiteFace[7]
W = whiteFace[8]
print(U)

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


Xturn()

Xturn()

#Done with white

Xturn()
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

GPIO.output(DIR1, CCW)
GPIO.output(DIR3, CCW)
for x in range(30):
    GPIO.output(STEP1, GPIO.HIGH)
    GPIO.output(STEP3, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP1, GPIO.LOW)
    GPIO.output(STEP3, GPIO.LOW)
    sleep(delay)


orangeFace = colorfinder()
O = orangeFace[0]
o = orangeFace[1]
P = orangeFace[2]
n = orangeFace[3]
back = orangeFace[4]
p = orangeFace[5]
N = orangeFace[6]
m = orangeFace[7]
M = orangeFace[8]

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


Xprimeturn

#Done with Orange

Yturn()
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

GPIO.output(DIR1, CCW)
GPIO.output(DIR3, CCW)
for x in range(30):
    GPIO.output(STEP1, GPIO.HIGH)
    GPIO.output(STEP3, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP1, GPIO.LOW)
    GPIO.output(STEP3, GPIO.LOW)
    sleep(delay)


blueFace = colorfinder()
T = blueFace[0]
t = blueFace[1]
Q = blueFace[2]
s = blueFace[3]
left = blueFace[4]
q = blueFace[5]
S = blueFace[6]
r = blueFace[7]
R = blueFace[8]

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


Yprimeturn()

#Done with blue

Yprimeturn()
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

GPIO.output(DIR1, CCW)
GPIO.output(DIR3, CCW)
for x in range(30):
    GPIO.output(STEP1, GPIO.HIGH)
    GPIO.output(STEP3, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP1, GPIO.LOW)
    GPIO.output(STEP3, GPIO.LOW)
    sleep(delay)


greenFace = colorfinder()
J = greenFace[0]
j = greenFace[1]
K = greenFace[2]
i = greenFace[3]
right = greenFace[4]
k = greenFace[5]
I = greenFace[6]
l = greenFace[7]
L = greenFace[8]

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


Yturn()

#Done With green


main()