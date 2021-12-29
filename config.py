setting = {
    "time":10,
    "apache": {
        "accesslog_path":"/home/logdrive/apache2/access.log",
        "errorlog_path":"/home/logdrive/apache2/error.log",
        "accesslog_dateformat":"%d/%b/%Y:%H:%M",
        "errorlog_dateformat":"%a %b %d %H:%M",
        "2xx_match":"@@@2","3xx_match":"@@@3","4xx_match":"@@@4","5xx_match":"@@@5",
        "time_consuming":" @@[0-9][0-9][0-9]+",
        "regex_match":" @@[0-9][0-9][0-9]+",
        "phpN":"php7:notice",
        "phpW":"php7:warn",
        "phpE":"php7:error"
    },
    "custom" :{
        "access_count_ip_top10":{
            "is_active":1,
            "file_path":"/home/logdrive/apache2/access.log",
            "dateformat":"%d/%b/%Y:%H:%M",
            "time":"10", # 0 equal to current date time as per format.
            "after_cmd":'awk -F" " \'{if($2!="-") print $2}\' | sed \'s/"GET\|"POST\|,//g\' | sort -n | uniq -c | sort -nr | head -10 | awk -F" " \'{a= "\\""$2"\\":\\""$1"\\","a }END { print "{"substr (a,1,length(a)-1)"}" }\''
            }        
    },
    "service" :{
        "dsagent":{
            "is_active":1,
            "system_name":"ds_agent",
            "match":"running",
            },
        "apache":{
            "is_active":1,
            "system_name":"apache2",
            "match":"running",
            },
        "tdagent":{
            "is_active":1,
            "system_name":"td-agent",
            "match":"running",
            },
    },
    "command" :{
        "apachectl_totaltraffic_mb":{
            "is_active":1,
            "commstr":"apachectl status | grep 'Total Traffic:' | awk -F\" \" '{print $7}'",
            },
        "apachectl_requests_being_processed":{
            "is_active":1,
            "commstr":"apachectl status | grep 'requests currently being processed' | awk -F\" \" '{print int($1)}'",
            },
        "apachectl_idle_workers":{
            "is_active":1,
            "commstr":"apachectl status | grep 'requests currently being processed' | awk -F\" \" '{print int($6)}'",
            },
        "apachectl_req_count_sec":{
            "is_active":1,
            "commstr":"apachectl status | grep 'requests/sec' | awk -F\" \" '{print int($1)}'",
            },
        "apachectl_bite_sec":{
            "is_active":1,
            "commstr":"apachectl status | grep 'requests/sec' | awk -F\" \" '{print int($4)}'",
            },
        "apachectl_kb_per_req":{
            "is_active":1,
            "commstr":"apachectl status | grep 'requests/sec' | awk -F\" \" '{print int($7)}'",
            },
        "apachectl_ms_per_req":{
            "is_active":1,
            "commstr":"apachectl status | grep 'requests/sec' | awk -F\" \" '{print int($10)}'",
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