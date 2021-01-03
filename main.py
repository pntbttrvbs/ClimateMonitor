#!/usr/bin/python3
    
from flask import Flask, render_template
import adafruit_dht
import board
    
app = Flask(__name__)
sensor = adafruit_dht.DHT22(board.D4)
    
@app.route(“/”)
def main():
   
   humidity = sensor.humidity
   temperature = sensor.temperature 
   templateData = {
      ‘temperature’ : temperature,
      ‘humidity’: humidity
   }

   return render_template(‘main.html’, **templateData)
     
if __name__ == “__main__”:
   app.run(host=’0.0.0.0′, port=80, debug=True)
