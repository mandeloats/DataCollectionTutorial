##Where Does Data Come From?

In the contemporary world the majority of data can be accessed in one of two ways. Much like your favorite vegetables, you can grow your own, or you can get it at the market. In this meaphor, growing your own data is akin to experimentation/simulation, and your market is the internet!

##Growing Your Own Data

Data can be generated by virtually anyone. Typically this is done by simulation, experimentation, or often times both. 

###Simulation

Simulation is essentially just the imitation of real world system over time. In a simulation you develop a model. This model is essentially just an approximation of your system. The goal of a model is to approximate the characteristics of your system accurately, while remaining as simple as possible. Often there is going to be a tradeoff between accuracy and simplicity. A simulation then is just the observation of your model over time.

###Experimentation

Data can also be aquired through experimentation. Experimentation is quite literally what you think it is. It is an emperical procedure carried out and recoreded. Experiments are often used to verify models or hypothesis. This can be as simple as recording the temperature every day for a year, flipping a quarter 100 times, or something much more complex. 

###Which one is better?

* Simulation is often much cheaper and faster
* Experiments are the "real" data
* Experiments are required to verify the simulation

##Data from the Web

There are many sources of data already on the web. Instead of simulating your own data or performing your own experiment, you can often find the data you need already available. There are three main ways of downloading data from the Web: Raw data donloads, APIs, and Webscraping. 

###Raw Data Downloads

This is the simplest way to get data from the internet. If somone has been kind enough to post all of their data in a database or csv file, you can simply download it and use it locally. This is the most common way to obtain a dataset. Websites like Kaggle and Data.gov offer free, searchable, easy to download datasets. 

###APIs

API stands for Application Package Index. If you're familliar with software you've probably heard the term. APIs simply offer "hooks" into a software so that it can be use programatically. In this context, the software offering hooks is a website. We use APIs to access data that is readily available on a given website. These are often accessed simply via a URL, which returns an object. This object can be a JSON string or XML file. It is often neatly organized and structured, making programatic access much simpler. 

###Webscraping

Webscraping is the process of pulling the raw HTML text of a webpage, and parsing it for information. HTML itself is often structured in a way that makes this fairly easy, however that is not always the case. HTML can often be poorly designed making the process of parsing it quite tedious. 

###Which is best? 

* Raw Data is most common, easy to download, and structured.
* APIs offer real time results that aren't available in Raw Data, but these services sometimes are not free.
* Webscraping is for when the data is out there, and not available via an API. 