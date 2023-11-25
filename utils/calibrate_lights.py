import cv2
import neopixel
import board

colorWhite = [255, 255, 255]


def calibrate(PIXEL_COUNT: int = 200) -> None:
    cap = cv2.VideoCapture(0)
    print(dir(neopixel))
    # pixels = neopixel.NeoPixel(board.D18, PIXEL_COUNT, auto_write=False)

    for LED in range(PIXEL_COUNT):
        ret, frame = cap.read()
        # (x, y, z) = cv2.minMaxLoc(frame)
        # print(f"Location: x {x}, y {y}, value {z}")
        cv2.imshow("webcame", frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    calibrate(1)
