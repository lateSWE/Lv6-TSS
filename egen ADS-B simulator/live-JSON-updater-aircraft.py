import json
import time
import re

url = "temp.json"

def writeToJson(out):
    write_file = open(url, "w")
    json.dump(out, write_file)
    write_file.close()

choise = input("Do you want to enter the values manualy? It will fly in a circle around the given coordenates\n(Not recomended)[Y] or [N]: ")
if  choise == "Y" or choise == "y":
    Hex         = int(input("Hex: "), 16)
    Squawk      = float(input("Squawk: "))
    Flight      = float(input("Flight: "))
    ELat        = float(input("Lat: "))
    ELon        = float(input("Lon: "))
    #SeenPos     = float(input("SeenPos: "))
    Altitude    = float(input("Altitude: "))
    VertRate    = float(input("VertRate: "))
    Track       = float(input("Track: "))
    Speed       = float(input("Speed: "))
    Category    = float(input("Category: "))
    #Mlat        = float(input("Mlat: "))
    #Messages2   = float(input("Messages: "))
    Seen        = float(input("Seen: "))
    Rssi        = float(input("Rssi: "))
else:
    print("What premade flight dou you want to use?")
    print("1: circle around you")
    print("2: circle around given coordenates")
    choise = input("Starting number: ")
if(choise == 1):
    print("1")
elif(choise == 2):
    print("2")
else:
    print("ERROR, the number you enterd does not match up to any premade flight!")
    quit()
refreshRate = int(input("What refresh rate? "))

while True:

    #Lat = ELat+radius*cos(angle)
    #Lon = ELon+radius*sin(angle)




    Time = round(time.time(), 1)
    Messages1 = Messages2
    String = {
        'now':Time,
        'messages': Messages1,
        'aircraft': [
            {
                'hex': str(Hex),
                'squawk': str(Squawk),
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
                #'messages2': Messages,
                'seen': Seen,
                'rssi': Rssi
            }
        ]
    }
    writeToJson(String)
    time.sleep(refreshRate)
    print(String)
