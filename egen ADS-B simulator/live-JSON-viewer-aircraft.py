import json
import time
import re
'''
def readJson():
    fileObject = open("simple-aircraft.json", "r")
    jsonContent = fileObject.read()
    return(json.loads(jsonContent))

while True:
    readList = readJson()
    temp = "now: {}".format(readList["now"])
    print(temp)
    time.sleep(1)
'''
#loads the .json file
def readJson():
    url = "aircraft.json"
    f = open(url, 'r')
    return(f)
    f.close()

while True:
    data = json.load(readJson())
    Time        = data['now']
    Aircraft    = data['aircraft']
    AircraftLen = len(Aircraft)

    print("Amount of aircrafts: {}".format(str(AircraftLen)))
    print("Time is: {}\n".format(str(Time)))
    for i in range(0, AircraftLen):
        try:
            Hex         = data['aircraft'][i]['hex']        #
            Squawk      = data['aircraft'][i]['squawk']     #
            Flight      = data['aircraft'][i]['flight']     #
            Lat         = data['aircraft'][i]['lat']        #
            Long        = data['aircraft'][i]['lon']        #
            #SeenPos    = data['aircraft'][i]['seen_pos']
            Altitude    = data['aircraft'][i]['altitude']   #
            VertRate    = data['aircraft'][i]['vert_rate']  #
            Track       = data['aircraft'][i]['track']      #
            Speed       = data['aircraft'][i]['speed']      #
            Category    = data['aircraft'][i]['category']   #
            #MLat       = data['aircraft'][i]['mlat']
            #Seen       = data['aircraft'][i]['seen']
            Rssi        = data['aircraft'][i]['rssi']       #

            print("Aircraft number: {}".format(i+1))
            print("Hex: {}, Flight: {}, Squawk: {}, Track: {}, Category: {}, Rssi: {}".format(Hex, Flight, Squawk, Track, Category, Rssi))
            print("Latitude: {}, Longitude: {}, Speed: {}".format(Lat, Long, Speed))
            print("Altitude: {}, VertRate: {} \n".format(Altitude, VertRate))

        except:
            print("Aircraft number: {}".format(i+1))
            print("not correct data from .json file \n")

    time.sleep(1)




# formats the "aircraft" dictionary
# temp = re.sub("\[|{|}|\]", "", str(data['aircraft])).split(', ')