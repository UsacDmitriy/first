import requests

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
response = requests.get(url, headers={'Accept': 'application/json'}, params={
    'format': 'geojson',
    'starttime': '2014-01-01',
    'endtime': '2014-01-02',
    'minmagnitude': '5'
})

# print(response.json())

data = response.json()
print(data['features'][1]['properties']['place'])