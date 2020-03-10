import json

jsonfile = './jobs.json'
with open(jsonfile) as data_file:
    jobs = json.load(data_file)

# response = requests.get()  # api call
# jobs = json.load(response.text)

for job in jobs:
    print(job['id'])
    print('==================================')
    print(job)
    print('==================================')
