# crea aggregato delle statistiche
# import mapped data
# calc stats
# write to a file

import sys
import json
import os
import datetime

def max(list):
  max = list[0]
  for x in list:
    if x > max:
      max = x
  return max

def min(list):
  min = list[0]
  for x in list:
    if x < min:
      min = x
  return min

def avg(list):
  sum = 0
  for x in list:
    sum += x
  return sum / len(list)

# Paths for files
pathMapped = '{}/Data/Mapped'.format(os.getcwd())
pathReduced = '{}/Data/Reduced'.format(os.getcwd())

file_list = [f for f in os.listdir(pathMapped) if f.startswith('MappedFile')]
for f in file_list:
  print('Processing file {} in folder {}'.format(pathMapped, f))
  filepath = '{}/{}'.format(pathMapped, f)
  with open(filepath, 'r') as inputfile:
    data = json.loads(inputfile.read())
    
    reduced = dict()
    for d in data:
      id = '{}{}'.format(d['id'], d['time'])
      temp = d['measures']['Temp']
      hum = d['measures']['Hum']

      if id in reduced.keys():
        reduced[id]['Temp'].append(temp)
        reduced[id]['Hum'].append(hum)
        continue
      
      measures = dict()
      measures['Temp'] = [temp]
      measures['Hum'] = [hum]
      reduced[id] = measures

stats = dict()
for key in reduced:
  temps = reduced[key]['Temp']
  hums = reduced[key]['Hum']
  stats[key] = {"minTemp": min(temps), "maxTemp": max(temps), "avgTemp": avg(temps), "minHum": min(hums), "maxHums": max(hums), "avgHums": avg(hums)}

fileout = '{}/{}'.format(pathReduced, 'ReducedFile-{}'.format(datetime.datetime.now()))
with open(fileout, 'w') as outfile:
    json.dump(stats, fileout)
print ('File {} reduced to {}'.format(fileout, pathReduced))
