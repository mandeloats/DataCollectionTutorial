import pandas


url = "http://sports.yahoo.com/ncaa/football/stats/byteam?cat1=offense&cat2=Receiving&conference=I-A_all&year=2016"

list = pandas.read_html(url) #returns a list of dataframes created from the available tables
dataframe = list[4].dropna(axis=1,how='all') # We needed the 4th table with the NaN columns dropped

names = dataframe.iloc[0] #row 0
dataframe.columns = names #assigns column names instead of numbers
dataframe = dataframe.ix[1:] #drops row 0

print(dataframe)
