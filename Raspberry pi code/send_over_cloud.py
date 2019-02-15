#!/usr/bin/env python
         
     
import time
import serial
import re
import pymongo
from datetime import datetime 
from pymongo import MongoClient


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
    data_to_entry = {"date" : d, "time" : t,  "temperature": entryList[0], "humidity" : entryList[1]}
    idid = collection.insert_one(data_to_entry).inserted_id
    print(idid)

# check whether the serial frame is valid or not
def isValidFrame(frame):
    pat = re.compile(b'T = [0-9][0-9]\.[0-9] deg\. C\, H = [0-9][0-9]\.[0-9]\%\r\n')
    jj = pat.match(frame)
    if (jj != None):
        return 1
    else:
        return 0

# parse temperature and humidity from serial frame        
def deriveTnH(frame):
    brokenframe = str(frame).split(' ')
    temp = float(brokenframe[2])
    humidity = float(brokenframe[-1][0:3])
    return [temp, humidity]          
      
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
    )

uri = "mongodb://redwan1006066:14243444redwan@ds125602.mlab.com:25602/redwan-uga-spr2019-data"
database = connectDB(uri)

while 1:
    x=ser.readline()
    if (len(x) != 0 and isValidFrame(x) == 1):
        print(deriveTnH(x))
        addEntry(returnCollection(database), deriveTnH(x))
        


