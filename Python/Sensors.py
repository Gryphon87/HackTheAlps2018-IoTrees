import sys
import Adafruit_DHT
import datetime as dt
import json
import time
import io

# Set sensor type : Options are DHT11,DHT22 or AM2302
sensor = Adafruit_DHT.DHT11

# Set GPIO sensor is connected to
gpio = 17

#BeaconId
beaconid = 1



#delay (seconds)
delay = 15

#Folder
folder = 'Data/Raw'

while True:
    #sensor data
    hum, te = Adafruit_DHT.read_retry(11, 17)
    #timestamp
    timeOfRecording = dt.datetime.now()
    #filename
    filename = '{}/IoTrees-Beacon-{}-{}.json'.format(folder, beaconid, timeOfRecording)

    #print('Time: {}, Temp={}*C  Humidity={}%'.format( time, te, hum ))
    if te is not None and hum is not None:
        Status= 'Ok'
    else:
        Status= 'Err'
    data = {'Beacon': beaconid, 'Status': Status, 'Date': '{}'.format(time.strftime('%Y%m%d', timeOfRecording)), 'Time': '{}'.format(time.strftime('%H:%M', timeOfRecording)), 'Temp': te, 'Hum': hum}
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)
        print('File {} written in folder {}!'.format(filename, folder))
    time.sleep(delay) #Wait X seconds between measurements
