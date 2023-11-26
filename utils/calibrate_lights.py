import cv2
import neopixel
import board
import time
import math

from loguru import logger

white_c = [255, 255, 255]
black_c = [0, 0, 0]
middle_c = [128, 128, 128]


def l2(pair):
    return math.sqrt(pair[0] ** 2 + pair[1] ** 2)


def l1(pair):
    return pair[0] + pair[1]


def calibrate(PIXEL_COUNT: int = 200) -> None:
    cap = cv2.VideoCapture(0)
    print(dir(neopixel))
    pixels = neopixel.NeoPixel(board.D18, PIXEL_COUNT, auto_write=False)

    # Four passes rotating clockwise
    # The middle of the image is the origin
    # First pass:
    #   positive x to the right
    #   positive y going into the image
    #   positive z going up
    positions = [[], [], [], []]
    for rotation in range(4):
        # paint the LEDs, take a picture, and record the brightest location
        for LED in range(PIXEL_COUNT):
            # color the lights

            if LED > 0:
                pixels[LED - 1] = black_c
            pixels[LED] = white_c

            # display the lights
            pixels.show()
            time.sleep(0)

            # capture an image of the lights and determine where
            # it is in the image (2d-space)
            ret, frame = cap.read()
            logger.debug(frame.shape)

            orig = frame.copy()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
            logger.debug(f"Location: {maxLoc}, value {maxVal}")
            if maxVal > 128:
                positions[rotation].append([maxLoc[0], maxLoc[1]])
            else:
                positions[rotation].append([100000, 100000])

            # testing to make sure, what is happening makes sense
            # before circle
            """
            cv2.imshow("webcame", frame)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            # after circle
            cv2.circle(frame, maxLoc, 5, (0, 0, 255), -1)
            cv2.imshow("webcame", frame)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            """
        if rotation < 3:
            logger.info("Time to turn")
            pixels.fill(middle_c)
            pixels.show()
            cv2.waitKey(0)
            pixels.fill(black_c)
            pixels.show()

    # get a new reference image to get the coordinate frame
    ret, frame = cap.read()
    height, width, _ = frame.shape

    # reframe the collected coordinates
    xdelta = width // 2
    ydelta = height // 2

    for rotation in range(2):
        for pos in range(len(positions[0])):
            # TODO: is this right? might need to switch xdelta & ydelta
            positions[rotation][pos][0] = positions[rotation][pos][0] - xdelta
            positions[rotation][pos][1] = positions[rotation][pos][1] - ydelta
    for rotation in range(2, 4):
        for pos in range(len(positions[0])):
            # TODO: also this?
            positions[rotation][pos][0] = xdelta - positions[rotation][pos][0]
            positions[rotation][pos][1] = ydelta - positions[rotation][pos][1]

    # filter the values
    for pos in range(len(positions[0])):
        if positions[0][1]:
            pass


if __name__ == "__main__":
    calibrate(1)
