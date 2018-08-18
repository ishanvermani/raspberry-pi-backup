#/usr/lib/python3
from sense_hat import SenseHat
from random import randint
from time import sleep
sense = SenseHat()



def select(choice):
    x = randint(0, (len(choice)-1))
    y = choice[x]
    y()


def scroll_blue():
    sense.show_message("6351", text_colour=[0, 0, 255])

def scroll_red():
    sense.show_message("6351", text_colour=[255, 0, 0])

def flash_blue():
    sense.show_letter("6", text_colour=[0, 0, 255], back_colour=[0, 0, 0])
    sleep(1)
    sense.show_letter("3", text_colour=[0, 0, 0], back_colour=[0, 0, 255])
    sleep(1)
    sense.show_letter("5", text_colour=[0, 0, 255], back_colour=[0, 0, 0])
    sleep(1)
    sense.show_letter("1", text_colour=[0, 0, 0], back_colour=[0, 0, 255])
    sleep(1)

def flash_red():
    sense.show_letter("6", text_colour=[255, 0, 0], back_colour=[0, 0, 0])
    sleep(1)
    sense.show_letter("3", text_colour=[0, 0, 0], back_colour=[255, 0, 0])
    sleep(1)
    sense.show_letter("5", text_colour=[255, 0, 0], back_colour=[0, 0, 0])
    sleep(1)
    sense.show_letter("1", text_colour=[0, 0, 0], back_colour=[255, 0, 0])
    sleep(1)

def cheer():
    sense.show_message("Lets Go Cobras! ", scroll_speed=0.05, text_colour=[255, 255, 255])

def logo():
    x = [0, 0, 0]
    n = [71, 0, 18]
    mountain = [x, x, x, x, x, x, x, x,
                x, x, x, x, x, x, x, n,
                x, x, x, x, x, x, n, n,
                x, x, x, x, x, n, n, n,
                x, x, x, n, n, n, n, n,
                x, x, n, n, n, n, n, n,
                x, n, n, n, n, n, n, n,
                n, n, n, n, n, n, n, n]
    for i in range(0, 360, 90):
        sense.set_pixels(mountain)
        sense.set_rotation(i)
        sleep(1)
    sense.set_rotation(0)

    
try: 
    while True:
        choice = [scroll_blue, scroll_red, flash_red, flash_blue, cheer, logo]
        select(choice)
        

except KeyboardInterrupt:
    pass
finally:
    sense.clear()

    







