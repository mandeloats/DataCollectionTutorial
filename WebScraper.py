import pandas
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

url = "http://sports.yahoo.com/ncaa/football/stats/byteam?cat1=offense&cat2=Receiving&conference=I-A_all&year=2016"

list = pandas.read_html(url) #returns a list of dataframes created from the available tables
dataframe = list[4].dropna(axis=1,how='all') # We needed the 4th table with the NaN columns dropped

names = dataframe.iloc[0] #row 0
dataframe.columns = names #assigns column names instead of numbers
dataframe = dataframe.ix[1:] #drops row 0

#creates data and test set
msk = np.random.rand(len(dataframe)) < .8
data = dataframe[msk]
test = dataframe[~msk]

#Predicting the number of TDs
y_data = data['TD']
X_data = data.drop(['TD','Team','G'],axis = 1) #drop TD from data and other columns not used

y_test = test['TD']
X_test = test.drop(['TD','Team','G'],axis = 1)

regr = linear_model.LinearRegression() #from scikit-learn
regr.fit(X_data,y_data)

predictions = regr.predict(X_test)
y_test = y_test.astype(int) #convert from string

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f" % np.mean((predictions - y_test) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(X_test, y_test))



# Plot outputs
plt.scatter(y_test, predictions,  color='black')
plt.plot([y_test.min(),y_test.max()], [y_test.min(),y_test.max()], color = 'red')

plt.xlabel("Actual")
plt.ylabel("Predicted")

plt.show()

yg = X_test['Y/G'].astype(float) #yds/game

plt.xlabel("Y/G")
plt.ylabel("TD")
plt.scatter(yg,y_test, color = 'blue',label="Actual")
plt.scatter(yg,predictions,color='red',label ="Predicted")
plt.legend()
plt.show()




