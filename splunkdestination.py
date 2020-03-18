import socket
from time import sleep
import json
import datetime


# Function to send UDP data to splunk
def splunkudpsender(datatosend, splunksettings):
    # First, import splunk settings
    SplunkIP = splunksettings["SplunkIP"]
    SplunkPort = int(splunksettings["SplunkPort"])
    # Now convert the message to bytes
    MESSAGE = str.encode(datatosend)
    # Set up the socket to send (btw, how good is python)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Send datagram (UDP)
    sock.sendto(MESSAGE, (SplunkIP, SplunkPort))
    sock.close()
    sleep(0.01)


# Function to send data to Splunk and include the exchange it is from
def sendtosplunk(data, exchange, splunksettings):
    # Ensure the exchange is a string
    exchange = str(exchange)
    # Iterate through the data provided, adding in the exchange
    for crypto in data:
        # Add in the exchange
        # print(crypto)
        crypto.update({'exchange': exchange})
        crypto.update({'DateTime': str(datetime.datetime.now())})
        # Turn into json
        exchangedata = json.dumps(crypto)
        # Serialize the crypto object into a string
        exchangedata = str(exchangedata)
        # Now send joyfully to Splunk
        splunkudpsender(exchangedata, splunksettings)