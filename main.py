#!/usr/bin/python3
    
from flask import Flask, render_template
import adafruit_dht
    
app = Flask(__name__)
pin = 4
sensor = adafruit_dht.DHT11(pin)
    
@app.route("/")
def main():
   
   humidity = sensor.humidity
   temperature = sensor.temperature 
   templateData = {
      'temperature' : temperature,
      'humidity': humidity
   }

   return render_template('main.html', **templateData)
     
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
