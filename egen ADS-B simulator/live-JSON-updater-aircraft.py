import json
import time
import re

url = "temp.json"

def writeToJson(out):
    write_file = open(url, "w")
    json.dump(out, write_file)
    write_file.close()


while True:
    Time = round(time.time(), 1)
    Messages = 200
    Hex = 500

    String = {
        'now':Time,
        'messages': Messages,
        'aircraft': [
            {
                'hex': str(Hex),
                'squawk': str(Wquawk),
                'flight': str(Flight),
                'lat': Lat,
                'lon': Lon,
                #'seen_pos': SeenPos,
                'altitude': Altitude,
                'vert_rate': VertRate,
                'track': Track,
                'speed': Speed,
                'category': str(Category),
                #'mlat': Mlat,
                #'messages': Messages,
                'seen': Seen,
                'rssi': Rssi
            }
        ]
    }

print(String)
writeToJson(String)
