#!/usr/bin/python3
    
import adafruit_dht
import database
import time

pin = 4
sensor = adafruit_dht.DHT11(pin)
db = database.weather_database()

def main():

    humidity = sensor.humidity
    temperature = sensor.temperature 
    db.insert(temperature, 0, 0, 0, humidity, 0, 0, 0, 0)


if __name__ == "__main__":
    while True:
        try:
            main()
            time.sleep(60)
        except:
            pass

