import time
import adafruit_dht
import board
from gpiozero import Button

dht = adafruit_dht.DHT22(board.D14)
button = Button(2)

while True:
    try:
        temperature = dht.temperature
        humidity = dht.humidity
        # Print what we got to the REPL
        print("Temp: {:.1f} *C \t Humidity: {}%".format(temperature, humidity))
    except RuntimeError as e:
        # Reading doesn't always work! Just print error and we'll try again
        print("Reading from DHT failure: ", e.args)

def catch_temp()
	try:
		timestamp = time.asctime()
		temperature = dht.temperature
		humidity = dht.humidity
		print("{}	Temperature:{}C	Humidity:{}%".format(timestamp, temperature, humidity))
		print("-----------------------------------------------------------------------------")
	except RuntimeError as error:
		print("Failed to get temperature and humidity. Please try again...")
		print(error)
		print("=============================================================================")
		return

def main():
	print("=============================================================================")
	while True
		button.when_pressed = catch_temp
		time.sleep(1)	
	
	
if __name__ == "__main__":
    main()
