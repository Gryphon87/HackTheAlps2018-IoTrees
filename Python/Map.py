import sys
import json
import os

f_list = [f for f in os.listdir() if os.path.isfile(f)]
print (f_list)