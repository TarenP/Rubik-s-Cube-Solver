import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ControlPin = [10,9,11,25]

for pin in ControlPin:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,0)
    
Seq = [ [1,0,0,1],
        [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1] ]

for i in range(512):
    #512 is one revolution
    for halfstep in range(8):
        for pin in range(4):
            GPIO.output(ControlPin[pin], Seq[halfstep][pin])
        time.sleep(0.001)
GPIO.cleanup