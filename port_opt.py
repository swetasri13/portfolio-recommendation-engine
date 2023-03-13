#!/usr/bin/env python
# coding: utf-8


import glob
import pandas as pd
import matplotlib.pyplot as plt

# Get CSV files list from a folder
path = 'C:\\Users\\ratheesh\\data'
csv_files = glob.glob(path + "\*.csv")

# Read each CSV file into DataFrame
# This creates a list of dataframes
#df_list = (pd.read_csv(file) for file in csv_files)
df_list1= pd.read_csv('C:\\Users\\ratheesh\\data\\AAPL.csv')
df_list2= pd.read_csv('C:\\Users\\ratheesh\\data\\GOOGL.csv')
df_list3= pd.read_csv('C:\\Users\\ratheesh\\data\\MSFT.csv')
df_list4= pd.read_csv('C:\\Users\\ratheesh\\data\\NKE.csv')


df_list1['name']='AAPL'
df_list2['name']='GOOGL'
df_list3['name']='MSFT'
df_list4['name']='NKE'
# Concatenate all DataFrames
big_df   = pd.concat([df_list1,df_list2,df_list3,df_list4])


df= pd.DataFrame()


df['Date'] = df_list1['Date']
df['AAPL'] = df_list1['Close']
df['Date'] = df_list2['Date']
df['GOOGL'] = df_list2['Close']
df['Date'] = df_list3['Date']
df['MSFT'] = df_list3['Close']
df['Date'] = df_list4['Date']
df['NKE'] = df_list4['Close']


print(df.dtypes)

df_ii = df.set_index(pd.DatetimeIndex(df["Date"])).drop("Date",axis=1)


df_ii.head()


returns=df_ii.pct_change()


# In[8]:


returns.head()


# In[9]:


weights=[0.2,0.4,0.3,0.1]
port_ret=returns.dot(weights)
port_ret.head()


# In[34]:


port_ret.tail()


# In[10]:


var_matrix=returns.cov()*252


# In[58]:


var_matrix.head()


# In[11]:


import numpy as np

portfolio_variance=np.transpose(weights)@var_matrix@weights
portfolio_vol=np.sqrt(portfolio_variance)
print ("Variance ",portfolio_variance )
print ("Risk ",portfolio_vol )


# In[12]:

#num_assets=len(df_i.columns)
num_portfolios=10000
indvidual_ret=df_ii.resample('Y').last().pct_change().mean()



# In[13]:


opt_port_returns=[]
opt_port_vol=[]
opt_port_weights=[]


# In[14]:


for port in range(num_portfolios):
    weights=np.random.random(4)
    weights=weights/np.sum(weights)
    opt_port_weights.append(weights)
    returns_t=np.dot(weights,indvidual_ret)
    opt_port_returns.append(returns_t)
    
    var=var_matrix.mul(weights,axis=0).mul(weights,axis=1).sum().sum()
    
    sd=np.sqrt(var)
    ann_sd=sd*np.sqrt(250)
    opt_port_vol.append(ann_sd)        



# In[16]:


data1={'Returns':opt_port_returns, 'Volatility':opt_port_vol}
for counter, symbol in enumerate (df_ii.columns.tolist()):
    data1[symbol+' weight'] = [w[counter] for w in opt_port_weights ]

    


# In[17]:


portfolios_V1=pd.DataFrame.from_dict(data1, orient='index')


# In[18]:


portfolios_V1.head()


# In[19]:


abc=portfolios_V1.transpose()


# In[20]:


abc.head()


# In[21]:


print(abc.dtypes)


# In[23]:



abc.plot.scatter(x='Volatility',y='Returns',marker='o',color='y',s=15,alpha=0.5,grid=True,figsize=[8,8])
plt.xlabel("Risk (Volatility)")
plt.ylabel("Expected Returns")


# In[24]:


min_vol_port=abc.iloc[abc['Volatility'].idxmin()]
print (min_vol_port)


# In[26]:


rf=0.01
optimal_risk_port=abc.iloc[((abc['Returns']-rf)/abc['Volatility']).idxmax()]


# In[27]:


print (optimal_risk_port)


# In[33]:


plt.subplots(figsize=(8,8))
plt.scatter(abc['Volatility'],abc['Returns'],marker='o',color='g',s=15,alpha=0.3)
plt.scatter(min_vol_port[1],min_vol_port[0],color='r',marker='*',s=500)
plt.scatter(optimal_risk_port[1],optimal_risk_port[0],color='b',marker='*',s=500)
plt.xlabel("Risk (Volatility)")
plt.ylabel("Expected Returns")
plt.savefig('port.png')


# In[ ]:




