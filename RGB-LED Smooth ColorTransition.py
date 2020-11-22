import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time # Import the sleep function from the time module

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# make pins into an output
ledR =GPIO.setup(17,GPIO.OUT) #Set pin for RED color
ledG =GPIO.setup(27,GPIO.OUT) #Set pin for GREEN color
ledB =GPIO.setup(22,GPIO.OUT) #Set pin for BLUE color

#Set up outputs as PWM @ 144Hz
freq=60

ledR = GPIO.PWM(17,freq)
ledG = GPIO.PWM(27,freq)
ledB = GPIO.PWM(22,freq)

ledR.start(100)
ledG.start(0)
ledB.start(0)


while True: # Run forever / infinity loop
    for r, g in zip(range(100), range(100,0,-1)):
        ledR.ChangeDutyCycle(r)
        ledG.ChangeDutyCycle(g)
        time.sleep(0.02)

    for g, b in zip(range(100), range(100,0,-1)):
        ledG.ChangeDutyCycle(g)
        ledB.ChangeDutyCycle(b)
        time.sleep(0.02)

    for b, r in zip(range(100), range(100,0,-1)):
        ledB.ChangeDutyCycle(b)
        ledR.ChangeDutyCycle(r)
        time.sleep(0.02)








