import json
import collections
import wiotp.sdk.device
import time
myConfig = {
    "identity" : {
        "orgId" :"mcf86g",
        "typeId" : "Child_Location",
        "deviceId" : "childlocation"
    },
    "auth":{
        "token":"12345678"
        }
}

client = wiotp.sdk.device.DeviceClient(config=myConfig ,logHandlers=None)
client.connect()
while True:
    name = "Trichy"
    #child is in school(SARANATHAN)
    latitude = 10.7560
    longitude = 78.6513
    
    #child is in playground(SWAMIMALAI)
    #latitude = 10.9569
    #longitude = 79.3260
    
    #out of the network(JAMMU & KASHMIR)
    #latitude = 32.7266
    #longitude = 74.8570

    #child is in home(TANJORE)
    #latitude = 10.7828
    #longitude = 79.1318
    myData = {'latitude' :latitude, 'longitude':longitude}
    client.publishEvent(eventId="status",msgFormat="json",data=myData,qos=0,onPublish=None)
    print("Data published to IBM IoT platform : ",myData)
    time.sleep(20)
client.disconnect()
    

        
