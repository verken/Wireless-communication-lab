from gpiozero import RGBLED
from time import sleep

# Set up RGB LED
led = RGBLED(red=11, green=10, blue=9) # Assuming the KY-009 module is connected to GPIO pins 10, 9, and 11 for red, green, and blue respectively

# Loop to cycle through colors
while True:
    led.color = (0, 1, 1) # Red
    print("red")
    sleep(1)
    led.color = (1, 0, 1) # Green
    print("green")
    sleep(1)
    led.color = (1, 1, 0) # Blue
    print("blue")
    sleep(1)
