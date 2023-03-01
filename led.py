from gpiozero import RGBLED
from time import sleep

# Set up RGB LED
led = RGBLED(red=22, green=17, blue=27) # Assuming the KY-009 module is connected to GPIO pins 10, 9, and 11 for red, green, and blue respectively

# Loop to cycle through colors
while True:
    led.color = (1, 0, 0) # Red
    sleep(1)
    led.color = (0, 1, 0) # Green
    sleep(1)
    led.color = (0, 0, 1) # Blue
    sleep(1)