import time
import board
import neopixel
import re
import math
import json
import random
from datetime import datetime, timedelta


def xmaslight():
    # set up the pixels (AKA 'LEDs')
    PIXEL_COUNT = 200  # this should be 500

    pixels = neopixel.NeoPixel(board.D18, PIXEL_COUNT, auto_write=False)

    for i in range(PIXEL_COUNT):
        pixels[i] = [0, 0, 0]

    pixels.show()

    # get colors
    with open("colors.json") as json_file:
        colors = json.load(json_file)

    print(colors)

    colorKeys = list(colors.keys())

    ind = 0
    # Get the current time
    now = datetime.now()
    while True:
        # Get the time one hour ago
        one_hour_ago = now - timedelta(minutes=1)

        # Check if an hour has passed
        if now > one_hour_ago:
            break
        ind = ind % len(colorKeys)
        pixels[random.randint(0, 199)] = colors[colorKeys[ind]]
        ind += 1

        time.sleep(0.100)


if __name__ == "__main__":
    xmaslight()
