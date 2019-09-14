from sense_hat import SenseHat
from random import randint
from time import sleep


def colour_range(start, end, steps):
    step = (end - start) // steps
    while True:
        colour = start
        while colour < end:
            yield colour
            colour += step

def major_colour_range(start, end, steps):
    step = (end - start) // steps
    while True:
        colour = start
        while start < end:
            for i in range(steps):
                yield colour
            colour += step

def pixel_range(red_range, blue_range, green_range):
    yield (next(red_range), next(blue_range), next(green_range))

sense = SenseHat()

green_range = colour_range(50, 255, 7)
blue_range = colour_range(50, 255, 7)

for x in range(8):
    g = next(green_range)
    for y in range(8):
##        print(x, y, 0, g, b)
        b = next(blue_range)
        sense.set_pixel(x, y, 0, g, b)

sleep(1)

red_range = colour_range(50, 255, 7)

for x in range(8):
    blue_range = colour_range(50, 255, 7)
    r = next(red_range)
    for y in range(8):
##        print(x, y, 0, g, b)
        b = next(blue_range)
        sense.set_pixel(x, y, r, 0, b)
