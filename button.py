import board
import digitalio
import time

# Setup button on GPIO 21
button = digitalio.DigitalInOut(board.D21)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP  # Enable internal pull-up resistor

# Setup LEDs
led_red = digitalio.DigitalInOut(board.D17)
led_red.direction = digitalio.Direction.OUTPUT

led_green = digitalio.DigitalInOut(board.D27)
led_green.direction = digitalio.Direction.OUTPUT

# Initial state
value = False

print("Press the button!")

while True:
    if not button.value:  # Button pressed (LOW state)
        value = not value
        print("Button Pressed! ", value)

        # Change LED color based on value
        if value:
            led_red.value = True
            led_green.value = False
        else:
            led_red.value = False
            led_green.value = True

        time.sleep(0.2) 
