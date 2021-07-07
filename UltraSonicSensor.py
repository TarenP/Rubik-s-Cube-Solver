import time
import RPi.GPIO as GPIO
GPIO.setmode (GPIO.BCM)
trig = 16      # GPIO pin numbers
echo = 12
GPIO.setup(echo, GPIO.IN)
GPIO.setup(trig, GPIO.OUT)
while True:
    GPIO.output (trig, True)
    time.sleep (0.00001) # 10 microseconds
    GPIO.output (trig, False)
    while GPIO.input (echo) == 0:
        print("0")
        pass
    start = time.time ()
    while GPIO.input (echo) == 1:
        print("1")
        pass
    end = time.time ()
    distance = (end - start)
    print (distance * 1000)
    #time.sleep (0.5)