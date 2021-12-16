debug=True
options={"x4":{"A":"/media/jignesh/Data/Script/pycommander/samplelog/access.log","B":"%d/%b/%Y:%H:%M","M1":"@@@4"},
"x5":{"A":"/media/jignesh/Data/Script/pycommander/samplelog/access.log","B":"%d/%b/%Y:%H:%M","M1":"@@@5"},
"x2":{"A":"/media/jignesh/Data/Script/pycommander/samplelog/access.log","B":"%d/%b/%Y:%H:%M","M1":"@@@2"},
"x3":{"A":"/media/jignesh/Data/Script/pycommander/samplelog/access.log","B":"%d/%b/%Y:%H:%M","M1":"@@@3"},
"timeC":{"A":"/media/jignesh/Data/Script/pycommander/samplelog/access.log","B":"%d/%b/%Y:%H:%M","Reg":" @@[0-9][0-9][0-9]+"},
"gRx":{"A":"/media/jignesh/Data/Script/pycommander/samplelog/access.log","B":"%d/%b/%Y:%H:%M","Reg":" @@[0-9][0-9][0-9]+/"},
"ip":{"A":"/media/jignesh/Data/Script/pycommander/samplelog/access.log","B":"%d/%b/%Y:%H:%M","awk":'awk -F" " \'{if($2!="-") print $2}\' | sed \'s/"GET\|"POST\|,//g\' | sort -n | uniq -c | sort -nr | head -10 | awk -F" " \'{a= "\\""$2"\\":\\""$1"\\","a }END { print "{"substr (a,1,length(a)-1)"}" }\''},
"mat":{"A":"/media/jignesh/Data/Script/pycommander/samplelog/access.log","B":"%d/%b/%Y:%H:%M"},
"phpN":{"A":"/home/logdrive/apache2/error.log","B":"%d/%b/%Y:%H:%M","M1":"php7:notice"},
"phpW":{"A":"/home/logdrive/apache2/error.log","B":"%d/%b/%Y:%H:%M","M1":"php7:warn"},
"phpE":{"A":"/home/logdrive/apache2/error.log","B":"%d/%b/%Y:%H:%M","M1":"php7:errors"},
}