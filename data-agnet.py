#!/usr/bin/env python3
import sys
import argparse
import json
import os
from collector import *
from functions import *

parser = argparse.ArgumentParser(description='some description here')
parser.add_argument('-v',"--version", help="get version", action="store_true")
parser.add_argument('-vv',"--verbose", help="increase output verbosity",action="store_true")
parser.add_argument('-m',"--memory", help="get memory infomation", action="store_true")
parser.add_argument('-c',"--cpu", help="get cpu infomation", action="store_true")
parser.add_argument('-x2',"--twoxx", help="get 2xx count from last [N] time",type=int)
parser.add_argument('-x3',"--threexx", help="get 3xx count from last [N] time",type=int)
parser.add_argument('-x4',"--fourxx", help="get 4xx count from last [N] time",type=int)
parser.add_argument('-x5',"--fivexx", help="get 5xx count from last [N] time",type=int)
parser.add_argument('-timeC',"--timeConsuming", help="get time consuming request count from last [N] time",type=int)
parser.add_argument('-gRx',"--gRegex", help="run grep with E (regex)",type=int)
parser.add_argument('-phpN',"--phpNotice", help="get notice count from last [N] time",type=int)
parser.add_argument('-phpW',"--phpWarning", help="get warning count from last [N] time",type=int)
parser.add_argument('-phpE',"--phpError", help="get error count from last [N] time",type=int)

parser.add_argument('-mat',"--match", help="get idex count from last [N] time",type=int)
parser.add_argument('-ip',"--ipcount", help="get idex count from last [N] time",type=int)
parser.add_argument('-fi',"--find", help="find the match text works with mat")
parser.add_argument('-co',"--command", help="execute command")
##parser.add_argument('-x5',"--fivexx", help="get memory infomation",nargs='?',type=int)
#parser.add_argument('-x4',"--fourxx", help="get memory infomation",action="store_true")


args = parser.parse_args()
time=5 
#print(args)
verbose(args,'1')

# agnet version information
if (args.version):
	print("v1.0")

#System Memory Details
if (args.memory):
        #print("memory")
        os.system('free -m')

#System CPU
if (args.cpu):
        print("cpu")

# linux/ubuntu command execution
# sample: 
if (args.command):
	cmd=args.command	
	verbose(args,cmd)
	os.system(cmd)

# get 4xx count from last [N] time as per settings.default is 5
# sample: python3 sample.py -x4=10
if (args.fourxx):
	if (args.fourxx == 15):
		time=15
	elif (args.fourxx == 10):
		time=10
	else:
		time=5		
	collectxx("x4",time,args)

# get 5xx count from last [N] time as per settings.default is 5
# sample: python3 sample.py -x5=10	
if (args.fivexx):
	if (args.fivexx == 15):
		time=15
	elif (args.fivexx == 10):
		time=10
	else:
		time=5
	collectxx("x5",time,args)

# get 2xx count from last [N] time as per settings. default is 5
# sample: python3 sample.py -x2=10
if (args.twoxx):
	if (args.twoxx == 15):
		time=15
	elif (args.twoxx == 10):
		time=10
	else:
		time=5
	collectxx("x2",time,args)	

# get 3xx count from last [N] time as per settings. default is 5
# sample: python3 sample.py -x3=10
if (args.threexx):
	if (args.threexx == 15):
		time=15
	elif (args.threexx == 10):
		time=10
	else:
		time=5
	collectxx("x3",time,args)	

# get time consuming count from last [N] time as per settings.default is 5
# sample: python3 sample.py -timeC=10
if (args.timeConsuming):
	if (args.timeConsuming == 15):
		time=15
	elif (args.timeConsuming == 10):
		time=10
	else:
		time=5		
	collectxx("timeC",time,args)

# get time consuming count from last [N] time as per settings.default is 5
# sample: python3 sample.py -gRx=10
if (args.gRegex):
	if (args.gRegex == 15):
		time=15
	elif (args.gRegex == 10):
		time=10
	else:
		time=5		
	collectxx("gRx",time,args)

# String or pattern match from the file , defined in the settings.
# sample: python3 sample.py -mat=15 -fi=/index.php/ 
# How it works: the example will return the nuber of match 	"/index.php/" from the accesslog from last 15 minutes
if (args.match):
	if (args.match == 15):
		time=15
	elif (args.match == 10):
		time=10
	else:
		time=5
	collectxx("mat",time,args)

# String or pattern match from the file , defined in the settings.
# sample: python3 sample.py -mat=15 -fi=/index.php/ 
# How it works: the example will return the nuber of match 	"/index.php/" from the accesslog from last 15 minutes
if (args.ipcount):
	if (args.ipcount == 15):
		time=15
	elif (args.ipcount == 10):
		time=10
	else:
		time=5
	collectxx("ip",time,args)	

# last 15 minutes php Notice count from apache error log. as per settings.
# sample: python3 sample.py -phpN=15 
if (args.phpNotice):
	if (args.phpNotice == 15):
		time=15
	elif (args.phpNotice == 10):
		time=10
	else:
		time=5
	collectxx("phpN",time,args)	

# last 15 minutes php Warnings count from apache error log. as per settings.
# sample: python3 sample.py -phpW=15 
if (args.phpWarning):
	if (args.phpWarning == 15):
		time=15
	elif (args.phpWarning == 10):
		time=10
	else:
		time=5
	collectxx("phpW",time,args)

# last 15 minutes php Errors count from apache error log. as per settings.
# sample: python3 sample.py -phpE=15 	
if (args.phpError):
	if (args.phpError == 15):
		time=15
	elif (args.phpError == 10):
		time=10
	else:
		time=5
	collectxx("phpE",time,args)