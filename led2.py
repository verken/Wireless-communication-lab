import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT) # Red pin
GPIO.setup(27, GPIO.OUT) # Green pin
GPIO.setup(22, GPIO.OUT) # Blue pin

# Loop to cycle through colors
while True:
    GPIO.output(17, GPIO.HIGH) # Red
    time.sleep(1)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.HIGH) # Green
    time.sleep(1)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(22, GPIO.HIGH) # Blue
    time.sleep(1)
    GPIO.output(22, GPIO.LOW)