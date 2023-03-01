import time
import adafruit_dht
import board
from gpiozero import Button

dht = adafruit_dht.DHT22(board.D14)
button = Button(2)

def main():
	print("=============================================================================")
	while True
		button.when_pressed = catch_temp
		time.sleep(1)	
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


	
	
if __name__ == "__main__":
    main()
