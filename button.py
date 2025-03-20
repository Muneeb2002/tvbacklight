import board
import digitalio
import time

# Setup button on GPIO 21
button = digitalio.DigitalInOut(board.D21)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP  # Enable internal pull-up resistor
value = False

print("Press the button!")

while True:
    if not button.value:  # Button pressed (LOW state)
        print("Button Pressed! ", value)
        value = not value
        time.sleep(0.2)  # Prevent multiple detections

