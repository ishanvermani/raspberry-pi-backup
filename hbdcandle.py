#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import random
import pygame.mixer
from pygame.mixer import Sound
pygame.mixer.init()

def setup():
    global pwm
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17, GPIO.OUT)


    pwm = GPIO.PWM(17, 200)

    pwm.start(100)

def set_brightness(new_brightness):
    pwm.ChangeDutyCycle(new_brightness)

def flicker():
    set_brightness(random.randrange(0, 100))
    time.sleep(random.randrange(1, 10) * 0.01)

def loop():
    try:
        while True:
            flicker()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

setup()

loop()
