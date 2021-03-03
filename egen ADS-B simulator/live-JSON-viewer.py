import json
import time

def readJson():
    fileObject = open("temp.json", "r")
    jsonContent = fileObject.read()
    return(json.loads(jsonContent))

while True:
    readList = readJson()
    print("a: " + str(readList['a']) + ", b: " + str(readList['b']) + ", c: " + str(readList['c']))
    time.sleep(1)

