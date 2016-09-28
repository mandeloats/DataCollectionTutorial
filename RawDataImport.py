import pandas
import sqlite3
import matplotlib.pyplot as plt
import sklearn.preprocessing as preprocess

con = sqlite3.connect("omnidirectional_data.db") # Gives Access to DB

dataframe = pandas.read_sql_query("SELECT * FROM MERGED_DATA_without_err_points",con) #USES SQL queries

print(dataframe)

x = preprocess.scale(dataframe['Latitude']) #Used for Graphing
y = preprocess.scale(dataframe['Longitude'])
plt.title("Geographic Locations of Collected Points")
plt.scatter(x,y)
plt.show()