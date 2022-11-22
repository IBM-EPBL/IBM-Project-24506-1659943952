import json
import collections
import wiotp.sdk.device
import time
myConfig = {
    "identity" :{
        "orgId" :"ylse17",
        "typeId" : "Android",
        "deviceId" : "ylse17"
    },
    "auth":{
        "token":"WORLDSpretty@1811"
        }
}

client = wiotp.sdk.device.DeviceClient(config=myConfig ,logHandlers=None)
client.connect()
while True:
    name = "salem"
    #child is in safe(Salem)
    #latitude = 11.664325
    #ongitude = 78.146011
    
    #child is in playing area(Coimbatore)
    latitude = 11.004556
    longitude = 76.961632

    #child in school(Chennai)
    #latitude = 13.067439
    #ongitude = 80.237617

    
    myData = {'latitude' :latitude, 'longitude':longitude}
    client.publishEvent(eventId="status",msgFormat="json",data=myData,qos=0,onPublish=None)
    print("Data published to IBM IoT platform : ",myData)
    time.sleep(20)
client.disconnect()
    

        
