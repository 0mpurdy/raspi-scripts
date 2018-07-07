"""Attempting to create brown"""

from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

for x in range(8):
        for y in range(8):
            colour = (x * 32) + (y * 4)
            print(colour)
            sense.set_pixel(x, y, colour, colour, 0)

sleep(5)

for x in range(8):
  for y in range(8):
    sense.set_pixel(x, y, 210, 105, 30)
