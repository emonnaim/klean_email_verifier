import csv
import requests

template = lambda : {
    "record":None,
    "is_validformat":None,
    "is_freeesp":None,
    "is_disposable":None,
    "is_catchall":None,
    "is_exist":None,
    "is_greylisted":None,
    "is_spamtrap":None,
    "is_deliverable":None,
    "delivery_status":None,
    "is_error":None,
    "message":None,
    "status":None
}

url = "https://api.kleanmail.com/record_verification/api_record"

headers = {
  'api_key': 'api_key::<key>', # Your API KEY 
  'Content-Type': 'application/json'
}

with open('input_file.txt', 'r') as input_file, open('output_file.csv', 'w', newline='') as output_file:
    csv_reader = csv.reader(input_file)
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(list(template().keys()))
    for index, row in enumerate(csv_reader):
        data = template()
        email = row[0]
        data['record'] = email
        payload = {
            "record": email
        }
        response = requests.post(url, headers=headers, json=payload)
        response_json = response.json()
        for key in data.keys():
            data[key]=response_json[key]
        print(index+1, data)
        csv_writer.writerow(list(data. Values()))
