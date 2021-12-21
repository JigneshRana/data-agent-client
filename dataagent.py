#!/usr/bin/env python3
import sys
import argparse
import json
import os
import datetime
from config import setting as stg
import subprocess
import logger

stg['time']
class DataAgent():

    def __init__(self, dataobj,time):
        self.dataobj = dataobj
        self.time = time
        self.resdata = {}
        self.log = logger.logger(True,False)
        
    def get_all_data(self):
        self.validate_it()
        #self.log.logstr("*********************")
        return self.resdata

    def validate_it(self):
        #print("Type of dict_obj", type(self.dataobj))
        if(type(self.dataobj) is dict):
            if(self.dataobj['action'] == "get" and self.dataobj['value'] == "all"):
                self.dataobj["time"] = stg['time']
                self.resdata["2xx"] = self.get_2xx()
                self.resdata["3xx"] = self.get_3xx()
                self.resdata["4xx"] = self.get_4xx()
                self.resdata["5xx"] = self.get_5xx()
                self.resdata["timec"] = self.get_timeconsuming()
                self.resdata["custom"] = self.get_custom()
                self.resdata["services"] = self.check_service()
                self.resdata["command"] = self.exe_command()
                self.resdata["phpe"] = self.get_phperror("E",stg['time'])
                self.resdata["phpw"] = self.get_phperror("W",stg['time'])
                self.resdata["phpn"] = self.get_phperror("N",stg['time'])
                #print(self.resdata)
                return (json.JSONEncoder().encode(self.resdata))
                
    def get_memory(self):
        return os.system('free -m')

    def get_2xx(self):
        return  self.collectxx("2xx",stg['time'])
    
    def get_3xx(self):
        return  self.collectxx("3xx",stg['time'])

    def get_4xx(self):
        return  self.collectxx("4xx",stg['time'])

    def get_5xx(self):
        return  self.collectxx("5xx",stg['time'])

    def get_timeconsuming(self):
        return  self.collectxx("timec",stg['time'])

    def get_regexmatch(self):
        return  self.collectxx("regexm",stg['time'])

    def get_custom(self):
        return  self.collect_custom("after",stg['time'])

    def collectxx(self,xxtype,time):
        access_type = ["2xx","3xx","4xx","5xx","timec","regexm"]

        if (xxtype in access_type):
            if(os.path.exists(stg.get('apache')['accesslog_path'])):
                s=[]
                for x in range(time):
                    next_date = datetime.datetime.now() - datetime.timedelta(minutes=x)
                    s.append(next_date.strftime(stg.get('apache')['accesslog_dateformat']))
                
                cmd="grep -i \""+'\|'.join(s)+"\" "+stg.get('apache')['accesslog_path']

                if (xxtype == "2xx"):
                    cmd=cmd+" | grep \""+stg.get('apache')['2xx_match']+"\""

                if (xxtype == "3xx"):
                    cmd=cmd+" | grep \""+stg.get('apache')['3xx_match']+"\""

                if (xxtype == "4xx"):
                    cmd=cmd+" | grep \""+stg.get('apache')['4xx_match']+"\""
                
                if (xxtype == "5xx"):
                    cmd=cmd+" | grep \""+stg.get('apache')['5xx_match']+"\""
                
                if (xxtype == "timec"):
                    cmd=cmd+" | grep -E \""+stg.get('apache')['time_consuming']+"\""
                
                if (xxtype == "regexm"):
                    cmd=cmd+" | grep -E \""+stg.get('apache')['regex_match']+"\""
                
                cmd=cmd+" | wc -l"
                

                output = subprocess.check_output(cmd, shell=True)
                #output = os.system(cmd)
                #convert output to utf-8 and remove \n from the last
                return str(output,"utf-8").rstrip("\n")
        else:
            print("File Not Foud")
        return False

    def get_phperror(self,etype,time):
        error_type = ["E","W","N"]

        if (etype in error_type):
            if(os.path.exists(stg.get('apache')['errorlog_path'])):
                s=[]
                for x in range(time):
                    next_date = datetime.datetime.now() - datetime.timedelta(minutes=x)
                    s.append(next_date.strftime(stg.get('apache')['errorlog_dateformat']))
                
                cmd="grep -i \""+'\|'.join(s)+"\" "+stg.get('apache')['errorlog_path']

                if (etype == "E"):
                    cmd=cmd+" | grep \""+stg.get('apache')['phpE']+"\""

                if (etype == "W"):
                    cmd=cmd+" | grep \""+stg.get('apache')['phpW']+"\""

                if (etype == "N"):
                    cmd=cmd+" | grep \""+stg.get('apache')['phpN']+"\""    
                
                cmd=cmd+" | wc -l"
                

                output = subprocess.check_output(cmd, shell=True)
                #output = os.system(cmd)
                #convert output to utf-8 and remove \n from the last
                return str(output,"utf-8").rstrip("\n")
        else:
            print("File Not Foud")
        return False

    def collect_custom(self,xxtype,time):    
        access_type = ["after"]
        self.cust_match = {}
        if (xxtype in access_type and stg.get('custom')):

            for c_item in stg.get('custom'):
                self.log.logstr(c_item)
                if(stg.get('custom')[c_item]['is_active'] == 1):
                    s=[]
                    if (int(stg.get('custom')[c_item]['time']) > 0):
                        time = int(stg.get('custom')[c_item]['time'])
                        
                        for x in range(time):
                            next_date = datetime.datetime.now() - datetime.timedelta(minutes=x)
                            s.append(next_date.strftime(stg.get('custom')[c_item]['dateformat']))
                    else:
                        today_date = datetime.datetime.now()
                        s.append(today_date.strftime(stg.get('custom')[c_item]['dateformat']))

                    cmd="grep -i \""+'\|'.join(s)+"\" "+stg.get('custom')[c_item]['file_path']
                    cmd=cmd+ " | "+stg.get('custom')[c_item]['after_cmd']

                    self.log.logstr(cmd)
                    output = subprocess.check_output(cmd, shell=True)
                    #convert output to utf-8 and remove \n from the last
                   
                    self.cust_match[c_item] =  str(output,"utf-8").rstrip("\n")

        return self.cust_match

    def check_service(self):    
        self.cust_match = {}
        if (stg.get('service')):
            for c_item in stg.get('service'):
                self.log.logstr(c_item)
                if(stg.get('service')[c_item]['is_active'] == 1):
                    
                    cmd="service "+stg.get('service')[c_item]['system_name'] +" status "
                    cmd=cmd+ " | grep 'Active:' | grep "+stg.get('service')[c_item]['match'] +" | wc -l "

                    self.log.logstr(cmd)
                    output = subprocess.check_output(cmd, shell=True)
                    #convert output to utf-8 and remove \n from the last
                   
                    self.cust_match[c_item] =  str(output,"utf-8").rstrip("\n")

        return self.cust_match

    def exe_command(self):    
        self.cust_match = {}
        if (stg.get('command')):
            for c_item in stg.get('command'):
                self.log.logstr(c_item)
                if(stg.get('command')[c_item]['is_active'] == 1):
                    cmd=stg.get('command')[c_item]['commstr']
                    self.log.logstr(str(cmd))
                    output = subprocess.check_output(cmd, shell=True)
                    #convert output to utf-8 and remove \n from the last
                    self.cust_match[c_item] =  str(output,"utf-8").rstrip("\n")

        return self.cust_match    