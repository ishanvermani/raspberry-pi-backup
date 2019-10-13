'''
Project created to experiment with the Joystick on the Raspberry Pi Sense hat. It moves a pixel depending on the direction inputted
'''

from sense_hat import SenseHat, ACTION_RELEASED
from time import sleep
sense = SenseHat()

def down(x, y, c, l):
    if y < 7:
        sense.set_pixel(x, y, 0, 0, 0)
        sense.set_pixel(x, (y + 1), l[c])
        global vert
        vert += 1

    
        

def up(x, y, c, l):
    if y > 0:
        sense.set_pixel(x, y, 0, 0, 0)
        sense.set_pixel(x, (y - 1), l[c])
        global vert
        vert -= 1
    
def left(x, y, c, l):
    if x > 0:
        sense.set_pixel(x, y, 0, 0, 0)
        sense.set_pixel((x - 1), y, l[c])
        global hori
        hori -= 1
    
def right(x, y, c, l):
    if x < 7:
        sense.set_pixel(x, y, 0, 0, 0)
        sense.set_pixel((x + 1), y, l[c])
        global hori
        hori += 1
    
def press(x, y, c, l):
    global col
    if c < 2:
        col += 1
        c +=1
    else:
        col = 0
        c = 0
    sense.set_pixel(x, y, l[c])

hori = 0
vert = 0
col = 0

cols = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

def sup(event):
    if event.action != ACTION_RELEASED:
        global hori
        global vert
        global col
        global cols
        up(hori, vert, col, cols)

def sdown(event):
    if event.action != ACTION_RELEASED:
        global hori
        global vert
        global col
        global cols
        down(hori, vert, col, cols)
   

def sright(event):
    if event.action != ACTION_RELEASED:
        global hori
        global vert
        global col
        global cols
        right(hori, vert, col, cols)

def sleft(event):
    if event.action != ACTION_RELEASED:
        global hori
        global vert
        global col
        global cols
        left(hori, vert, col, cols)

def spress(event):
    if event.action != ACTION_RELEASED:
        global hori
        global vert
        global col
        global cols
        press(hori, vert, col, cols)
    
sense.stick.direction_up = sup
sense.stick.direction_down = sdown
sense.stick.direction_left = sleft
sense.stick.direction_right = sright
sense.stick.direction_middle = spress

sense.set_pixel(hori, vert, cols[col])

try:
    while True:
        pass

except KeyboardInterrupt:
    pass
finally:
    sense.clear()
