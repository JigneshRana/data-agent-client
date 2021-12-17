#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import datetime

class logger():
    def __init__(self, debug,verbose):
        self.string = ""
        self.debug = debug
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