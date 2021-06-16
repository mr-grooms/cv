#!/bin/python
import pandas as pd

currency = pd.read_html(f'https://finance.yahoo.com/currencies')

print('------------------------------')
print('Total # of tables:', len(currency))

# prints all the tables
print(currency)


##############################################################
######### No Longer Working Code #############################
# import json
# from urllib.request import urlopen

# with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
#    source = response.read()

# data = json.loads(source)

# print(json.dumps(data, indent=2))

# usd_rates = dict()

# for item in data['list']['resources']:
#    name = item['resource']['fields']['name']
#    price = item['resource']['fields']['price']
#    usd_rates[name] = price

# print(50 * float(usd_rates['USD/INR']))

#############################################################
#############################################################
