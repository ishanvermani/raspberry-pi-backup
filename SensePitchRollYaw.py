from sense_hat import SenseHat
from time import sleep
sense = SenseHat()



#x is pitch, y is roll, z is yaw
def extract_led(x,y,z):

    if x == 0 and y == 0:
        for a in range(0, 8):
            for b in range(0, 8):
                sense.set_pixel(a, b, 255, 255, 255)
    
    elif x >= 270 and (y <= 45 or y>= 315):
        x -= 360
        x *= -1
        xr = round((x/10))
        xr -= 1
        if xr >= 0 and xr < 8:
            
            for i in range(0, 8):
                sense.set_pixel(xr, i, 0, 255, 0)

            for a in range(0, 8):
                if xr >= a:
                    for c in range (0, 8):
                        sense.set_pixel(a,c,0,255,0)
                elif xr < a:
                    for b in range (0, 8):

                        sense.set_pixel(a, b, 0, 0, 0)
        elif xr <= -1:
            sense.clear()
                        
                           
    elif x <= 90 and (y <= 45 or y>= 315):
        x -= 90
        x *= -1
        xr = round((x/10))
        xr -= 1
        
        
        if 0<= xr < 8:
            
            for i in range(0, 8):
                sense.set_pixel(xr, i, 0, 0, 255)

            for a in range(0, 8):
                if xr <= a:
                    for c in range (0, 8):
                        sense.set_pixel(a,c,0,0,255)
                elif xr > a:
                    for b in range (0, 8):
                        sense.set_pixel(a, b, 0, 0, 0)
        elif xr >= 8:
            sense.clear()

        '''    
    elif y <= 90 and (x <= 45 or x>= 315):
        yr = round((y/10))
        yr -= 1
        if  0 <= yr < 8:
            for i in range (0, 8):
                sense.set_pixel(i, yr, 255, 0, 0)
            for a in range (0, 8):
                if a > yr:
                    for c in range (0, 8):
                        sense.set_pixel(c, a, 0, 0, 0)
                elif yr >= a:
                    for b in range (0, 8):
                        sense.set_pixel(b, a, 255, 0, 0)
        elif yr < 0:
            sense.clear()
        

    elif y >= 270 and (x <=45 or x >= 315):
        y -= 270
        yr = round((y/10))
        yr -= 1
        if 0 <= yr < 8:
            for i in range(0, 8):
                sense.set_pixel(i, yr, 255, 255, 0)
            for a in range(0, 8):
                if a >= yr:
                    for c in range(0, 8):
                        sense.set_pixel(c, a, 255, 255, 0)
                elif a < yr:
                    for b in range(0,8):
                        sense.set_pixel(b, a, 0, 0, 0)
        elif yr > 7:
            sense.clear()

         '''
    
    
    
        
    else:
        sense.clear()
        





try:
    while True:
        o = sense.get_orientation()
        pitch = o['pitch']
        roll = o['roll']
        yaw = o['yaw']

        x = round(pitch)
        y = round(roll)
        z = round(yaw)
        print("x {0}, y {1}, z {2}".format(x, y, z))
        extract_led(x,y,z)
        
except KeyboardInterrupt:
    pass
finally:
    sense.clear()
