"""Creates random sparkle effects all over the sense hat"""

from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

for x in range(8):
        for y in range(8):
            sense.set_pixel(x, y, 0, 0, 0)


while True:
    x = randint(0, 7)
    y = randint(0, 7)

    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    sense.set_pixel(x, y, r, g, b)
    sleep(0.1)
