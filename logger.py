#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import datetime
group = os.getenv("DATA_AGENT_CONF", default=None)
if (group == "local"):
    from config_local import setting as stg
elif (group == "interface"):
    from config_interface import setting as stg
elif (group == "distari"):
    from config_distari import setting as stg    
else:
    from config import setting as stg


class logger():
    def __init__(self, debug,verbose):
        self.string = ""
        self.debug = stg['debug']
        self.verbose = verbose
        self.logdir = "debuglog/"
        self.logpre = "debug_"

    def logstr(self,string):
        self.string = string
        #if (self.verbose == "-vvv"):
            #print(self.string)

        if (self.debug == True):
            today = datetime.datetime.now() 
            
            logfile_name = self.logdir+self.logpre + today.strftime("%Y%m%d") +".log"
            f = open(logfile_name, "a")

            if isinstance(self.string, list):
                str1 = ','.join(str(e) for e in self.string)
                self.string = str1

            log_string=os.environ.get('USER')+" ["+today.strftime('%Y-%m-%d %H:%M:%S')+"] "+self.string
            f.write(log_string + "\n")
            f.close()
            return False