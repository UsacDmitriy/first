import requests
import sqlite3

def save_earthquakes(place_magnitude_list):
    conn = sqlite3.connect('earthquakes_db.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE earthquakes (place TEXT, magnitude REAL)")
    cursor.executemany("INSERT INTO earthquakes VALUES (?, ?)", place_magnitude_list)
    conn.commit()
    conn.close()

def select_all_quakes():
    conn = sqlite3.connect('earthquakes_db.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM earthquakes")
    data = cursor.fetchall()
    [print(row) for row in data]
    conn.commit()
    conn.close()


# url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
#
# response = requests.get(url, headers={'Accept': 'application/json'}, params={
#     'format': 'geojson',
#     'starttime': '2014-01-01',
#     'endtime': '2014-01-02',
#     'minmagnitude': '5'
# })
#
# data = response.json()
#
# earthquake_list = data['features']
# place_magnitude_list = []
# for i in earthquake_list:
#     place_magnitude_list.append((i['properties']['place'], i['properties']['mag']))
#
#
# print(place_magnitude_list)
# save_earthquakes(place_magnitude_list)

select_all_quakes()