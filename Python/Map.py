import sys
import json
import os

pathRaw = 'Data/Raw'
pathProcessed = 'Data/Processed'

f_list = [f for f in os.listdir(pathRaw) if os.path.isfile(f) and f.endswith('.json')]
print (f_list)