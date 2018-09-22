import sys
import Adafruit_DHT
import datetime as dt
import json
import time import sleep
import io

# Set sensor type : Options are DHT11,DHT22 or AM2302
sensor = Adafruit_DHT.DHT11

# Set GPIO sensor is connected to
gpio = 17

#BeaconId
beaconid = 1

while True:
    hum, temp = Adafruit_DHT.read_retry(11, 17)
    time = dt.datetime.now()
    print('Time: {}, Temp={}*C  Humidity={}%'.format( time, temp, hum ))
    if temp is not None and hum is not None:
        Status= 'Ok'
    else:
        Status= 'Ok'

    #print (json.dumps({'Beacon': beaconid, 'Status': Status, 'Time': time, 'Temp': temp, 'Hum': hum}))
    sleep(30) #Wait 30 seconds between measurements
