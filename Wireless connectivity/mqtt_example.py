import network
import socket
from time import sleep
import machine
from umqtt.simple import MQTTClient
import random

# temp sensor
import ahtx0
from machine import Pin ,I2C



import wificonnect
print("Connected to Wifi.")

i2c = I2C(1,scl =Pin(15),sda = Pin(14))
sensor = ahtx0.AHT10(i2c)

mqtt_server = 'io.adafruit.com'
mqtt_port = 1883 # non-SSL port   ,try ssl in future
mqtt_user = 'evahns' #Adafruit ID
mqtt_password = 'aio_kAzg24oRB6ZemXyDriZ3oWr2pors' # Under Keys
mqtt_topic = 'evahns/feeds/temp' # Under "Feed info"
# mqtt_topic = 'evahns/dashboards/temp'
mqtt_client_id = str(random.randint(10000,999999)) #must have a unique ID - good enough for now

event_index = 0
def mqtt_connect():
    client = MQTTClient(client_id=mqtt_client_id, server=mqtt_server, port=mqtt_port, user=mqtt_user, password=mqtt_password, keepalive=3600)
    client.connect()
    print('Connected to %s MQTT Broker'%(mqtt_server))
    return client

def reconnect():
    print('Failed to connect to the MQTT Broker. Reconnecting...')
    time.sleep(5)
    reset()

try:
    client = mqtt_connect()
except OSError as e:
    reconnect()
    
while True:
    Temperature = str(round(sensor.temperature, 1)) # The server works on strings
    humidity =str(round(sensor.relative_humidity , 1))
    wlan = network.WLAN(network.STA_IF) #to  be noted ,, 
    if wlan.isconnected():
#     print(sensor.temperature) #Temperature
        client.publish(mqtt_topic,humidity)
#         client.publish(mqtt_topic,Temperature)
        event_index = event_index + 1
        print(f'''Number of data packets sent {event_index}
                                                           ''')
#         print("Latest Temp value: " + Temperature)
        print("Latest Humidity value: " + humidity)
       # client.publish(mqtt_topic, '34')
    else:
        reconnect()
    sleep(2)