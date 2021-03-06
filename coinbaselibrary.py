import requests
import json
from time import sleep
import splunkdestination

# Library to get basic prices from coinbase


def getspotpricecoinbase(currencypair):
    # Turn the currency pair into a string just in case it wasn't already
    currencypairstring = str(currencypair)
    # Setup the apirequest
    apirequest = "https://api.coinbase.com/v2/prices/" + currencypairstring + "/spot"
    # Now setup the session
    session = requests.session()
    information = session.get(apirequest)
    # Convert into json
    return information.text


# Get the BTC spot price
def getbtcspotprice():
    # Get the spotprice
    btcspotprice = getspotpricecoinbase("BTC-USD")
    # Serialize into JSON
    btcspotprice = json.loads(btcspotprice)
    return btcspotprice["data"]


# Get the ETH spot price
def getethspotprice():
    # Get the spot price
    ethspotprice = getspotpricecoinbase("ETH-USD")
    # Serialize into JSON
    ethspotprice = json.loads(ethspotprice)
    return ethspotprice["data"]


# Get combined index tracking prices
def combinespotprices():
    # Create the list
    spotprices = []
    # Get the BTC Spot price
    btc = getbtcspotprice()
    # Get the ETH spot price
    eth = getethspotprice()
    # Append both to list
    spotprices.append(btc)
    spotprices.append(eth)
    return spotprices


# Function to get a list of Coinbase currencies
def getlistfromcoinbase(list):
    spotprices = []
    for currencypair in list:
        print("Getting: " + currencypair)
        token = getspotpricecoinbase(currencypair)
        token = json.loads(token)
        spotprices.append(token["data"])
        # Coinbase has an API limit of 3 requests per second
        sleep(0.5)
    return spotprices

