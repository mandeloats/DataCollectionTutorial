import pandas

APIKey = "0a79f051a659d792f6a98e3b4e416f98" #Get yours at https://darksky.net/dev/
url = "https://api.darksky.net/forecast/"+APIKey+"/30.6280,-96.3344" #Note an API key is required

series = pandas.read_json(url) #returns a labeled series of dataframes
dataframe = series['currently']
print(dataframe)

print("The current temperature in College Station is " + str(dataframe['temperature'])+" degrees F")
