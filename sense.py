from sense_hat import SenseHat
from datetime import datetime, date, time
sense = SenseHat()




try:
    while True:
#        t = str(datetime.now())
 #       sense.show_message(t, scroll_speed=0.05, text_colour=[255, 0, 0])
        sense.load_image("/home/pi/Desktop/Google_G.png&f=1", redraw=True)        
except KeyboardInterrupt:
        pass

finally:
    sense.clear()

