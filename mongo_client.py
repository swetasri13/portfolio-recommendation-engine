#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np
import datetime as dt
from pandas_datareader import data as pdr
import yfinance as yfin
import scipy.optimize as sc
import plotly.graph_objects as go
import pandas as pd
import pandas as pd
from pymongo import MongoClient

yfin.pdr_override()

stockList=[]
stockList= ['GOOGL']

enddate=dt.datetime.now()
startdte=enddate-dt.timedelta(days=365)
stockData = pdr.get_data_yahoo(stockList, startdte, enddate)

client =  MongoClient("mongodb+srv://mongouser:market101@cluster0.fgigdzs.mongodb.net/?retryWrites=true&w=majority")
db = client['journaldev']
collection = db['stock_returns']
stockData.reset_index(inplace=True)
data_dict = stockData.to_dict("records")
# Insert collection
collection.insert_many(data_dict)

   


# In[ ]:




