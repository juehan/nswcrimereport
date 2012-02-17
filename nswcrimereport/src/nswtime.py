'''
module to get Sydney/Australia's localtime
This module is not portable as time.tzset() is not supported at Windows Environment 
'''

import os
import time
from time import strftime
import sys

def getTime():
	os.environ['TZ'] = 'Australia/Sydney'
	if not sys.platform == "win32":
		time.tzset()
	return strftime("%Y-%m-%d %H:%M:%S")

