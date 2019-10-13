'''
Mini project testing a Light Detecting Resistor with a Raspberry Pi GPIO input
'''

#/usr/bin/python
from gpiozero import LightSensor

ldr = LightSensor(4)
high = [0]
try:
    while True:
        print(str((ldr.value)* 100) + '%')
        if ldr.value > high[0]:
            high[0] = ldr.value
except KeyboardInterrupt:
    print(high[0])
