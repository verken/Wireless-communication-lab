import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.OUT) # Red pin
GPIO.setup(10, GPIO.OUT) # Green pin
GPIO.setup(9, GPIO.OUT) # Blue pin

# Loop to cycle through colors
while True:
    GPIO.output(11, GPIO.LOW) # 
    GPIO.output(10, GPIO.HIGH) # 
    GPIO.output(9, GPIO.HIGH) # 
    time.sleep(1)
    GPIO.output(11, GPIO.HIGH) # 
    GPIO.output(10, GPIO.LOW) # 
    GPIO.output(9, GPIO.HIGH) # 
    time.sleep(1)
    GPIO.output(11, GPIO.HIGH) # 
    GPIO.output(10, GPIO.HIGH) # 
    GPIO.output(9, GPIO.LOW) # 
    time.sleep(1)
    GPIO.output(11, GPIO.HIGH) # 
    GPIO.output(10, GPIO.HIGH) # 
    GPIO.output(9, GPIO.HIGH) # 
    time.sleep(1)
    GPIO.output(11, GPIO.LOW) # 
    GPIO.output(10, GPIO.LOW) # 
    GPIO.output(9, GPIO.HIGH) # 
    time.sleep(1)
    GPIO.output(11, GPIO.HIGH) # 
    GPIO.output(10, GPIO.LOW) # 
    GPIO.output(9, GPIO.LOW) # 
    time.sleep(1)
    GPIO.output(11, GPIO.LOW) # 
    GPIO.output(10, GPIO.HIGH) # 
    GPIO.output(9, GPIO.LOW) # 
    time.sleep(1)
    GPIO.output(11, GPIO.HIGH) # 
    GPIO.output(10, GPIO.HIGH) # 
    GPIO.output(9, GPIO.HIGH) # 
    time.sleep(1)
    GPIO.output(11, GPIO.LOW) # 
    GPIO.output(10, GPIO.LOW) # 
    GPIO.output(9, GPIO.LOW) # 
    time.sleep(1)