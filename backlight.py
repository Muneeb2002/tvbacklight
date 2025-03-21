import time
import board
import neopixel
import random

# Configuration
LED_COUNT = 159          # Number of LEDs in the strip
LED_PIN = board.D18    # GPIO pin connected to the LED strip (D18 is common for WS2812)
BRIGHTNESS = 0.5       # Brightness (0.0 to 1.0)

# Initialize the LED strip
pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=BRIGHTNESS, auto_write=False)

def random_color():
    """Generate a random RGB color."""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


while True:
    print("lolcat")
    # Set each LED to a random color
    for i in range(LED_COUNT):
        pixels[i] = random_color()
        print(pixel[i])
    
    # Show the new colors
    pixels.show()
    
    # Wait for half a second
    time.sleep(0.5)
