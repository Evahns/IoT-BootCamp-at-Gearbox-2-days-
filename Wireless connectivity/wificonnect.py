import network
import socket
from time import sleep
import machine

# ssid = 'Gearbox Members'
# password = 'Members@Gearbox'
ssid = 'Tenda-353B20'
password = '4263jones'

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    print(wlan.ifconfig())

try:
    connect()
except KeyboardInterrupt:
    machine.reset()