setting = {
    "debug":False,
    "time":10,
    "group":"App",
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
            },
        "pms_req_count":{
            "is_active":1,
            "file_path":"/home/saasfinal/logs/pms_interface_*.log",
            "dateformat":"%Y-%m-%d %H:%M",
            "time":"5", # 0 equal to current date time as per format.
            "after_cmd":' wc -l'
            },
        "pms_day_sum":{
            "is_active":1,
            "file_path":"/home/saasfinal/logs/pms_interface_*.log",
            "dateformat":"%Y-%m-%d %H:%M",
            "time":"5", # 0 equal to current date time as per format.
            "after_cmd":' awk -F"#" \'{D+=$8} END {print D}\''
            },
        "pms_wise_req":{
            "is_active":1,
            "file_path":"/home/saasfinal/logs/pms_interface_*.log",
            "dateformat":"%Y-%m-%d %H:%M",
            "time":"5", # 0 equal to current date time as per format.
            "after_cmd":' awk -F"#" \'{print $5}\' | sort -nr | uniq -c | sort -nr | awk -F" " \'{a= "\\""$2"\\":\\""$1"\\","a }END { print "{"substr (a,1,length(a)-1)"}" }\''
            },
        "pms_th_req_list_actions":{
            "is_active":1,
            "file_path":"/home/saasfinal/logs/pms_threshold_logs_*.log",
            "dateformat":"%Y-%m-%d %H:%M",
            "time":0, # 0 equal to current date time as per format.
            "after_cmd":' awk -F"#" \'{print $6}\' | sort -nr | uniq -c | sort -nr | awk -F" " \'{a= "\\""$2"\\":\\""$1"\\","a }END { print "{"substr (a,1,length(a)-1)"}" }\''
            },
        "pms_th_req_list_pms":{
            "is_active":1,
            "file_path":"/home/saasfinal/logs/pms_threshold_logs_*.log",
            "dateformat":"%Y-%m-%d %H:%M",
            "time":0, # 0 equal to current date time as per format.
            "after_cmd":' awk -F"#" \'{print $3}\' | sort -nr | uniq -c | sort -nr | awk -F" " \'{a= "\\""$2"\\":\\""$1"\\","a }END { print "{"substr (a,1,length(a)-1)"}" }\''
            },
        "pms_th_req_list_endpoint":{
            "is_active":1,
            "file_path":"/home/saasfinal/logs/pms_threshold_logs_*.log",
            "dateformat":"%Y-%m-%d %H:%M",
            "time":0, # 0 equal to current date time as per format.
            "after_cmd":' awk -F"#" \'{print $4}\' | sort -nr | uniq -c | sort -nr | awk -F" " \'{a= "\\""$2"\\":\\""$1"\\","a }END { print "{"substr (a,1,length(a)-1)"}" }\''
            },
        "pms_th_req_list_ip_gt_100":{
            "is_active":1,
            "file_path":"/home/saasfinal/logs/pms_threshold_logs_*.log",
            "dateformat":"%Y-%m-%d %H:%M",
            "time":5, # 0 equal to current date time as per format.
            "after_cmd":' awk -F"#" \'{print $5}\' | sort -nr | uniq -c | sort -nr | awk -F" " \'{if ($1 > 100) a= "\\""$2"\\":\\""$1"\\","a }END { print "{"substr (a,1,length(a)-1)"}" }\''
            },
        "pms_th_req_list_hc_gt_100":{
            "is_active":1,
            "file_path":"/home/saasfinal/logs/pms_threshold_logs_*.log",
            "dateformat":"%Y-%m-%d %H:%M",
            "time":5, # 0 equal to current date time as per format.
            "after_cmd":' awk -F"#" \'{print $7}\' | sort -nr | uniq -c | sort -nr | awk -F" " \'{if ($1 > 100) a= "\\""$2"\\":\\""$1"\\","a }END { print "{"substr (a,1,length(a)-1)"}" }\''
            },
        "pms_th_days_list_hc_gt_100":{ #last 5 miutes day sum per hotel 
            "is_active":1,
            "file_path":"/home/saasfinal/logs/pms_threshold_logs_*.log",
            "dateformat":"%Y-%m-%d %H:%M",
            "time":5, # 0 equal to current date time as per format.
            "after_cmd":' awk -F"#" \'{print $7}\' | sort -nr | uniq -c | sort -nr | awk -F" " \'{a[$2] +=int($1);}END {for (i in a) if(a[i]>100) print a[i],"",i}\' | sort -nr | awk -F" " \'{if ($1 > 100) a= "\\""$2"\\":\\""$1"\\","a }END { print "{"substr (a,1,length(a)-1)"}" }\''
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
            "tag":"apachectl"
            },
        "apachectl_requests_being_processed":{
            "is_active":1,
            "commstr":"apachectl status | grep 'requests currently being processed' | awk -F\" \" '{print int($1)}'",
            "tag":"apachectl"
            },
        "apachectl_idle_workers":{
            "is_active":1,
            "commstr":"apachectl status | grep 'requests currently being processed' | awk -F\" \" '{print int($6)}'",
            "tag":"apachectl"
            },
        "apachectl_req_count_sec":{
            "is_active":1,
            "commstr":"apachectl status | grep 'requests/sec' | awk -F\" \" '{print int($1)}'",
            "tag":"apachectl"
            },
        "apachectl_bite_sec":{
            "is_active":1,
            "commstr":"apachectl status | grep 'requests/sec' | awk -F\" \" '{print int($4)}'",
            "tag":"apachectl"
            },
        "apachectl_kb_per_req":{
            "is_active":1,
            "commstr":"apachectl status | grep 'requests/sec' | awk -F\" \" '{print int($7)}'",
            "tag":"apachectl"
            },
        "apachectl_ms_per_req":{
            "is_active":1,
            "commstr":"apachectl status | grep 'requests/sec' | awk -F\" \" '{print int($10)}'",
            "tag":"apachectl"
            },
        "ps_php":{
            "is_active":1,
            "commstr":"ps -auxw | grep '\.php' | grep -v 'grep' | wc -l",
            "tag":"ps_php"
            },
        "ps_sh":{
            "is_active":1,
            "commstr":"ps -auxw | grep '\.sh' | grep -v 'grep' | wc -l",
            "tag":"ps_sh"
            }
    }
}