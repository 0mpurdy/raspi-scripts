from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

start = 50

b = start
g = start

c_change = (255 - start) // 7

for x in range(8):
    b = start
    for y in range(8):
##        print(x, y, 0, g, b)
        sense.set_pixel(x, y, 0, g, b)
        b += c_change
    g += c_change

sleep(5)

while True:
    sense.set_pixel(randint(0,7), randint(0,7), randint(0,255), randint(0,255), randint(0,255))
