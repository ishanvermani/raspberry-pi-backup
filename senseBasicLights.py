from sense_hat import SenseHat

sense = SenseHat()
red = (255, 0, 0)
try:
    while True:
        for x in range(0, 8):
            for y in range(0, 8):
                sense.set_pixel(x, y, 255, 0, 0)


        
        
except KeyboardInterrupt:
    pass
finally:
    sense.clear()
