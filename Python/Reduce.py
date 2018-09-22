# crea aggregato delle statistiche
# import mapped data
# calc stats
# write to a file

import sys
import json
import os

# Paths for files
pathMapped = '{}/Data/Mapped'.format(os.getcwd())
file_list = [f for f in os.listdir(pathMapped) if f.startswith('MappedFile')]
for f in file_list:
  print('Processing file {} in folder {}'.format(pathMapped, f))
  filepath = '{}/{}'.format(pathMapped, f)
  with open(filepath, 'r') as inputfile:
    data = json.loads(inputfile.read())
    
    aggregatedData = dict()
    for d in data:
      id = '{}{}'.format(d['id'], d['time'])
      measures = d['measures']
      temp = measures['Temp']
      hum = measures['Hum']

      if id in aggregatedData.keys():
        aggregatedData[id]['Temp'].append(temp)
        aggregatedData[id]['Hum'].append(hum)
        continue
      
      aggregated = dict()
      aggregated['Temp'] = [temp]
      aggregated['Hum'] = [hum]
      aggregatedData[id] = aggregated

