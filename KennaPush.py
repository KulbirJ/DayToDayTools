// For bulk data push to Kenna Tools, data must be stored in C:/Users/somedirectory/ 


import os
import requests
import json
import time

connector_id = 152611
headers = {
    'X-Risk-Token': 'YourKennaApiKey',
}

for file in os.listdir('C:/Users/somedirectory/'):
    print(file)
    files = {
        'file': (file, open('C:/Users/somedirectory/' + file, 'rb')),
    }

    response = requests.post('https://api.kennasecurity.com/connectors/' + str(connector_id) + '/data_file',
                             headers=headers, files=files)
    print(response.text)

    success = "false"
    while success != "true":
        response = requests.get('https://api.kennasecurity.com/connectors/' + str(connector_id) + '/run',
                                headers=headers)
        print(response.text)
        success = json.loads(response.text)["success"]
        time.sleep(70)
