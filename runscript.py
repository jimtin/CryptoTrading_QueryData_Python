import binanceAPIlibrary
import splunkdestination
import coinbaselibrary
from pathlib import Path
import json
import datetime
from time import sleep


# Script which runs data gathering
def main(SettingsFilePath, sleeptime=120, runfromcron=True):
    # Turn the settings filepath into a Path object
    settings = Path(SettingsFilePath)
    # Settings format should be JSON
    # Load splunk settings into program
    f = open(settings)
    splunksettings = f.read()
    splunksettings = json.loads(splunksettings)
    splunksettings = splunksettings["SplunkSettings"]
    if runfromcron == True:
        getdata(splunksettings)
    else:
        while 1:
            getdata(splunksettings)
            # Now sleep till next query
            print("Sleeping for " + str(sleeptime) + " seconds")
            sleep(sleeptime)

def getdata(splunksettings):
    # Get binance data
    print("Getting binance data " + str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
    binancedata = binanceAPIlibrary.getpricechanges()
    # Send to Splunk
    splunkdestination.sendtosplunk(binancedata, "binance", splunksettings)
    # Get CoinbaseData
    print("Getting coinbase data " + str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
    coinbasedata = coinbaselibrary.combinespotprices()
    splunkdestination.sendtosplunk(coinbasedata, "coinbase", splunksettings)


