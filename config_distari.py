setting = {
    "debug":False,
    "time":10,
    "group":"Dist",
    "apache": {
        "accesslog_path":"/var/log/apache2/access.log",
        "errorlog_path":"/var/log/apache2/error.log",
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
            "file_path":"/var/log/apache2/access.log",
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
            },
        "dist_ticket_inflow_action":{ #last 5 miutes ticket table cound group by daemon|sync
            "is_active":1,
            "file_path":"/home/saasfinal/ebschannel/logs/channel_pending_tickets_db_statistics_*.log",
            "dateformat":"%Y-%m-%d %H:%M",
            "time":5, # 0 equal to current date time as per format.
            "after_cmd":' grep "updatetypehoteloperationwise" | awk -F"#" \'{print $3,$6}\' | awk -F" " \'{a[$1] +=int($2);}END{for (i in a)  print a[i],"",i}\' | awk -F" " \'{a= "\\""$2"\\":\\""$1"\\","a }END { print "{"substr (a,1,length(a)-1)"}" }\''
            },
        "dist_ticket_inflow_operation":{ #last 5 miutes ticket table cound group by operation
            "is_active":1,
            "file_path":"/home/saasfinal/ebschannel/logs/channel_pending_tickets_db_statistics_*.log",
            "dateformat":"%Y-%m-%d %H:%M",
            "time":5, # 0 equal to current date time as per format.
            "after_cmd":' grep "updatetypehoteloperationwise" | awk -F"#" \'{print $5,$6}\' | awk -F" " \'{a[$1] +=int($2);}END{for (i in a)  print a[i],"",i}\' | awk -F" " \'{a= "\\""$2"\\":\\""$1"\\","a }END { print "{"substr (a,1,length(a)-1)"}" }\''
            },
        "dist_ticket_inflow_usersource":{ #last 5 miutes ticket table cound group by operation
            "is_active":1,
            "file_path":"/home/saasfinal/ebschannel/logs/channel_pending_tickets_db_statistics_*.log",
            "dateformat":"%Y-%m-%d %H:%M",
            "time":5, # 0 equal to current date time as per format.
            "after_cmd":' grep "updatetypeuserwise" | awk -F"#" \'{print $4,$5}\' |  sort -nr | awk -F" " \'{a[$1] +=int($2);}END{for (i in a)  print a[i],"",i}\' | awk -F" " \'{a= "\\""$2"\\":\\""$1"\\","a }END { print "{"substr (a,1,length(a)-1)"}" }\''
            },
        "dist_ticket_inflow_hotel":{ #last 5 miutes ticket table cound group by operation
            "is_active":1,
            "file_path":"/home/saasfinal/ebschannel/logs/channel_pending_tickets_db_statistics_*.log",
            "dateformat":"%Y-%m-%d %H:%M",
            "time":5, # 0 equal to current date time as per format.
            "after_cmd":' grep "updatetypehoteloperationwise" | awk -F"#" \'{print $4,$6}\' |  sort -nr | awk -F" " \'{a[$1] +=int($2);}END{for (i in a)  print a[i],"",i}\' | awk -F" " \'{a= "\\""$2"\\":\\""$1"\\","a }END { print "{"substr (a,1,length(a)-1)"}" }\''
            },
        "dist_ticket_inflow_hotel_load":{ #last 5 miutes ticket table cound group by operation
            "is_active":1,
            "file_path":"/home/saasfinal/ebschannel/logs/channel_pending_tickets_db_statistics_*.log",
            "dateformat":"%Y-%m-%d %H:%M",
            "time":5, # 0 equal to current date time as per format.
            "after_cmd":' grep "updatetypehoteloperationwise" | awk -F"#" \'{print $4,$6}\' |  sort -nr | awk -F" " \'{a[$1] +=int($2);}END{for (i in a)  if(a[i]>500) print a[i],"",i}\' | awk -F" " \'{a= "\\""$2"\\":\\""$1"\\","a }END { print "{"substr (a,1,length(a)-1)"}" }\''
            },
        "dist_ticket_serialcount_inprocess":{ #Last five minute action vise serial count
            "is_active":1,
            "file_path":"/home/saasfinal/ebschannel/logs/channel_ticket_process_statistics_*.log",
            "dateformat":"%Y-%m-%d %H:%M",
            "time":5, # 0 equal to current date time as per format.
            "after_cmd":' grep "update_requested_by_user" | awk -F"#" \'{print $6,$7}\' |  sort -nr | awk -F" " \'{a[$1] +=int($2);}END{for (i in a)  print a[i],"",i}\' | awk -F" " \'{a= "\\""$2"\\":\\""$1"\\","a }END { print "{"substr (a,1,length(a)-1)"}" }\''
            },
        "dist_ticket_requested_by_user_inprocess":{ #Last 5 minute ticket requested by user
            "is_active":1,
            "file_path":"/home/saasfinal/ebschannel/logs/channel_ticket_process_statistics_*.log",
            "dateformat":"%Y-%m-%d %H:%M",
            "time":5, # 0 equal to current date time as per format.
            "after_cmd":' grep "update_requested_by_user" | awk -F"#" \'{print $6}\' | sort -nr | uniq -c | awk -F" " \'{a= "\\""$2"\\":\\""$1"\\","a }END { print "{"substr (a,1,length(a)-1)"}" }\''
            },
        "dist_ticket_xml_generated_by_feeder_inprocess":{ #Last 5 minute ticket generated by feeder
            "is_active":1,
            "file_path":"/home/saasfinal/ebschannel/logs/channel_ticket_process_statistics_*.log",
            "dateformat":"%Y-%m-%d %H:%M",
            "time":5, # 0 equal to current date time as per format.
            "after_cmd":' grep "ticket_generated_by_feeder" | awk -F"#" \'{print $6}\' | sort -nr | uniq -c | awk -F" " \'{a= "\\""$2"\\":\\""$1"\\","a }END { print "{"substr (a,1,length(a)-1)"}" }\''
            },
        "dist_ticket_count_ota":{ #Last 5 minute ticket picked  by OTA
            "is_active":1,
            "file_path":"/home/saasfinal/ebschannel/logs/channel_ticket_process_statistics_*.log",
            "dateformat":"%Y-%m-%d %H:%M",
            "time":5, # 0 equal to current date time as per format.
            "after_cmd":' grep "ticket_picked_by_channel" | awk -F"#" \'{print $4}\' | sort -nr | uniq -c | sort -nr |awk -F" " \'{a= "\\""$2"\\":\\""$1"\\","a }END { print "{"substr (a,1,length(a)-1)"}" }\''
            },
        "dist_ticket_xml_for_ota":{ #Last 5 minute xml  generated for OTA Format
            "is_active":1,
            "file_path":"/home/saasfinal/ebschannel/logs/channel_ticket_process_statistics_*.log",
            "dateformat":"%Y-%m-%d %H:%M",
            "time":5, # 0 equal to current date time as per format.
            "after_cmd":' grep "xml_generated_for_channel" | awk -F"#" \'{print $4}\' | sort -nr | uniq -c | sort -nr |awk -F" " \'{a= "\\""$2"\\":\\""$1"\\","a }END { print "{"substr (a,1,length(a)-1)"}" }\''
            },
        "dist_ticket_sent_to_ota":{ #Last 5 Min tickets sent to OTA
            "is_active":1,
            "file_path":"/home/saasfinal/ebschannel/logs/channel_ticket_process_statistics_*.log",
            "dateformat":"%Y-%m-%d %H:%M",
            "time":5, # 0 equal to current date time as per format.
            "after_cmd":' grep "xml_sent_to_channel" | awk -F"#" \'{print $4}\' | sort -nr | uniq -c | sort -nr |awk -F" " \'{a= "\\""$2"\\":\\""$1"\\","a }END { print "{"substr (a,1,length(a)-1)"}" }\''
            },
        "dist_ticket_sent_to_ota":{ #Last 5 Min tickets sent to OTA
            "is_active":1,
            "file_path":"/home/saasfinal/ebschannel/logs/channel_ticket_process_statistics_*.log",
            "dateformat":"%Y-%m-%d %H:%M",
            "time":55, # 0 equal to current date time as per format.
            "after_cmd":' grep "xml_sent_to_channel" | awk -F"#" \'{print $4}\' | sort -nr | uniq -c | sort -nr |awk -F" " \'{a= "\\""$2"\\":\\""$1"\\","a }END { print "{"substr (a,1,length(a)-1)"}" }\''
            },
        "dist_ticket_generate_latency":{ #Last 5 minute total tickts, total seconds , total serials picked by feeder
            "is_active":1,
            "file_path":"/home/saasfinal/ebschannel/logs/channel_ticket_process_statistics_*.log",
            "dateformat":"%Y-%m-%d %H:%M",
            "time":55, # 0 equal to current date time as per format.
            "after_cmd":' grep "ticket_generated_by_feeder"| awk -F"#" \'{a +=int($8);b+=1;c +=int($7);}END{ print "{\\"t_sec\\":\\""a"\\",\\"t_tics\\":\\""b"\\",\\"t_srs\\":\\""c"\\",\\"avg\\":\\""a/b"\\"}"}\''
            },
        "dist_ticket_process_latency":{ #Last 5 minute ticket request to ticket processed to ota
            "is_active":1,
            "file_path":"/home/saasfinal/ebschannel/logs/channel_ticket_process_statistics_*.log",
            "dateformat":"%Y-%m-%d %H:%M",
            "time":55, # 0 equal to current date time as per format.
            "after_cmd":' grep "ticket_generated_by_feeder\|xml_sent_to_channel" | awk -F"#" \'{print $3,$7,$4}\' | sort -nr | awk -F" " \'{a[$1] +=int($2);}END{for (i in a)  print a[i],i}\' | awk -F" " \'{a +=int($1);b +=1}END{ print "{\\"t_sec\\":\\""a"\\",\\"t_tics\\":\\""b"\\"}"}\''
            }

    }
}