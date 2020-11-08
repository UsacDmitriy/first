import requests

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'

response = requests.get(url, headers={'Accept': 'application/json'}, params={
    'format': 'geojson',
    'starttime': '2014-01-01',
    'endtime': '2014-01-02',
    'minmagnitude': '5'
})

data = response.json()

earthquake_list = data['features']
count = 0
for i in earthquake_list:
    print()