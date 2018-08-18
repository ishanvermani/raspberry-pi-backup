#/usr/bin/python
from gpiozero import LED, Button, LightSensor
from time import sleep
from signal import pause
import sys
ldr = LightSensor(17)
button = Button(2)
eighteen = LED(18)
fifteen = LED(15)
twentyone = LED(21)
four = LED(4)
five = LED(5)
six = LED(6)
seven = LED(7)
eight = LED(8)
nine = LED(9)
ten = LED(10)
eleven = LED(11)
twelve = LED(12)
thirteen = LED(13)

number = 0
list1 = [twentyone, five, eight, ten, thirteen]
list2 = [eighteen, fifteen, twentyone, five, eight, seven, six, nine, eleven, twelve, thirteen]
list3 = [eighteen, fifteen, twentyone, five, eight, seven, six, ten, eleven, twelve, thirteen]
list4 = [eighteen, four, six, seven, twentyone, five, eight, ten, thirteen]
list5 = [twentyone, eighteen, fifteen, four, six, seven, eight, ten, eleven, twelve, thirteen]
list6 = [eighteen, fifteen, twentyone, four, six, seven, eight, nine, ten, eleven, twelve, thirteen]
list7 = [eighteen, fifteen, twentyone, five, eight, ten, thirteen]
list8 = [eighteen, twentyone, fifteen, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen]
list9 = [eighteen, fifteen, twentyone, four, five, six, seven, eight, ten, eleven, twelve, thirteen]
list0 = [eighteen, fifteen, twentyone, four, five, six, eight, nine, ten, eleven, twelve, thirteen]


def lightup(x):
    for item in list8:
        item.off()
    if x == 1:
        for item in list1:
            item.on()
    elif x == 2:
        for item in list2:
            item.on()
    elif x == 3:
        for item in list3:
            item.on()
    elif x == 4:
        for item in list4:
            item.on()
    elif x == 5:
        for item in list5:
            item.on()
    elif x == 6:
        for item in list6:
            item.on()
    elif x == 7:
        for item in list7:
            item.on()
    elif x == 8:
        for item in list8:
            item.on()
    elif x == 9:
        for item in list9:
            item.on()
    elif x == 10:
        for item in list0:
            item.on()
        
    else:
       sys.exit()

def function():
    global number
    number = number + 1
    lightup(number)
    
    
while True:        
    button.when_pressed = function    

    
