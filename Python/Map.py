import sys
import json
import os
import time

#Paths for files
pathRaw = '{}/Data/Raw'.format(os.getcwd())
pathMapped = '{}/Data/Mapped'.format(os.getcwd())
pathError = '{}/Data/Errors'.format(os.getcwd())
pathArchive = '{}/Data/Archive'.format(os.getcwd())

#value for dividing minutes (i.e. with 5 you get aggregated data every five minutes)
div = 5

out = []
processedFiles = []
f_list = [f for f in os.listdir(pathRaw) if f.endswith('.json')]
for f in f_list:
    print('Processing file {} in folder {}'.format(pathRaw, f))
    filepath = '{}/{}'.format(pathRaw, f)
    with open(filepath, 'r') as inputfile:
        data = json.loads(inputfile.read())
    
    if data['Status'] == 'Err':
        #on errors, move files away and keep going
        os.rename('{}/{}'.format(pathRaw, f), '{}/{}'.format(pathError, f))
        print ('File {} moved to {} because of errors'.format(f, pathError))
        continue
    
    minute = int(data['Minutes'])
    time = '{}:{}'.format(data['Hour'], minute - minute%div)
    #mapped = {'Beacon': data['Beacon'], 'Date': {'Date': data['Date'], 'Time': [{'Time' time,  'Measurements': [ {'Temp': data['Temp'], 'Hum': data['Hum'] }]}] }}
    measurements =  {'Temp': data['Temp'], 'Hum': data['Hum'] }

    out.append({'Beacon': data['Beacon'], 'Date': {'Date': data['Date', 'Time': [{'Time': time, 'Measurements': [measurements]}]}})

           
    processedFiles.add(f)

#write the mapped file
fileout = '{}/{}'.format(pathMapped, 'MappedFile-{}'.format(datetime.datetime.now()))
with open(fileout, 'w') as outfile:
    json.dump(out, outfile)
print ('File {} mapped to {}'.format(fileout, pathMapped))

#move the files
for f in processedFiles:
    os.rename('{}/{}'.format(pathRaw, f), '{}/{}'.format(pathArchive, f))
    print ('File {} archived to {}'.format(f, pathArchive))