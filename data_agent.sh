#!/bin/bash
#move this file to /home/ubuntu/script/

if ! ps auxww | grep -v grep | grep "python3 ./appclient.py 10.0.1.75 65432 get all"
then
	cd /home/ubuntu/data-agent-client/
	python3 ./appclient.py 10.0.1.75 65432 get all
fi;