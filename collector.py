#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import datetime
import settings
from functions import *

def collectxx(xxtype,time,args):
	logstr("Type:"+str(xxtype)+",Time:"+str(time))
	logstr("Args:"+str(args))
	logstr("settings:"+str(settings.options[xxtype]["A"]))

	if(os.path.exists(settings.options[xxtype]["A"])):
		logstr("---If---")
		s=[];
		for x in range(time):
			next_date = datetime.datetime.now() - datetime.timedelta(minutes=x)
			
			
			verbose(args,"Date:"+str(x)+"-"+next_date.strftime(settings.options[xxtype]["B"]))
			s.append(next_date.strftime(settings.options[xxtype]["B"]))

		#print('\|'.join(s))
		cmd="grep -i \""+'\|'.join(s)+"\" "+settings.options[xxtype]["A"]
		if "M1" in settings.options[xxtype]:
			cmd=cmd+" | grep \""+settings.options[xxtype]["M1"]+"\""
		
		if "M2" in settings.options[xxtype]:
			cmd=cmd+" | grep \""+settings.options[xxtype]["M2"]+"\""	
			
		if "Reg" in settings.options[xxtype]:
			cmd=cmd+" | grep -E \""+settings.options[xxtype]["Reg"]+"\""
		
		if xxtype == "mat":
			cmd=cmd+ " | grep \"" +args.find + "\""

		if xxtype == "ip":
			cmd=cmd+ " | "+settings.options[xxtype]["awk"]
		
		if xxtype not in ["ip"]:
			cmd=cmd+" | wc -l"	

		logstr("cmd:"+str(cmd))
		os.system(cmd)
	else:
		logstr("---else---")
		print("File Not Foud")
		logstr("File Not Foud")
		
		
	return False
