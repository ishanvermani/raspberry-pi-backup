#!/usr/bin/python3
from signal import pause
import sys
import pygame
import pygame.camera
from pygame.locals import *
from sense_hat import SenseHat, ACTION_RELEASED
from twython import Twython
from datetime import datetime
import random
from time import sleep
import os

sense = SenseHat()
white = (255, 255, 255)

pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0", (1600,1200))


consumer_key = *
consumer_secret = *
access_key = *
access_secret = *

# Twitter Keys can be found under GAFEphotos Twitter application manager

api = Twython(
    consumer_key,
    consumer_secret,
    access_key,
    access_secret
)
thumsup = [
    '───────────────────████',
    '───────────────────█████',
    '───────────────────██████',
    '───────────────────███████',
    '──────────────────████████',
    '──────────────────████████',
    '─────────────────█████████',
    '────────────────█████████',
    '───────────────█████████',
    '──────────────█████████',
    '──────────────██████████████████',
    '────────────█████████████████████',
    '───────────███████████████████████',
    '████████─██████████████████████████',
    '████████─███████████████████████████',
    '████████─████████████████████████████',
    '████████─████████████████████████████',
    '████████─████████████████████████████',
    '████████─████████████████████████████',
    '████████─███████████████████████████',
    '████████─██████████████████████████',
    '████████─█████████████████████████',
    '████████─████████████████████████',
    '████████─███████████████████████'
]
   
def people(photopath):
    #comment out here to remove keyboard component
    while True:
        username = input("Enter your twitter handles (without the @ sign), separated by a space: ")
        if len(username) < 240:
            break
        else:
            print('Too Many Characters; Try Again')
    if username == "ishanisawesome":
        ask = input("Custom message?")
        if ask == "exit":
            os.system("clear")
            for i in range(5):
                print ('')
            print ("Exiting program... To restart, type 'sudo python3 photobooth.py' ")
            for i in range(5):
                print ('')
            sys.exit()
        elif ask == 'nopic':
            custom = input("Custom message: ")
            if len(custom) < 111:
                api.update_status(status=custom)
            else:
                upload(photopath)
        else:
            return 'ishanisawesome'
    else:
        handles = []
        for item in username.split():
                handles.append(" @" + str(item))
        coolio = "".join(handles)
        return coolio
        
# end of cut
def choose_message(photopath):
#Cut to to remove keyboard
    handles = people(photopath)
    length = len(handles)
    if handles == 'ishanisawesome':
        custom = input("Custom Message: ")
        if len(custom) < 111:
            os.system('clear')
            print ("Push Button to take picture")
            return custom
        else:
            upload(photopath)
    else:                 
        if length < 205:
            message = "Learning a lot today at the CRPS/SEA Custom Summit!! I love this automated photo booth! #RaspberryPi #EdTechTeam" + handles
            return message
        elif length < 240:
            message = "Lots of cool things at #EdTechTeam!" + handles
            return message
        elif length < 269:
            message = '#EdTechTeam' + handles
            return message
        else:
            return handles
# End Cut. Uncomment below
    '''
def choose_message(photopath):
    message = "Learning a lot today at the CRPS/SEA Custom Summit!! I love this automated photo booth! #RaspberryPi #EdTechTeam"
    return message
'''
        
def upload(photopath):
    message = choose_message(photopath)
    photo = open(photopath, "rb")
    response = api.upload_media(media=photo)
    api.update_status(status=message, media_ids=[response['media_id']])
    for i in range(0,3):
        print (' ')
    print('Tweet uploaded: Download it from twitter.com/gafephotos. Enjoy your day!')
    for i in range(0,3):
        print (' ')
    for item in thumsup:
        print (item)

def capture():
    time = datetime.now().isoformat()
    photopath = '/home/pi/photobooth/%s.jpg' % time
    cam.start()    
    image = cam.get_image()
    pygame.image.save(image, photopath)
    cam.stop()
    sense.clear()
    upload(photopath)

def light_show():
    os.system("clear")
    sense.show_letter("5", white)
    sleep(1)
    sense.show_letter("4", white)
    sleep(1)
    sense.show_letter("3", white)
    sleep(1)
    sense.show_letter("2", white)
    sleep(1)
    sense.show_letter("1", white)
    sleep(1)
    for x in range (0, 8):
        for y in range(0, 8):
            sense.set_pixel(x, y, 0, 255, 0)
    capture()  
    
    
def trigger(event):
    if event.action != ACTION_RELEASED:
        light_show()

sense.stick.direction_any = trigger


try:
    while True:
        pass
except KeyboardInterrupt:
    pass
finally:
    sense.clear()
    os.system("clear")
