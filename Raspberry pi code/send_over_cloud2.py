#!/usr/bin/env python
         
     
import time
import serial
import re
import pymongo
import json
from datetime import datetime 
from pymongo import MongoClient
from godirect import GoDirect


# connect to database
def connectDB(uri):
    client = MongoClient(uri)
    database = client['redwan-uga-spr2019-data'] #hardcoded database name
    return database

# connect to collection
def returnCollection(database):
    collection = database['envdata'] #hardcoded collection name
    return collection 

# add entry to collection
def addEntry(collection, entryList):
    d = datetime.now().date().strftime("%d-%m-%Y")
    t = datetime.now().time().strftime("%H-%M-%S")
    data_to_entry = {"date" : d, "time" : t,  "salinity": entryList[0], "moisture" : entryList[1], "potential" : entryList[2], "pH" : entryList[3]}
    idid = collection.insert_one(data_to_entry).inserted_id
    print(idid)
    
# check whether the serial JSON is valid or not
def isValidJSON(json_string):
    try:
        json.loads(json_string)
        return True
    except ValueError as e:
        return False 
    
# parse salinity and moisture from serial JSON       
def deriveResults(results_JSON):
    JSON_dict = json.loads(results_JSON)
    salinity = float(JSON_dict["Salinity"])
    moisture = float(JSON_dict["SoilMoisture"])
    potential = float(JSON_dict["Potential"])
    pH = float(JSON_dict["pH"])
    return [salinity, moisture, potential, pH]

def combine(analog_JSON, digital_JSON):
    analog_dict = json.loads(analog_JSON)
    digital_dict = json.loads(digital_JSON)
    results_dict = {}
    for k,v in analog_dict.items():
        results_dict[k] = v
    for k,v in digital_dict.items():
        results_dict[k] = v
    return json.dumps(results_dict)


ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
    )

godirect = GoDirect()
devices = godirect.list_devices()

uri = "mongodb://sdvickers98:Dakota#32@cluster0-shard-00-00-5kbmb.mongodb.net:27017,cluster0-shard-00-01-5kbmb.mongodb.net:27017,cluster0-shard-00-02-5kbmb.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true"
database = connectDB(uri)

while 1:
    analog_JSON = ser.readline().decode('utf-8')[:-2] # getting JSON of analog sensor data from arduino
    if isValidJSON(analog_JSON):    
        digital_JSON = '{'
        for dev in devices: # assembles JSON of digital sensor data
            dev.open(auto_start=True)
            sensors = dev.get_enabled_sensors()
            if dev.read():
                for sensor in sensors:
                    digital_JSON += str('"')
                    digital_JSON += sensor.sensor_description
                    digital_JSON += str('":')
                    digital_JSON += "{0:.3f}".format(sensor.value)
                    digital_JSON += str(',')
            dev.stop()
            dev.close()
        digital_JSON = digital_JSON[:-1] + str('}')
        results_JSON = combine(analog_JSON, digital_JSON)
        print(deriveResults(results_JSON))
        addEntry(returnCollection(database), deriveResults(results_JSON))
    
godirect.quit()    