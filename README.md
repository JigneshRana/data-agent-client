# data-agent
The data agent is a python3 base command tool, which executes Linux commands on a timely base which can be further used for statistics. In the sample demonstration, it collects all meaning full information which requires for the webserver monitoring team.

## Settings.py
data-agent works with your configuration only. It generates logs under /debuglog/debug_date.log. This helps to debug and check more details.

```
debug=True
```

### settings
```
options={"x4":{"A":"/media/jignesh/Data/Script/pycommander/samplelog/access.log","B":"%d/%b/%Y:%H:%M","M1":"@@@4"},
```
x4 = Option to collect 4xx count fomr the given file
A = Filetoscan
B = DateFormat
M1 = Match Pattern

```
"gRx":{"A":"/media/jignesh/Data/Script/pycommander/samplelog/access.log","B":"%d/%b/%Y:%H:%M","Reg":" @@[0-9][0-9][0-9]+/"},
```
gRx = Option to perorm regex with grep -E 
A = Filetoscan
B = DateFormat
Reg = Match Pattern

### php warning,Notice,Error 

settings
```
"phpN":{"A":"/home/logdrive/apache2/error.log","B":"%d/%b/%Y:%H:%M","M1":"php7:notice"},
"phpW":{"A":"/home/logdrive/apache2/error.log","B":"%d/%b/%Y:%H:%M","M1":"php7:warn"},
"phpE":{"A":"/home/logdrive/apache2/error.log","B":"%d/%b/%Y:%H:%M","M1":"php7:errors"},
```

# PHP Notice from last 15 minutes log
```
python3 data-agnet.py -phpN=15
```

# PHP Warning from last 10 minutes log
```
python3 data-agnet.py -phpW=10
```

# PHP Errors from last 10 minutes log
```
python3 data-agnet.py -phpE=15
```

## Apache Details

### Apache request count 2XX,3XX,4XX,5XX
```
python3 data-agnet.py -x2=10
python3 data-agnet.py -x3=10
python3 data-agnet.py -x4=10
python3 data-agnet.py -x5=10

#Apache Time consuming request count(taking more than 100 seconds) from last 10
python3 commander.py -timeC=10

# Total accesses: [eg:123817744]
pachectl status | grep 'Total accesses:' | awk -F" " '{print $3}'

# Total Traffic: in gb [eg: 765.4 GB]
apachectl status | grep 'Total Traffic:' | awk -F" " '{print $7,$8}'

# [N1] requests currently being processed, [N2] idle workers
apachectl status | grep 'requests currently being processed' | awk -F" " '{print $1,$6}'

# [N1] requests/sec - [N2] kB/second - [N3] kB/request - [N4] ms/request
apachectl status | grep 'requests/sec' | awk -F" " '{print $1,$4,$7,$10}'

# last 10 top Ips in list
grep "24/Nov/2021:06:27" /home/logdrive/apache2/access.log | awk -F" " '{if($2!="-") print $2}' | sed 's/"GET\|"POST\|,//g' | sort -n | uniq -c | sort -nr | head -10 

# last 10 top Ips in json
grep "24/Nov/2021:06:27" /home/logdrive/apache2/access.log | awk -F" " '{if($2!="-") print $2}' | sed 's/"GET\|"POST\|,//g' | sort -n | uniq -c | sort -nr | head -10 | awk -F" " '{a= "\""$2"\":\""$1"\","a }END { print "{"substr (a,1,length(a)-1)"}" }'

# last [N] minutes top 10 Ips
python3 commander.py -ip=10

```



## Custome linux command
```
# apache service running or not running
python3 data-agnet.py -co="service apache2 status | grep Active: | grep running | wc -l"

# ds_agent service running or not running
python3 data-agnet.py -co="service ds_agent status | grep Active: | grep running | wc -1"

# td_agent service running or not running, 1 = running 0 = not running
python3 data-agnet.py -co="service td-agent status | grep Active: | grep running | wc -1"

# Number of service process running
python3 data-agnet.py -co="ps -auxw | grep "\.php " | grep -v grep  | wc -l"

# count php processes
ps -auxw | grep "\.php " | grep -v grep  | wc -l

# count shell script processes
ps -auxw | grep "\.sh" | grep -v grep | wc -l

```