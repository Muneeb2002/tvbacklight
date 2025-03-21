#!/usr/bin python3

import board
import neopixel
import board
import digitalio
import cv2
import numpy as np
import time

#LED strip Configuration
WIDTH = 81             # Number of horizontal of LEDs
HEIGHT = 39            # Number of vertical of LEDs per side
LED_COUNT = 2*HEIGHT+WIDTH          # Number of LEDs in the strip
LED_PIN = board.D18    # GPIO pin connected to the LED strip (D18 is common for WS2812)
BRIGHTNESS = 1         # Brightness (0.0 to 1.0)
pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=BRIGHTNESS, auto_write=False) # Initialize the LED strip

# Button configuartion
# Setup button on GPIO 21
button = digitalio.DigitalInOut(board.D21)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP  # Enable internal pull-up resistor
# Setup LEDs
led_red = digitalio.DigitalInOut(board.D17)
led_red.direction = digitalio.Direction.OUTPUT
led_green = digitalio.DigitalInOut(board.D27)
led_green.direction = digitalio.Direction.OUTPUT
# initial state
smallScreen = False


#Capture card configs
# Open the capture device (modify device index if needed)
cap = cv2.VideoCapture(0)  # Use /dev/video0, change index if required

# Set resolution if needed (optional, depends on your capture card)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)



def colourTheLeds(colours):
    for i in range(len(colours)):
        pixels[i] = (colours[0],colours[1],colours[2])
    print("colours shown")
    pixels.show()

def button():
    if not button.value:  # Button pressed (LOW state)
        smallScreen = not smallScreen
        print("Button Pressed! ", smallScreen)

        # Change LED color based on value
        if not smallScreen:
            led_red.value = True
            led_green.value = False
        else:
            led_red.value = False
            led_green.value = True
        return
    
def crop_4_3_center(frame):
   

    height, width = frame.shape[:2]
    target_4_3_width = int((4 / 3) * height)
    x_pad = (width - target_4_3_width) // 2
    x_start = x_pad
    x_end = width - x_pad

    # Just return the center crop — let resizing happen later
    return frame[:, x_start:x_end]


def captureStream():
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        return
    
    if smallScreen:
        frame = crop_4_3_center(frame)


    resizeFrame = cv2.resize(frame, (WIDTH, HEIGHT), interpolation =cv2.INTER_AREA)
    
    imageArray = cv2.cvtColor(resizeFrame, cv2.COLOR_BGR2RGB)

    height, width, _ = imageArray.shape

    # Bottom-left corner
    bottom_left = imageArray[height - 1, 0, :].reshape(1, 3)

    # Left edge (upward), excluding corners
    left_edge = imageArray[height - 2:0:-1, 0, :]  # y=2,1 (x=0)

    # Top edge (left to right)
    top_edge = imageArray[0, :, :]  # y=0, x=0→3

    # Right edge (downward), excluding corners
    right_edge = imageArray[1:height - 1, width - 1, :]  # y=1,2 (x=3)

    # Bottom-right corner
    bottom_right = imageArray[height - 1, width - 1, :].reshape(1, 3)

    # Concatenate in clockwise order
    border_pixels = np.concatenate([
        bottom_left,
        left_edge,
        top_edge,
        right_edge,
        bottom_right
    ], axis=0)

    return border_pixels



while True:
    button()
    colours = captureStream()
    colourTheLeds(colours)
    time.sleep(15)


