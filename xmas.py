#/usr/lib/python3
from sense_hat import SenseHat
from time import sleep
from random import randint, choice
sense = SenseHat()




def tree1():
    g = [0, 255, 0]
    x = [0, 0, 0]
    n = [139, 69, 19]

    tree = [
    x, x, x, g, g, x, x, x,
    x, x, g, g, g, g, x, x,
    x, g, g, g, g, g, g, x,
    x, x, g, g, g, g, x, x,
    x, g, g, g, g, g, g, x,
    g, g, g, g, g, g, g, g,
    x, x, x, n, n, x, x, x,
    x, x, x, n, n, x, x, x
    ]

    sense.set_pixels(tree)
    sleep(5)


def tree2():
    g = [0, 0, 255]
    x = [0, 0, 0]
    n = [139, 69, 19]

    tree = [
    x, x, x, g, g, x, x, x,
    x, x, g, g, g, g, x, x,
    x, g, g, g, g, g, g, x,
    x, x, g, g, g, g, x, x,
    x, g, g, g, g, g, g, x,
    g, g, g, g, g, g, g, g,
    x, x, x, n, n, x, x, x,
    x, x, x, n, n, x, x, x
    ]

    sense.set_pixels(tree)
    sleep(5)

def tree3():
    g = [255, 255, 255]
    x = [0, 0, 0]
    n = [139, 69, 19]

    tree = [
    x, x, x, g, g, x, x, x,
    x, x, g, g, g, g, x, x,
    x, g, g, g, g, g, g, x,
    x, x, g, g, g, g, x, x,
    x, g, g, g, g, g, g, x,
    g, g, g, g, g, g, g, g,
    x, x, x, n, n, x, x, x,
    x, x, x, n, n, x, x, x
    ]

    sense.set_pixels(tree)
    sleep(5)

def tree4():
    g = [255, 0, 0]
    x = [0, 0, 0]
    n = [139, 69, 19]

    tree = [
    x, x, x, g, g, x, x, x,
    x, x, g, g, g, g, x, x,
    x, g, g, g, g, g, g, x,
    x, x, g, g, g, g, x, x,
    x, g, g, g, g, g, g, x,
    g, g, g, g, g, g, g, g,
    x, x, x, n, n, x, x, x,
    x, x, x, n, n, x, x, x
    ]

    sense.set_pixels(tree)
    sleep(5)

def tree5():
    

    r = 255
    g = 255
    b = 255

    for y in range(8):
        for x in range(8):
            while True:
                colour = [255, 0]
                r = choice(colour)
                g = choice(colour)
                b = choice(colour)
                if r == 0 and g == 0 and b == 0:
                    pass
                else:
                    break
                
            sense.set_pixel(x, y, r, g, b) 

    one = 0
    two = 1

    while True:
        dark = [3, 0, 4, 0,
            2, 1, 3, 1, 4, 1, 5, 1,
            1, 2, 2, 2, 3, 2, 4, 2, 5, 2, 6, 2,
            2, 3, 3, 3, 4, 3, 5, 3,
            1, 4, 2, 4, 3, 4, 4, 4, 5, 4, 6, 4,
            0, 5, 1, 5, 2, 5, 3, 5, 4, 5, 5, 5, 6, 5, 7, 5,
            3, 6, 4, 6,
            3, 7, 4, 7]

        c = dark[one]
        d = dark[two]

        sense.set_pixel(c, d, 0, 0, 0)
        one += 2
        two += 2
        if one == 68:
            break
            

    sleep(5)

     
    

try:
    while True:
        listt = [tree1, tree2, tree3, tree4, tree5] 
        select = choice(listt)
        select()
except KeyboardInterrupt:
    pass
finally:
    sense.clear()



    
    
