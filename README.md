# CryptoTrading_QueryData_Python
Simple python program to query the exchanges for CryptoTrading platform

This program has been designed to run on something like a Raspberry Pi so that getting the data is split from the main analysis program

## Core functions and concepts
1. This program assumes a Splunk database with a reliable connection. Hence unencrypted UDP packets can be sent to listening Splunk port
2. Querying is transformed into JSON, and a key with the exchange this was queried and the timestamp is added to assist with later data analysis
3. This is a lightweight program. The binance and coinbase libraries do have extra functionality, this is in case future experimentation is needed

