"""Smiles when the humidity increases (blow on the sensor)"""

from sense_hat import SenseHat
from faces import normal, happy, sad

from time import sleep

sense = SenseHat()
#sense.show_message('Hello World!')

sense.set_pixels(sad)
sleep(1)
sense.set_pixels(normal)
sleep(1)
sense.set_pixels(happy)
sleep(1)

start_humidity = sense.humidity
print('Starting humidity: %.2f' % start_humidity)

while True:
    print(sense.humidity)
    if (sense.humidity > start_humidity + 10):
        sense.set_pixels(happy)
    elif (sense.humidity > start_humidity + 5):
        sense.set_pixels(normal)
    else:
        sense.set_pixels(sad)
