setting = {
    "time":10,
    "apache": {
        "accesslog_path":"/media/jignesh/Data/data-agent-client/samplelog/access.log",
        "errorlog_path":"/media/jignesh/Data/data-agent-client/samplelog/error.log",
        "accesslog_dateformat":"%d/%b/%Y:%H:%M",
        "errorlog_dateformat":"%d/%b/%Y:%H:%M",
        "2xx_match":"@@@2","3xx_match":"@@@3","4xx_match":"@@@4","5xx_match":"@@@5",
        "time_consuming":" @@[0-9][0-9][0-9]+",
        "regex_match":" @@[0-9][0-9][0-9]+",
        "phpN":"php7:notice",
        "phpW":"php7:warn",
        "phpE":"php7:errors"
    },
    "custom" :{
        "iplist_json1":{
            "is_active":1,
            "file_path":"/media/jignesh/Data/data-agent-client/samplelog/access.log",
            "dateformat":"%d/%b/%Y:%H:%M",
            "time":"10",
            "after_cmd":'awk -F" " \'{if($2!="-") print $2}\' | sed \'s/"GET\|"POST\|,//g\' | sort -n | uniq -c | sort -nr | head -10 | awk -F" " \'{a= "\\""$2"\\":\\""$1"\\","a }END { print "{"substr (a,1,length(a)-1)"}" }\''
            },
        "iplist_json2":{
            "is_active":1,
            "file_path":"/media/jignesh/Data/data-agent-client/samplelog/access.log",
            "dateformat":"%d/%b/%Y",
            "time":"0", # 0 equal to current date time as per format.
            "after_cmd":'awk -F" " \'{if($2!="-") print $2}\' | sed \'s/"GET\|"POST\|,//g\' | sort -n | uniq -c | sort -nr | head -10 | awk -F" " \'{a= "\\""$2"\\":\\""$1"\\","a }END { print "{"substr (a,1,length(a)-1)"}" }\''
            }
    },
    "service" :{
        "dsagent":{
            "is_active":0,
            "system_name":"ds_agent",
            "match":"running",
            },
        "apache":{
            "is_active":0,
            "system_name":"apache2",
            "match":"running",
            },
        "tdagent":{
            "is_active":0,
            "system_name":"td-agent",
            "match":"running",
            },
    },
    "command" :{
        "apachectl_totaltraffic":{
            "is_active":0,
            "commstr":"apachectl status | grep 'Total Traffic:' | awk -F" " '{print $7,$8}'",
            },
        "apachectl_requests_being_processed":{
            "is_active":0,
            "commstr":"apachectl status | grep 'requests currently being processed' | awk -F" " '{print $1}'",
            },
        "apachectl_idle_workers":{
            "is_active":0,
            "commstr":"apachectl status | grep 'requests currently being processed' | awk -F" " '{print $6}'",
            },
        "apachectl_req_sec":{
            "is_active":0,
            "commstr":"apachectl status | grep 'requests/sec' | awk -F" " '{print $1}'",
            },
        "apachectl_kb_sec":{
            "is_active":0,
            "commstr":"apachectl status | grep 'requests/sec' | awk -F" " '{print $4}'",
            },
        "apachectl_kb_req":{
            "is_active":0,
            "commstr":"apachectl status | grep 'requests/sec' | awk -F" " '{print $7}'",
            },
        "apachectl_ms_req":{
            "is_active":0,
            "commstr":"apachectl status | grep 'requests/sec' | awk -F" " '{print $10}'",
            },            
        "ps_php":{
            "is_active":1,
            "commstr":"ps -auxw | grep '\.php' | grep -v 'grep' | wc -l",
            },
        "ps_sh":{
            "is_active":1,
            "commstr":"ps -auxw | grep '\.sh' | grep -v 'grep' | wc -l",
            }
    }
}


