import RPi.GPIO as GPIO
import time

# Define GPIO pin
BUTTON_PIN = 18  # Connect this to the 'S' pin of the button
Value = false
# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Pull-up resistor enabled

print("Press the button!")

while True:
    if GPIO.input(BUTTON_PIN) == GPIO.LOW:  # Button pressed
        print("Button Pressed!")
        value = !value
        time.sleep(0.2)  # Small delay to prevent duplicate presses
