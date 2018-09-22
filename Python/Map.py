import sys
import json
import os

pathRaw = '{}/Data/Raw'.format(os.getcwd())
pathProcessed = '{}/Data/Processed'.format(os.getcwd())

f_list = [f for f in os.listdir(pathRaw) if f.endswith('.json')]
print(os.getcwd())
print (f_list)