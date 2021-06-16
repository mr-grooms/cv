import pandas as pd

# Gives a list of all insiders who have bought or sold a specific stock

company = input('Enter ticker symbol:')
insider = pd.read_html(f'http://openinsider.com/screener?s={company}&o=&pl=&ph=&ll=&lh=&fd=730&fdr=&td=0&tdr=&fdlyl=&fdlyh=&daysago=&xp=1&xs=1&vl=&vh=&ocl=&och=&sic1=-1&sicl=100&sich=9999&grp=0&nfl=&nfh=&nil=&nih=&nol=&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=0&cnt=500&page=1')

print('------------------------------')
print('Total # of tables', len(insider))

# prints all the tables
# print(insider)

executives = insider[11]
executives.to_csv('insider.csv')
print('insider.csv file has been created.')

# Just creating the file. Rather than displaying
#print(executives)

# Article on how to export data to csv:
# https://datatofish.com/export-dataframe-to-csv/
# the article at the top of the script also has information about exporting to excel


##################################################
### original code that I could NOT get to work ###
##################################################
# import pandas as pd

# company = ['AAPL','GME']

# insider = pd.DataFrame()
# for company in companies:
#     insider1 = pd.read_html(f'http://openinsider.com/screener?s={company}&o=&pl=&ph=&ll=&lh=&fd=730&fdr=&td=0&tdr=&fdlyl=&fdlyh=&daysago=&xp=1&xs=1&vl=&vh=&ocl=&och=&sic1=-1&sicl=100&sich=9999&grp=0&nfl=&nfh=&nil=&nih=&nol=&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=0&cnt=500&page=1')
#     insider1 = insider1[-3]
#     insider1['company'] = company
#     insider = pd.concat([insider,insider1])

# insider.to_csv('insider.csv)
##################################################
### original code that I could NOT get to work ###
##################################################
