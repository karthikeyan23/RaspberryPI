import RPi.GPIO as GPIO
import dht11
import time
import datetime
import json
import requests

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin
instance = dht11.DHT11(pin=23)

while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)
        url = 'http://192.168.0.4:8001'

        params = dict(
            celcius2=result.temperature,
            humidity=result.humidity
            )

        resp = requests.get(url=url, params=params)
    time.sleep(1)
