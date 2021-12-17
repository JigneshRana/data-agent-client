import json

x = {
  "name": "Ken",
  "age": 45,
  "married": True,
  "children": ("Alice","Bob"),
  "pets": ['Dog'],
  "cars": [
    {"model": "Audi A1", "mpg": 15.1},
    {"model": "Zeep Compass", "mpg": 18.1}
  ]
}
# sorting result in asscending order by keys:
sorted_string = json.dumps(x, indent=4, sort_keys=True)
#print(sorted_string)

print("-"*100)
print("example - 2")

# json data string
person_data = '{  "person":  { "name":  "Kenn",  "sex":  "male",  "age":  28}}'
# Decoding or converting JSON format in dictionary using loads()
dict_obj = json.loads(person_data)
print(dict_obj)
# check type of dict_obj
print("Type of dict_obj", type(dict_obj))
# get human object details
print("Person......",  dict_obj.get('person'))

print("-"*100)
print("example - 3")

# json data string
person_data = '{ "name":  "Kenn",  "sex":  "male",  "age":  28}'
# Decoding or converting JSON format in dictionary using loads()
dict_obj = json.loads(person_data)
print(dict_obj)
# check type of dict_obj
print("Type of dict_obj", type(dict_obj))
# get human object details
print("Person......",  dict_obj['name'])

print("-"*100)
print("example - 4")

# json data string
person_data = '{"list":[{ "name":  "Kenn",  "sex":  "male",  "age":  28},{ "name":  "Kenny",  "sex":  "female",  "age":  18}]}'
# Decoding or converting JSON format in dictionary using loads()
dict_obj = json.loads(person_data)
print(dict_obj)
# check type of dict_obj
print("Type of dict_obj", type(dict_obj))
# get human object details
print("Person......",dict_obj.get('list')[1]['name'])

print("-"*100)
print("example - 5")

setting = {
    "time":10,
    "apache": {
        "accesslog_path":"/media/jignesh/Data/data-agent-client/samplelog/access.log",
        "errorlog_path":"/media/jignesh/Data/data-agent-client/samplelog/error.log",
        "accesslog_dateformat":"%d/%b/%Y:%H:%M",
        "errorlog_dateformat":"%d/%b/%Y:%H:%M",
        "2xx_match":"@@@2","3xx_match":"@@@3","4xx_match":"@@@4","5xx_match":"@@@5",
        "time_consuming":" @@[0-9][0-9][0-9]+",
        "regex_match":" @@[0-9][0-9][0-9]+"
    },
    "custome" :{
        "iplist_json1":{
            "is_active":1,
            "file_path":"/media/jignesh/Data/data-agent-client/samplelog/access.log",
            "time":"10",
            "after_cmd":'awk -F" " \'{if($2!="-") print $2}\' | sed \'s/"GET\|"POST\|,//g\' | sort -n | uniq -c | sort -nr | head -10 | awk -F" " \'{a= "\\""$2"\\":\\""$1"\\","a }END { print "{"substr (a,1,length(a)-1)"}" }\''
            },
        "iplist_json2":{
            "is_active":1,
            "file_path":"/media/jignesh/Data/data-agent-client/samplelog/access.log",
            "time":"10",
            "after_cmd":'awk -F" " \'{if($2!="-") print $2}\' | sed \'s/"GET\|"POST\|,//g\' | sort -n | uniq -c | sort -nr | head -10 | awk -F" " \'{a= "\\""$2"\\":\\""$1"\\","a }END { print "{"substr (a,1,length(a)-1)"}" }\''
            }    
    }

}

print("Found......",setting.get('apache')['accesslog_path'])
print(len(setting.get('custome').keys()))

print("-"*100)
print("example - 6")

# set of letters
GEEK = {'g', 'e', 'k'}
  
# adding 's'
GEEK.add('s')
print('Letters are:', GEEK)
  
# adding 's' again
GEEK.add('s')
print('Letters are:', GEEK)



print("-"*100)
print("example - 7")

print "Hello World!\n"

test = {} 

print("Current Dict is: ", test) 
    
# using the subscript notation 
# Dictionary_Name[New_Key_Name] = New_Key_Value 
  
test['key3'] = 'Geeks'
test['key4'] = 'is'
test['key5'] = 'portal'
test['key6'] = 'Computer'

print("Updated Dict is: ", test)