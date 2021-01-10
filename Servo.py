import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

servo1 = GPIO.PWM(11, 50)
servo2 = GPIO.PWM(13, 50)
servo1.start(0)
servo2.start(0)
time.sleep(1)

def SetAngle1(angle):
    duty = angle/18 + 2
    GPIO.output(11, True)
    servo1.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(11, False)
    servo1.ChangeDutyCycle(0)
def SetAngle2(angle):
    duty = angle/18 + 2
    GPIO.output(13, True)
    servo2.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(13, False)
    servo2.ChangeDutyCycle(0)
SetAngle1(70)
SetAngle2(180)#120
servo1.stop()
servo2.stop()
GPIO.cleanup()