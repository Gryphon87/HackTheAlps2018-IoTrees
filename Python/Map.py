import sys
import json
import os
import time

pathRaw = '{}/Data/Raw'.format(os.getcwd())
pathMapped = '{}/Data/Mapped'.format(os.getcwd())
pathError = '{}/Data/Errors'.format(os.getcwd())
pathArchive = '{}/Data/Archive'.format(os.getcwd())

f_list = [f for f in os.listdir(pathRaw) if f.endswith('.json')]
for f in f_list:
    data = json.loads(f)
    if data.Status == 'Err':
        #on errors, move files away and keep going
        os.rename('{}/{}'.format(pathRaw, f), '{}/{}'.format(pathError, f))
        print ('File {} moved to {} because of errors'.format(f, pathError))
        continue
    time = '{}:{}'.format(time.strftime ('%H', data.Time), (time.strftime ('%M', data.Time) - time.strftime ('%M', data.Time)%5))
    mapped = {'Beacon': data.beaconid, 'Date': data.date, 'Time': time, 'Temp': data.temp, 'Hum': data.hum }
    
    #write the mapped file
    json.dump(data, '{}/{}'.format(pathMapped, f))
    print ('File {} mapped to {}'.format(f, pathMapped))

    #move the file
    os.rename('{}/{}'.format(pathRaw, f), '{}/{}'.format(pathArchive, f))
    print ('File {} archived to {}'.format(f, pathArchive))