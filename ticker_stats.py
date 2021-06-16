import pandas as pd

# Article on how this panda python script is built:
# https://codingandfun.com/scrape-yahoo-finance-using-python/ 

symbol = input('Enter ticker symbol:')
# use f-strings to pass the company variable into the url as an argument.
ticker_stats = pd.read_html(f'https://finance.yahoo.com/quote/{symbol}/key-statistics?p={symbol}')
ticker_summary = pd.read_html(f'https://finance.yahoo.com/quote/{symbol}?p={symbol}')

print('----------------------------')
print('Total # of tables:', len(ticker_stats))

# Prints all the tables
print(ticker_stats)
print(ticker_summary)

print('Total # of tables:', len(ticker_summary))
cash_flow = ticker_stats[9]
market_cap = ticker_summary[1]
short_interest = ticker_stats[2]

print('----------------------------')
print('Cash:')
print(cash_flow)
print(ticker_stats[8])
print('----------------------------')
print('Revenue:')
print(ticker_stats[7])
print('----------------------------')
print('Short Interest:')
print(short_interest)
print('----------------------------')
print('Ticker Summary:')
print(market_cap)


# Article on how to export data to csv:
# https://datatofish.com/export-dataframe-to-csv/
# the article at the top of the script also has information about exporting to excel

# Used to export specific table to .csv
# in this case, the short interest table
short_interest.to_csv('short_interest.csv')


