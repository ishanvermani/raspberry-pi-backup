#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.OUT)
try:
    while True:
        if GPIO.input(2) == GPIO.LOW:
            print "Button Pressed!"
            GPIO.output(21, 1)
            sleep(1)
            GPIO.output(21,0)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
