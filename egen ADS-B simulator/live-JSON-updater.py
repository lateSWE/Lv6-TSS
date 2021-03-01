import json
import time
'''center = float(input("Center coordinate:        "))
distance = float(input("Distance from Center:     "))
flightHexNumber = hex(input("The flights HEX number:   "))
flightNumber = input("The flights number:       ")
'''

#Function to write dictionary to a .json file
def writeFile(flight):
    jsonString = json.dumps(flight)
    jsonFile = open("data.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()

num = 0
while True:
    if num >= 10:
        num = 1
    else:
        num = num + 1
    print(num)
    dictionary = {'a': num, 'b':num+10, 'c':num+100}
    writeFile(dictionary)
    time.sleep(1)

#dictionary = {'a': 10, 'c': 100}

