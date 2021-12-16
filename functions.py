#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import datetime
import settings

def verbose(args,val):
	if (args.verbose):
		print(val)
	
	return False

def logstr(string):
	if (settings.debug == True):
		today = datetime.datetime.now() 
		dirname = "debuglog/"
		logfile_name = dirname+"debug_" + today.strftime("%Y%m%d") +".log"

		f = open(logfile_name, "a")
		#os.chmod(logfile_name, 0o777)
		#uid = settings.options["Loguid"]
		#gid = settings.options["Loggid"]
		#os.chown(logfile_name, uid, gid)


		if isinstance(string, list):
			str1 = ','.join(str(e) for e in string)
			string = str1

		log_string=os.environ.get('USER')+" ["+today.strftime('%Y-%m-%d %H:%M:%S')+"] "+string
		f.write(log_string + "\n")
		f.close()
		return False