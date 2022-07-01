import requests
url = 'https://diskuploader.mypowerdisk.com/v1/tp/info'
param = {'token':
'0HfKPq695PHOzNUq0sxX','rid':'5pdh8S','filename':'name_1'}
res = requests.post(url, json = param)
print(res.json())